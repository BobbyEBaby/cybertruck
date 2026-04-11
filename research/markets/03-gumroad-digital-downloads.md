# 03 — Gumroad digital downloads (templates, packs, guides)

## What it is
Sell a digital file (or zip of files) on Gumroad's free tier. Common formats: Notion templates, Excel/Sheets templates, prompt packs, icon packs, font collections, ebook PDFs, Figma kits, Blender assets, planner printables.

## Monetization paths
- One-time sales of the file ($3–$30 typical)
- Bundle multiple files for a higher price
- "Pay what you want" with a $0 minimum to maximize downloads + reviews

## Why this is interesting at $0
- Gumroad free tier is genuinely free; they take a percentage per sale (≈10% + Stripe fees on the free plan, check current rates)
- The agent can author Notion/Sheets templates, prompt packs, ebook PDFs
- Distribution is via Twitter/X, Reddit, Pinterest — all free organic

## Risks / honest downsides
- Gumroad does very little discovery work — you bring the traffic
- Templates are saturated for the obvious niches (productivity, fitness)
- Gumroad's payout terms and fees change; check `gumroad.com/pricing` before committing

## Scoring
- Time-to-first-dollar: **3** (days to ship a template, weeks to a sale if niche is right)
- $0 viability: **5**
- Automation-friendliness: **5** (agent can produce templates and listing copy)
- Ceiling: **4** (best-selling templates clear $1k–$10k+; possible to compound across many)
- **Total: 17 / 20**

## First concrete experiment idea
A "Claude Code prompt pack" or "AI agent operating-loop template" — sell to the same audience that follows AI tooling. Niche, but it's *our* niche, which is a defensibility edge.

## Refreshed 2026-04-10

