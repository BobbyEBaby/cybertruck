# cc-hooks-starter (free pack)

Five zero-dependency Claude Code hooks, installable with one command.

This is the **free tier** of a freemium bundle. An extended pack with 15+
hooks and walkthroughs will be available separately (details at the
bottom).

## What you get

| Hook | Event | What it does |
|---|---|---|
| `dangerous-command-guard.sh` | `PreToolUse:Bash` | Blocks `rm -rf /`, `dd of=/dev/sdX`, `mkfs`, fork bombs, `chmod 777 /`, `shutdown`/`reboot`, and other classics. One env-var override for when you actually mean it. |
| `secret-file-guard.sh` | `PreToolUse:Read\|Write\|Edit` | Stops Claude from reading or writing `.env`, `*.pem`, `*.key`, `id_rsa`, `secrets/**`, `~/.aws/credentials`, kubeconfig, GCP service-account JSONs. Allowlist file for exceptions. |
| `protected-branch-guard.sh` | `PreToolUse:Bash` | Blocks `git commit` / `git push` / `git reset --hard` / `git rebase -i` on `main`, `master`, `release/*`, `hotfix/*`. One-shot flag-file override. |
| `auto-format.sh` | `PostToolUse:Write\|Edit` | Runs `black`, `prettier`, `gofmt`, `rustfmt`, `shfmt`, `rubocop`, `stylua`, or `terraform fmt` on whatever Claude just edited. Silent no-op if the formatter isn't installed. |
| `session-logger.sh` | `SessionStart`/`SessionEnd`/`Stop` | Appends a one-line audit entry to `~/.claude/sessions.log` so you can answer "when did I run Claude on this project, and for how long?" without digging through shell history. |

All hooks are plain `bash` (no Python, no Node, no `jq`). You can read
every one of them in a minute and decide for yourself whether it belongs
in your environment. **Read them before you install them.** That goes
for every third-party hook, not just this one.

## Install (one command)

From inside Claude Code:

```text
/plugin marketplace add BobbyEBaby/cybertruck
/plugin install cc-hooks-starter@cc-hooks-starter-marketplace
```

> **Heads-up:** while this pack lives under
> `experiments/claude-code-hooks/free-pack/` in the Cybertruck Autopilot
> monorepo, you may need to point `/plugin marketplace add` at a branch
> or subdirectory once we split it out into its own repo. Until then,
> cloning and manually sourcing the hooks from your `settings.json`
> also works — see "Manual install" below.

Restart Claude Code. You're done.

## Manual install

If you'd rather wire it up yourself (or you're on a Claude Code version
without plugin marketplaces), drop this into your
`~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {"type": "command", "command": "/absolute/path/to/cc-hooks-starter/hooks/dangerous-command-guard.sh"},
          {"type": "command", "command": "/absolute/path/to/cc-hooks-starter/hooks/protected-branch-guard.sh"}
        ]
      },
      {
        "matcher": "Read|Write|Edit",
        "hooks": [
          {"type": "command", "command": "/absolute/path/to/cc-hooks-starter/hooks/secret-file-guard.sh"}
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {"type": "command", "command": "/absolute/path/to/cc-hooks-starter/hooks/auto-format.sh"}
        ]
      }
    ],
    "SessionStart": [
      {"hooks": [{"type": "command", "command": "/absolute/path/to/cc-hooks-starter/hooks/session-logger.sh"}]}
    ],
    "SessionEnd": [
      {"hooks": [{"type": "command", "command": "/absolute/path/to/cc-hooks-starter/hooks/session-logger.sh"}]}
    ],
    "Stop": [
      {"hooks": [{"type": "command", "command": "/absolute/path/to/cc-hooks-starter/hooks/session-logger.sh"}]}
    ]
  }
}
```

Then `chmod +x cc-hooks-starter/hooks/*.sh`.

## Overriding a hook when you actually mean it

Every safety hook has an explicit, audited override path. None of them
are "hold my beer" escape hatches — you have to type something specific,
and the hook logs the override to stderr so you see it.

- **dangerous-command-guard:** set `CC_HOOK_ALLOW_DANGEROUS=1` in the
  shell environment running Claude Code. Good for exactly the one
  session where you need to `mkfs` a test image.
- **secret-file-guard:** add the full path to
  `~/.claude/secret-file-guard.allowlist` (one per line, `#` comments
  supported).
- **protected-branch-guard:** from your repo root,
  `mkdir -p .claude && touch .claude/allow-protected-branch`. This is a
  one-shot flag — it gets deleted after the next bash command.

## Design principles

1. **Zero dependencies.** Only `bash`, `sed`, `grep`, `tr`, `date`,
   `basename`, `dirname`, `cat`, `printf`, `mkdir`. No `jq`, no Python,
   no Node.
2. **Fail open on parse errors.** If a hook can't parse stdin, it
   returns 0. A false block is worse than a false pass — the model and
   the user both have eyes on commands; the hook is a tripwire, not a
   firewall.
3. **Logging never blocks.** `session-logger.sh` always exits 0. If
   your home directory is full, Claude shouldn't stop working.
4. **Auditable rules.** Every block condition in every hook is a plain
   `case` statement or a short allowlist. You can read the whole set
   of rules in under five minutes.

## Troubleshooting

**Hook isn't firing.** Check that the script is executable
(`ls -l hooks/*.sh` — you should see `-rwxr-xr-x`). Claude Code won't
run a non-executable hook command.

**Hook is firing on the wrong file.** Read the hook source. Every rule
is a plain pattern you can see. If a pattern is wrong, open an issue.

**I don't want one of the hooks.** Edit the plugin's `plugin.json` (or
your `~/.claude/settings.json` for the manual-install path) and delete
the entry. Or point the `command` at `/bin/true` to disable that hook
specifically without removing the config.

## Not in the free pack (yet)

These are in the paid extended pack — they need more setup, more
walkthroughs, or more per-language adapters than the free tier should
carry:

- Language-chain formatters (black+isort+ruff chain, prettier+eslint,
  gofmt+goimports+golangci-lint, rustfmt+clippy, etc.)
- License / CVE audit on `npm install` / `pip install` / `cargo add`
- Destructive-SQL guard (intercepts raw SQL in bash for `DROP TABLE`,
  `TRUNCATE`, `DELETE FROM ...` without a `WHERE`)
- Cost-budget estimator (warns when hourly API spend exceeds a cap)
- Slack / Discord audit webhook
- Diff-review gate for protected-path edits
- TDD enforcer (blocks new source files without matching tests)
- Migration reviewer
- Test-runner on save (actually runs the tests; returns failures to Claude)
- Daily digest hook
- "DO NOT COMMIT" marker guard
- Custom-hook template set (walkthroughs for writing your own)
- Plus per-hook walkthroughs: what it does, when to use it, when NOT to
  use it, adaptation recipes.

(Paid pack status: building. When it's up, a link will land here.)

## License

MIT. Do what you want. Don't blame us if a hook you didn't read eats
your homework. (That's why we keep them short enough to read.)
