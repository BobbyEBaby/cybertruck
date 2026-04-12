# 04 — Niche content / SEO sites

## What it is
A static site targeting a specific long-tail search query cluster. Examples: a calculator site for one obscure profession, a database/wiki for a niche hobby, a comparison site for a small product category. Hosted free on GitHub Pages, Netlify, or Cloudflare Pages.

## Monetization paths
- Display ads (Ezoic, Mediavine — but Mediavine has minimum traffic requirements)
- Affiliate links (Amazon Associates, niche affiliate programs)
- A small paid product or course as the upsell

## Why this is interesting at $0
- Static site generators (or hand-rolled HTML) are free to host
- Content can be agent-authored at scale
- A single dominant page on a long-tail query can earn passively for years

## Risks / honest downsides
- Google is increasingly hostile to AI-generated content sites; recent updates have hammered them
- Time-to-first-dollar is *months* — SEO is a slow game
- Display ad networks have minimum traffic thresholds before approval
- Affiliate programs require disclosure and have restrictions

## Scoring
- Time-to-first-dollar: **1** (months minimum for SEO; first dollar often 3–6 months out)
- $0 viability: **5**
- Automation-friendliness: **4** (agent can write content; quality bar is the constraint)
- Ceiling: **5** (a real SEO winner can clear $10k+/mo; very rare though)
- **Total: 15 / 20**

## First concrete experiment idea
Defer this category until something faster has shipped. Good *long-term* compounding play, bad *first* play because it can't validate the loop.

## Refreshed 2026-04-11

Rolling B-009 refresh, 3rd file done (after 02-itchio-microgames and 08-open-source-donations). 5 WebSearch queries run for 2025/2026 data on AI Overviews impact on publishers, Google's stance on AI-generated content, display ad network thresholds, Amazon Associates commissions, and programmatic SEO case studies.

### Headline finding: this category is materially worse in 2026 than at bootstrap
The risks noted in the original scoring (Google hostility, slow TTF$, ad-network thresholds) have all intensified. **Zero-click search + AI Overviews are collapsing the top of the funnel faster than any scoring model from 2024 anticipated.** Concrete data:

- **Publisher traffic is down ~33% globally year-over-year to November 2025** (Press Gazette). The Digital Content Next (DCN) study found median YoY referral traffic from Google Search down 10% (news brands −7%, non-news brands −14%).
- **Zero-click queries are now 69% of all Google searches** (Similarweb, cited via Dataslayer). When an AI Overview is present, organic CTR drops from 1.76% to 0.61% — a **61% CTR collapse** on AI-Overview queries (Seer Interactive, Sept 2025). Some publishers have reported up to −89% CTR on desktop (DMG Media).
- **AI Overviews appear on 13.14% of all queries as of 2025**, up from 6.49% in January 2025 (Search Engine Land), and they disproportionately hit informational queries — which are exactly the long-tail niche-site target.
- **Real casualties, not just percentages:** The travel blog The Planet D **shut down after traffic fell 90%** post-AI-Overviews. Business Insider organic search fell −55% April 2022 → April 2025. NPR described the impact on online news publishers as an "extinction-level event."
- **Forward-looking survey:** publishers expect search traffic to drop a further **43% on average over the next 3 years** (Search Engine Land, citing a news-publisher report).

What this means for a zero-budget agent loop: the category's ceiling is still real at the extreme top (programmatic SEO giants with unique data assets still win), but the median niche-content path — hand-author long-tail articles, let Google send traffic, monetize with ads/affiliates — is a graveyard in 2026. We shouldn't pretend otherwise.

### Google's 2025 stance on AI-generated content — nuance matters
Google officially does not penalize AI content **as a category**. But the distinction has sharpened:

