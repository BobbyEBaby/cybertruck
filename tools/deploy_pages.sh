#!/usr/bin/env bash
# tools/deploy_pages.sh — deploy a single-file experiment to its own GitHub repo + Pages
#
# Usage: tools/deploy_pages.sh <repo-name> <local-source-dir>
# Example: tools/deploy_pages.sh prompt-cleaner experiments/prompt-cleaner
#
# Reads GITHUB_TOKEN from .env. Never echoes the token.
# Uses raw GitHub REST API via curl + git — no gh CLI dependency.
# Idempotent: re-running on an existing repo just updates the contents.

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

API="https://api.github.com"
AUTH_HEADER="Authorization: Bearer ${GITHUB_TOKEN}"
ACCEPT_HEADER="Accept: application/vnd.github+json"
API_VERSION_HEADER="X-GitHub-Api-Version: 2022-11-28"

# Helper: GitHub API call. Args: METHOD PATH [JSON_BODY]
gh_api() {
  local method="$1" path="$2" body="${3:-}"
  if [[ -n "$body" ]]; then
    curl -sS -X "$method" \
      -H "$AUTH_HEADER" -H "$ACCEPT_HEADER" -H "$API_VERSION_HEADER" \
      -H "Content-Type: application/json" \
      -d "$body" \
      "$API$path"
  else
    curl -sS -X "$method" \
      -H "$AUTH_HEADER" -H "$ACCEPT_HEADER" -H "$API_VERSION_HEADER" \
      "$API$path"
  fi
}

# 1. Determine GitHub username from token
GH_USER="$(gh_api GET /user | grep -o '"login":[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"\([^"]*\)"$/\1/')"
if [[ -z "$GH_USER" ]]; then
  echo "error: could not determine GitHub username from token (is the token valid?)" >&2
  exit 70
fi

REPO_FULL="$GH_USER/$REPO_NAME"
WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT

# 2. Create repo if it does not exist (404 from GET means not found)
REPO_STATUS="$(curl -sS -o /dev/null -w '%{http_code}' \
  -H "$AUTH_HEADER" -H "$ACCEPT_HEADER" -H "$API_VERSION_HEADER" \
  "$API/repos/$REPO_FULL")"

if [[ "$REPO_STATUS" == "404" ]]; then
  CREATE_BODY="{\"name\":\"$REPO_NAME\",\"private\":false,\"description\":\"Auto-deployed by Cybertruck Autopilot\",\"auto_init\":false,\"has_issues\":false,\"has_projects\":false,\"has_wiki\":false}"
  CREATE_RESP="$(gh_api POST /user/repos "$CREATE_BODY")"
  if ! echo "$CREATE_RESP" | grep -q '"full_name"'; then
    echo "error: repo creation failed" >&2
    echo "$CREATE_RESP" | grep -o '"message":[[:space:]]*"[^"]*"' >&2 || true
    exit 70
  fi
elif [[ "$REPO_STATUS" != "200" ]]; then
  echo "error: unexpected status $REPO_STATUS checking repo $REPO_FULL" >&2
  exit 70
fi

# 3. Clone (or init if clone of empty repo behaves oddly), copy files, push
# Use HTTP header-based auth (no username in URL) to avoid Credential Manager
# caching a bogus "x-access-token" entry. Auth via -c http.extraheader.
cd "$WORK_DIR"
PLAIN_URL="https://github.com/${REPO_FULL}.git"
GIT_AUTH_HDR="Authorization: Bearer ${GITHUB_TOKEN}"

if ! git -c "http.extraheader=${GIT_AUTH_HDR}" clone --quiet "$PLAIN_URL" repo 2>/dev/null; then
  mkdir -p repo
  cd repo
  git init -b main -q
  git remote add origin "$PLAIN_URL"
  cd ..
fi

cd repo
# Ensure we're on main
git checkout -B main -q 2>/dev/null || true
# Wipe everything except .git, then copy fresh
find . -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +
cp -R "$ROOT_DIR/$SOURCE_DIR/." .

git add -A
git -c user.email="autopilot@cybertruck.local" \
    -c user.name="Cybertruck Autopilot" \
    commit -q -m "deploy: $(date -u +%Y-%m-%dT%H:%M:%SZ)" 2>/dev/null || true

git -c "http.extraheader=${GIT_AUTH_HDR}" push -q -u origin main 2>/dev/null

# 4. Enable Pages on main / (root) — idempotent (POST returns 409 if already enabled)
PAGES_BODY='{"source":{"branch":"main","path":"/"}}'
PAGES_STATUS="$(curl -sS -o /dev/null -w '%{http_code}' -X POST \
  -H "$AUTH_HEADER" -H "$ACCEPT_HEADER" -H "$API_VERSION_HEADER" \
  -H "Content-Type: application/json" \
  -d "$PAGES_BODY" \
  "$API/repos/$REPO_FULL/pages")"
# 201 = created, 409 = already exists, 422 = also already-exists in some cases

# Build the predicted URL (works for user.github.io/repo)
GH_USER_LOWER="$(echo "$GH_USER" | tr '[:upper:]' '[:lower:]')"
PAGES_URL="https://${GH_USER_LOWER}.github.io/${REPO_NAME}/"

echo "deployed: $PAGES_URL"
echo "pages_status: $PAGES_STATUS"

# 5. Append to publish-log
{
  echo ""
  echo "## $(date -u +%Y-%m-%d\ %H:%M)"
  echo "- platform: github-pages"
  echo "- url: $PAGES_URL"
  echo "- experiment: $REPO_NAME"
  echo "- repo: https://github.com/$REPO_FULL"
} >> "$ROOT_DIR/state/publish-log.md"