**Current Gumroad fee structure** (verified 2026-04-10):
- **10% + $0.50** per transaction on direct sales (your own links)
- **30% flat** per transaction on Discover marketplace sales (when Gumroad's own search/browse surfaces your product)
- **Plus** payment processor fees: ~2.9% + $0.30 (Stripe / PayPal)
- **Effective total on direct sales:** ~12.9% + $0.80 per transaction
- **Effective total on Discover sales:** ~32.9% + $0.80 per transaction
- **Payouts:** every Friday. Bank deposit (US) free. PayPal payouts 2%. Instant payouts 3%.

**Implication for our $0/$1–$5 tier products:** the $0.50 flat fee is *brutal* on micro-priced items. A $3 product nets ~$2.20 after Gumroad + processor — not catastrophic. A $1 product nets ~$0.20. **Price floor should be $3+** to keep the take rate sane. Pay-what-you-want with a $3 suggested minimum is the right shape.

**Strategic note on Discover:** the 30% fee is a tax on Gumroad's own discoverability. If we're driving all our own traffic (Reddit, X, etc.), avoid the Discover surface. If we want passive sales, the 30% is the cost of that passivity — probably worth it on later experiments once we have something proven.

**Ko-fi as alternative for tip-jar use case:** for browser tools where the goal is "tip me", **Ko-fi charges 0% on direct support** (vs Buy Me a Coffee's 5%, vs Gumroad's 12.9%+). If the product is a tool not a download, Ko-fi is the better tip rail.

**Sources:**
- [Gumroad pricing official](https://gumroad.com/pricing)
- [Gumroad fees 2026 — wearefounders.uk](https://www.wearefounders.uk/gumroad-fees-2026-what-sellers-actually-pay-per-sale/)
- [Gumroad pricing breakdown — schoolmaker](https://www.schoolmaker.com/blog/gumroad-pricing)

## Refreshed 2026-04-11

Full re-verification pass driven by B-002 (Claude Code Power Prompts) being the next imminent ship — this is the category our first dollar most likely comes through, so the number underpinning the 17/20 top score needs to be current. No score change (still **17/20**) but **four material new findings** that change how we ship B-002 and how we queue B-011.

### 1. Merchant of Record since January 2025 — material simplification
As of January 2025, Gumroad operates as a **Merchant of Record** for global sales. This means Gumroad collects and remits **VAT, GST, and sales tax** on our behalf in every jurisdiction where a customer buys. **We do not need to register for tax in any foreign jurisdiction.** Previously this was a blocking concern for a solo operator — international tax compliance is a $1000+/year accountant bill at scale, and Gumroad now eats it internally. This is the single biggest structural change since the 2026-04-10 refresh and it materially de-risks B-002.

**Implication for the loop:** no `human_inbox/` note needed asking Robert to set up a VAT number, EU OSS registration, or UK MTD compliance. Revenue from non-US customers lands net-of-tax without separate bookkeeping. Keep the Kraken USDC-Solana rail in accounts.md as the downstream destination — the MoR status is about tax, not payouts.

### 2. Payout mechanics confirmed: no minimum threshold
Weekly Friday payouts confirmed current. **No minimum balance** to trigger a payout — even a first $2.20 sale pays out the following Friday (subject to a 7-day processing hold). Rails:
- **Bank (US, supported countries):** free, 2–7 business days in local currency
- **Stripe Connect:** connected directly, faster
- **PayPal:** 1–3 business days, **2% fee** (avoid for small amounts — eats disproportionately at $3 PWYW prices)
- **Instant payouts:** 3% fee, up to $10K per payout, available to US creators after 4 completed payouts (so not day-1)

**Implication for the loop:** first-dollar milestone actually settles on the first Friday after the first sale — no accumulation threshold to clear. This affects how `state/goal.json.milestones` get hit: expect `first dollar earned` to trigger within a week of the first sale, not after a month of accumulation.

### 3. Refund policy — Gumroad keeps its 10% on refunds
Confirmed: if a $10 product is refunded, Gumroad does **not refund its $1.00 platform fee**. The seller absorbs both the refund and the already-taken Gumroad fee. At B-002's $5 PWYW suggested price, a single refund means losing ≈$5.80 (the $5 paid out + $0.80 effective fees already taken on the sale) against a nominal $4.20 net received — so a **refund is a ~1.38× loss** on that sale, not a wash.

**Implication for the loop:** honest product descriptions and accurate preview pages are not just ethical, they're net-positive expected value. Do **not** oversell B-002 ("15 prompts" is the accurate count — do not round up, do not imply more). Include the full table-of-contents in the public listing so buyers can self-qualify before clicking Buy.

### 4. AI prompt pack category is saturated — niche specificity is now the only edge
Current data: Gumroad already hosts a dense field of "Claude AI Prompt Library (2026 Edition)", "The Prompt Bible — 1,000+ prompts", "All-in-One Booster AI Kit 3.0 — 150k AI Prompts + 7 AI Courses", "Claude Code for Designers — 2026 Course", "AI Prompt Pack for Digital Sellers — 100 ChatGPT Prompts", etc. Many price in the $10–$30 range and some are mega-bundles (thousands of prompts). The generic "AI prompts pack" category is now in the bifurcated state Gumroad commentators describe: **high-competition mature category with rapidly-emerging niche sub-pockets**. 150k-prompt bundles compete on raw volume; our 15-prompt pack cannot and should not.

Real success stories at our end of the curve: one public writeup ("How I Made My First $1,000 Selling AI Prompt Packs on Gumroad", Medium, March 2026) hit $1,000 in the first two months via a **specific niche + honest posting + small targeted audience**, not via volume. Another public data point: 609 sales in a full year earning just over $304 — that's ~$0.50 net per sale, consistent with a $1 PWYW pack where most buyers pay $0 and a few pay $2–5. Another: $25/month passive baseline on an existing pack. These are **median-curve honest numbers**, not outliers, and they match `honest-expectations.md` — no rubric change.

**Implication for B-002 specifically:** our positioning must lean hard on **"Claude Code" (the CLI tool) not "Claude" (the model)** as the distinguishing niche. The two are very different search intents. "Claude prompts" = 1000s of generic LLM-product pages. "Claude Code prompts" = much smaller field, and the existing "Claude Code for Designers" / "Claude Code — 2026 Course" products compete on course-length/comprehensiveness, not on a tight "15 prompts that made me ship faster" shape. Our niche is: **the CLI power-user audience who already uses Claude Code, not the general LLM-curious audience**. The listing title, description, and Reddit post must say "Claude Code" in the first three words, every time.

**Implication for B-011 (second Gumroad asset queue):** do **not** ship a generic "100 AI prompts" sequel — that's the exact saturated shape that underperforms. Candidates that fit our niche-specific shape:
- "Claude Code CLAUDE.md templates — 10 battle-tested project scaffolds"
- "Agent operating-loop starter kit — the cybertruck-autopilot pattern with the specific-to-you bits blanked out"
- "Claude Code hook recipes — 15 automation hooks for common dev workflows"

All three stay inside our authentic authority zone (we actually run this loop) and avoid the "me-too LLM prompt dump" category.

### 5. Platform health — modest growth with a shakeout
Gumroad company revenue hit **$23.8M in 2024, up from $21.4M in 2023** (+11% YoY, modest for a creator-economy platform). Active customer count ~27k as of 2024. Store count dropped **-43.5% Q/Q in Q4 2025 but +12% YoY** — the quarterly drop is consistent with an inactive-account cleanup / shakeout wave rather than organic churn. Broadly: the platform is still there, still growing slowly, still paying out. Not the boom-era Gumroad, not a dying platform either. **No platform-risk reason to avoid Gumroad for B-002.**

### 6. Category revenue distribution — our niche is mid-tail, not top-of-stack
Top-selling niches by revenue in 2026: **3D Design, Graphic Design, Business** — 3D alone accounts for ~88% of total platform revenue (~$2.2B GMV). Our AI-tooling/prompt-pack niche is not on the top-revenue list but is on the "viable and growing" side of the bifurcation. **This is fine and expected** — we are not trying to beat the top 3D-asset creators, we are trying to earn a first $1 from the exact niche audience that already reads AI tooling posts on Reddit/Twitter. The honest read is that our ceiling in this niche is `$50–$500/month for a hit product, $0 for a miss`, exactly what `honest-expectations.md` says.

### 7. Scoring — no change
- Time-to-first-dollar: **3** (unchanged — build in days, sell in weeks if the niche lands)
- $0 viability: **5** (unchanged — still free to list, still free to publish, MoR status removed a tax-compliance hidden cost)
- Automation-friendliness: **5** (unchanged — the agent can author the asset; only upload requires `GUMROAD_ACCESS_TOKEN`)
- Ceiling: **4** (unchanged — mid-tail niche, $1k–$10k+ achievable, 3D-Design category outliers are not our category)
- **Total: 17 / 20 — unchanged**

### Recommendation for the loop
1. **Ship B-002 as currently built** — the Claude Code Power Prompts pack is the right shape. No rewrite needed. But when Robert runs `ship.md` locally, the listing copy must use "Claude Code" (the CLI) in the first three words of the title and description, not generic "Claude" or "AI prompts" or "LLM". The title should specifically not be the shape "15 AI Prompts" — that falls into the saturated generic bucket. Prefer a shape like **"Claude Code Power Prompts — 15 prompts for shipping faster in the CLI"**.
2. **Pricing: stick with $5 PWYW with a $3 floor suggestion** — below $3 the Gumroad $0.50 flat fee eats the margin, above $5 the pack would need >15 prompts to justify against the saturated 100-prompt / 1000-prompt competitors. $5 PWYW is honest.
3. **B-011 candidate shortlist** (pick one after B-002 ships and produces a week of measurement data): (a) Claude Code CLAUDE.md templates pack, (b) Agent operating-loop starter kit, (c) Claude Code hook recipes. All three leverage our authentic authority and avoid the generic-prompts-pack graveyard.
4. **Do not touch Gumroad Discover paid-promotion surface** — the 30% Discover fee is a tax on passive traffic we don't have yet. All our early traffic should be direct (Reddit, X, our own GitHub Pages footers linking to the Gumroad product). Once a product has measurable organic direct sales, re-evaluate whether turning on Discover is worth the 30% cut — not before.
5. **Honest listing descriptions** — given the refund math (refunds are ~1.38× losses, not washes), every listing must accurately describe what's in the pack. Full table-of-contents, honest word counts, no "150+ use cases" inflation. This also compounds reputationally across products, which is the only path to a B-011/B-012+ cluster that actually earns.

### Sources (verified 2026-04-11)
- [Dodo Payments — Gumroad Fees in 2026: Complete Pricing Breakdown](https://dodopayments.com/blogs/gumroad-fees-explained) — flat 10% + $0.50 direct, 30% Discover, Stripe 2.9% + $0.30 processor, effective 13–23% depending on price point
- [SchoolMaker — Gumroad Pricing 2026: Plan Comparison](https://www.schoolmaker.com/blog/gumroad-pricing) — Merchant of Record since January 2025 (handles global VAT/GST/sales tax), payout rails + fees, instant-payout eligibility after 4 payouts
- [CheckoutPage — Gumroad pricing 2026: Fees, plans & what sellers pay](https://checkoutpage.com/blog/how-gumroad-pricing-works-and-a-cheaper-alternative) — refund policy (Gumroad keeps its 10% platform fee on refunds)
- [Gumroad Help Center — Getting paid](https://gumroad.com/help/article/13-getting-paid) — weekly Friday payouts, no minimum balance, 7-day processing hold
- [Gumroad Help Center — Payout delays](https://gumroad.com/help/article/281-payout-delays) — PayPal 2% + 1–3 days, bank 2–7 days, instant 3% up to $10K
- [Electroiq — Gumroad Statistics 2025](https://electroiq.com/stats/gumroad-statistics/) — 46k creators earned money in 2020, 8 over $1M
- [Sacra — Gumroad at $21M](https://sacra.com/research/gumroad-at-21m/) — $21.4M 2023 → $23.8M 2024 revenue, ~27k customers
- [StoreLeads — The State of Gumroad in 2026](https://storeleads.app/reports/gumroad) — store count -43.5% Q/Q Q4 2025, +12% YoY (shakeout wave)
- [Low Content Profits — Gumroad Earnings in 2025: Views, Sales, and Income Report](https://lowcontentprofits.com/gumroad-digital-products-earnings/) — 609 sales = $304 full-year median-curve data point, $25/month passive baseline data point
- [AIYA Hub — How All Major Platforms Regulate AI-Generated Content](https://www.aiyahub.com/blog/how-all-major-platforms-regulate-ai-generated-content) — Gumroad has no AI-content ban; sellers must own rights and not infringe
- [Simple Scale (Medium, March 2026) — How I Made My First $1,000 Selling AI Prompt Packs on Gumroad](https://simplescale.medium.com/how-i-made-my-first-1-000-selling-ai-prompt-packs-on-gumroad-93663abcc492) — $1,000 in first two months via niche + honest posting
- [InsightRaider — What Sells Best on Gumroad? 146K Products Ranked (2026)](https://insightraider.com/en/answers/what-digital-products-sell-best-on-gumroad) — top niches 3D Design / Graphic Design / Business, 3D = ~88% of platform revenue
- [Accio — Top Selling Products Gumroad 2026 Trends & Insights](https://www.accio.com/business/top-selling-products-on-gumroad) — AI prompt packs market "extremely saturated, niche beats broad every time"
- [InfoProdSpy — What Sells Best on Gumroad 2026 (207k products analyzed)](https://infoprodspy.com/blog/what-sells-best-on-gumroad) — bifurcation of saturated vs. emerging niche sub-pockets
- [Gumroad Help Center — Gumroad Discover](https://gumroad.com/help/article/79-gumroad-discover) — Discover feature surface, 30% fee trade-off for platform-driven traffic
