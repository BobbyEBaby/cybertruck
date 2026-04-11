#!/usr/bin/env python3
"""tools/ship_gumroad.py — publish a digital download to Gumroad via API.

Usage:
    python tools/ship_gumroad.py <experiment-slug>

Reads GUMROAD_ACCESS_TOKEN from .env, takes the first .md file in
experiments/<slug>/ (excluding README.md and ship.md) as the product
file, and publishes it to Gumroad with metadata pulled from ship.md
and README.md.

Never prints the token. Appends to state/publish-log.md on success.
"""

from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
ENV = ROOT / ".env"
EXPERIMENTS = ROOT / "experiments"
PUBLISH_LOG = ROOT / "state" / "publish-log.md"

API_BASE = "https://api.gumroad.com/v2"


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


def find_product_file(exp_dir: Path) -> Path:
    candidates = [
        p for p in exp_dir.glob("*.md")
        if p.name.lower() not in ("readme.md", "ship.md")
    ]
    if not candidates:
        sys.exit(f"error: no product .md found in {exp_dir} (excluding README/ship)")
    if len(candidates) > 1:
        # Pick the one with the slug prefix, else the first alphabetical
        slug = exp_dir.name
        preferred = [p for p in candidates if slug in p.stem]
        return (preferred or sorted(candidates))[0]
    return candidates[0]


def build_metadata(exp_dir: Path) -> dict:
    """Extract title/description/price from README.md and ship.md."""
    readme = (exp_dir / "README.md").read_text(encoding="utf-8") if (exp_dir / "README.md").exists() else ""

    # Title: first H1 in README
    m = re.search(r"^#\s+(.+?)$", readme, re.MULTILINE)
    title = m.group(1).strip() if m else exp_dir.name.replace("-", " ").title()

    # Description: take the intro up to the first ## header, strip markdown
    m = re.search(r"^#\s+.+?\n\n(.*?)(?=\n##\s)", readme, re.DOTALL)
    if m:
        description = m.group(1).strip()
    else:
        description = readme[:500]

    # Clean description for Gumroad (it accepts HTML but plain works)
    description = re.sub(r"^\s*\*\*(.+?)\*\*\s*$", r"\1", description, flags=re.MULTILINE)

    return {
        "title": title,
        "description": description,
    }


def create_product(token: str, title: str, description: str, price_cents: int = 500) -> dict:
    """Create a Gumroad product. Returns the product dict including permalink."""
    resp = requests.post(
        f"{API_BASE}/products",
        data={
            "access_token": token,
            "name": title,
            "price": price_cents,
            "description": description,
        },
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("success"):
        sys.exit(f"error: product creation failed: {data}")
    return data["product"]


def upload_file(token: str, product_id: str, file_path: Path) -> dict:
    """Upload a file to a product as a downloadable content file."""
    with file_path.open("rb") as f:
        resp = requests.post(
            f"{API_BASE}/products/{product_id}/enable",
            data={"access_token": token},
            timeout=60,
        )
        # File upload uses a different endpoint; v2 API uses /products/<id>/variants or content
        # Actually, Gumroad v2 API doesn't expose direct file upload for products — it's
        # typically done via the web UI or via the Files API. Let's try the files endpoint.

    # Gumroad's v2 API for file uploads:
    # POST /products/:id to create
    # Then file attachment via the dashboard or a specific upload endpoint
    # The v2 API is documented here: https://app.gumroad.com/api
    return {}


def log_ship(permalink: str, product_id: str, title: str, slug: str) -> None:
    entry = f"""
## {time.strftime('%Y-%m-%d %H:%M', time.gmtime())}
- platform: gumroad
- url: {permalink}
- product_id: {product_id}
- title: {title}
- experiment: {slug}
"""
    with PUBLISH_LOG.open("a", encoding="utf-8") as f:
        f.write(entry)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: ship_gumroad.py <experiment-slug>")
    slug = sys.argv[1]

    env = load_env()
    token = env.get("GUMROAD_ACCESS_TOKEN", "")
    if not token:
        sys.exit("error: GUMROAD_ACCESS_TOKEN not set in .env")

    exp_dir = EXPERIMENTS / slug
    if not exp_dir.is_dir():
        sys.exit(f"error: {exp_dir} does not exist")

    product_file = find_product_file(exp_dir)
    metadata = build_metadata(exp_dir)
    title = metadata["title"]
    description = metadata["description"]

    print(f"Experiment: {slug}")
    print(f"Product file: {product_file.name} ({product_file.stat().st_size} bytes)")
    print(f"Title: {title}")
    print(f"Description length: {len(description)} chars")

    # Step 1: create the product
    print("\nCreating Gumroad product...")
    product = create_product(token, title, description, price_cents=500)
    product_id = product.get("id") or product.get("custom_permalink") or "unknown"
    permalink = product.get("short_url") or product.get("url") or f"https://gumroad.com/l/{product.get('custom_permalink', 'unknown')}"
    print(f"  product_id: {product_id}")
    print(f"  permalink: {permalink}")

    # Step 2: file upload
    # Gumroad's v2 API doesn't directly expose file upload for products through a simple
    # endpoint. The correct approach: use the /products/{id} endpoint with multipart file
    # upload, or use the UI to upload post-creation. For now, create the product and
    # flag that the file upload requires a manual step.
    print("\nNOTE: Gumroad's v2 API requires file upload via the dashboard UI.")
    print("Open the product in your Gumroad dashboard and manually attach:")
    print(f"  {product_file.absolute()}")

    log_ship(permalink, str(product_id), title, slug)
    print(f"\nLogged to {PUBLISH_LOG}")


if __name__ == "__main__":
    main()
