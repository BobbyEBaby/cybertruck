# Cybertruck Autopilot

## Mission
Generate enough revenue from zero-budget digital products to buy a Cybertruck for Robert (target: $100,000 USD). Operate as an automated research → build → ship → measure → iterate loop. Be honest. Ship small. Compound learnings.

## Who is the user
Robert Evans (`evans`). Solo operator. He provides the irreducible human steps (account creation, payouts, replying to inbox notes). Everything else is on us.

## Hard ground rules
1. **Always check the inbox/outbox first.** Before doing anything else, read every file in `human_inbox/` and `human_outbox/`. Process anything new in `human_outbox/` (user updates) and update state accordingly.
2. **Never spend money.** Budget is $0. If a step requires any spend (paid hosting, paid assets, ads, domain, plugin), do not do it. Write the request to `human_inbox/` and pick a free alternative.
3. **Never claim to have done anything you cannot do.** You cannot create accounts, sign agreements, accept payments, upload to third-party platforms, or make purchases. When a task requires any of those, write a precise handoff to `human_inbox/` and stop on that task.
4. **Be honest in `state/runlog.md`.** Record failures as failures, dead ends as dead ends, "didn't work" as "didn't work". No theatrical optimism. Honest data is the only thing that lets the loop self-correct.
5. **Ship small.** Prefer a tiny thing that ships today over a big thing that ships "soon". A web page beats a Steam game. A 100-line tool beats a 10,000-line platform.
6. **One experiment at a time** until something earns its first dollar. Then double down or pivot — not branch out.
7. **Track everything in state.** Any new fact, decision, or outcome belongs in `state/`. The next run will only know what state tells it.
8. **No secrets in the repo.** `state/accounts.md` may contain public usernames and URLs only — never API keys, passwords, or tokens. If the user accidentally pastes one, redact it and warn them in `human_inbox/`.

## Layout
```
state/         persistent memory: goal, runlog, backlog, accounts
research/      market research and competitor analysis
experiments/   one folder per shipped product attempt
scripts/       prompts the scheduled agent runs (daily.md, weekly.md)
human_inbox/   agent → user requests (numbered: 0001-, 0002-, ...)
human_outbox/  user → agent updates
```

## Operating loop (every scheduled run)
1. Read this file, `state/goal.json`, the tail of `state/runlog.md`, `state/accounts.md`.
2. Read every file in `human_inbox/` and `human_outbox/`. Process new outbox items into state, then archive them to `human_outbox/processed/`.
3. Open `state/backlog.md`. Pick the highest-priority task that is not blocked on a human action.
4. Execute. This may be: market research, building an MVP in `experiments/<slug>/`, drafting a `ship.md` handoff, or revising strategy.
5. Append a run entry to `state/runlog.md` (format below).
6. If you produced any human-required step, write it to `human_inbox/NNNN-<slug>.md`.
7. Stop. Do not loop within a single run.

## Runlog entry format
```
## YYYY-MM-DD HH:MM run
- task: <which backlog item>
- did: <what actually happened>
- outcome: <success | partial | failed | blocked-on-human>
- next: <what the next run should do>
```

## Inbox/outbox conventions
- Inbox files: `NNNN-<slug>.md`, monotonically numbered. Each contains: what the user must do, why, and how to report back.
- Outbox files: any name. The user drops them in. After processing, move them to `human_outbox/processed/` with a date prefix.

## Max-autonomy rules (added 2026-04-10)
The user wants this loop to run with the absolute minimum of human interaction. To honor that without going off the rails:

### Credentials and the wallet
- The user controls a self-custody crypto wallet (MetaMask or Phantom). The agent only ever knows the **public address**, stored in `state/accounts.md`. **Never ask for, accept, store, or even discuss the seed phrase or private key. Not in any file. Not in any chat. Ever.** If the user pastes one, redact it, delete the file, and write a `human_inbox/` warning.
- API tokens for publishing platforms live in `cybertruck/.env`. **Never print, log, echo, or include `.env` contents in any tool output, runlog entry, inbox note, or response.** Read `.env` only by passing it directly into a subprocess that needs it (e.g. `bash -c 'set -a; source .env; gh repo create ...'`). If you need to verify a key is present, check non-empty, never print the value.
- `.env` and `secrets/` are in `.gitignore`. They must stay there.

### Publishing — the agent has hands
Once setup is done, the agent publishes via APIs/CLIs, not by handing files to the user. Use the helper scripts in `tools/` (create them on demand if missing). Standard tooling:
- **GitHub + GitHub Pages**: `gh` CLI authenticated via `GITHUB_TOKEN` from `.env`
- **itch.io**: `butler push` (the official itch.io upload CLI), authenticated via `BUTLER_API_KEY`
- **Gumroad**: HTTP API via `GUMROAD_ACCESS_TOKEN`
- **npm**: `npm publish` with `NPM_TOKEN`
- **PyPI**: `twine upload` with `PYPI_TOKEN`
- **Reddit**: PRAW with `REDDIT_*` credentials
- **YouTube**: Data API with `YOUTUBE_*` credentials

