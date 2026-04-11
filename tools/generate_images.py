#!/usr/bin/env python3
"""tools/generate_images.py — generate episode images via Pollinations.ai.

Usage:
    python tools/generate_images.py <video-slug>

Reads the "Pollinations prompts" section from the episode's script file,
calls https://image.pollinations.ai/prompt/{url-encoded-prompt} for each,
saves to experiments/youtube-history-channel/assets/<slug>/img_NN.jpg,
and writes an images.md manifest.

Pollinations.ai is free, no API key, no signup. Respect their service:
2-second delay between requests, exponential backoff on 429.

REAL: prefix: if a prompt is prefixed with 'REAL: <url>', download the
URL directly instead of generating a new image (used for iconic
public-domain artworks that audiences recognize).
"""

from __future__ import annotations

import re
import sys
import time
import urllib.parse
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "experiments" / "youtube-history-channel" / "scripts"
ASSETS_DIR = ROOT / "experiments" / "youtube-history-channel" / "assets"

POLLINATIONS_URL = "https://image.pollinations.ai/prompt/{prompt}"
# width/height/model query params — SDXL via width=1280&height=720 for 16:9
POLLINATIONS_PARAMS = "?width=1280&height=720&nologo=true&enhance=true"

REQUEST_DELAY = 2.0  # seconds between API calls, be nice to the free service
MAX_RETRIES = 3
BACKOFF_BASE = 5.0


def find_script(slug: str) -> Path:
    """Locate the script file for a given slug."""
    candidates = list(SCRIPTS_DIR.glob(f"*{slug}*.md"))
    if not candidates:
        sys.exit(f"error: no script found matching slug '{slug}' in {SCRIPTS_DIR}")
    if len(candidates) > 1:
        sys.exit(f"error: multiple script candidates for '{slug}': {candidates}")
    return candidates[0]


def extract_prompts(script_path: Path) -> list[str]:
    """Pull numbered prompts from the 'Pollinations prompts' section.

    Accepts either:
        ## Pollinations prompts
        01. prompt text here
        02. another prompt
    or:
        ## Pollinations prompts
        - prompt text
        - another prompt
    """
    text = script_path.read_text(encoding="utf-8")
    # Find the Pollinations prompts section
    m = re.search(r"##\s+Pollinations\s+prompts\s*\n(.*?)(?=\n##\s|\Z)", text, re.DOTALL | re.IGNORECASE)
    if not m:
        sys.exit(f"error: no '## Pollinations prompts' section found in {script_path.name}")
    section = m.group(1)

    prompts: list[str] = []
    for line in section.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Match "01. prompt" or "1. prompt" or "- prompt"
        m2 = re.match(r"^(?:\d+\.\s*|-\s+)(.+)$", line)
        if m2:
            prompts.append(m2.group(1).strip())
    return prompts


def fetch_image(prompt: str, out_path: Path) -> tuple[bool, str]:
    """Fetch one image. Returns (success, engine_used_or_error)."""
    if prompt.upper().startswith("REAL:"):
        url = prompt.split(":", 1)[1].strip()
        engine = "real-pd-passthrough"
    else:
        encoded = urllib.parse.quote(prompt, safe="")
        url = POLLINATIONS_URL.format(prompt=encoded) + POLLINATIONS_PARAMS
        engine = "pollinations"

    for attempt in range(MAX_RETRIES):
        try:
            r = requests.get(url, timeout=120, stream=True)
            if r.status_code == 200:
                with out_path.open("wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                if out_path.stat().st_size < 1024:
                    return False, f"tiny response ({out_path.stat().st_size} bytes)"
                return True, engine
            if r.status_code == 429:
                wait = BACKOFF_BASE * (2 ** attempt)
                print(f"    rate-limited, sleeping {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            return False, f"HTTP {r.status_code}"
        except requests.RequestException as e:
            if attempt == MAX_RETRIES - 1:
                return False, f"exception: {e}"
            time.sleep(BACKOFF_BASE * (2 ** attempt))
    return False, "max retries exceeded"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: generate_images.py <video-slug>")
    slug = sys.argv[1]

    script_path = find_script(slug)
    prompts = extract_prompts(script_path)
    if not prompts:
        sys.exit(f"error: no prompts parsed from {script_path.name}")

    out_dir = ASSETS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Found {len(prompts)} prompts in {script_path.name}")
    print(f"Output: {out_dir}")

    manifest_lines = [
        "# images.md — generated image manifest",
        f"",
        f"**Episode:** {slug}",
        f"**Script:** {script_path.name}",
        f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}",
        f"**Source:** Pollinations.ai (SDXL-family models, free tier, no key)",
        f"",
        "| # | File | Engine | Prompt |",
        "|---|---|---|---|",
    ]

    successes = 0
    for idx, prompt in enumerate(prompts, 1):
        filename = f"img_{idx:02d}.jpg"
        out_path = out_dir / filename
        print(f"  [{idx:02d}/{len(prompts)}] {prompt[:70]}...")
        ok, engine = fetch_image(prompt, out_path)
        backslash_pipe = "\\|"
        safe_prompt = prompt.replace("|", backslash_pipe)
        if ok:
            successes += 1
            manifest_lines.append(f"| {idx:02d} | `{filename}` | {engine} | {safe_prompt} |")
        else:
            print(f"    FAILED: {engine}", file=sys.stderr)
            manifest_lines.append(f"| {idx:02d} | FAILED | - | {safe_prompt} ({engine}) |")
        time.sleep(REQUEST_DELAY)

    (out_dir / "images.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    print(f"\ndone: {successes}/{len(prompts)} images generated")
    print(f"manifest: {out_dir / 'images.md'}")


if __name__ == "__main__":
    main()
