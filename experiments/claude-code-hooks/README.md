# experiment: claude-code-hooks

## What this is
B-011 — the second digital asset in the Cybertruck Autopilot's Gumroad-style
backlog. A **freemium dual-channel** pack of Claude Code hook recipes:

1. **Free layer** — 5–8 curated production-ready hooks published as a GitHub
   repo, installable inside Claude Code itself via
   `/plugin marketplace add BobbyEBaby/<repo>`. Distribution runs on
   Anthropic's plugin marketplace infrastructure. Lead-gen for the paid pack.
2. **Paid layer** — 15–18 extended hooks with walkthroughs, templates,
   failure-mode notes, and per-language adapters. Sold as a single markdown
   file (optionally compiled to PDF locally) on a Gumroad- or Lemon-Squeezy-
   style storefront.

This is the **scoping run** (remote run #65, 2026-04-13 21:31 UTC — the first
run after the B-011 48-hour post-B-002-ship gate tripped at ≈ 21:15 UTC). The
product isn't built yet. This README + the sibling `PLATFORM.md` are the
scoping artifacts. Next runs will build the free hooks, then the paid pack,
then `ship.md` handoffs.

## Why hook recipes (candidate #1 per 03-refresh 2026-04-12)
The 03-Gumroad refresh surfaced Claude Code's plugin marketplace as the first
B-011 candidate with a built-in distribution channel beyond cold-posting on
Reddit/HN. Candidate ranking from that refresh:

1. **Claude Code hook recipes** — hooks are an official plugin type, the
   freemium dual-channel fits cleanly (free hooks in the marketplace,
   extended pack paid), and we run hooks in this project so the authentic-
   authority angle is real.
2. Claude Code CLAUDE.md templates pack — could also be a plugin (skills
   that scaffold CLAUDE.md files), but the free/paid split is less natural.
3. Agent operating-loop starter kit — doesn't map to the plugin model.

Hook recipes are **strictly dominant** because of the plugin-marketplace
channel. Robert has not vetoed; default pick is hook recipes.

## Hypothesis

**Audience:** developers who run Claude Code daily, have read enough of the
docs to know hooks exist, but have not set up more than one or two of their
own. They want boilerplate that works — safety guards, auto-formatters,
test runners, session loggers — without hand-wiring every `settings.json`
block. They already pay for Claude API usage and spend $20–$200/month on dev
tools.

**Value proposition (free tier):** "here are 5 hooks you can install in 30
seconds that make Claude Code safer and more automated. No config file to
hand-edit. One `/plugin marketplace add` command." The free tier alone has to
be good enough that someone posts about it in a Claude Code thread.

**Value proposition (paid tier):** "here are 15+ hooks that took me a week
to figure out, with walkthroughs explaining exactly what each one does,
when to use it, and how to adapt it. Plus templates for writing your own."
The paid tier has to feel like a time-saver, not a content dump.

**Why this audience would pay $5–$9 for the paid pack:**
- Already paying for Claude API usage — price point is negligible
- One avoided `rm -rf` incident, one `.env` leak, one test-before-commit
  catch pays for the pack 50×
- The hooks themselves are scripts they could write — but the failure modes
  and "when NOT to use this" notes are the real value

**Why they might NOT pay:**
- Anyone serious enough to read docs can write their own hooks in an hour
- The free plugin marketplace creates the expectation that Claude Code
  tooling should be free
- Unknown-seller trust gap (same problem B-002 has)
- The Claude Code plugin ecosystem has 2,400+ skills already — a paid pack
  has to meaningfully outshine free alternatives

## Free pack outline (targeting 5–8 hooks)
Working list for the next build run. Each free hook must be: (a) immediately
useful, (b) safe by default, (c) documented inline, (d) zero-dependency
(pure bash / POSIX sh, no Python, no npm installs). Final selection happens
in run #66.

1. **Dangerous-command guard** (`PreToolUse: Bash`) — blocks `rm -rf /`,
   `rm -rf ~`, `git push --force` to protected branches, `chmod -R 777 /`,
   `dd of=/dev/sd*`. Configurable allowlist of destructive commands the user
   actually wants.
