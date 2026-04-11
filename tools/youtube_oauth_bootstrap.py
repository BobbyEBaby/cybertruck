#!/usr/bin/env python3
"""tools/youtube_oauth_bootstrap.py — one-time YouTube Data API OAuth consent flow.

Run this ONCE locally after you've created a Google Cloud project, enabled the
YouTube Data API v3, created OAuth 2.0 Client credentials (Desktop app), and
downloaded the client_secret.json to cybertruck/secrets/youtube_client_secret.json.

What it does:
1. Reads the client_secret.json from secrets/
2. Starts a local HTTP server on 127.0.0.1 (random free port)
3. Opens your browser to Google's consent screen for YouTube upload scope
4. You click "Allow"
5. Google redirects back to the local server with an authorization code
6. Script exchanges the code for access + refresh tokens
7. Writes ONLY the refresh token to .env as YOUTUBE_OAUTH_REFRESH_TOKEN
8. Never prints the token to stdout/stderr/logs

The refresh token is long-lived — once written, you don't need to do this again.
The access token (short-lived, regenerated from the refresh token on each use) is
never persisted by this bootstrap.

Usage:
    pip install google-auth-oauthlib
    python tools/youtube_oauth_bootstrap.py

Security:
- client_secret.json stays in secrets/ (gitignored)
- refresh token goes to .env (gitignored)
- nothing is echoed, logged, or sent anywhere except Google's OAuth endpoints
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLIENT_SECRET = ROOT / "secrets" / "youtube_client_secret.json"
ENV = ROOT / ".env"

# YouTube upload scope. Read-only analytics scope added for future stats fetching.
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
]


def ensure_client_secret() -> None:
    if CLIENT_SECRET.exists():
        return
    sys.exit(
        "error: secrets/youtube_client_secret.json not found.\n"
        "  1. Go to https://console.cloud.google.com/\n"
        "  2. Create a project\n"
        "  3. Enable YouTube Data API v3 (APIs & Services -> Library)\n"
        "  4. Configure OAuth consent screen (External, add yourself as test user)\n"
        "  5. Create OAuth client ID (Desktop app type)\n"
        "  6. Download the JSON and save as cybertruck/secrets/youtube_client_secret.json"
    )


def run_flow() -> str:
    """Run OAuth flow and return the refresh token. Never print it."""
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
    except ImportError:
        sys.exit(
            "error: google-auth-oauthlib not installed.\n"
            "  run: pip install google-auth-oauthlib"
        )

    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
    # run_local_server spins up a local HTTP listener, opens browser, waits for redirect
    credentials = flow.run_local_server(
        host="127.0.0.1",
        port=0,  # pick a free port
        open_browser=True,
        authorization_prompt_message="",  # suppress the "please visit this URL" print
        success_message="OK. Refresh token captured. You can close this tab.",
    )
    if not credentials.refresh_token:
        sys.exit(
            "error: no refresh_token returned. This usually means you've already\n"
            "  granted consent before. Revoke the app at\n"
            "  https://myaccount.google.com/permissions and run this again, OR\n"
            "  pass prompt='consent' in the flow (edit this script)."
        )
    return credentials.refresh_token  # type: ignore[no-any-return]


def write_env(token: str) -> None:
    """Upsert YOUTUBE_OAUTH_REFRESH_TOKEN in .env without disturbing other keys
    and without echoing the token value."""
    if not ENV.exists():
        ENV.write_text(
            "# Cybertruck Autopilot — local environment\nYOUTUBE_OAUTH_REFRESH_TOKEN=\n",
            encoding="utf-8",
        )

    lines = ENV.read_text(encoding="utf-8").splitlines()
    found = False
    for i, line in enumerate(lines):
        if line.startswith("YOUTUBE_OAUTH_REFRESH_TOKEN="):
            lines[i] = f"YOUTUBE_OAUTH_REFRESH_TOKEN={token}"
            found = True
            break
    if not found:
        # Insert under a YouTube section
        lines.append("")
        lines.append("# === YouTube Data API v3 ===")
        lines.append(f"YOUTUBE_OAUTH_REFRESH_TOKEN={token}")

    ENV.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_client_secret()
    print("Opening browser for one-time YouTube consent...")
    print("(If the browser doesn't open automatically, check the terminal for a URL.)")
    token = run_flow()
    write_env(token)
    # DO NOT print the token. Confirm only that it was written.
    print("")
    print("Success. Refresh token written to .env as YOUTUBE_OAUTH_REFRESH_TOKEN.")
    print("You do not need to see or copy the token — the autopilot will use it directly.")
    print("You will never need to run this script again unless you revoke the app's access.")


if __name__ == "__main__":
    main()
