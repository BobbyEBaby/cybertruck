# Backlog

Ranked tasks. The daily run picks the top task that is **not blocked on a human action**. When picking up a task, mark it `[in_progress]`. When done, mark it `[done YYYY-MM-DD]` and move it to the bottom under "Done".

Priority signals: time-to-first-dollar, $0 viability, automation-friendliness, ceiling.

## Ranking summary (from research/markets/)
Top scores from Phase 0:
1. **17/20** — Gumroad digital downloads (`03-gumroad-digital-downloads.md`)
2. **16/20** — Browser utilities (`01-browser-utilities.md`)
3. **15/20** — Niche content / SEO (`04-niche-content-sites.md`) — too slow for first ship
4. **15/20** — Open-source + donations (`08-open-source-donations.md`)
5. **14/20** — itch.io micro games (`02-itchio-microgames.md`)

**B-001 picks browser utilities (16) over Gumroad (17)** for the *first* ship because browser utilities can go live with zero external account (a `username.github.io` page works once GitHub is set up). Gumroad needs the account fully wired with payouts before the first sale can settle. After the first ship validates the loop, the next experiment will be the higher-ceiling Gumroad play.

## Active

### B-001 — Build & ship a tiny browser tool: "AI Prompt Cleaner"
**Status:** [done 2026-04-11] — live at https://bobbyebaby.github.io/prompt-cleaner/. Repo: https://github.com/BobbyEBaby/prompt-cleaner. Shipped by the local run 2026-04-11 06:03 (see runlog + publish-log).
**Follow-up:** 7-day measurement window is running. No Reddit post yet — deferred until the live URL is visually confirmed and REDDIT_* credentials are in `.env`.

### B-002 — Build & ship a Gumroad digital download (highest-ceiling first product)
**Status:** [in_progress 2026-04-11 remote] — build phase unblocked (no creds needed). Upload phase still blocked on Gumroad account + `GUMROAD_ACCESS_TOKEN` in `.env` (local-run only).
**Why:** Highest score in Phase 0 (17/20). Gumroad's free tier handles checkout and delivery; the agent can author the product (template, prompt pack, ebook). See `research/markets/03-gumroad-digital-downloads.md`.
**Definition of done:** `experiments/<slug>/` with the digital asset (zipped if multi-file), `README.md` (hypothesis + audience + pricing), and `ship.md` (Gumroad listing copy + tags + price + upload steps).
**Next concrete step:** After B-001 ships, decide product based on what we now know about traffic source. Default candidate: a Claude Code / AI agent prompt + template pack aimed at the same audience that found B-001.