- **Scaled content abuse is now an active enforcement category.** Google has issued manual actions to sites publishing "large amounts of AI-generated content at scale" where the purpose is ranking manipulation rather than user value, with Search Console notifications explicitly citing "scaled content abuse" (Google Search Central, Search Engine Land).
- **Data from Ahrefs' 600,000-page study**: 86.5% of top-ranking content uses some AI assistance; correlation between AI use and ranking penalties is near-zero (0.011). BUT:
- Sites relying on AI content **with no human oversight** lost an average **17% of traffic** and dropped 8 positions. Sites combining AI with meaningful human review dropped only 3 positions, lost 6% traffic (Rankability 2025 case study).
- Quality raters now explicitly assess whether content shows human oversight. "AI + no human review" = "Lowest" quality rating in the Quality Rater Guidelines (Search Engine Land, Rankability).
- **93% of penalized programmatic-SEO sites lacked unique data differentiation** (GrackerAI case study compilation). Template variation is not a moat.

Implication for the loop: an agent that mass-publishes AI-written niche articles with no unique data and no human editorial loop is the exact profile most at risk of a manual action. The only honest path here is **original data + scripted layout + human sanity check**, which contradicts the "run unattended" thesis.

### Display ad network thresholds in 2026 — slightly more reachable, still unrealistic for us
- **Ezoic**: still no minimum traffic requirement; just AdSense good-standing and non-prohibited niches (Adsterra, Monetag).
- **Mediavine main tier**: 50,000 sessions/month AND — this is newer — **sites must now demonstrate ≥$5,000 annual ad earnings** to qualify for the primary platform (Blogging Guide, The Website Flip). This effectively requires the site to already be earning before Mediavine will help it earn more.
- **Mediavine Journey** (the 2024-launched lower tier): 10,000 sessions/month minimum. Still high but within reach if one article went viral.
- **Raptive** (formerly AdThrive): **Oct 16 2025 — dropped from 100,000 to 25,000 monthly pageviews**, a 75% reduction. This is the single biggest change in the ad-network landscape since our bootstrap research. Old: "need massive traffic." New: "need solid mid-tier traffic."
- **AdSense**: still the only truly cold-start option with no traffic minimum, but RPMs on niche content are typically $1–3 vs. Mediavine/Raptive $10–25.

Even the lowered thresholds are an order of magnitude above what a cold-start zero-budget agent-authored site can realistically hit inside the measurement windows we have (7–14 days). The only reason any of this matters is if we later decide to invest 3–6 months into a single content site bet.

### Amazon Associates in 2025 — still viable but commissions remain thin for niche topics
- Commission structure is now published and transparent (via the Associates Operating Agreement updates).
- **Standard rates: 1–10% depending on category.** Luxury Beauty 10%, Watches/Jewelry/Handbags/Shoes 4%, most categories 1–4%. Groceries and basic electronics sit at 1–4% (AffiliateX, Voluum).
- **New 2025 high-priority categories**: **Amazon Games up to 20%**, **Amazon Haul 7%** (Logie Buzz, Flywheel Digital). Amazon is clearly pushing these.
- **New**: Amazon is testing **Native Commerce Advertising** which compensates publishers for *driving traffic to Amazon* even without a sale. CNN and Vox Media are beta testers. Not available to small affiliates yet, but worth tracking (Flywheel Digital).
- **Influencer program** (separate from Associates, requires a qualifying social audience) pays 1–20% with promotional period boosts — inaccessible to a purely agent-written static site but relevant if we ever pair niche content with the YouTube channel.

For our loop: Amazon Associates remains the easiest affiliate program to join, but the math on an unknown niche site with cold zero-click traffic and 1–4% commissions is bleak. Would need ~$100 in purchase volume per published article just to clear $1–4 in commission.

### Programmatic SEO — the top of the category is alive, the middle is dead
The winners remain: Canva (millions of template landing pages, millions of visits/month), Zapier (300k+ organic visitors/month from integration pages), G2, Webflow, Zillow, TripAdvisor, Yelp. These have two things in common that a cold-start agent-authored site does not:

1. **A unique data asset** (user-generated content, product catalogs, real-estate data, SaaS integration metadata) that makes each page genuinely non-duplicative.
2. **Brand + backlink authority** accumulated over years.

