#!/usr/bin/env python3
"""tools/regen_images.py — regenerate specific images by number.

Usage:
    python tools/regen_images.py <video-slug> <img-number>[,<img-number>...]

Re-reads the "Pollinations prompts" section of the script, finds the
numbered prompts, re-downloads only those images (overwriting in place).
Same backoff/rate-limit behavior as generate_images.py.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

# Reuse the helpers from generate_images.py
sys.path.insert(0, str(Path(__file__).parent))
from generate_images import find_script, extract_prompts, fetch_image, REQUEST_DELAY  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT / "experiments" / "youtube-history-channel" / "assets"


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: regen_images.py <slug> <nums-comma-separated>")
    slug = sys.argv[1]
    nums = [int(x) for x in sys.argv[2].split(",") if x.strip()]

    script_path = find_script(slug)
    prompts = extract_prompts(script_path)

    out_dir = ASSETS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    for num in nums:
        if num < 1 or num > len(prompts):
            print(f"skip {num}: out of range (1-{len(prompts)})", file=sys.stderr)
            continue
        prompt = prompts[num - 1]
        filename = f"img_{num:02d}.jpg"
        out_path = out_dir / filename
        print(f"[{num:02d}] regenerating: {prompt[:80]}...")
        ok, engine = fetch_image(prompt, out_path)
        if ok:
            print(f"  OK ({engine}) -> {filename}")
        else:
            print(f"  FAILED ({engine})", file=sys.stderr)
        time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    main()
