# 01 — Browser utilities (single-page tools)

## What it is
Tiny single-page web tools that solve one annoying problem. Examples in the wild: JSON formatters, regex testers, image compressors, color pickers, "remove background", PDF mergers, AI prompt cleaners, unit converters, name generators. Single HTML file, no backend, hosted free on GitHub Pages or Netlify free tier.

## Monetization paths
- "Buy me a coffee" / Ko-fi tip jar (free, no platform fee on Stripe-direct)
- Affiliate links to relevant paid tools
- Pro version on Gumroad (free tier) for an upgraded feature
- Display ads (only after meaningful traffic — not day 1)

## Why this is interesting at $0
- Truly $0: GitHub Pages is free, no domain required (`username.github.io/tool` works)
- Discoverable by SEO long-tail and by posting in niche subreddits / Hacker News
- Agent can build, ship, iterate without any external creative bottleneck

## Risks / honest downsides
- Saturated for the obvious tools (JSON formatter has 10,000 competitors)
- Discoverability is the entire game; building is the easy 10%
- Tip jars convert at fractions of a percent — needs traffic at scale or a niche audience

## Scoring
- Time-to-first-dollar: **3** (days to ship, weeks to first tip if niche is right)
- $0 viability: **5**
- Automation-friendliness: **5**
- Ceiling: **3** (rare hits can clear $10k/yr; most clear $0)
- **Total: 16 / 20**

## First concrete experiment idea
"AI Prompt Cleaner" — paste a messy LLM prompt, get a normalized version (strip markdown noise, collapse whitespace, optionally rephrase). Targets the AI tooling subreddit audience which is large and growing.

## Refreshed 2026-04-10

**Donation conversion rates for free indie tools** (verified 2026-04-10):
- **Free games:** 1–3% of *downloads* convert to a tip (10k downloads → 100–300 tippers). This is the *high* end because games create emotional engagement. Tools convert worse.
- **Free browser tools / utilities:** typical conversion is **0.1%–0.5%**. One Indie Hackers writeup reported **1 tip per 4,206 visitors** (~0.024%) on Buy Me a Coffee — this is more representative for utility tools than the game numbers above.
- Implication: a browser tool needs **high four-digit visits per month** to make even modest tip income ($10–50). A *viral* moment (~50k visits) might net ~$100. This is order-of-magnitude expectations, not a forecast.

**Best tip rail for browser tools** (lowest fees, simplest setup):
1. **Ko-fi** — 0% on direct support. Best.
2. **Buy Me a Coffee** — 5% flat. Acceptable.
3. **Gumroad** — 10%+ + $0.50, only good for *paid* products not tips.
4. **GitHub Sponsors** — 0% from GitHub, but eligibility-gated and slow.

**Strategy for prompt-cleaner specifically:**
- Embed a Ko-fi link in the footer (not a popup, not a paywall)
- Add a USDC tip option pointing at the Kraken Solana address (`EQwtTPe3GfcAGAiQAh3AxmCZ1WAyCviDsNnBmfCaQwf7`) for crypto-native users
- Honest expectation: first 30 days probably $0–$5 in tips. Real signal is *traffic*, not money.

**Sources:**
- [Indie Hackers — 1/4206 BMaC conversion rate](https://www.indiehackers.com/post/1-4206-conversion-rate-on-buy-me-a-coffee-1ed21a2288)
- [Itch.io revenue guide 2026 — generalistprogrammer.com](https://generalistprogrammer.com/tutorials/how-to-make-money-on-itchio-indie-game-guide)
- [Buy Me a Coffee alternatives 2026 — fourthwall](https://fourthwall.com/blog/buy-me-a-coffee-alternatives-for-creators)
