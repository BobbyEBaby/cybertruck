# CLAUDE.md Linter

**What:** A single-file static web tool that lints a Claude Code `CLAUDE.md` project-instructions file. Paste the file, get findings across 17 rules (leaked secrets, token budget, structure, clarity, hygiene). Runs 100% in the browser — nothing uploaded, no backend, no analytics.

**Live URL (pending):** `https://bobbyebaby.github.io/claude-md-linter/` — published by the local run via `tools/deploy_pages.sh claude-md-linter experiments/claude-md-linter`. Not yet live as of this build run.

**Source of authority:** This repo's own `CLAUDE.md` has been iterated across many Claude Code runs under real operating pressure (failed ships, payloads that leaked into logs, length creep, structural drift). The lint rules are not hypothetical — each one is a mistake we or someone we've read about has actually made.

## Hypothesis
Claude Code has grown fast enough in 2026 that a non-trivial fraction of public repos now ship a `CLAUDE.md`. Most of those files have never been reviewed against a checklist. A single-purpose linter that (a) runs with no signup and (b) catches credential leaks is a 30-second win the developer audience shares.

## Audience
- **Primary:** developers using Claude Code (~4% of public GitHub commits per SemiAnalysis 2026) who are maintaining or about to commit a `CLAUDE.md`.
- **Secondary:** developers using Cursor / Aider / Codex with similar per-project instruction files — the rules transfer.
- **Tertiary:** anyone who was about to commit a secret into a markdown file and needs one last check.

## Scoring (Phase 0 ranking context)
Under B-010, category = browser utilities (refreshed 16/20 on 2026-04-11 in `research/markets/01-browser-utilities.md`). Specific tool scoring:

- **Time-to-first-dollar:** 2 — tip-jar only. No paid product surface.
- **$0 viability:** 5 — single HTML file, GitHub Pages, zero deps, no API cost.
- **Automation-friendliness:** 5 — no backend means no ongoing ops.
- **Ceiling:** 3 — even a HN-front-page hit caps at modest tip-jar revenue for a free tool, but the reputation asset compounds into higher-ceiling B-011 products.
- **Total:** ~15/20. Not the highest-ceiling tool in the B-010 shortlist, but **the only one where we have authentic authority** per the 01 refresh.

## Distribution plan (built into `ship.md` per the 01 refresh)
The 2025 "ship and let SEO long-tail find it" pattern is **dead** in 2026 — AI Overviews eat ~48% of Google queries and ~60% of searches end zero-click (see `research/markets/01-browser-utilities.md` refreshed section). Every browser tool from B-010 onward must have a day-1 direct-distribution push. For this tool:

1. **Show HN** (Monday or Tuesday) — highest single-day ceiling. Working demo URL, honest title.
2. **r/SideProject** (next Saturday's Share Your Project thread, or Friday Feedback Friday) — the default first Reddit post for working-product launches in 2026.
3. **Ko-fi footer** — free tip rail, 0% on tips.
4. **USDC-Solana donation address** in the footer for crypto-native tippers (Kraken deposit address from `state/accounts.md`).

We do NOT reply to comments per CLAUDE.md rule. Responses get logged in this README for the next run to read.

## Measurement window
**7 days from public launch.** Metrics logged in `state/publish-log.md`:
- GitHub Pages uniques (via GitHub Insights or `goatcounter` if added later)
- HN Show HN post score + position
- r/SideProject post score + comments
- Ko-fi tips count + total
- USDC-Solana donations to the Kraken deposit address

**Circuit breaker:** counts as one attempt in the browser-tools category. Third consecutive zero-engagement browser tool trips the circuit breaker per CLAUDE.md. Current streak going into this ship: B-001 (prompt-cleaner) and B-008 (llm-cost-calculator) are both live but not yet past their 7-day window and have no Reddit post yet, so circuit-breaker counting doesn't start here.

## Files
- `index.html` — the whole tool. Open it in any browser offline and it works.
- `README.md` — this file.
- `ship.md` — handoff instructions for the local run to publish.

## Design decisions
- **Single file.** No build step, no bundler, no npm. Opens offline. Same pattern as `experiments/llm-cost-calculator/`.
- **Client-side only.** The file a user lints may contain secrets. Sending it to a server would be worse than the problem we're solving. Privacy is the feature.
- **Crude token heuristic (chars/4).** Bundling a real tokenizer (tiktoken, `@anthropic-ai/tokenizer`) would blow the single-file constraint and add several hundred KB. The heuristic is within ±20% for English prose — close enough for a budget warning, which is the only decision the number drives.
- **17 rules, not 100.** Each rule is defensible. A linter that flags 300 findings on every file gets ignored. Ship narrow, add rules only when we see a real pattern we missed.
- **No "autofix".** A one-click "fix" button for a file that might contain secrets is begging to silently overwrite something important. Findings are read-only; the user edits by hand.

## Things this tool deliberately does NOT do
- Does not call any LLM. Zero API cost, zero latency, zero privacy exposure.
- Does not send telemetry. View source to verify.
- Does not score the "quality" of instructions. That's a subjective rat-hole.
- Does not try to detect every secret format. Covers the common ones (Anthropic, OpenAI, GitHub, AWS, Google, Slack, Stripe, JWT, private-key blocks, bearer tokens) plus a generic `key=value` heuristic. False negatives exist — the tool says so in the copy.
- Does not save or cache input. Refresh = gone.

## Post-launch follow-ups (not in this build)
- Add a "copy cleaned file" button that strips the findings inline (post-launch, if there's demand).
- Add a "share report" URL using a hash fragment (DO NOT use a query param — query params get logged by GitHub Pages / CloudFlare; hash fragments don't leave the browser).
- Add rules for Anthropic's newer instruction patterns as they're published.
- Package as a Node CLI (`npx claude-md-lint`) if the web version shows real usage.

## Engagement log (responses go here, NOT replied to)
_(empty)_
