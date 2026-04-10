# Honest expectations

This file is the permanent reality check. It exists because optimism is the failure mode of automated income loops, and Robert specifically asked for honest collaboration over performative confidence. Future runs of the agent **must read this file before drafting any forecast or revenue claim** and must not edit it to be more optimistic without recording the reason in `runlog.md`.

## What this loop is
A scheduled agent that researches, builds, and ships small zero-budget digital products to platforms where the public can find them, then measures honest engagement and either doubles down or pivots. The human is in the loop only for: account creation, generating API tokens, replying to circuit-breaker decisions, and receiving payouts.

## What this loop is NOT
- A money printer.
- A "set it and forget it for 12 months and come back to a Cybertruck" device.
- A way to bypass the fact that revenue requires real humans willing to pay for real things.
- An exception to the rule that most attempts in any digital-product category earn $0.

## What is realistically likely
Based on what is publicly known about indie digital product earnings (itch.io games, Gumroad templates, micro-SaaS, browser tools, OSS donations) the **median** outcome is $0. The **optimistic-realistic** band for a year of consistent shipping by a solo automated loop is somewhere in **$0–$5,000 lifetime**, with most of that concentrated in 1–2 products that happened to find a niche. The **lucky** outcome is **$5k–$50k**. The **moonshot** outcome — clearing six figures — happens but is rare and usually involves a viral moment or a real strategic insight, not just volume.

The loop's job is to maximize the *number of legitimate shots on goal* while keeping costs at $0 and not burning Robert's reputation. It is not to fake the funnel.

## What 100% autonomous can and cannot do
**Can (with API tokens stored in `.env`):**
- Build single-file web tools, web games, CLI utilities, templates, ebooks, prompt packs
- Push them live: GitHub Pages, itch.io (Butler), Gumroad, npm, PyPI, Cloudflare/Netlify
- Post the launch on Reddit (PRAW, organic, rate-limited)
- Track engagement, update state, decide what's working

**Cannot:**
- Make a person *want* to buy something. Demand is the bottleneck and demand is human.
- Defeat platform anti-bot/spam systems. Those exist for good reasons. The loop will get banned the moment it crosses a line.
- Avoid all fees. Fiat → crypto conversion, payment processor cuts, gas fees, and platform commissions will eat **5–15% of small payouts**. The plan stays $0 *upfront*; downstream cuts are not "spend" but they're not zero either.
- Scale by spam. The hard rate limits and no-engagement rules in CLAUDE.md exist precisely because the only path to long-term revenue is reputation, not volume.
- Replace the user's strategic judgment over time. Every few months a real human (Robert) needs to look at the runlog and decide whether the bet still makes sense. The agent will surface this in weekly reviews.

## The honest deal
**Robert's side:**
- ~2 hours of one-time setup (wallet + accounts + API tokens + cron install)
- ~10 minutes per week reading the weekly review
- Occasional decision when the circuit breaker fires
- Receiving payouts and (eventually, if we're lucky) buying a Cybertruck

**The agent's side:**
- Scheduled runs with no excuses, no theatrics, no fake progress
- Every run produces either a real artifact, real measurement, or an honest "blocked because X"
- Honest runlog. Failures recorded as failures.
- Never pretends the loop is more capable than it is.

## What success actually looks like
- **Month 1:** First experiment shipped, live URL exists, first measurement taken (probably $0)
- **Month 3:** 5–10 experiments shipped across 2–3 categories, one might have shown faint signal, the rest dead. Circuit breaker has fired at least once.
- **Month 6:** Probably $0–$200 lifetime revenue. Maybe one product has a small repeat audience. We know what doesn't work, which is worth more than it sounds.
- **Year 1:** If we're going to win, this is when we'd see it — one product earning $50–$500/month or a cluster of small wins totaling similar. If lifetime revenue is still $0 at month 12, the weekly review will write a "honest reassessment" inbox note asking Robert whether to keep going, change strategy, or wind down.

If the loop isn't earning by year 2, the honest answer is that this approach didn't work and we should stop pretending.

## When to update this file
- Update the "What is realistically likely" band ONLY when we have ≥6 months of real data from this specific loop.
- Update the timeline ONLY based on what actually happened, not what we hoped.
- Never delete the "What this loop is NOT" section. That's the anchor.
