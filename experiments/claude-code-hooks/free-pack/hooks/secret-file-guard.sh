#!/usr/bin/env bash
# secret-file-guard.sh
#
# Claude Code PreToolUse:Read|Write|Edit hook. Blocks reads and writes
# to files whose names match known secret / credential patterns, so
# Claude never sees their contents and never overwrites them.
#
# Patterns blocked:
#   - .env, .env.*, *.env
#   - credentials.json / credentials.yaml / credentials.yml / credentials
#   - *.pem, *.key, *.p12, *.pfx, *.jks (private keys / keystores)
#     (allows *.pub.pem, *.cert.pem, *.crt.pem — those are public)
#   - id_rsa, id_ed25519, id_ecdsa, id_dsa (ssh keys, any location)
#   - **/secrets/**, **/.secrets/**
#   - **/.aws/credentials
#   - **/.kube/config (kubeconfig)
#   - *-service-account*.json, **/.gcp/*.json (gcp service-account keys)
#   - **/.ssh/id_* (except .pub)
#
# This is a name-based safety hook. It does NOT scan file contents — a
# secret stored in "notes.md" will still go through. Pair with a
# content-scanning hook for full coverage.
#
# Allowlist: put absolute paths (one per line) into
#   ~/.claude/secret-file-guard.allowlist
# Lines starting with # are comments.
#
# Stdin:  JSON with tool_input.file_path
# Exit:   0 allow, 2 block.

set -u

payload=$(cat || true)

path=$(printf '%s' "$payload" \
  | tr -d '\n' \
  | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"\\]*\(\\.[^"\\]*\)*\)".*/\1/p' \
  | head -n1)

[ -z "$path" ] && exit 0

base=$(basename -- "$path" 2>/dev/null || echo "$path")
dir=$(dirname -- "$path" 2>/dev/null || echo "")

block() {
  reason=$1
  {
    echo "[secret-file-guard] BLOCKED: $path"
    echo "[secret-file-guard] Rule: $reason"
    echo "[secret-file-guard] Name-based secret pattern matched — Claude will not"
    echo "[secret-file-guard] read or write this file."
    echo "[secret-file-guard] If this is a false positive, add the full path to:"
    echo "    \$HOME/.claude/secret-file-guard.allowlist"
    echo "[secret-file-guard] (one absolute path per line; lines starting with # are comments)"
  } >&2
  exit 2
}

# Allowlist short-circuit.
allowlist="${HOME}/.claude/secret-file-guard.allowlist"
if [ -f "$allowlist" ]; then
  abs_path=$path
  case "$path" in
    /*) : ;;
    *)
      if abs_dir=$(cd "$dir" 2>/dev/null && pwd); then
        abs_path="$abs_dir/$base"
      fi
      ;;
  esac
  while IFS= read -r line || [ -n "$line" ]; do
    [ -z "$line" ] && continue
    case "$line" in \#*) continue ;; esac
    if [ "$line" = "$path" ] || [ "$line" = "$abs_path" ]; then
      exit 0
    fi
  done < "$allowlist"
fi

# Name-based checks (most specific first).
case "$base" in
  .env|.env.*|*.env)
    block "dotenv file (.env / .env.*)" ;;
  credentials|credentials.json|credentials.yaml|credentials.yml)
    block "credentials file" ;;
  id_rsa|id_ed25519|id_ecdsa|id_dsa)
    block "ssh private key" ;;
  *.p12|*.pfx|*.jks)
    block "keystore file" ;;
  *.pem)
    case "$base" in
      *.pub.pem|*.cert.pem|*.crt.pem|*-cert.pem|*-ca.pem) : ;;
      *) block "*.pem (likely private key)" ;;
    esac ;;
  *.key)
    case "$base" in
      *.pub.key|*.cert.key) : ;;
      *) block "*.key (likely private key)" ;;
    esac ;;
esac

# Path-based checks.
case "$path" in
  */secrets/*|*/.secrets/*)
    block "secrets/ directory" ;;
  */.aws/credentials|*/.aws/credentials.*)
    block "aws credentials" ;;
  */.kube/config|*/.kube/config.*)
    block "kubeconfig" ;;
  */.gcp/*.json|*service-account*.json|*service_account*.json)
    block "gcp service-account key" ;;
  */.ssh/id_*)
    case "$path" in
      *.pub) : ;;
      *) block "ssh private key under ~/.ssh" ;;
    esac ;;
esac

exit 0
