#!/usr/bin/env bash
# protected-branch-guard.sh
#
# Claude Code PreToolUse:Bash hook. Blocks destructive git operations
# against protected branches unless you've opted in via a one-shot
# flag file. Safer than relying on "I'll be careful" after a long
# coding session.
#
# Protected branches (default): main, master, trunk, prod, production,
# release/*, hotfix/*.
#
# Blocked on a protected branch:
#   - git commit         (direct commit to main — make a feature branch)
#   - git push           (any push while HEAD is on main)
#   - git push --force / -f / --force-with-lease
#   - git reset --hard / --keep
#   - git clean -fdx / -fdX
#   - git rebase -i
#   - git branch -D / -d <current-protected-branch>
#
# One-shot override (from repo root):
#   mkdir -p .claude && touch .claude/allow-protected-branch
# The flag file is deleted after the NEXT bash command passes the hook,
# so an override lets through exactly one command.
#
# Stdin: JSON with tool_input.command
# Exit:  0 allow, 2 block.

set -u

payload=$(cat || true)

cmd=$(printf '%s' "$payload" \
  | tr -d '\n' \
  | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"\\]*\(\\.[^"\\]*\)*\)".*/\1/p' \
  | head -n1)

[ -z "$cmd" ] && exit 0

# Fast reject: if it isn't a git command, we have nothing to say.
case "$cmd" in
  *"git "*|*"git	"*) : ;;
  *) exit 0 ;;
esac

# Not in a git repo -> no branch -> nothing to protect.
branch=$(git symbolic-ref --short HEAD 2>/dev/null || true)
[ -z "$branch" ] && exit 0

protected=0
case "$branch" in
  main|master|trunk|prod|production) protected=1 ;;
  release/*|hotfix/*) protected=1 ;;
esac

[ "$protected" -eq 0 ] && exit 0

# One-shot override: if the flag file exists, consume it and allow.
flag=".claude/allow-protected-branch"
if [ -f "$flag" ]; then
  rm -f "$flag" 2>/dev/null || true
  echo "[protected-branch-guard] override flag consumed, allowing one command on '$branch'" >&2
  exit 0
fi

block() {
  why=$1
  {
    echo "[protected-branch-guard] BLOCKED on branch '$branch'"
    echo "[protected-branch-guard] Reason: $why"
    echo "[protected-branch-guard] Command: $cmd"
    echo "[protected-branch-guard] One-shot override (from repo root):"
    echo "    mkdir -p .claude && touch .claude/allow-protected-branch"
    echo "[protected-branch-guard] The flag is deleted after one allowed command."
  } >&2
  exit 2
}

case "$cmd" in
  *"git commit"*)
    block "direct commit to protected branch — create a feature branch first" ;;
  *"git push --force"*|*"git push -f"*|*"git push --force-with-lease"*)
    block "force push to protected branch" ;;
  *"git push"*)
    block "push while HEAD is on protected branch" ;;
  *"git reset --hard"*|*"git reset --keep"*)
    block "git reset --hard on protected branch" ;;
  *"git clean -fdx"*|*"git clean -fdX"*|*"git clean -fd "*)
    block "git clean -fdx on protected branch" ;;
  *"git rebase -i"*)
    block "interactive rebase on protected branch" ;;
  *"git branch -D "*|*"git branch -d "*)
    case "$cmd" in
      *"git branch -D $branch"*|*"git branch -d $branch"*)
        block "deleting the protected branch you're currently on" ;;
    esac ;;
esac

exit 0
