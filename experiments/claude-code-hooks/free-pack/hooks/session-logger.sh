#!/usr/bin/env bash
# session-logger.sh
#
# Claude Code SessionStart|SessionEnd|Stop hook. Appends one timestamped
# line to ~/.claude/sessions.log per event. Zero-config audit trail so
# you can answer "when did I run Claude on this project, and for how
# long?" without fishing around in the terminal history.
#
# Line format:
#   <ISO-8601 UTC timestamp> <event> session=<id> cwd=<working-dir>
#
# Example:
#   2026-04-13T22:35:17Z SessionStart session=abc12345 cwd=/home/me/proj
#   2026-04-13T23:02:44Z Stop         session=abc12345 cwd=/home/me/proj
#
# Stdin: JSON with hook_event_name, session_id, cwd
# Exit:  always 0 — a logging failure must NEVER block Claude.

set -u

LOG_DIR="${HOME}/.claude"
LOG_FILE="${LOG_DIR}/sessions.log"

mkdir -p "$LOG_DIR" 2>/dev/null || true
: >> "$LOG_FILE" 2>/dev/null || true

payload=$(cat 2>/dev/null || true)

extract() {
  key=$1
  printf '%s' "$payload" \
    | tr -d '\n' \
    | sed -n "s/.*\"${key}\"[[:space:]]*:[[:space:]]*\"\\([^\"\\\\]*\\(\\\\.[^\"\\\\]*\\)*\\)\".*/\\1/p" \
    | head -n1
}

event=$(extract hook_event_name)
session=$(extract session_id)
cwd=$(extract cwd)

: "${event:=unknown}"
: "${session:=-}"
: "${cwd:=-}"

ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || date -u 2>/dev/null || echo "unknown-time")

# Short session id for readability (first 8 chars).
short_session=$(printf '%s' "$session" | cut -c1-8)
[ -z "$short_session" ] && short_session="-"

printf '%s %-12s session=%s cwd=%s\n' \
  "$ts" "$event" "$short_session" "$cwd" \
  >> "$LOG_FILE" 2>/dev/null || true

exit 0
