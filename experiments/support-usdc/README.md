# experiments/support-usdc/

A minimal static page that accepts direct-crypto tips for the Cybertruck
Autopilot project. Phase-1 deliverable of backlog item **B-006** (direct-crypto
earning experiment).

Once `tools/deploy_pages.sh support-usdc experiments/support-usdc` is run, it
lives at `https://bobbyebaby.github.io/support-usdc/`.

## Hypothesis

Most visitors to the free tools (prompt-cleaner, llm-cost-calculator, claude-md-linter, flipline, …) will not tip. A small fraction are crypto-native and
will send $1–$5 in USDC-Solana if the friction is low, the rail is legitimate,
and the page is honest about what the money funds. Expected conversion rate:
near zero — this is a supplementary rail, not the primary one.

## What it is

- Single-file static `index.html`, no dependencies, no build step, no JS
  frameworks.
- **Zero network calls from the page after load.** No analytics, no fonts,
  no tracking pixels, no CDN assets. Verified by grepping the source for
  `fetch(`, `XMLHttpRequest`, `sendBeacon`, `new Image(`, and `.src = "http`
  — all zero matches. Outbound links exist in `<a href>` anchors only, which
  fire on user click, not on page load.
- Displays the USDC-Solana Kraken deposit address from `state/accounts.md`
  (`EQwtTPe3...Qwf7`), exactly matching the canonical source.
- Copy button via `navigator.clipboard.writeText` with a `document.execCommand`
  fallback for older browsers.
- Solscan verification link so visitors can see the address is real.
- Cross-links to the Ko-fi fiat rail (Robert's existing `ko-fi.com/bobbyebaby`)
  for non-crypto visitors.
- Cross-links back to the repo, runlog, `goal.json`, and `honest-expectations.md`
  so every claim is auditable.
- Explicitly warns that this is a **Kraken custodial deposit address**, not a
  self-custody wallet, and that the self-custody migration triggers at $5k
  (per B-007 in `state/backlog.md`).
- Dark, readable, mobile-responsive. ~170 lines total.

## Audience

The intersection of (a) people who find the free tools through organic
channels (r/SideProject, Show HN, Google), and (b) people who hold USDC on
Solana and know how to send it. Expected numerator: very small. Expected
denominator: also small. Lifetime tips in the first 14-day window: probably 0.

## Measurement window

14 days from first GitHub Pages deployment. Primary metric: did *any* USDC-SPL
or SOL deposit land in the Kraken deposit address during the window?

### Thresholds

- **alive:** ≥ 1 tip received (any amount above the $0.40 Kraken minimum)
  within 14 days.
- **soft-zero:** 0 tips received, but the existing live tools (prompt-cleaner,
  llm-cost-calculator) have been updated to link to this page. At least the
  distribution channel exists.
- **hard-zero:** 0 tips AND no live tool cross-links this page. That means the
  distribution channel never materialized, so the outcome tells us nothing
  about the rail itself. Fix by deploying the tool-footer cross-links (Phase 2
  in `ship.md`).

Note on measurability: GitHub Pages does not expose access logs to repo
owners. Page traffic is effectively unmeasurable without adding an analytics
pixel, which we are deliberately not doing. The only honest signal is "did a
deposit land?" — tracked by checking the Kraken account, not by client-side
instrumentation.

## Why this, and why now

Per the 2026-04-11 refresh of `research/markets/08-open-source-donations.md`
(remote run #15), the three viable direct-earning rails for a solo operator
in 2026 are:

1. **Polar.sh** (merchant-of-record, 4%+$0.40, supports paid repo access,
   file downloads, subscriptions) — primary paid-tier rail.
2. **GitHub Sponsors** (0% platform fee on personal sponsorships, human-reviewed
   eligibility gate) — secondary 0%-fee tip rail.
3. **Direct USDC on Solana** (zero platform fees, sub-cent network fees,
   aligns with the project's canonical savings rail in `state/accounts.md`)
   — supplementary crypto-native rail.

All three were explicitly named in the refresh's "Actionable updates for B-006"
section. Rails 1 and 2 require human action (account creation, API tokens,
identity verification, in the case of Sponsors a human-reviewed application).
Rail 3 ships in one remote run with no credentials, because the Solana address
is already public in `state/accounts.md`.

This experiment is Rail 3. Rails 1 and 2 are handoffs to the local agent via
`ship.md` Phase 3 and Phase 4.

## What this is NOT

- Not a self-custody wallet. Funds accumulate in Kraken (custodial) until the
  B-007 trigger fires at $5k.
- Not a pitch for subscriptions, services, or consulting — there are none.
- Not a changelog or status page — it's a tip rail, nothing more.
- Not an analytics page. Zero network calls after load.
- Not a Reddit/HN launch candidate. A standalone "please donate" post would
  be engagement bait and would violate CLAUDE.md's reputation-as-asset rule.
  The page distributes passively via cross-links from the actual utility
  tools.
- Not a replacement for Polar.sh or GitHub Sponsors. It is their complement.

## Ship phase

See `ship.md` in this directory. Phase 1 (deploy the static page) is the only
step required to mark B-006 as shipped. Phase 2 (cross-link from the live
tools) closes the distribution loop. Phases 3 and 4 (Polar.sh and GitHub
Sponsors) extend the rail catalogue but are not gating.

## When to rotate this address

Per B-007 in `state/backlog.md`, the self-custody migration triggers at
$5k balance. When it fires:

1. The agent proposes the self-custody wallet address via `human_inbox/`.
2. Robert moves funds from Kraken to the self-custody wallet (one-time).
3. A future remote run edits `index.html` to show the new address.
4. A future remote run updates `state/accounts.md` to reference both addresses
   with the transition date.

Until then, this Kraken deposit address is the canonical direct-crypto tip
rail for the project.
