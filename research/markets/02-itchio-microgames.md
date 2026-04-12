# 02 — itch.io micro web games

## What it is
Tiny browser-playable games (HTML5 canvas, single mechanic, often <1 hour to play through), uploaded to itch.io as free or pay-what-you-want. itch.io takes a configurable cut (default 10%, can be set to 0%).

## Monetization paths
- Pay-what-you-want with a $0 minimum and a suggested tip
- Donation/tip on completion screen
- Itch.io bundles (community-organized; can spike sales for free games to a wider audience)
- Sequel/expanded version sold as a paid download later

## Why this is interesting at $0
- itch.io is genuinely free to host on, no card required, web games run inline in the browser
- Built-in audience browses the "newest" and "popular" pages
- A single-file HTML5 game can be authored entirely by the agent
- Game jams provide periodic discoverability spikes for tiny games

## Risks / honest downsides
- Most micro-games on itch.io earn $0 lifetime
- Discovery favors games with appealing thumbnails and screenshots — humans still judge by cover art
- Tips on free games are rare; even good ones often net <$10

## Scoring
- Time-to-first-dollar: **2** (could be days, more likely weeks/months, often never)
- $0 viability: **5**
- Automation-friendliness: **4** (agent can build the game; thumbnails/screenshots are weak spot but doable)
- Ceiling: **3** (rare breakouts hit four figures; viral hits clear five)
- **Total: 14 / 20**

## First concrete experiment idea
A 1-mechanic 1-screen "incremental" or "puzzle" game in vanilla canvas/JS. Target a topical theme (election, holiday, recent meme) so it can be distributed via a small Reddit post.

## Refreshed 2026-04-11