2. **Secret file guard** (`PreToolUse: Read/Write/Edit`) — blocks reads and
   writes to `.env`, `.env.*`, `secrets/`, `credentials.json`, `*.pem`,
   `*.key`. Returns exit code 2 with a warning.
3. **Session logger** (`SessionStart` + `SessionEnd` + `Stop`) — appends
   timestamped session start/stop lines to `~/.claude/sessions.log`. One-
   file audit trail with zero config.
4. **Auto-format on edit** (`PostToolUse: Write/Edit`) — runs a formatter if
   the file extension matches (`black` for `.py`, `prettier` for `.js/.ts`,
   `gofmt` for `.go`, `rustfmt` for `.rs`). Silent no-op if the formatter
   isn't installed.
5. **Test-after-edit nudge** (`PostToolUse: Write/Edit`) — if the edited
   file has a matching `test_*.py` / `*.test.js` / `*_test.go`, prints a
   reminder in stdout that Claude sees ("consider running the tests for
   this file").
6. **Desktop notifier** (`Stop`) — fires a platform-native desktop
   notification when Claude finishes a response (macOS `osascript`, Linux
   `notify-send`, WSL `wsl-notify-send`). Useful for long runs.
7. **Protected branch guard** (`PreToolUse: Bash`) — blocks `git commit`
   and `git push` on `main` / `master` / `release/*` unless the command
   already contains an explicit `--force-with-lease` or the user has
   opted in via a local flag file.
8. **Token-budget reminder** (`UserPromptSubmit`) — appends a one-line
   reminder to the user's prompt showing approximate loaded-context size
   in tokens and a warning if it exceeds a configurable soft cap.

## Paid pack outline (targeting 15–18 hooks + walkthroughs)
Working list for run #67. Paid hooks can depend on common interpreters
(Python 3 / Node 18+) but must still list deps explicitly. Each hook gets
a walkthrough section: what it does, when to use it, when NOT to use it,
adaptation recipes. Final selection in run #67.

1. Everything in the free pack, with extended walkthroughs (the free
   hooks are included — the paid version is additive, not a wedge).
2. **Language-chain formatters** (per-language): Python (black+isort+ruff),
   JS/TS (prettier+eslint --fix), Go (gofmt+goimports+golangci-lint --fix),
   Rust (rustfmt+clippy --fix), Ruby (rubocop -a), Shell (shfmt+shellcheck).
3. **License/CVE audit on install** (`PreToolUse: Bash`) — intercepts
   `npm install`, `pip install`, `cargo add`, `go get`, `brew install`
   and runs a lightweight advisory check via `osv-scanner` or similar
   (hook ships without the scanner; docs explain how to install).
4. **Destructive-SQL guard** (`PreToolUse: Bash`) — pattern-matches raw
   SQL in bash commands for `DROP TABLE`, `TRUNCATE`, `DELETE FROM ...`
   without a `WHERE`, and requires an explicit opt-in file.
5. **Git-history safety** (`PreToolUse: Bash`) — blocks `git reset --hard`,
   `git clean -fdx`, `git checkout .`, `git rebase -i`, `git push --force`
   to main without a confirmation flag file.
6. **Cost-budget estimator** (`UserPromptSubmit` + `PostToolUse`) —
   estimates Claude API token cost of the current context and the
   recent Bash/Read/Write spend. Warn when hourly cost exceeds a cap.
7. **Slack / Discord audit webhook** (`Stop`) — posts a one-line summary
   of the just-finished response to a webhook URL. Team-mode only.
   Configurable redaction patterns.
8. **Diff-review gate** (`PreToolUse: Write/Edit` for protected globs) —
   when a file in a configurable `protected_paths` list would be edited,
   print the proposed diff to stdout and require the user to confirm
   via a flag file before the next run.
9. **TDD enforcer** (`PreToolUse: Write/Edit`) — when creating a new
   source file, block unless a matching test file already exists. Opt-in
   per-project via a `.claude/tdd-required` flag.
10. **Migration reviewer** (`PreToolUse: Write/Edit` on migration dirs) —
    print the current migration file count, warn if the file being added
    isn't the next in sequence, flag downgrade steps.
11. **Test-runner on save** (`PostToolUse: Write/Edit`) — actually runs
    the matching test (pytest / jest / go test) and returns the output
    to Claude so it sees failures immediately.
12. **Subagent spawn-on-PR-touch** (`PostToolUse: Bash` on `gh pr`) —
    auto-dispatches the code-reviewer subagent on PR creation. Only
    fires if the user has the reviewer agent installed.
13. **Daily digest hook** (`SessionEnd`) — appends a 1-line run summary
    (files touched, bash commands run, tokens spent) to a daily log
    and writes a weekly rollup every Sunday.
14. **Claude-vs-human diff logger** (`PostToolUse: Edit`) — records the
    before/after of each edit to a per-session JSONL file. Useful for
    retrospective analysis.
15. **"Do not commit" marker guard** (`PreToolUse: Bash` on `git commit`) —
    scans staged files for `DO NOT COMMIT`, `TODO(security)`, `XXX`,
    `FIXME(release-blocker)` comments and blocks the commit.
16. **Dependency-freeze guard** (`PreToolUse: Write` on `package.json`,
    `requirements.txt`, `Cargo.toml`) — requires the user to tag the
    reason in the file itself or via an opt-in flag.
17. **Custom-hook template set** — walkthroughs + copy-pasteable Python
    and Node.js scaffolds for writing your own hooks, including the JSON
    protocol, exit-code semantics, and stdin/stdout contract.
18. **Hook-config manager** — a pair of bash helpers (`hook-enable`,
    `hook-disable`) that let users toggle installed hooks without
    hand-editing `settings.json`.

**Budget:** 15 minimum, 18 maximum. Cap at 18 to keep the deliverable from
bloating into a "100 hooks mega-bundle" that nobody reads.

## Platform decision (see `PLATFORM.md`)
**Default pick: Gumroad** (existing account from B-002, single-storefront
cross-sell benefit with Power Prompts, zero new setup). **Objectively
cheaper alternative: Lemon Squeezy** (5%+$0.50 vs Gumroad's
10%+$0.50+processor — ~30% more revenue per sale at our $3–$5 price points).
Full fee table and decision logic in the sibling `PLATFORM.md`. Robert can
override via `human_outbox/` if he prefers LS; the handoff note is
`human_inbox/0009-b011-platform-decision.md`.

If Robert does not override by the next remote run, **the build proceeds
on Gumroad by default** — do not stall the loop waiting for an answer.

## Pricing
- **Free pack:** free, GitHub repo, `/plugin marketplace add` installable.
- **Paid pack:** **$5 fixed** (default, fits Robert's current Gumroad tier
  which does not support PWYW-with-minimum per the B-002 listing note).
  Alternative: $7 fixed if the paid pack ends up shipping 18 hooks + full
  walkthroughs (adjust in ship.md based on final asset size).
- **Why $5 fixed:** Gumroad 10% + $0.50 + ~3% processor on $5 nets ~$3.95.
  At $3 net is only ~$2.10 — the marginal dollar from pricing at $5 is
  worth more than the conversion cost of the higher price.
- **Why not PWYW:** Robert's Gumroad tier doesn't support PWYW-with-minimum
  (per B-002 status note — he had to drop to $3 fixed). Same constraint here.
- **Why not higher than $7:** unknown-seller trust floor. $5–$7 fits the
  "impulse buy for a developer" category. $15 triggers "read reviews first"
  which we don't have.

## Distribution
Ordered by expected leverage:

1. **Free plugin listed on the Claude Code plugin marketplace** (primary —
   this is the whole reason hook recipes is candidate #1). Submit to the
   official Anthropic marketplace at claude.ai/settings/plugins/submit
   after the free repo is live. Human-reviewed but free to submit.
2. **awesome-claude-code PR** (38.1k-star repo per the 01-refresh — the
   highest sustained-traffic free channel for Claude Code tooling). PR the
   free pack in after the repo is live. Also PR the paid pack link in a
   separate "paid" or "commercial" section if awesome-claude-code has one
   that accepts commercial entries.
3. **Show HN post** — "I built 8 Claude Code hooks so you don't have to"
   or similar. Lead with the safety guards. Post Monday/Tuesday per the
   01-refresh HN cadence guidance. One shot, no engagement in comments
   per CLAUDE.md rules.
4. **r/SideProject post** — honest "I built this" post, link to the
   free repo first (trust signal), paid pack as the follow-up. Honor
   the no-engagement rule.
5. **r/ClaudeAI post** — specifically for the Claude Code audience.
   Lead with the free pack, mention the paid pack in the footer. Blocked
   on REDDIT_* credentials (same blocker as B-003).
6. **claude-hub.com submission** — community aggregator (per 01-refresh).
7. **Footer links from live browser tools** — add a one-line "Check out
   the Claude Code hooks pack" footer on prompt-cleaner, llm-cost-calculator,
   and claude-md-linter once they're all live. One-touch cross-sell from
   the existing tools.
8. **Gumroad Discover** — avoid initially (30% fee vs 10% direct). Only
   enable after 14 days of zero direct traffic.

## Measurement window
**14 days** from the day the Gumroad (or LS) listing goes live. At the
14-day mark, regardless of outcome, write a runlog entry with:
- Views on the listing
- Downloads (free marketplace installs vs paid)
- Revenue (gross, net after fees)
- Any public feedback (Reddit, HN, PR comments, DMs) — log only, do not
  reply per CLAUDE.md rules
- Honest read: did the freemium dual-channel work as a funnel?

## Honest expectations
Median outcome for an unknown seller's first freemium-funnel digital
product with zero paid promotion is **zero paid sales** and a handful of
free installs. Optimistic-realistic band over 14 days: **0–20 free
marketplace installs, 0–3 paid sales**. Anything above that is signal
worth doubling down on.

If the 14-day window closes at zero paid sales:
- Zero free installs → the marketplace submission didn't land, or the
  hooks themselves aren't compelling. Iterate on the free pack next.
- Some free installs but zero paid sales → free-to-paid conversion funnel
  is broken; either the paid pack isn't compelling enough or the cross-
  sell copy is weak. Pivot the paid pack, not the category.
- Zero of both → same category-fail zone as B-002. One more strike toward
  the per-category circuit breaker (3 consecutive zero-engagement ships
  in the same category → pause that category per CLAUDE.md).

## Definition of done for this experiment
- [x] Scoping: README.md (this file), PLATFORM.md, hooks outline — **run #65**
- [ ] Free pack built (5–8 working hooks + install README + `.claude-plugin/marketplace.json`) — next run
- [ ] Paid pack built (15–18 hooks with walkthroughs, single markdown deliverable) — run after next
- [ ] `ship.md` written (Gumroad or LS upload instructions + awesome-claude-code PR draft + Show HN title options) — subsequent run
- [ ] Free repo published on GitHub (blocked-on-human: `gh repo create` via local `GITHUB_TOKEN`)
- [ ] Paid pack uploaded to chosen storefront (blocked-on-human: `GUMROAD_ACCESS_TOKEN` or LS equivalent)
- [ ] Plugin marketplace submission (blocked-on-human: Anthropic review)
- [ ] Distribution posts scheduled (awesome-claude-code PR, Show HN, r/SideProject, r/ClaudeAI)
- [ ] 14-day measurement window closes → update this README with results

## Status (2026-04-13 21:31 UTC, remote run #65)
Scoping only. No code written yet. Next remote run begins building the
free pack.

## Files
- `README.md` — this file (scoping, hypothesis, outline, pricing, distribution, measurement)
- `PLATFORM.md` — Gumroad vs Lemon Squeezy decision for Robert (default: Gumroad)

(Files to be added in future runs:)
- `free-pack/` — the 5–8 free hooks + install README + `.claude-plugin/marketplace.json`
- `claude-code-hooks-paid.md` — the paid deliverable (15–18 hooks with walkthroughs)
- `ship.md` — handoff for the local agent

## Metrics table (fill in after measurement window)
| Date | Free installs | Paid views | Paid downloads | Revenue (gross) | Revenue (net) | Notes |
|------|---------------|------------|----------------|-----------------|---------------|-------|
| TBD  | —             | —          | —              | $—              | $—            | Not yet built — scoping complete 2026-04-13 remote run #65 |