The programmatic-SEO pattern still works in 2026, but **only with unique data**. Template-pSEO with no proprietary data lost the game. Timeline on a new programmatic site: indexing 2–4 weeks, first meaningful traffic 4–8 weeks, organic growth 3–6 months, ROI 6–12 months. That's still after you have the unique data asset in hand.

### Rescoring
| Dimension | Old | New | Reasoning |
|---|---|---|---|
| Time-to-first-dollar | 1 | 1 | Unchanged — still months at best, longer with AI Overviews cannibalizing clicks. |
| $0 viability | 5 | 5 | Unchanged — hosting is free (GitHub Pages / Cloudflare Pages / Netlify). |
| Automation-friendliness | 4 | **2** | **Dropped 2 points.** Google's scaled-content-abuse enforcement and the quality-rater guidance explicitly punish "AI + no human review." A fully autonomous content loop is the exact profile at highest risk of manual action. Making this safe requires human editorial loop, which defeats the purpose. |
| Ceiling | 5 | **3** | **Dropped 2 points.** The far-right-tail programmatic-SEO winners (Canva, Zapier) are still possible but require unique data assets we don't have. For an agent-authored no-backlink niche content site, AI Overviews + zero-click have cut the realistic ceiling roughly in half. |
| **Total** | **15** | **11** | **Drops from #3 to below the viable-for-first-dollar cluster.** |

### Recommendation for the loop
- **Do not pursue this category for a first-dollar experiment.** The original "defer this category until something faster has shipped" advice is now stronger: we should defer it **indefinitely** unless a later run identifies a unique data asset we could build and wrap in a minimal site.
- **Do not mass-publish agent-written long-tail articles to a generic niche site.** That's the Google-manual-action profile.
- **If we ever revisit**: the only honest play is (a) pick a narrow domain where we can generate or aggregate **unique data** (e.g. a small database, a live-updated calculator, a comparison scraped from public-domain sources with explicit licensing), (b) build the site as a *tool/data asset*, not a content farm, (c) accept that this is a 6–12 month bet, not a first-dollar bet. This is closer to B-001 / B-008 / B-010 (browser tools) than to traditional "niche content."
- **The 10k-session Mediavine Journey threshold is a useful forward target** if a single browser tool ever gets organic pickup — it's now reachable with one viral post, which it wasn't in 2023.

### Sources cited
1. Press Gazette — "Global publisher Google traffic dropped by a third in 2025" — https://pressgazette.co.uk/media-audience-and-business-data/google-traffic-down-2025-trends-report-2026/
2. Search Engine Land — "News publishers expect search traffic to drop 43% by 2029: Report" — https://searchengineland.com/news-publishers-search-referrals-drop-report-467408
3. Search Engine Land — "Google AI Overviews surged in 2025, then pulled back: Data" — https://searchengineland.com/google-ai-overviews-surge-pullback-data-466314
4. Dataslayer — "AI Overviews Killed CTR 61%: 9 Strategies to Show Up (2026)" — https://www.dataslayer.ai/blog/google-ai-overviews-the-end-of-traditional-ctr-and-how-to-adapt-in-2025
5. Digital Content Next — "Google's AI overviews linked to lower publisher clicks" — https://digitalcontentnext.org/blog/2025/05/06/googles-ai-overviews-linked-to-lower-publisher-clicks/
6. NPR — "Online news publishers face 'extinction-level event' from Google's AI-powered search" — https://www.npr.org/2025/07/31/nx-s1-5484118/google-ai-overview-online-publishers
7. Rankability — "Does Google Penalize AI Content? New SEO Case Study (2025)" — https://www.rankability.com/data/does-google-penalize-ai-content/
8. Google Search Central — "Google Search's guidance about AI-generated content" — https://developers.google.com/search/blog/2023/02/google-search-and-ai-content
9. Search Engine Land — "Google quality raters now assess whether content is AI-generated" — https://searchengineland.com/google-quality-raters-content-ai-generated-454161
10. Blogging Guide — "Display Ad Traffic Requirements" — https://bloggingguide.com/display-ad-traffic-requirements/
11. PPC Land — "Is your site finally ready? The new math behind premium ad network approvals" — https://ppc.land/is-your-site-finally-ready-the-new-math-behind-premium-ad-network-approvals/
12. Adsterra — "The best Ezoic Alternatives to Maximize Your Ad Revenue in 2026" — https://adsterra.com/blog/ezoic-alternatives/
13. AffiliateX — "Amazon Affiliate Commission Rates in 2026: Guide for Amazon Affiliates" — https://affiliatexblocks.com/amazon-affiliate-commission-rates/
14. Flywheel Digital — "Analyzing Amazon Associates Program Changes, Evolution & Impact" — https://www.flywheeldigital.com/blog/amazon-associates-program-updates
15. Voluum — "Is the Amazon Affiliate Program Still Profitable in 2025?" — https://voluum.com/blog/amazon-affiliate-program-guide/
16. GrackerAI — "10+ Programmatic SEO Case Studies & Examples in 2025" — https://gracker.ai/blog/10-programmatic-seo-case-studies--examples-in-2025
17. Passionfruit — "Programmatic SEO Without Traffic Loss: Complete 2025 Guide" — https://www.getpassionfruit.com/blog/programmatic-seo-traffic-cliff-guide