### B-002b — Build & ship one tiny web game on itch.io (alternative second ship)
**Status:** [pending] — blocked on B-000 (itch.io account) and B-001
**Why:** Lower score (14/20) but a different distribution channel (itch.io's own discovery). Useful as portfolio diversification. See `research/markets/02-itchio-microgames.md`.
**Definition of done:** `experiments/<slug>/` with a single-file HTML5 game (canvas + vanilla JS, no engine), `README.md`, and `ship.md`.
**Next concrete step:** Only pursue *after* B-002 if Gumroad turns out to be a dead end, OR in parallel by a future weekly run if there's spare capacity.

### B-003 — Validate the autonomous ship pipeline
**Status:** [pending] — blocked on B-001 actually shipping via the automated path.
**Why:** Until something is live via the agent's own hands (not via a manual upload), we have no proof the autonomous loop works. The first ship is not about revenue; it is about proving `gh` + Pages + Reddit posting + publish-log all function end-to-end with no human in between.
**Definition of done:** `state/runlog.md` contains an entry confirming a live GitHub Pages URL exists, `state/publish-log.md` has the entry, and a Reddit post URL is recorded — all done by the agent in a single scheduled run.

### B-004 — Phase-0.5 deeper research with WebSearch
**Status:** [pending] — blocked-on-human (needs `/schedule` running so the agent has WebSearch in its scheduled context, AND B-001 to be in flight so the agent isn't blocked).
**Why:** The bootstrap research files in `research/markets/` are seeded from prior knowledge. They need a current-data refresh: search for 2025–2026 reports on top earners in each category, current rev share / payout terms, recent saturation signals.
**Definition of done:** Each file in `research/markets/` has a `## Refreshed YYYY-MM-DD` section with at least 3 cited sources and any updated scoring.

### B-005 — Wire fiat → Kraken auto-conversion
**Status:** [pending] — depends on B-001 actually earning a first dollar (no point wiring this until something pays out)
**Why:** When Gumroad/Stripe pays out fiat, we want it to land in the Kraken USDC deposit address from `.env` automatically — not sit in a bank account. The cleanest path: link Gumroad → bank → standing instruction to buy USDC on Kraken when fiat lands → withdraw USDC to the deposit address (which is already a Kraken-internal address, so this is more about *holding it as USDC* than transferring).
**Next concrete step:** When the first payout is imminent, write `human_inbox/` instructions for Robert to set up the fiat → USDC conversion rule on Kraken and confirm the bank link from his payout platform.
**Definition of done:** First fiat payout has been observed converting to USDC in Kraken without per-payout human action, recorded in runlog.

### B-006 — Direct-crypto earning experiments
**Status:** [pending] — parallel-eligible after B-001
**Why:** Skip the fiat onramp entirely by earning crypto directly. Targets:
- **Polar.sh** — sponsorships and issue funding for OSS projects (free, crypto + fiat payouts)
- **Gitcoin Grants / bounties** — bounties for OSS contributions
- **GitHub Sponsors** — ties into B-008-ish OSS shipping
**Definition of done:** At least one experiment is published with a "support this in USDC" link wired to the Kraken deposit address or a self-custody wallet, even if it earns nothing.

### B-007 — Self-custody migration trigger
**Status:** [pending] — sleeps until balance crosses $5,000
**Why:** Custodial Kraken holdings are fine while small but become a single-point-of-failure as the balance grows. At $5k, the agent will write an inbox note recommending Robert install MetaMask/Phantom and withdraw the bulk of holdings to self-custody.
**Trigger:** `state/goal.json.balance_usd >= 5000`
**Next concrete step:** Sleep. The daily run checks the balance at the top of each run; when threshold is crossed, this becomes an inbox note instead of staying on the backlog.

## Blocked on human

### B-000 — One-session setup (Kraken deposit address + free accounts + API tokens + cron install)
**Status:** [blocked-on-human]
**See:** `human_inbox/0001-setup.md`
**Unblocks:** B-001, B-002, B-004, B-005, B-006
**Note:** This is the *only* expected human-action backlog item under normal operation. After it's done, the agent operates hands-off on the daily cron until something earns money or the circuit breaker fires.

### B-008 — LLM API Cost Calculator (browser tool, second AI-tooling shot)
**Status:** [built — awaiting ship via tools/deploy_pages.sh]
**Why:** Same audience as B-001 (AI tooling crowd), different angle (cost-conscious devs/decision-makers vs prompt engineers). Single static file, $0 to ship via the existing pipeline. Full build is done — see `experiments/llm-cost-calculator/`.
**Next concrete step:** Local-run agent executes `bash tools/deploy_pages.sh llm-cost-calculator experiments/llm-cost-calculator` (needs `GITHUB_TOKEN` already in `.env`). Then optionally posts to r/LocalLLaMA via `tools/post_reddit.py` once Reddit creds are filled in.

### B-009 — Refresh remaining 6 market research files
**Status:** [in_progress 2026-04-11 remote] — rolling refresh, one file per remote run. **Done so far:** 02-itchio-microgames (2026-04-11, this run). **Still stale:** 04 (niche content), 05 (Chrome ext), 06 (faceless YouTube), 07 (POD), 08 (OSS donations). Next remote run should pick the next oldest.
**Why:** Files 02 (itch.io), 04 (niche content), 05 (Chrome ext), 06 (faceless YouTube), 07 (POD), 08 (OSS donations) still have stale data from May 2025 cutoff. Refresh each with a "Refreshed YYYY-MM-DD" section + 3 cited sources. The remote agent should pick the oldest unrefreshed one each run.
**Next concrete step:** Pick one file. Use WebSearch to find current 2026 data. Append a "Refreshed" section with rescored values. Commit. Move to next file on next run.

### B-010 — Build a third browser tool (open category)
**Status:** [pending] — fully remote-doable, no creds for build phase
**Why:** Inventory expansion. Two browser tools (B-001 + B-008) is a small portfolio. A third widens the surface area. Constraints: must be single static file, must target AI tooling audience or adjacent dev audience, must not duplicate B-001 or B-008.
**Next concrete step:** Pick one of: (a) Anthropic tool-definition validator (paste JSON schema, get validated tool def), (b) prompt diff viewer (paste two prompts, see line-by-line diff), (c) markdown→plaintext converter, (d) regex tester with named-capture support, (e) JWT decoder, (f) something else suggested by current research. Build it as `experiments/<slug>/`. Hand off to local for ship.

### B-011 — Author a second Gumroad digital asset (queue behind B-002)
**Status:** [pending] — remote-doable for build phase
**Why:** B-002 (Claude Code Power Prompts) is a single product. Once it ships, having a second asset ready to upload back-to-back is the right move (one-product creators almost never make sales; clusters do). Candidates: "AI agent CLAUDE.md template pack", "Cybertruck-Autopilot-style operating-loop starter kit", "100 prompts for X niche".
**Next concrete step:** Decide on the second product after B-002 is shipped and we have measurement data. Until then, keep this as a placeholder so the agent doesn't redundantly start it.

## Done
_(none yet — note: B-001 prompt-cleaner is shipped externally as of 2026-04-11, see runlog. Should be moved here on a future cleanup pass.)_
