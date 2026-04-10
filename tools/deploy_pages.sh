#!/usr/bin/env bash
# tools/deploy_pages.sh — deploy a single-file experiment to its own GitHub repo + Pages
#
# Usage: tools/deploy_pages.sh <repo-name> <local-source-dir>
# Example: tools/deploy_pages.sh prompt-cleaner experiments/prompt-cleaner
#
# Reads GITHUB_TOKEN from .env. Never echoes the token.
# Creates the repo if it doesn't exist, copies the contents of <local-source-dir>
# into a fresh checkout, pushes to main, enables Pages on main /, returns the URL.
#
# This script is intentionally idempotent: re-running on an existing repo just
# updates the contents and prints the existing Pages URL.

set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 <repo-name> <local-source-dir>" >&2
  exit 64
fi

REPO_NAME="$1"
SOURCE_DIR="$2"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [[ ! -d "$ROOT_DIR/$SOURCE_DIR" ]]; then
  echo "error: source dir $ROOT_DIR/$SOURCE_DIR does not exist" >&2
  exit 66
fi

# Load .env without leaking it to logs
if [[ ! -f "$ROOT_DIR/.env" ]]; then
  echo "error: $ROOT_DIR/.env missing — see human_inbox/0001-setup.md" >&2
  exit 78
fi
set -a
# shellcheck disable=SC1091
source "$ROOT_DIR/.env"
set +a

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "error: GITHUB_TOKEN not set in .env" >&2
  exit 78
fi

# Authenticate gh non-interactively
export GH_TOKEN="$GITHUB_TOKEN"

# Determine GitHub username from token
GH_USER="$(gh api user --jq .login)"
if [[ -z "$GH_USER" ]]; then
  echo "error: could not determine GitHub username from token" >&2
  exit 70
fi

REPO_FULL="$GH_USER/$REPO_NAME"
WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT

# Create repo if missing
if ! gh repo view "$REPO_FULL" >/dev/null 2>&1; then
  gh repo create "$REPO_FULL" --public --description "Auto-deployed by Cybertruck Autopilot" --confirm >/dev/null
fi

# Clone fresh, copy contents in, push
git clone --quiet "https://${GITHUB_TOKEN}@github.com/${REPO_FULL}.git" "$WORK_DIR/repo" 2>/dev/null || {
  # Empty repo case — init and add remote
  mkdir -p "$WORK_DIR/repo"
  cd "$WORK_DIR/repo"
  git init -b main -q
  git remote add origin "https://${GITHUB_TOKEN}@github.com/${REPO_FULL}.git"
}

cd "$WORK_DIR/repo"
# Wipe everything except .git, then copy fresh
find . -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +
cp -R "$ROOT_DIR/$SOURCE_DIR/." .

git add -A
if git diff --cached --quiet; then
  echo "no changes to deploy"
else
  git -c user.email="autopilot@cybertruck.local" -c user.name="Cybertruck Autopilot" \
    commit -q -m "deploy: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  git push -q -u origin main
fi

# Enable Pages on main / (root) — idempotent
gh api "repos/$REPO_FULL/pages" >/dev/null 2>&1 || \
  gh api -X POST "repos/$REPO_FULL/pages" \
    -f "source[branch]=main" -f "source[path]=/" >/dev/null

PAGES_URL="https://${GH_USER,,}.github.io/${REPO_NAME}/"

echo "deployed: $PAGES_URL"

# Append to publish-log
{
  echo ""
  echo "## $(date -u +%Y-%m-%d\ %H:%M)"
  echo "- platform: github-pages"
  echo "- url: $PAGES_URL"
  echo "- experiment: $REPO_NAME"
} >> "$ROOT_DIR/state/publish-log.md"
