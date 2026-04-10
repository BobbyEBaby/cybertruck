# tools/

The agent's hands. Helper scripts that wrap publishing platforms so the daily run can ship without a human.

## Conventions
- Each helper is **single-purpose** (one platform, one verb). No mega-scripts.
- Helpers read credentials from `cybertruck/.env`. They **never echo, log, or print** credential values.
- Helpers are created **on first use** by the daily run. Don't pre-create them speculatively.
- Each helper exits non-zero on failure with a one-line error to stderr (no stack traces leaking env).
- Each successful publish appends to `state/publish-log.md`.

## Expected helpers (created when first needed)
- `tools/deploy_pages.sh <repo-name> <local-dir>` — `gh` + GitHub Pages
- `tools/publish_itch.sh <experiment-slug> <channel>` — `butler push`
- `tools/publish_gumroad.py <experiment-slug>` — Gumroad API
- `tools/post_reddit.py <subreddit> <title> <url>` — PRAW, one post, no comment engagement
- `tools/publish_npm.sh <package-dir>` — `npm publish` with token
- `tools/publish_pypi.sh <package-dir>` — `twine upload`

## Pattern for env loading without leaking
```bash
#!/usr/bin/env bash
set -euo pipefail
set -a
source "$(dirname "$0")/../.env"
set +a
# now use $GITHUB_TOKEN etc. but NEVER echo it
```

## Hard rule
A helper that prints any credential value — even partially, even in an error message — is broken and must be fixed before next use.