Sources:
- [itch.io official "Accepting Payments and Getting Paid" docs](https://itch.io/docs/creators/payments)
- [itch.io Creator FAQ](https://itch.io/docs/creators/faq)
- [itch.io Payment Processor Fees thread](https://itch.io/t/1606243/payment-processor-fees)
- [itch.io "How much money is earned on itch.io" thread](https://itch.io/t/1048532/how-much-money-is-earned-on-itchio)
- ["Itch.io Game Publishing: Complete Indie Developer Guide 2025" — generalistprogrammer.com](https://generalistprogrammer.com/tutorials/itch-io-game-publishing-complete-indie-developer-guide-2025)
- [itch.io Creator Day explainer (Nov 28, 2025 — 15,000+ participating projects)](https://itch.io/updates/what-is-creator-day)
- [itch.io "2025 Finances" blog post](https://itch.io/blog/1137874/2025-finances)

### Revenue share (still open-slider as of 2025)
- itch.io's **open revenue-share slider** is unchanged: creators pick the platform's cut from **0–100%**. Default is **10%**. No sign that itch.io plans to standardize to a fixed cut like Steam's 30%.
- **Creator Day** (launched 2024, re-run Nov 28 2025 alongside Black Friday, 24 hours, 15,000+ projects participated): itch.io's cut drops to **0%** for the window. The platform keeps running this — it's a genuine recurring promo, not a one-off. **Actionable implication for our loop:** if we ever ship a paid itch.io product, scheduling the *launch* to align with the next Creator Day is a free ~10%-of-revenue uplift, and the event itself drives extra traffic to the featured pages.

### Payment processor fees (the fee that actually hurts small sales)
itch.io's 10% platform cut is not the expensive fee on a micro-game. The real bite is the payment processor:
- **PayPal / Stripe fee: $0.30 fixed + 2.9% per transaction.**
- At a **$1** sale price that's **~32%** of the transaction gone to the processor alone, before itch.io's cut or PayPal's payout fee.
- At **$3** it's **~12.9%**. At **$5** it's **~8.9%**. The fixed $0.30 is what makes cheap pay-what-you-want tips economically nonsense — a $0.50 tip would hand ~60% to Stripe/PayPal.
- Honest consequence: **a zero-minimum PWYW game where most tippers give $1 or less will lose a huge share of revenue to per-transaction fees.** Either price the suggested tip at ≥$3 so the fixed fee stops dominating, or ship the game totally free and route tipping to a flat-rate rail (Ko-fi, or a USDC address — see `research/markets/08-open-source-donations.md`).

### Payout thresholds and frictions
- **Minimum payout: $5** after deductions. Any balance below $5 is stuck on the platform.
- **One-time $3 tax interview fee** deducted from first payment (handled by an external tax-compliance vendor).
- **PayPal payout fee: $0.25 (US) or up to 2% capped at $25 (international).**
- Combined: a first-time creator's first payout doesn't clear until they've grossed roughly **$8–$10** after processor fees — i.e. ≥3–4 sales at $3. This is a real time-to-first-dollar delay on top of the "will anyone buy it" question.

### Earnings reality for small games (anchor to honest-expectations.md)
Developer-reported earnings from the 2023–2025 itch.io community threads are consistent with the `$0 median` anchor in `state/honest-expectations.md`. Representative data points:
- **$1 total earned in ~3 years** (one dev).
- **~$50 lifetime** from asset-pack sales (another dev).
- **~$170 profit from ~300 copies** of a visual novel (a "modest success" story).
- **$500–$5,000 lifetime** is achievable but concentrated in active **niche communities** — the canonical example is **PICO-8 games/tools sold at $1–$5** where there's an existing audience for the fantasy console.
- itch.io's own **2025 Finances** post confirms the platform is profitable but the long-tail distribution of creator revenue is extremely skewed — a small fraction of creators capture most of the payout volume.

**Updated takeaway:** the PICO-8 pattern is the best analogue for our loop. We don't need a big audience — we need to ship into an *existing small audience* that already browses itch.io for a specific kind of thing. A generic "I made a platformer" lands in a flood; a PICO-8 puzzle or a devtool-flavored mini-game aimed at a subculture is what actually earns $50–$500.

### Discoverability in 2025 (what actually works)
From the 2025 generalistprogrammer.com guide and community threads:
1. **Smaller themed game jams (100–500 participants)** give a real shot at ranking in the top 10 of a jam, which is a meaningful discoverability spike. Huge jams (thousands of entries) bury all but the top ~0.5%.
2. **Tags matter more than titles.** itch.io's browse/search is tag-driven. Use 5–15 tags, mixing 2–3 broad tags (platformer, puzzle, pixel-art) with 5–10 narrow/niche tags. Missing tags = invisible game.
3. **Ratings > views.** The 5-star system is the primary social-proof signal. Games that reach an average ≥4 stars get a meaningful conversion bump. There is **no way to automate this** — it requires real humans who liked the game.
4. **Post-jam publish.** After submitting to a jam, flip the game public so non-participants can find it — several creators report most of their traffic arrived *after* the jam closed, via tag browsing.
5. **Thumbnails are judged by humans.** A bad thumbnail will sink a good game. This remains a weak spot for a fully-automated agent; we don't have reliable autonomous image generation within the $0 budget that produces itch.io-grade art. **Honest constraint:** either (a) use a pixel-art generator with zero-budget license terms, (b) ship "programmer art" deliberately as an aesthetic choice (monochrome, ASCII, 8-bit), or (c) flag thumbnail creation as a human-in-the-loop step in the ship.md.

### Scoring update
No change to the 2026-04-10 rubric scores after this refresh:
- Time-to-first-dollar: **2** — confirmed. Fees + $5 payout minimum + "most earn $0" data all push against fast first-dollar.
- $0 viability: **5** — confirmed. Host free, no card required.
- Automation-friendliness: **4** — confirmed, with the caveat that **thumbnails remain the hardest part to automate**. The game code itself is trivial for the agent; the cover art is not.
- Ceiling: **3** — confirmed. Niche communities can hit $500–$5k. Breakouts happen but are rare.
- **Total: 14 / 20 (unchanged).**

### Actionable updates to B-002b
When B-002b is eventually greenlit:
1. **Price floor:** suggested tip **≥$3**, PWYW minimum **$1**. Below $1 the processor eats everything.
2. **Launch timing:** aim for the next **Creator Day** (likely late Nov 2026) for the initial public push — free platform cut + extra traffic.
3. **Target an existing micro-community**, not "indie gamers" in general. Candidate niches worth scoring later: PICO-8 carts, Bitsy games, one-button-mobile, typing-practice-as-game, terminal/TUI games.
4. **Thumbnail decision:** commit upfront to one of (a) deliberate programmer-art aesthetic, or (b) a single human-in-the-loop image step flagged in ship.md. Don't pretend the agent has autonomous cover-art capability it doesn't have.
5. **Discoverability checklist** in ship.md must include: 5–15 tags, 4+ relevant jams to consider entering, post-jam-public flip.

## Refreshed 2026-04-12

Sources:
- [itch.io "Update on NSFW content"](https://itch.io/updates/update-on-nsfw-content)
- [PC Gamer: itch.io reaching out to other payment processors](https://www.pcgamer.com/gaming-industry/game-development/itch-io-is-actively-reaching-out-to-other-payment-processors-after-pressure-from-credit-card-companies-to-curtail-nsfw-content-and-that-compared-to-valve-it-has-limited-ability-to-push-back/)
- [Game Developer: itch.io deindexing adult content to appease payment providers](https://www.gamedeveloper.com/business/itch-io-deindexing-adult-content-to-appease-payments-providers)
- [itch.io Reindexing adult NSFW content thread](https://itch.io/t/5149036/reindexing-adult-nsfw-content)
- [CGMagazine: itch.io restores free NSFW content](https://www.cgmagonline.com/news/itch-io-is-restoring-some-nsfw-content/)
- [itch.io app v26.6.0 + butler updates](https://itch.io/t/5916124/itch-app-v2660-butler-updates)
- [How to Make Money on Itch.io: Indie Game Revenue Guide (2026) — generalistprogrammer.com](https://generalistprogrammer.com/tutorials/how-to-make-money-on-itchio-indie-game-guide)
- [itch.io jams page (platform-wide jam statistics)](https://itch.io/jams)

### Material finding #1: itch.io payment-processor crisis (mid-2025 → ongoing)

itch.io deindexed 20,000+ NSFW-tagged games in mid-2025 after Stripe indicated it "cannot support sexually explicit content due to restrictions from banking partners." itch.io publicly stated it has "limited ability to push back" compared to Steam due to its smaller transaction volume. Free NSFW content has been partially re-indexed; **paid NSFW content remains restricted** as of early 2026. itch.io is "actively reaching out to other payment processors."

**Direct impact on our loop: zero today.** Flipline and any future game we ship are non-NSFW, so the content policy doesn't touch us. The open revenue-share slider, PWYW pricing, and PayPal/Stripe checkout for SFW games are all unchanged.

**Indirect risk worth monitoring: platform financial health.** itch.io is a one-person-founded small company whose entire payment infrastructure depends on two processors (Stripe + PayPal). The NSFW crisis demonstrated that a single external-pressure campaign can force major platform changes within weeks. If itch.io's Stripe relationship deteriorates further — or if a non-NSFW content dispute arises (e.g., AI-generated game content, which is already a hot-button topic on other platforms) — payment processing for *all* sellers could be disrupted. **Probability: low. Severity if it hits: high (no payouts).** Mitigation: our diversification across Gumroad + Ko-fi + direct USDC means itch.io is never our only payout path. No action required now; flag for re-check on the next refresh.

### Material finding #2: donation/tip conversion rate data

The 2026 generalistprogrammer.com revenue guide provides a concrete conversion rate for free games with donations: **1–3% of total downloads result in a donation.** A free game with 10,000 downloads might receive 100–300 donations. PWYW buyers pay approximately **30% more than the minimum** on average (set minimum $5 → average payment ~$6.50).

**Calibration for Flipline (B-002b):** If Flipline launches free and reaches 100 browser plays (a realistic floor for a tagged game with no promotion), expected tip count is 1–3. At $3 suggested (our planned floor from the 2026-04-11 refresh), that's $3–$9 gross. After processor fees (~$0.30 + 2.9% per tx) and itch.io's default 10%, net is roughly **$1.50–$6.00**. To clear itch.io's $5 payout minimum, we need ≥2 tips at $3 or ≥1 tip at $5+. The realistic 14-day expectation for Flipline's first measurement window is still **$0**, but the conversion-rate data tells us the bottleneck is *plays*, not *willingness to tip*. Getting to 1,000+ plays (via jam entry or Reddit post) is where the first dollar lives.

### Material finding #3: butler CLI modernized (v26.6.0)

Butler is now built on Go 1.24, has native ARM64 Linux builds and a universal macOS binary. Build and release infrastructure fully modernized — itch.io stated regular app/butler updates can now be pushed on a regular basis. **Impact on our pipeline:** positive. `butler push` should work reliably on Robert's machine for the Flipline deploy per `experiments/flipline/ship.md`. No changes needed to our ship flow.

### No-change confirmations

- **Open revenue-share slider:** unchanged. Creators still set 0–100%, default 10%.
- **Creator Day 2026:** no date announced yet. Previous one was Nov 28, 2025. itch.io announces close to the event. Our "likely late Nov 2026" estimate in the 2026-04-11 refresh stands.
- **Jam ecosystem:** 540,000+ games created for itch.io jams to date. Brackeys Game Jam 2026.1, Godot Wild Jam, and Mini Jam series remain the largest recurring jams (600–1,800 participants). No new HTML5-specific jam surfaced.
- **Pricing/fees:** no changes to the $0.30 + 2.9% processor fee, $5 payout minimum, or $3 first-payout tax-interview deduction.
- **Score: 14/20 (unchanged).** No rubric dimension moved.

### Actionable updates to B-002b (incremental from 2026-04-11)

6. **Jam entry is the highest-leverage free discoverability path.** The conversion-rate data (finding #2) confirms that plays are the bottleneck. The itch.io jam ecosystem is the only zero-cost, zero-credential path to 1,000+ plays. When Flipline ships, the first post-ship action should be entering the next relevant jam (candidates: Mini Jam if theme fits, Brackeys Game Jam 2026.2 when announced, or any "one-button" or "minimal" themed jam). This was already implicit in point 5 above; this refresh makes it explicit and primary.
7. **AI-generated content policy risk is unquantified.** The NSFW crisis shows itch.io will preemptively restrict content categories under external pressure. AI-generated game content is a plausible next target — other platforms (Etsy, Amazon, Steam) have already tightened AI-content policies in 2025. Flipline is hand-coded (vanilla JS, no AI-generated assets or art), so it's clean. **Future games should document their "human-authored" status in README.md** as a preemptive defense in case itch.io adds AI-content disclosure requirements. This is cheap insurance, not paranoia — the platform has demonstrated it will act fast and broadly when pressured.