## Refreshed 2026-04-12

Rolling re-refresh (B-004 fallback, remote run #25). 4 WebSearch queries + 3 targeted follow-ups. Two days since the 2026-04-11 pass. Focus: whether the March 2026 core update and AI Overviews expansion change the scoring or recommendation.

### Material finding #1: Google March 2026 core update (rolled out March 27 – April 8) further punishes low-effort niche sites

The first core update of 2026 completed 4 days ago. SEMrush Sensor peaked at 9.5/10 — one of the most volatile core updates in recent history. Over 55% of websites experienced noticeable ranking changes. Key signals:

- **Topical authority amplified as a ranking multiplier.** Sites with clear, consistent niche depth gained visibility; sites ranking across unrelated topics without depth saw declines. This is a stronger version of the E-E-A-T signal: Google is now explicitly rewarding *focus* at the domain level, not just per-page quality.
- **Original data = +22% visibility.** Websites offering original data saw visibility increases of ~22% post-update (Clickrank, LinkDoctor). This is the same "unique data differentiation" signal from the 04-11 refresh (93% of penalized pSEO sites lacked it), now with a concrete positive measurement.
- **Scaled/templated AI content = –71% traffic.** Sites relying heavily on scaled or templated AI-generated content experienced traffic declines up to 71% (Clickrank, BytesPlatform). AI-assisted content is NOT penalized as a category — the filter targets content produced at scale without meaningful editorial oversight. The distinction: "AI as production tool + human expertise" is fine; "AI as replacement for human expertise" is dropping.
- **Author bylines matter.** Sites with author bylines linked to bio pages correlated with ranking stability. Generic "Staff Writer" or "Editorial Team" attributions correlated with negative impact. This is a new E-E-A-T signal not in the 04-11 refresh.
- **Low-effort niche sites: 20–35% organic traffic drops**, with some seeing steeper declines (LinkDoctor, DigitalApplied).

**Impact on this category:** All 04-11 findings are reinforced, not weakened. The March 2026 core update is the newest concrete data confirming that a zero-budget agent-authored niche content site — no unique data, no human editorial byline, no topical authority history — is the exact profile most at risk. Score: unchanged at 11/20. Recommendation: unchanged (do not pursue).

**Relevance to browser tools (B-010, B-001, B-008):** The topical authority signal is mildly positive for our AI-dev-tooling portfolio. Three tools on a single GitHub Pages domain (prompt-cleaner, llm-cost-calculator, claude-md-linter once live) compound each other's topical authority in the AI-dev niche. This is a small organic-SEO bonus, not a strategy change — our distribution plan correctly leads with direct launches (Reddit, HN, awesome-claude-code PR), not SEO.

### Material finding #2: AI Overviews expanded from ~13% to ~50% of US queries

The 04-11 refresh cited "AI Overviews appear on 13.14% of all queries as of 2025" (Search Engine Land). New 2026 data: **~50% of US search queries now generate AI Overview responses** (Stackmatix, Position Digital, EnFuse Solutions — multiple sources converging on this figure). AI-driven SERP features appear in 30–45% of *informational* searches specifically (the query type niche content sites target).

The click reduction when AI Overviews are present: **58%** (Ahrefs, February 2026 data), consistent with the 61% CTR collapse figure from Seer Interactive in the 04-11 refresh. B2B Technology has the highest AI Overview exposure at 70%; e-commerce the lowest at 4%.

The jump from 13% → 50% is the single most important quantitative update in this file. It means AI Overviews are no longer a growing threat — they are the default search experience for half of all queries. The "wait and see if it gets worse" framing from the 04-11 refresh is now obsolete; it is already as bad as the pessimistic scenario implied.

**Forward-looking:** Publishers still expect search traffic to drop a further 40%+ over the next 3 years (Search Engine Land, unchanged from 04-11). By 2028, the median niche content site may receive less than 20% of the Google search traffic it would have received in 2023 for the same rankings.

One partial offset: **brands cited in AI Overviews earn 35% more organic clicks and 91% more paid clicks** (Stackmatix). This means appearing *as a source* within AI summaries partially compensates — but only for established, cited brands. Cold-start niche sites have near-zero probability of being cited in AI Overviews.

### Material finding #3: Mediavine Journey dropped to 1,000 sessions/month (January 15, 2026)

**The 04-11 refresh had the wrong number.** We reported "Mediavine Journey: 10,000 sessions/month minimum." As of January 15, 2026, Journey's minimum is **1,000 sessions/month** — a 90% reduction (Productive Blogging, This Week in Blogging, Mediavine official Threads announcement).

Requirements beyond sessions: must install Grow plugin for traffic verification, original content, brand-safe, engaged audience, frequently updated content. Revenue share: 70%. RPMs typically $10–$15. Auto-upgrade to full Mediavine at $5k/year ad revenue.

**Impact on the category:** This is a genuine correction. 1,000 sessions/month (≈33 sessions/day) is dramatically more reachable than 10,000. A single browser tool with modest organic traffic could qualify. However, this doesn't change the category deprioritization — the bottleneck was never the ad-network threshold; it was getting traffic in the first place under the AI Overviews / zero-click regime. Mediavine Journey at 1,000 sessions is now a realistic *monetization trigger* for any browser tool that achieves organic pickup, which makes it relevant to B-010 post-deploy planning rather than to a standalone niche content site.

**Updated ad-network threshold ladder:**
| Network | Minimum | RPM range | Revenue share |
|---|---|---|---|
| AdSense | 0 (cold start) | $1–$3 | ~68% |
| Ezoic | 0 (no minimum) | $5–$15 | varies |
| **Mediavine Journey** | **1,000 sessions/mo** (was 10,000) | $10–$15 | 70% |
| Raptive | 25,000 pageviews/mo (was 100,000) | $15–$50+ | 75% |
| Mediavine (full) | $5,000/yr ad revenue | $15–$25 | 75%+ |

### Material finding #4 (minor): Microsoft Publisher Content Marketplace (PCM) — new AI licensing revenue channel

Microsoft launched PCM on February 3, 2026 — a marketplace where publishers set licensing terms for their content and get paid when Microsoft Copilot or other AI systems ground answers in it. Early partners: AP, Business Insider, Condé Nast, Hearst, Vox Media, USA TODAY. Open to "smaller, specialized outlets" in principle.

Example economics: a 500k-token niche science blog could earn ~$12k/year through PCM (NicheBlogLab estimate).

**Impact on our loop:** Near-zero. PCM is designed for publishers with substantial content libraries. Our three browser tools are tools, not licensable content. Even a hypothetical niche content site from this loop would be far below the content volume where PCM economics make sense. Filed as a signal that the "publishers lose to AI" narrative is developing a counter-narrative ("publishers license to AI"), which is mildly positive for the category's 5-year ceiling but irrelevant to our 1-year trajectory.

### No-change confirmations
- Amazon Associates commission structure unchanged (1–10%, Games up to 20%, Haul 7%)
- Programmatic SEO still requires unique data (unchanged; the March 2026 core update's +22% original-data bonus reinforces this)
- GitHub Pages / Cloudflare Pages free tiers unchanged
- Zero-click rate still 69% (unchanged from 04-11)
- Score: **11/20 unchanged** — the March 2026 core update and AI Overviews expansion reinforce rather than change the deprioritization. The Mediavine Journey correction is the only item that softens the picture at all, and it applies to browser tools more than to niche content sites.

### Recommendation update
No change to the 04-11 recommendation: **do not pursue this category for a first-dollar experiment.** The March 2026 core update provides the freshest possible confirmation (completed 4 days ago) that the scaled-AI-content enforcement is intensifying, not relaxing.

Two new propagation items for other backlog entries:
1. **B-010 post-deploy:** Consider Mediavine Journey (1,000 sessions/mo threshold) as a future monetization trigger if the claude-md-linter or any browser tool achieves sustained organic traffic. Not actionable now, but worth noting in the distribution plan.
2. **All browser tools:** The topical authority signal from the March 2026 core update is a small organic-SEO bonus for having multiple tools in the same AI-dev niche on one domain. No action needed — we're already doing this by default.

### Sources cited (new in this refresh)
18. SE Roundtable — "Google's March 2026 Broad Core Update Has Completed Rolling Out" — https://www.seroundtable.com/google-march-2026-core-update-complete-41145.html
19. Search Engine Journal — "Google Confirms March 2026 Core Update Is Complete" — https://www.searchenginejournal.com/google-confirms-march-2026-core-update-is-complete/571459/
20. Search Engine Land — "Google March 2026 core update rollout is now complete" — https://searchengineland.com/google-march-2026-core-update-rollout-is-now-complete-473883
21. Clickrank — "Google March 2026 Core Update: What Changed & What To Do" — https://www.clickrank.ai/google-march-2026-core-update/
22. LinkDoctor — "March 2026 Core Update: Early Data, Volatility & SEO Impact" — https://linkdoctor.io/march-2026-core-update/
23. BytesPlatform — "Google Core Update April 2026: Full Guide" — https://bytesplatform.com/blogs/google-core-update-april-2026
24. Stackmatix — "Google AI Overview SEO Impact: 2026 Data & Statistics" — https://www.stackmatix.com/blog/google-ai-overview-seo-impact
25. Position Digital — "100+ AI SEO Statistics for 2026 (Updated April)" — https://www.position.digital/blog/ai-seo-statistics/
26. EnFuse Solutions — "How Google's AI Overviews Are Changing SEO In 2026" — https://www.enfuse-solutions.com/how-googles-ai-overviews-are-changing-seo-in-2026/
27. Productive Blogging — "Everything you need to know about Journey by Mediavine [2026]" — https://www.productiveblogging.com/everything-you-need-to-know-about-journey-by-mediavine/
28. This Week in Blogging — "Mediavine and Raptive Change Entry Requirements" — https://thisweekinblogging.com/mediavine-raptive-requirements/
29. Search Engine Land — "Microsoft launches Publisher Content Marketplace for AI licensing" — https://searchengineland.com/microsoft-launches-publisher-content-marketplace-for-ai-licensing-468191
30. NicheBlogLab — "Content site investments - what you need to know in 2026" — https://nichebloglab.com/content-site-investments-2026/