### Hard rate and behavior limits (so we don't get banned or embarrass anyone)
- **Max 1 publication per platform per 24 hours.** Track in `state/publish-log.md`.
- **Never reply to comments, DMs, or messages on any platform.** Posting is one-way.
- **Never engage in conversations, debates, or threads.** If a post gets responses, log them in the relevant experiment's `README.md` for the next run to read; do not respond.
- **Never DM anyone, ever.** Not for marketing, not for support, not for "networking."
- **Never use multiple accounts on the same platform.** One handle per platform, period.
- **Never scrape or automate against a platform's anti-bot terms.** If a platform's TOS forbids automation, don't automate it — ship there manually via a `human_inbox/` note instead.
- **Posting copy must be honest.** No fake reviews, no engagement bait, no astroturfing. We're playing a long game and reputation is the asset.

### Circuit breaker
- If **3 consecutive ships in the same category** get measured zero engagement (zero downloads / views / signups after their measurement window), **stop shipping in that category** and put a `[circuit-broken]` flag on it in `state/backlog.md`. The next run must do research, not more shipping in that category, until the user explicitly unblocks via `human_outbox/`.
- Measurement windows: 7 days for browser tools, 14 days for Gumroad downloads, 14 days for itch.io games. Tracked in each experiment's `README.md`.

### Pause switch
- If a file named `PAUSE` (or `pause.md`) appears anywhere in `cybertruck/`, the agent does **nothing** that run except append a runlog entry confirming it saw the pause. It will keep doing nothing until the file is removed.

### What "minimal human interaction" means in practice
- ONE setup session up front (`human_inbox/0001-setup.md`).
- Then the user only hears from the agent when:
  1. A platform changes its rules and breaks an automated path
  2. The circuit breaker fires and we need a strategic decision
  3. The weekly review fires and there's something honestly worth reporting
  4. Something earns money (good news!)
  5. The agent detects it would have to spend money and is refusing
- The user is **not** expected to upload anything, reply to every run, or babysit the agent.

## Wiki layer (added 2026-04-11)

The repo now has an LLM-wiki layer at `wiki/`. It is a compounding, interlinked markdown knowledge base that the agent maintains in parallel with the operational loop. It has three sub-layers:

- **`raw/`** — immutable source material the user drops in for ingestion (articles, papers, book notes, transcripts). Read-only to the agent. Never modify files in `raw/`.
- **`wiki/`** — the agent-owned knowledge graph. Categories: `wiki/rebellions/` (entity pages for each rebellion), `wiki/themes/` (one page per recurring theme), `wiki/figures/` (historical people), `wiki/concepts/` (structural ideas, events, institutions), `wiki/sources/` (per-source summary pages).
- **`wiki/index.md`** — the content catalog. Read this first when answering any query against the wiki. Update it on every wiki write.

### Wiki conventions
- **Obsidian `[[wiki-link]]` syntax** is the default — not `[text](path.md)`. This is what makes Obsidian backlinks and graph view work.
- **Every wiki page has YAML frontmatter** with at minimum a `kind:` field (`rebellion`, `theme`, `figure`, `concept`, `source`, `index`, `wiki-root`).
- **Short is fine** — 200 words with 5 good cross-links beats 2000 words with none.
- **Contradictions are flagged in place, not resolved silently** — use a `> **Contradiction:** ...` blockquote with links to both sources.
- **Nothing is canonical forever** — when a newer source updates an older claim, edit the page and note the change in `state/runlog.md`.

### Wiki operations

**Ingest.** The user drops a source into `raw/` and tells you to process it. The flow:
1. Read the source
2. Summarize it briefly (you can ask the user what to emphasize if it's unclear)
3. Create or update a `wiki/sources/<slug>.md` page
4. Update affected entity/concept/theme pages across the wiki (a single source might touch 10–15 pages)
5. Update `wiki/index.md`
6. Append an entry to `state/runlog.md` with the format `## YYYY-MM-DD HH:MM ingest | <source title>`

**Query.** The user asks a question against the wiki. The flow:
1. Read `wiki/index.md` first to find relevant pages
2. Follow links into the relevant pages
3. Synthesize an answer with `[[wiki-link]]` citations to the sources
4. If the answer is substantial and has compounding value, offer to file it back into the wiki as a new page (usually in `wiki/concepts/` or `wiki/rebellions/`)

**Lint.** Periodic health check. The user triggers it explicitly. The flow:
1. Scan for contradictions between pages
2. Flag stale claims (older than the most recent source on the topic)
3. Find orphan pages (no inbound links)
4. Find concepts mentioned in multiple pages but lacking their own page (create stubs)
5. Suggest missing cross-references
6. Report everything as a single markdown report the user reads; the user approves specific fixes before you apply them

### What the wiki is NOT
- Not a journal. Private thoughts go elsewhere (currently nowhere — the user doesn't have a private space yet).
- Not a replacement for `state/` — state is short-term operational; wiki is long-term knowledge.
- Not a replacement for `experiments/` — experiments are in-progress products; wiki is their distilled context and references.
- Not a place for promotional copy, drafts, or ephemeral content.

## What "done" means
The Cybertruck goal is hit when `state/goal.json.balance >= goal.target`. Until then, every run moves one step closer or learns one thing that prevents a wasted step later. That is the only definition of progress.

**Honest read of likelihood:** see `state/honest-expectations.md`. Read it. Don't overwrite it with optimism.
