#!/usr/bin/env bash
# dangerous-command-guard.sh
#
# Claude Code PreToolUse:Bash hook. Blocks destructive shell commands
# before Claude Code runs them. Exits with code 2 + a reason on stderr,
# which Claude Code surfaces to the model so it can pick a safer path.
#
# Patterns blocked (auditable list — read and tune):
#   - rm -rf on /, ~, or /* (and --no-preserve-root)
#   - dd writing to a block device (/dev/sd*, /dev/nvme*, etc.)
#   - mkfs.* / mkfs (filesystem format)
#   - classic fork bomb :(){ :|:& };:
#   - chmod 777 / chown -R root on /
#   - shutdown / reboot / halt / poweroff
#   - redirect to /dev/sd* or /dev/nvme* (raw block-device write)
#
# Override: set CC_HOOK_ALLOW_DANGEROUS=1 in the shell environment
# that launched Claude Code for a single session. The override is
# logged to stderr so you see when it fires.
#
# Stdin:  JSON with {"tool_name":"Bash","tool_input":{"command":"..."}}
# Stdout: (none on allow)
# Exit:   0 allow, 2 block

set -eu

payload=$(cat)

# Best-effort JSON field extraction without jq. Pulls the first
# "command":"..." value. Backslash-escaped quotes are tolerated; we
# accept that pathological inputs may slip through (the cost of a
# miss is low — you still see the command in Claude's normal flow).
cmd=$(printf '%s' "$payload" \
  | tr -d '\n' \
  | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"\\]*\(\\.[^"\\]*\)*\)".*/\1/p' \
  | head -n1)

# If we can't find a command string, don't block — let Claude proceed.
# False-blocks are worse than false-passes here.
[ -z "$cmd" ] && exit 0

override_active=0
if [ "${CC_HOOK_ALLOW_DANGEROUS:-}" = "1" ]; then
  override_active=1
fi

block() {
  reason=$1
  rule=$2
  {
    echo "[dangerous-command-guard] BLOCKED: $reason"
    echo "[dangerous-command-guard] Rule matched: $rule"
    echo "[dangerous-command-guard] Command: $cmd"
    if [ "$override_active" = "1" ]; then
      echo "[dangerous-command-guard] CC_HOOK_ALLOW_DANGEROUS=1 — override active, allowing."
    else
      echo "[dangerous-command-guard] Single-command override:"
      echo "    export CC_HOOK_ALLOW_DANGEROUS=1 && <re-issue> && unset CC_HOOK_ALLOW_DANGEROUS"
    fi
  } >&2
  if [ "$override_active" = "1" ]; then
    exit 0
  fi
  exit 2
}

case "$cmd" in
  *"rm -rf /"*|*"rm -rf /*"*|*"rm -fr /"*|*"rm -fr /*"*|*"rm -Rf /"*|*"rm -rf --no-preserve-root"*|*"rm -fr --no-preserve-root"*|*"--no-preserve-root"*)
    block "rm -rf on filesystem root" "rm -rf / (or --no-preserve-root)" ;;
  *"rm -rf ~"*|*"rm -fr ~"*|*"rm -rf \$HOME"*|*"rm -rf \"\$HOME\""*)
    block "rm -rf on home directory" "rm -rf ~" ;;
  *"dd if=/dev/zero of=/dev/"*|*"dd if=/dev/random of=/dev/"*|*"dd if=/dev/urandom of=/dev/"*|*"dd of=/dev/sd"*|*"dd of=/dev/nvme"*|*"dd of=/dev/hd"*|*"dd of=/dev/xvd"*|*"dd of=/dev/vd"*)
    block "dd overwriting a block device" "dd of=/dev/*" ;;
  *"mkfs."*|*"mkfs "*)
    block "mkfs (filesystem format)" "mkfs" ;;
  *":(){ :|:& };:"*|*":(){:|:&};:"*|*":(){ :|: &};:"*)
    block "classic fork bomb" ":(){ :|:& };:" ;;
  *"chmod -R 777 /"*|*"chmod 777 /"*|*"chmod -R 0777 /"*|*"chmod -Rf 777 /"*)
    block "chmod 777 on filesystem root" "chmod -R 777 /" ;;
  *"chown -R root /"*|*"chown -R root:root /"*|*"chown -Rf root /"*)
    block "chown -R root on filesystem root" "chown -R root /" ;;
  *" shutdown "*|*";shutdown "*|*"&&shutdown"*|*"|shutdown"*|*"shutdown -h"*|*"shutdown -r"*|*"shutdown now"*)
    block "shutdown command" "shutdown" ;;
  *" reboot"*|*";reboot"*|*"&&reboot"*|*"|reboot"*|*"/sbin/reboot"*)
    block "reboot command" "reboot" ;;
  *" halt"*|*";halt"*|*"&&halt"*|*"/sbin/halt"*)
    block "halt command" "halt" ;;
  *"poweroff"*)
    block "poweroff command" "poweroff" ;;
  *"> /dev/sd"*|*">/dev/sd"*|*"> /dev/nvme"*|*">/dev/nvme"*|*"> /dev/hd"*|*">/dev/hd"*)
    block "direct block-device redirect" "> /dev/sdX" ;;
esac

exit 0
