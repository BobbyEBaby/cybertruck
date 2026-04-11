#!/usr/bin/env python3
"""tools/youtube_upload.py — upload an episode to Robert's YouTube channel.

Usage:
    python tools/youtube_upload.py <video-slug> [--privacy private|unlisted|public]

Uses the OAuth refresh token in .env (YOUTUBE_OAUTH_REFRESH_TOKEN) to
authenticate. Uploads assets/<slug>/final.mp4, sets title/description/
tags/thumbnail, and records the resulting URL to state/publish-log.md.

Default privacy: unlisted (safe for first-episode test ships — you get
a shareable URL but it's not public-searchable until you flip it).
Pass --privacy public to publish publicly. Pass --privacy private to
make it only visible to the channel owner.

Reads metadata from:
    experiments/youtube-history-channel/scripts/*<slug>*.md (frontmatter)
    experiments/youtube-history-channel/video-description-template.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV = ROOT / ".env"
SCRIPTS_DIR = ROOT / "experiments" / "youtube-history-channel" / "scripts"
ASSETS_DIR = ROOT / "experiments" / "youtube-history-channel" / "assets"
PUBLISH_LOG = ROOT / "state" / "publish-log.md"
SECRETS = ROOT / "secrets"

CLIENT_SECRET_FILE = SECRETS / "youtube_client_secret.json"
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
]


def load_env() -> dict[str, str]:
    out: dict[str, str] = {}
    if not ENV.exists():
        sys.exit("error: .env missing")
    for line in ENV.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def find_script(slug: str) -> Path:
    candidates = list(SCRIPTS_DIR.glob(f"*{slug}*.md"))
    if not candidates:
        sys.exit(f"error: no script for '{slug}'")
    return candidates[0]


def parse_frontmatter(script_path: Path) -> dict:
    text = script_path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    meta: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.strip().startswith("-"):
            continue
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip().strip('"')
    return meta


def build_description(slug: str, title: str) -> str:
    """Build the video description. Uses the 4-tip-rail structure from
    experiments/youtube-history-channel/video-description-template.md
    but simplified and filled in."""
    return f"""{title}

Episode 1 of Popular Uprisings — a history channel analyzing rebellions across time through six recurring themes: economy, royalty, government, wars, environment, and debt. Every episode adds one more rebellion to an open public database of the conditions that produce revolts.

Source code, research notes, and the public themes database:
https://github.com/BobbyEBaby/cybertruck

SUPPORT INDEPENDENT HISTORY RESEARCH
Ko-fi (0% fee, all of it goes to the project):
https://ko-fi.com/bobbyebaby (if link is live)

Crypto tips (low fees, no middleman):
USDC on Solana: EQwtTPe3GfcAGAiQAh3AxmCZ1WAyCviDsNnBmfCaQwf7
Dogecoin: DUJPtjifrXtiykXcN389Gw36g5T9ZpWvgZ
XRP: rLHzPsX6oXkzU2qL12kHCH8G8cnZv1rBJh (destination tag: 2272490000 — REQUIRED)

SOURCES FOR THIS EPISODE
- Britannica, Peasants' Revolt: https://www.britannica.com/event/Peasants-Revolt
- Wikipedia, Peasants' Revolt: https://en.wikipedia.org/wiki/Peasants%27_Revolt
- Historic UK, The Peasants' Revolt: https://www.historic-uk.com/HistoryUK/HistoryofEngland/The-Peasants-Revolt/
- Charles Oman, "The Great Revolt of 1381" (Oxford, 1906, public domain, Internet Archive)

IMAGES were generated with AI models (Pollinations.ai / Flux family) in the style of period-appropriate oil paintings and illuminated manuscripts. Script was written by an automated research loop with inline source citations and human oversight. The narration uses Microsoft Edge TTS voices (en-US-GuyNeural narration, en-US-JennyNeural for thematic analysis, en-US-AriaNeural for outro).

This is a zero-budget, fully-honest experiment. Everything about the production pipeline — the scripts, the research process, the honest expectations doc — is public at the GitHub link above.

#history #rebellion #peasantsrevolt #wattyler #medievalhistory #historythroughlines
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("--privacy", choices=["private", "unlisted", "public"], default="unlisted")
    parser.add_argument("--title-override", default=None)
    args = parser.parse_args()

    env = load_env()
    refresh = env.get("YOUTUBE_OAUTH_REFRESH_TOKEN", "")
    if not refresh:
        sys.exit("error: YOUTUBE_OAUTH_REFRESH_TOKEN not set in .env")
    if not CLIENT_SECRET_FILE.exists():
        sys.exit(f"error: {CLIENT_SECRET_FILE} missing")

    asset_dir = ASSETS_DIR / args.slug
    video = asset_dir / "final.mp4"
    if not video.exists():
        sys.exit(f"error: {video} does not exist — run render_video.py first")

    script_path = find_script(args.slug)
    meta = parse_frontmatter(script_path)
    title = args.title_override or meta.get("title", args.slug)
    description = build_description(args.slug, title)
    tags = [
        "history", "rebellion", "peasants revolt", "wat tyler",
        "medieval history", "1381", "breaking points", "england",
        "historical analysis",
    ]

    # Build credentials from refresh token + client secret
    from google.oauth2.credentials import Credentials  # type: ignore
    from googleapiclient.discovery import build  # type: ignore
    from googleapiclient.http import MediaFileUpload  # type: ignore

    client_info = json.loads(CLIENT_SECRET_FILE.read_text())
    # Handles both "installed" and "web" key shapes
    app = client_info.get("installed") or client_info.get("web")
    credentials = Credentials(
        token=None,
        refresh_token=refresh,
        token_uri=app["token_uri"],
        client_id=app["client_id"],
        client_secret=app["client_secret"],
        scopes=SCOPES,
    )

    youtube = build("youtube", "v3", credentials=credentials)

    body = {
        "snippet": {
            "title": title[:100],
            "description": description[:5000],
            "tags": tags,
            "categoryId": "27",  # Education
            "defaultLanguage": "en",
            "defaultAudioLanguage": "en",
        },
        "status": {
            "privacyStatus": args.privacy,
            "selfDeclaredMadeForKids": False,
            "embeddable": True,
        },
    }

    print(f"Uploading {video.name} ({video.stat().st_size / 1_000_000:.1f} MB)")
    print(f"  title:    {title}")
    print(f"  privacy:  {args.privacy}")

    media = MediaFileUpload(str(video), chunksize=8 * 1024 * 1024, resumable=True, mimetype="video/mp4")
    request = youtube.videos().insert(part=",".join(body.keys()), body=body, media_body=media)

    response = None
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print(f"  progress: {int(status.progress() * 100)}%")
        except Exception as e:
            print(f"  error during upload: {e}", file=sys.stderr)
            raise

    video_id = response["id"]
    video_url = f"https://youtu.be/{video_id}"
    watch_url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"\ndone: {video_url}")

    # Append to publish-log.md
    with PUBLISH_LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"\n## {time.strftime('%Y-%m-%d %H:%M', time.gmtime())}\n"
            f"- platform: youtube\n"
            f"- url: {watch_url}\n"
            f"- video_id: {video_id}\n"
            f"- privacy: {args.privacy}\n"
            f"- experiment: youtube-history-channel\n"
            f"- episode: {args.slug}\n"
        )


if __name__ == "__main__":
    main()
