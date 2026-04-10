#!/usr/bin/env python3
"""tools/post_reddit.py — post a single link to a single subreddit, then exit.

Usage:
    python tools/post_reddit.py <subreddit> <title> <url>

Reads REDDIT_* credentials from .env. Hard rules enforced in this script:
- One post, then exit. Never poll for comments.
- Never reply to anything.
- Never post if there has already been a Reddit post within the last 24h
  (checked against state/publish-log.md).

Requires: praw (`pip install praw`). The cron's first run will pip-install it
into a venv at tools/.venv if missing.
"""

from __future__ import annotations

import os
import re
import sys
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV = ROOT / ".env"
PUBLISH_LOG = ROOT / "state" / "publish-log.md"


def load_env() -> dict[str, str]:
    if not ENV.exists():
        sys.exit("error: .env missing — see human_inbox/0001-setup.md")
    out: dict[str, str] = {}
    for line in ENV.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def check_rate_limit(env: dict[str, str]) -> None:
    """Refuse to post if any reddit post happened in last 24h."""
    if not PUBLISH_LOG.exists():
        return
    text = PUBLISH_LOG.read_text(encoding="utf-8")
    # find timestamps tagged with reddit
    blocks = re.split(r"\n## ", text)
    cutoff = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
    for block in blocks:
        if "platform: reddit" not in block:
            continue
        m = re.match(r"(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})", block)
        if not m:
            continue
        ts = datetime.datetime.strptime(
            f"{m.group(1)} {m.group(2)}:{m.group(3)}", "%Y-%m-%d %H:%M"
        )
        if ts >= cutoff:
            sys.exit(f"rate-limit: a reddit post already exists at {ts.isoformat()}")


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit("usage: post_reddit.py <subreddit> <title> <url>")
    sub, title, url = sys.argv[1], sys.argv[2], sys.argv[3]
    env = load_env()

    required = [
        "REDDIT_CLIENT_ID",
        "REDDIT_CLIENT_SECRET",
        "REDDIT_USERNAME",
        "REDDIT_PASSWORD",
        "REDDIT_USER_AGENT",
    ]
    missing = [k for k in required if not env.get(k)]
    if missing:
        sys.exit(f"error: missing env vars: {', '.join(missing)}")

    check_rate_limit(env)

    try:
        import praw  # type: ignore
    except ImportError:
        sys.exit("error: praw not installed. run: pip install praw")

    reddit = praw.Reddit(
        client_id=env["REDDIT_CLIENT_ID"],
        client_secret=env["REDDIT_CLIENT_SECRET"],
        username=env["REDDIT_USERNAME"],
        password=env["REDDIT_PASSWORD"],
        user_agent=env["REDDIT_USER_AGENT"],
    )

    submission = reddit.subreddit(sub).submit(title=title, url=url)
    post_url = f"https://reddit.com{submission.permalink}"

    # Append to publish log
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    with PUBLISH_LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"\n## {now}\n- platform: reddit\n- subreddit: r/{sub}\n- url: {post_url}\n"
        )

    print(post_url)


if __name__ == "__main__":
    main()
