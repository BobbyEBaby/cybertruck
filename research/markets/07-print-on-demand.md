# 07 — Print-on-demand (Redbubble, Merch, Etsy POD)

## What it is
Upload designs to a print-on-demand marketplace (Redbubble, TeePublic, Amazon Merch on Demand, Etsy via Printful). The platform handles printing, shipping, and payment. You get a royalty per sale.

## Monetization paths
- Royalty per sale (typically $1–$5 net per t-shirt, more for larger products)
- Volume game: hundreds of designs across many products

## Why this is interesting at $0
- Genuinely free to upload on Redbubble and TeePublic (no card required)
- The agent can generate design concepts, tags, descriptions
- Amazon Merch requires an application and approval but is free

## Risks / honest downsides
- AI-generated art is a controversial input on these platforms; some are tightening rules
- Discovery is brutal; mass-uploaders dominate
- Royalties are tiny — high volume needed for meaningful revenue
- Image generation costs money (most APIs aren't free), so agent → image is not strictly $0
- Trademark and copyright violations get accounts banned permanently — be careful

## Scoring
- Time-to-first-dollar: **2** (weeks to a first sale if anything)
- $0 viability: **3** (free if you use free image tools; downgraded otherwise)
- Automation-friendliness: **3** (agent can write listings; visual generation is the constraint)
- Ceiling: **3** (some sellers do clear five figures; most clear $0)
- **Total: 11 / 20**

## First concrete experiment idea
Defer. Low score, account ban risk, image-gen cost question, and AI-art political risk make this a worse bet than tools and templates.

## Refreshed 2026-04-11

Data pass run from a scheduled remote agent as the final B-009 file. This is the last stale file in `research/markets/`; after this commit, B-009 moves to Done. **Conclusion: deprioritized hard — score 11 → 7.** Print-on-demand is no longer an honest fit for a zero-budget, fully-automated, agent-authored loop. Every major platform tightened against the exact profile we'd produce (AI-generated art + no human-built brand + bulk uploads + no original photographs to license), and the one remaining platform that's truly free upfront (Redbubble + TeePublic) explicitly rate-limits new AI accounts to a level where the volume math no longer works.

### What changed since the May 2025 cutoff

**1. Etsy's June 10 2025 Creativity Standards rewrite is the hardest single hit to POD.**
On 2025-06-10 Etsy quietly removed the phrase "or using a templated design or pattern" from its Creativity Standards, narrowing the policy to require every item to be "based on a seller's original design" ([Value Added Resource — Etsy Creativity Standards Update June 10 2025](https://www.valueaddedresource.net/etsy-creativity-standards-update-june-2025/), [Etsy — Creativity Standards / House Rules](https://www.etsy.com/legal/creativity/), [Listing Compliance Shield — Etsy Creativity Standards POD Sellers Guide](https://iscompliant.app/Blog/etsy-creativity-standards-pod-sellers-guide)). The change was applied **retroactively with no grace period**, with appeals only available for listings removed after July 15 2025 ([Medium — Libée Lune: Etsy Changes the Rules June 2025](https://medium.com/@libelune/etsy-changes-the-rules-what-pod-and-ai-creators-need-to-know-june-2025-ce447125f86a)). Designs built from purchased templates, clip-art bundles, ready-made graphics, or commercially-licensed AI prompts now violate policy *even with a valid commercial license*. Sellers must use original prompts, disclose AI use in the listing, label items as "Designed by" not "Made by", and survive an aggressive automated enforcement system that reportedly removes original work while leaving obvious template products up ([eFulfillment Service — Etsy Updates July 2025](https://www.efulfillmentservice.com/2025/07/etsy-updates-july-2025-new-creativity-standards/), [XHBT — Etsy AI Art Policy 2025 Guide](https://www.xhbt.org/blog/etsy-s-ai-art-policy-2025-complete-guide), [Etsy Seller Handbook — Etsy's stance on AI creations](https://www.etsy.com/seller-handbook/article/1275449912004)). For our loop this is effectively a closed door — every artifact we'd produce would be a templated AI generation by definition.

**2. Redbubble made AI disclosure mandatory and rate-limits new AI uploads to 5 per day.**
Redbubble shipped a dedicated AI Disclosure checkbox + dropdown in Q2 2025 and tightened seller-compliance checks against tag dishonesty (no "hand-drawn" or "traditional painting" tags on AI work) ([EC Arts — Redbubble AI Art Upload Tutorial 2025 Policy](https://ec-arts.com/redbubble-ai-art-upload-tutorial-2025-policy/), [PrintKK — Can You Sell AI Art on Redbubble: New Rules](https://www.printkk.com/blog/articles/can-you-sell-ai-art-on-redbubble)). More importantly for our volume math: **new accounts that tag uploads as AI-generated are capped at 5 uploads per day**, established sellers (100+ sales) at 20/day, and Boosted Artists at 50/day. AI-tagging is required, so the cap binds. POD strategies that work on Redbubble in 2025+ are 100% volume-driven — successful sellers post hundreds to thousands of designs to surface a handful of winners. A 5/day cap means a fresh agent account would take ~2 months to reach 300 designs, by which point Redbubble's automated takedown sweeps will have eliminated a chunk of them anyway. The category's main mechanic — flood the catalog and let the long tail find buyers — is structurally broken for a new account. Existing suspension-reason categories (mass-produced reproductions, stock images, spam, fraud) remain in force ([Redbubble Help — Why was my account suspended](https://help.redbubble.com/hc/en-us/articles/360056437771-Why-was-my-account-suspended)).

**3. Amazon Merch on Demand is invitation-only with explicit anti-AI-bot vetting.**
Merch on Demand requires an application that takes "three weeks to three months" to process, and the application stage now explicitly screens against low-effort AI bots ([amzprep — 2025 Guide to Amazon Merch on Demand](https://amzprep.com/amazon-merch-on-demand/), [BeBold Digital — Is Amazon Merch on Demand Still Worth It in 2025](https://www.bebolddigital.com/blog/amazon-merch-on-demand), [Print on Demand Business — How to Start Amazon POD in 2026](https://www.printondemandbusiness.com/blog/how-to-start-amazon-print-on-demand-in-2025/), [Stores Automation — Amazon Merch on Demand 2026](https://storesautomation.com/amazon-merch-on-demand/)). Approval is not guaranteed and sellers report the bar tightened materially in 2025. The tier system is strictly enforced — new accounts start at **Tier 10** (10 active designs only), graduating to 25, 100, 500 only after sales accrue. Mass-uploaded raw Midjourney output with generic titles gets accounts "search suppressed" ([Merch Momentum — The Truth About Amazon Merch's Approval Process](https://merchmomentum.com/the-truth-about-amazon-merchs-rigged-design-approval-process/)). Linking to a legitimate external portfolio (Behance, Instagram art account) significantly increases approval odds — which we can't fake. Royalties remain $1–$5/sale on $15–$25 t-shirts, monthly EFT payouts, the only first-party rail that could legitimately exceed the Kraken minimum without extra conversion ([Amazon — Merch on Demand Royalties](https://merch.amazon.com/resource/201858580)). But the application moat is now the binding constraint, and it requires Robert's portfolio + identity, not the agent's.

**4. TeePublic stayed permissive on AI but is small and zero-leverage.**
TeePublic's TOS doesn't explicitly address AI art and the platform is the most lenient of the big three on input source ([Top Bubble Index — TeePublic & AI Art: Can You Sell AI-Generated Designs](https://www.topbubbleindex.com/blog/teepublic-ai-art/)). Daily upload cap is 50 designs, image minimums are 1500×1995 ([TeePublic Zendesk — Upload Limits](https://teepublic.zendesk.com/hc/en-us/articles/115013698727-Is-there-a-limit-to-how-many-designs-I-can-upload)). Royalties are fixed: $4 per $20 t-shirt, $8 per $45 hoodie, halved during sale events that run most of the time. The platform is smaller than Redbubble and TeePublic's discoverability is dominated by mass-uploaders with 5,000+ design catalogs. The fixed-royalty + sale-cannibalization structure makes the per-unit math worse than Amazon Merch's variable royalty.

**5. The "free AI image generation with commercial rights" path is murkier than it looked in 2024.**
Bing Image Creator (Microsoft, free tier) is the most-cited free option, but the Terms of Use grant Microsoft a license to "use your prompts and Generations in connection with [its] services," which means **non-exclusive output and ambiguous commercial sublicensing** even though commercial use is technically permitted ([Microsoft Q&A — Can I use Bing AI images for commercial use](https://learn.microsoft.com/en-us/answers/questions/5442930/can-i-use-the-images-that-i-generated-in-bing-ai-f), [Microsoft Bing — Image Creator features page](https://www.microsoft.com/en-us/bing/features/bing-image-creator/?form=MA13FV)). 15 fast generations/day, then throttled. FLUX.2 only supports commercial use through Black Forest Labs' **paid** services ([Webyurt — Top Free AI Image Generators for Commercial Use](https://www.webyurt.com/top-free-ai-image-generators-for-commercial-use)). Stable Diffusion run locally is genuinely $0-and-commercial-clean, but requires a GPU with ≥8GB VRAM that the remote sandbox does not have. The honest answer for *this* loop's environment: there is **no free, agent-runnable, commercially-clean image generation pipeline** today. Every viable path either costs money, retains some rights for the provider, or requires Robert's local hardware — making the "agent → image" link in the chain a real constraint, not the easy dependency it appeared to be in the bootstrap.

**6. Saturation + AI fatigue + algorithmic suppression means the long-tail floor is now $0.**
The 2017–2022 "gold rush" on POD is over and most current sources agree the field is "fragmented, not saturated" — meaning success now requires dominating a hyper-specific niche rather than uploading volume ([Merchize — Is POD Oversaturated in 2026](https://merchize.com/is-print-on-demand-oversaturated/), [Print on Demand Business — Is POD Dead in 2026](https://www.printondemandbusiness.com/blog/is-print-on-demand-dead-in-2025/), [Gelato — Is POD still profitable 2025](https://www.gelato.com/blog/is-print-on-demand-still-profitable-in-2025)). Reported earnings vary wildly: Gelato cites $1.5k–$9.8k/mo for *active* sellers, Printify says new sellers reach $1k in ~165 days "on average". These are survivor-biased numbers from people who haven't quit. The honest reading consistent with `honest-expectations.md` is the same as Redbubble's published distribution: a small minority earn meaningfully, the median is $0, and the gap is widening as platforms enforce against bulk-AI accounts.

### Rescore (11 → 7)

| Axis | Old | New | Reason |
|---|---|---|---|
| Time-to-first-dollar | 2 | **1** | Downgraded. Etsy's June 2025 retroactive policy + Amazon Merch's 3-week-to-3-month invite review + Redbubble's 5/day AI cap = TTF$ measured in months for a brand-new account *if* it ever clears at all. |
| $0 viability | 3 | **2** | Downgraded. Free upload tier survives, but the input chain (commercially-clean image generation) is no longer reliably free for an agent without local GPU hardware, and Amazon Merch remains application-gated even on the upload side. |
| Automation-friendliness | 3 | **1** | Downgraded hard. Every major platform now has AI disclosure requirements + automated takedown sweeps + bulk-upload rate caps specifically designed to filter the agent profile. Etsy retroactively bans templated/prompt-purchased designs. Amazon Merch's application screening explicitly filters AI bots. Redbubble caps new AI accounts at 5/day. The few automation-friendly footholds left (TeePublic, Redbubble pre-cap) are the lowest-leverage of the platforms. |
| Ceiling | 3 | **3** | Unchanged. Top sellers do still clear five figures monthly. They get there through niche moats, brand identity, and human marketing — none of which the agent can manufacture. |
| **Total** | **11** | **7** | Material downgrade. POD now scores **lower than every other refreshed category** including 04-niche-content-sites (11) and 05-chrome-extensions (10). It is the worst-fit category in the entire research set for this loop. |

### Recommendation for the loop

**Do not pursue print-on-demand as a Cybertruck path. At all.** Specifically:

1. **Do not create POD accounts as part of any future setup ask.** The original `human_inbox/0001-setup.md` does not list Redbubble/TeePublic/Etsy/Amazon Merch — keep it that way. If a future run is tempted to add them, re-read this section first.
2. **Do not propose POD experiments under B-010, B-011, or any new backlog item.** The category fails the zero-budget rule (image generation is no longer cleanly free for our environment), the automation rule (every platform's enforcement specifically filters our profile), and the ship-small rule (the volume math requires hundreds of designs to find a single winner).
3. **Do not propose "wrapping a browser tool as POD merch" as a follow-on.** It's a different category entirely (apparel branding around an existing audience), would only make sense after one of the browser tools earned a real audience, and even then would be a Robert-judgment call, not an autopilot expansion.
4. **If Robert manually reports POD interest via `human_outbox/`**, the agent should write an honest reply note pointing at this section and asking him to confirm before any backlog action — POD requires Robert's identity, portfolio, and creative voice to clear the application/disclosure gates we cannot. This is fundamentally a Robert-led category, not an agent-led one.
5. **Treat POD as a permanently `[circuit-broken]`-equivalent category** without consuming an actual circuit-breaker slot. The circuit-breaker mechanism in CLAUDE.md is for categories that *shipped and got zero* — POD is a category we're declining to ship to *before* burning effort on it. Honest preemptive deprioritization is cheaper than three failed experiments.

### What's still worth watching

- **Whether Etsy walks back the June 2025 Creativity Standards revision.** They've already made one mid-policy clarification; if seller pushback forces a templated-design carve-out, POD becomes worth a single low-cost re-evaluation.
- **Whether a genuinely free, locally-runnable, commercial-clean image generator emerges that the remote sandbox can use without GPU.** Stable Diffusion needs hardware; FLUX needs paid API; Bing retains rights. If a CPU-friendly model with a clean license appears, the "$0 viability" score moves up by 1 — but not enough by itself to revive the category.
- **Whether Amazon Merch lowers its application bar for accounts linked to a verified external portfolio.** If they ever reduce the wait below ~7 days and accept a GitHub Pages portfolio (e.g. one of our shipped browser tools as the "external portfolio"), the application moat becomes crossable. We'd still need Robert's identity for the W-9, so it stays at most a Robert-action task.
- **Whether Redbubble removes the new-account AI cap.** The 5/day cap is the single biggest mechanical block on volume strategies. If it goes away, Redbubble's score recovers a point — still the worst category in the set, but worth re-checking.
- **Whether one of our shipped browser tools spontaneously generates demand for branded merch from real users.** That signal would be the only honest trigger for any POD-shaped experiment, and it would be Robert-led (he'd have to design or commission the merch art), not agent-led.

