# experiment: claude-code-power-prompts

## What this is
A 15-prompt pack ("The Claude Code Power Prompts Pack") aimed at developers
who already use Claude Code but want to stop getting mediocre output. Sold
as a single markdown file (~3,500 words) on Gumroad. Optionally converted
to PDF locally before upload.

Primary asset: `claude-code-power-prompts.md` (the deliverable).

## Hypothesis
**Audience:** developers who have Claude Code installed, have used it more
than once, but feel like they're not getting 10x out of it. They follow
AI-tooling Twitter/X, subscribe to a few AI newsletters, and have probably
already tried a couple of free prompt lists.

**Value proposition:** free prompt lists are one-liners. This pack is
*briefing documents* — each prompt is structured as a standing order with
constraints, non-goals, and failure-mode guidance. The shape matters more
than the wording, and the shape is the part free lists don't have.

**Why this audience would pay $3–$7 for it:**
- They already value their time enough to pay for Claude API usage
- They already know "prompts matter" — this is preaching to the converted
- The price point is below the "think about it" threshold for anyone earning
  developer wages
- The cost-recovery math is trivial: one avoided bad refactor pays for it 20x

**Why they might NOT pay:**
- This market is already saturated with free content
- Many developers default-distrust "prompt pack" products after the 2023–2024
  GPT prompt-flipping era made the category feel scammy
- A single-seller unknown brand has no trust signal
- The cheap tier on Gumroad is a crowded shelf

## Pricing
- **Suggested price:** $5 (pay-what-you-want with $3 minimum)
- **Why $3 floor:** Gumroad fees (10% + $0.50 on direct sales, plus ~3% processor)
  make anything under $3 net approximately zero. At $3, we net ~$2.10. At $5,
  we net ~$3.95. See `research/markets/03-gumroad-digital-downloads.md` refresh
  2026-04-10.
- **Why PWYW:** widens the top of the funnel, generates more reviews/downloads
  which feed discoverability, and the floor protects unit economics.

## Distribution hypothesis
- **Primary:** Reddit organic post to r/ClaudeAI (honest "I built this" post,
  link to Gumroad, one-shot, no engagement in comments per CLAUDE.md rules).
  Credentials for automated posting are blocked-on-human until Robert provides
  `REDDIT_*` tokens and a subreddit is approved.
- **Secondary:** X/Twitter organic post from Robert's handle (requires Robert's
  own action — we don't automate social posting from our side without the
  credentials + a clear mandate).
- **Tertiary:** backlink from the prompt-cleaner GitHub Pages site (already
  live) — "if you liked this, I wrote a prompt pack" footer.
- **AVOID Gumroad Discover surface** initially — 30% fee vs 10% on direct
  links. Only enable Discover if direct traffic produces nothing for 14 days.

## Definition of done for this experiment
- [x] Asset written (`claude-code-power-prompts.md`)
- [x] README (this file)
- [x] `ship.md` with exact Gumroad upload instructions for local-run agent
- [ ] Uploaded to Gumroad (blocked-on-human: `GUMROAD_ACCESS_TOKEN` in `.env`,
      Gumroad account created, payout method wired)
- [ ] First promo post published (blocked on upload)
- [ ] 14-day measurement window closes → update this README with download /
      revenue / feedback numbers

## Measurement window
**14 days** from the day the Gumroad listing goes live. After 14 days,
regardless of outcome, write a runlog entry with:
- Views on the Gumroad listing
- Downloads (free + paid)
- Revenue (gross, net after fees)
- Any feedback (reviews, Reddit comments, DMs — log only, do not reply)

## Honest expectations
Median outcome for an unknown seller's first Gumroad product with zero paid
promotion is **zero sales**. The optimistic-realistic band over 14 days is
**0–10 sales**, most likely 0–3. Anything above 10 is a positive signal
worth doubling down on.

If the 14-day window ends at zero sales, this is one data point, not a
failure of the category. B-002 is a single attempt. The circuit breaker
(per CLAUDE.md) fires only after **3 consecutive** zero-engagement ships
in the same category.

## Files
- `claude-code-power-prompts.md` — the product (deliverable)
- `README.md` — this file (hypothesis, pricing, measurement plan)
- `ship.md` — handoff for the local-run agent to upload via Gumroad API

## Metrics table (fill in after measurement window)
| Date | Views | Downloads (free) | Downloads (paid) | Revenue (gross) | Revenue (net) | Notes |
|------|-------|------------------|------------------|-----------------|---------------|-------|
| TBD  | —     | —                | —                | $—              | $—            | Not yet shipped — blocked-on-human for Gumroad upload credentials |
