# 0007 — Ship experiments/support-usdc/

**Priority: low.** This does not jump the queue ahead of `0005-ship-claude-md-linter.md` (the B-010 browser tool, highest-leverage AI-tooling shot) or `0006-ship-flipline-to-itchio.md` (the B-002b itch.io portfolio-diversification bet). Ship order suggestion: 0005 → 0007 → 0006. Or do 0007 at the same time as any other deploy_pages.sh run — it's literally one extra command.

## What was built (remote run #18, 2026-04-12)

`experiments/support-usdc/` — Phase-1 deliverable of backlog item **B-006** (direct-crypto earning experiment).

- `index.html` — single-file static page. Shows the USDC-Solana Kraken deposit address (`EQwtTPe3…Qwf7`, exactly matching `state/accounts.md` and `.env`), copy button, Solscan verification link, explicit warning that it's a custodial Kraken address (not self-custody), cross-link to the Ko-fi fiat rail, cross-links to `state/goal.json` / `state/runlog.md` / `state/honest-expectations.md` / the repo. Dark theme, mobile-responsive, ~170 lines. **Zero network calls after load** — no fonts, no analytics, no CDN assets, no tracking pixels. Verified by grepping the source for `fetch(`, `XMLHttpRequest`, `sendBeacon`, `new Image(`, and `.src = "http` (all zero matches). Outbound URLs are `<a href>` only, which fire on user click.
- `README.md` — hypothesis, audience, measurement window (14 days), alive/soft-zero/hard-zero thresholds, why-this-over-Polar-first, what-this-is-NOT, and the B-007 rotation plan for when self-custody kicks in at $5k.
- `ship.md` — four phases:
  - **Phase 1** (one command): `tools/deploy_pages.sh support-usdc experiments/support-usdc` → live at `https://bobbyebaby.github.io/support-usdc/`
  - **Phase 2** (5 min): cross-link from the live tools (prompt-cleaner, llm-cost-calculator now; claude-md-linter and flipline when those ship) by adding a one-line "Send USDC on Solana →" footer below each tool's existing Ko-fi line, then redeploying
  - **Phase 3** (optional, human-gated): create a Polar.sh account + add `POLAR_ACCESS_TOKEN` to `.env`. Polar is the primary paid-tier rail per the 2026-04-11 research refresh (merchant-of-record, supports paid repo access, file downloads, subscriptions)
  - **Phase 4** (optional, human-gated, slow): apply for GitHub Sponsors. Human-reviewed, may take days to weeks. 0% platform fee if accepted.

Backlog entry B-006 was marked `[in_progress remote run #18 2026-04-12]` in `state/backlog.md` with the full scope and the 08-refresh-driven rail ordering documented.

## What you do

Minimum to mark B-006 as *shipped*:

1. Run `tools/deploy_pages.sh support-usdc experiments/support-usdc`.
2. Open `https://bobbyebaby.github.io/support-usdc/` and verify the address matches `state/accounts.md` *exactly* (do NOT trust your eyeballs on a crypto address — use `diff` or a copy-paste compare). Also confirm the copy button actually copies the full address, not a truncated version.
3. Do the Phase 2 cross-link edits for `prompt-cleaner` and `llm-cost-calculator` (the two live tools), then redeploy each. The exact HTML snippet is in `ship.md` Phase 2. ~5 minutes.

Phases 3 and 4 are entirely optional and extend the rail catalogue, but B-006's definition of done is already met after Phases 1 and 2.

## How to report back

Drop a file in `human_outbox/` like:

```
support-usdc deployed (or not)
- live url: https://bobbyebaby.github.io/support-usdc/ [confirmed loads / broken / other]
- address verified against state/accounts.md: yes / no
- cross-linked tools: prompt-cleaner / llm-cost-calculator / both / neither
- polar account: created / not yet
- github sponsors application: submitted / not yet
```

Next remote run will process that and mark B-006 `[done <date>]` if Phases 1 and 2 landed.

## Do NOT

- **Do NOT** post the support page to Reddit or Hacker News as a standalone "please donate" pitch. That is engagement bait and violates CLAUDE.md's reputation-as-asset rule. Distribution happens passively via the tool footers.
- **Do NOT** add any analytics / tracking pixel / CDN asset / fetch call to `index.html`. The "zero network calls" guarantee is part of the page's value and is what makes it safe to cross-link from every tool we ship.
- **Do NOT** change the Solana address without re-verifying it matches `state/accounts.md`, `.env`, and Kraken's deposit-address page for the Solana network. A one-character typo = funds lost.
- **Do NOT** echo the contents of `.env` in any runlog entry or commit message — this applies especially to `POLAR_ACCESS_TOKEN` if/when you add it.
- **Do NOT** ship a Cybertruck-themed image or any asset implying the project has already earned the truck. The only honest visual is the one on the page (text-only).

## Why only now (and not earlier)

B-006 has been on the backlog since 2026-04-10 but was gated on "parallel-eligible after B-001". B-001 (prompt-cleaner) shipped 2026-04-11. B-006 was picked in this remote run because:

1. B-002b (Flipline) and B-010 (CLAUDE.md linter) are both built but still awaiting local deploys from runs #16/#17 — per run #17's explicit "do not rebuild, do not panic-note" rule, I avoided those.
2. B-011 (second Gumroad asset) is gated on B-002 first-sale data, which isn't in the outbox yet.
3. All 8 `research/markets/*.md` files were refreshed 2026-04-11 (yesterday) — same-day research refresh would be theatre, not signal.
4. B-006 was explicitly listed in run #17's recommended-next-step candidates `(iii) scope B-006 since B-001 is done`.
5. The 08-refresh already did all the research work (Polar.sh as primary, GitHub Sponsors as secondary, Open Collective deprioritized, USDC-Solana as the supplementary crypto rail). All that was left was the static page itself and the scoped handoffs — both fully remote-doable.
