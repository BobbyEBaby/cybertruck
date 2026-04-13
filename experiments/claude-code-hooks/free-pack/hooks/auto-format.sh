#!/usr/bin/env bash
# auto-format.sh
#
# Claude Code PostToolUse:Write|Edit hook. Runs an appropriate formatter
# on the file Claude just edited, if a formatter is installed. Silent
# no-op when the formatter isn't on PATH — never blocks the hook chain
# on a missing dep.
#
# Formatter map:
#   .py                                  -> black, fallback to ruff format
#   .js .jsx .ts .tsx .json .css .scss
#   .html .md .yaml .yml                 -> prettier (direct or npx)
#   .go                                  -> gofmt
#   .rs                                  -> rustfmt
#   .sh .bash                            -> shfmt
#   .rb                                  -> rubocop -a
#   .lua                                 -> stylua
#   .tf .tfvars                          -> terraform fmt
#
# Stdin: JSON with tool_input.file_path
# Exit:  always 0 — formatter errors print to stderr but do not block.

set -u

payload=$(cat 2>/dev/null || true)

path=$(printf '%s' "$payload" \
  | tr -d '\n' \
  | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"\\]*\(\\.[^"\\]*\)*\)".*/\1/p' \
  | head -n1)

[ -z "$path" ] && exit 0
[ -f "$path" ] || exit 0

have() { command -v "$1" >/dev/null 2>&1; }

run() {
  # Run formatter silently; surface failures to stderr but do not
  # propagate the exit code.
  if ! "$@" >/dev/null 2>&1; then
    echo "[auto-format] $1 failed on $path (continuing)" >&2
  fi
}

case "$path" in
  *.py)
    if have black; then run black --quiet "$path"
    elif have ruff; then run ruff format "$path"
    fi ;;
  *.js|*.jsx|*.ts|*.tsx|*.mjs|*.cjs|*.json|*.css|*.scss|*.html|*.md|*.yaml|*.yml)
    if have prettier; then
      run prettier --write --log-level silent "$path"
    elif have npx && npx --no-install prettier --version >/dev/null 2>&1; then
      run npx --no-install prettier --write --log-level silent "$path"
    fi ;;
  *.go)
    have gofmt && run gofmt -w "$path" ;;
  *.rs)
    have rustfmt && run rustfmt --quiet "$path" ;;
  *.sh|*.bash)
    have shfmt && run shfmt -w "$path" ;;
  *.rb)
    have rubocop && run rubocop -a --format quiet "$path" ;;
  *.lua)
    have stylua && run stylua "$path" ;;
  *.tf|*.tfvars)
    have terraform && run terraform fmt "$path" ;;
esac

exit 0
