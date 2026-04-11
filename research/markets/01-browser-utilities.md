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

## Refreshed 2026-04-11

Closes out the B-004 refresh pass (last of the 8 `research/markets/*.md` files). Refreshed against current 2026 data on free static hosting, tip rails, discovery channels, and the AI-tooling niche specifically — the three subjects that most directly inform the in-flight B-001/B-008/B-010/B-011 bets.

### What changed since the bootstrap

**1. AI Overviews are eating organic discovery — this is the biggest structural change.** As of April 2026, AI Overviews appear in ~**48%** of all Google search queries (up materially from a year ago), and industry data shows ~**60%** of searches now end zero-click as users read the AI summary and move on. `<!-- source: position.digital 2026 AI SEO stats + semrush AI Overviews study + digitalapplied.com SEO after AI Overviews 2026 -->` The 2025 SEO playbook of "ship a single-page tool and let long-tail SEO bring visitors over months" is materially weakened. Ranking position can stay stable while CTR and traffic fall. This does NOT kill browser utilities as a category — it kills **passive SEO acquisition** as the default distribution story. The implication: **budget acquisition to direct distribution channels (Reddit / Hacker News / X) from day 1, not "ship and hope search picks it up."**

**2. GitHub Pages free tier: unchanged — still the default.** Confirmed limits for 2026: 1 GB recommended repo size, **100 GB/month soft bandwidth limit**, **10 builds/hour soft limit**, public repos only on Free plan. No announced changes for 2026. `<!-- source: GitHub Docs "GitHub Pages limits" 2026 + freetiers.com infographic -->` Our existing `tools/deploy_pages.sh` pipeline (B-001 + B-008 already live on GitHub Pages) stays in place. **Do not rebuild the deploy pipeline on spec.**

**3. Cloudflare Pages is the better free rail for viral-traffic scenarios.** Cloudflare Pages offers **unlimited bandwidth** on the free tier plus 500 builds/month across 300+ edge locations. Netlify's free tier was reduced from 300 → 100 build minutes in 2025 and caps at 100 GB bandwidth; Vercel caps at 100 GB/month + 1M edge requests. `<!-- source: cloudflare-pages-vs-netlify-vs-vercel-static-hosting-2026 on danubedata.ro + juxtaposedtides.com Complete 2026 Guide to Frontend Hosting -->` Honest read: Cloudflare Pages is the correct free rail **if a tool gets a viral HN or Reddit moment that exceeds GitHub Pages' 100 GB soft limit.** That's a great problem to have and we don't have it yet. **Migrate only on measured overflow**, not preemptively.

**4. Ko-fi is still the best tip rail — also unchanged.** Ko-fi still takes **0% on tips** (Stripe/PayPal fees only pass through), 5% on shop sales/memberships with the 5% removable via Ko-fi Gold at $6/month. Buy Me a Coffee still takes **5% on everything including tips.** `<!-- source: ko-fi.com pricing 2026 + ruzuku.com Ko-fi Pricing 2026 + schoolmaker.com BMaC 2026 pricing + talks.co Ko-fi vs BMaC 2026 -->` No change to the bootstrap recommendation — Ko-fi remains the default tip jar, with the Kraken USDC-Solana address as the crypto-native alternative.

**5. Reddit self-promo rules: r/SideProject is the default first post, not r/webdev.** r/SideProject **explicitly welcomes** working-product self-promotion and has dedicated threads (Share Your Project Saturdays, Feedback Fridays) where it's the point of the subreddit. r/webdev allows self-promo but enforces the **9:1 rule** (9 non-promotional comments per promotional post). `<!-- source: reddit-radar-marketing.com r/SideProject guide + mediafa.st r/SideProject marketing + karmaguy.io Reddit self-promotion rules 2026 -->` For B-001/B-008/B-010 ship posts, **r/SideProject is the zero-friction first channel**; r/webdev requires account warming and is higher-risk. This changes nothing about the CLAUDE.md "never reply to comments" rule — post honestly, do not engage with responses.

**6. Hacker News Show HN: highest single-day upside by a wide margin.** ~**90% of Show HN attempts fail to reach the front page**, but those that do see **10,000–30,000 visitors in 24 hours**, with documented cases like 11k uniques + 300 signups from a single 13-hour front-page run. `<!-- source: indiehackers.com Show HN front page guide + marcotm.com HN front page stats + onlook.substack.com HN launch -->` This is the single most important structural fact for our category: **the ceiling of a browser utility is not set by SEO long-tail; it's set by whether one launch hits HN.** One HN front-page hit can dwarf six months of SEO trickle on the same tool. Implications: (a) the ship must be HN-worthy in its own right (novel angle, working demo, no marketing speak, monday/tuesday posting); (b) spray-and-pray volume does NOT work on HN — you get one shot per tool; (c) a tool that's obviously derivative (a 10,001st JSON formatter) has a near-zero probability of the front-page outcome. This strongly argues for **narrower, more distinctive tools** rather than more generic utilities.

**7. The AI-tooling niche is expanding in 2026, not contracting.** Claude Code (Anthropic) is described in April 2026 power rankings as *"the undisputed king of CLI-based agentic coding"* with Opus 4.6 now accounting for **~4% of all public GitHub commits** per SemiAnalysis estimates, largely in personal/experimental repos. `<!-- source: tokencalculator.com Best AI IDE CLI Tools April 2026 + blog.logrocket.com AI dev tool power rankings March 2026 + apidog.com Claude Code vs Codex 2026 -->` OpenAI Codex, Cursor, and Aider are all mature competitors with real user bases. Every one of our active browser-tool experiments (B-001 prompt-cleaner, B-008 llm-cost-calculator, and the pending B-010 third tool and B-011 second Gumroad asset) targets this developer audience. **The audience we're betting on is growing, not shrinking.** No reason to diversify out of it on spec — "stay in the niche you actually know" remains the honest call.

### Scoring update

Component-by-component:
- **Time-to-first-dollar: 3** (unchanged — days to ship, weeks-to-months to first tip)
- **$0 viability: 5** (unchanged — GitHub Pages + Cloudflare Pages both still 100% free at our scale)
- **Automation-friendliness: 5** (unchanged — build + deploy + ship-post all scriptable)
- **Ceiling: 3** (unchanged — the HN front-page upside is the *ceiling*, but it's one-shot not recurring; a tool that cleared $10k/yr would be extraordinary)
- **Total: 16/20 — unchanged**

The score is the same but the **distribution story shifted from "passive SEO long-tail" to "direct launches into Reddit and HN with narrow, distinctive tools."** That's a bigger change than it sounds.

### Recommendation for the loop

1. **B-010 (third browser tool) — shortlist refined.** The original B-010 candidates were: Anthropic tool-definition validator, prompt diff viewer, markdown→plaintext converter, regex tester with named-capture, JWT decoder. After this refresh, re-rank:
   - **#1 — CLAUDE.md linter / validator** *(NEW candidate, not in original list)*. Paste a `CLAUDE.md` file, get: (a) lint warnings against the published Claude Code best-practices, (b) estimated token cost of the loaded context, (c) a diff showing where it violates the 2025-era conventions. **Why it wins:** it's the only tool in this shortlist where *we have authentic authority* — the Cybertruck Autopilot repo's own `CLAUDE.md` is in active use across 15+ remote runs and has been iterated on honestly. That domain authority is exactly what Hacker News rewards and what a generic utility lacks. It also pulls directly from the AI-tooling audience expansion in finding #7.
   - **#2 — Anthropic tool-definition JSON validator.** Developer-audience laser-focused, novel-enough-for-HN, paste-and-check UX. Depends on clear JSON schema from the Anthropic docs; fully buildable remotely.
   - **#3 — Prompt diff viewer.** Two-panel line-by-line diff of two prompts with highlighting for inserted/removed/moved sections. Useful when refining Claude Code prompts — we literally do this by hand every run.
   - **#4 — Claude Code CLI cheat-sheet / keybind reference** (static page, zero JS). Lowest effort, weakest HN angle.
   - ~~**markdown→plaintext converter**~~ — deprioritize (too generic, saturated category).
   - ~~**regex tester with named-capture**~~ — deprioritize (regex101.com owns this category).
   - ~~**JWT decoder**~~ — deprioritize (jwt.io owns this category).
   
   **Recommendation: next remote build run should pick the CLAUDE.md linter.** Second choice: the Anthropic tool-definition validator.

2. **B-001 (prompt-cleaner) and B-008 (llm-cost-calculator) — distribution action needed.** Both are live on GitHub Pages but neither has been posted anywhere. Their 7-day measurement windows are running silently because there is no distribution driving traffic. **Next local-run action** (write this into `human_inbox/` when appropriate): post each tool to r/SideProject (zero-friction first channel per finding #5) and separately as a Show HN on HN (Monday/Tuesday, honest title, working demo URL — per findings #5 and #6). Reddit still needs REDDIT_* credentials; HN posting is manual from Robert's browser.

3. **Do not preemptively migrate off GitHub Pages.** The `tools/deploy_pages.sh` automation is working and the free tier is unchanged. Only re-evaluate if a tool actually crosses 100 GB bandwidth/month (which would be the best possible problem).

4. **Acquisition-channel budget:** for every browser tool we ship from this point forward, the ship checklist must include: (a) r/SideProject post (Saturday thread or direct), (b) Show HN post (Monday/Tuesday), (c) Ko-fi footer link, (d) Kraken USDC-Solana donation link. Long-tail SEO is a bonus, not a strategy.

5. **Niche discipline:** stay in the AI-tooling audience (Claude Code / Codex / Cursor / Aider developers). Do NOT propose generic utility tools outside this niche under B-010 / B-011 even if they're technically easier to build. Our authentic authority in this niche is the single most valuable asset we have and it compounds per ship.

**Sources:**
- [position.digital — 100+ AI SEO Statistics for 2026](https://www.position.digital/blog/ai-seo-statistics/)
- [eMarketer — FAQ on content marketing: AI saturation, zero-click search, what's still working in 2026](https://www.emarketer.com/content/faq-on-content-marketing--ai-saturation--zero-click-search--what-s-still-working-2026)
- [digitalapplied.com — SEO After AI Overviews: Complete Strategy Guide 2026](https://www.digitalapplied.com/blog/seo-after-ai-overviews-complete-strategy-guide-2026)
- [ALM Corp — Semrush AI Overviews Study 2026](https://almcorp.com/blog/semrush-ai-overviews-study-2026-complete-analysis/)
- [GitHub Docs — GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
- [freetiers.com — GitHub Pages Free Tier infographic](https://www.freetiers.com/directory/github-pages)
- [DanubeData — Cloudflare Pages vs Netlify vs Vercel: Static Site Hosting Compared 2026](https://danubedata.ro/blog/cloudflare-pages-vs-netlify-vs-vercel-static-hosting-2026)
- [juxtaposedtides.com — The Complete 2026 Guide to Frontend Hosting](https://www.juxtaposedtides.com/post/the-complete-2026-guide-to-frontend-hosting-every-platform-compared-for-performance-pricing-and-s)
- [devtoolreviews.com — Vercel vs Netlify vs Cloudflare Pages (2026 Update)](https://www.devtoolreviews.com/reviews/vercel-vs-netlify-vs-cloudflare-pages-2026)
- [ko-fi.com — official pricing page](https://ko-fi.com/)
- [Ruzuku — Ko-fi Pricing 2026](https://www.ruzuku.com/learn/articles/ko-fi-pricing)
- [SchoolMaker — Buy Me a Coffee Pricing in 2026](https://www.schoolmaker.com/blog/buy-me-a-coffee-pricing)
- [talks.co — Ko-fi vs Buy Me a Coffee 2026 Guide](https://talks.co/p/kofi-vs-buy-me-a-coffee/)
- [reddit-radar-marketing.com — How to Market on r/SideProject](https://www.reddit-radar-marketing.com/guides/r/sideproject)
- [mediafa.st — Marketing on r/SideProject without getting banned](https://www.mediafa.st/marketing-on-rsideproject)
- [karmaguy.io — Reddit's Self-Promotion Rules 2026](https://karmaguy.io/en/blog/reddit-self-promotion-rules)
- [Indie Hackers — My Show HN reached the HN front page](https://www.indiehackers.com/post/my-show-hn-reached-hacker-news-front-page-here-is-how-you-can-do-it-44c73fbdc6)
- [marcotm.com — Stats of being on the Hacker News front page](https://marcotm.com/articles/stats-of-being-on-the-hacker-news-front-page/)
- [onlook.substack.com — How to absolutely crush your Hacker News launch](https://onlook.substack.com/p/launching-on-hacker-news)
- [TokenCalculator — Best AI IDE & CLI Tools April 2026: Claude Code Wins, Codex Catches Up](https://tokencalculator.com/blog/best-ai-ide-cli-tools-april-2026-claude-code-wins)
- [LogRocket — AI dev tool power rankings March 2026](https://blog.logrocket.com/ai-dev-tool-power-rankings/)
- [apidog.com — Claude Code vs OpenAI Codex in 2026](https://apidog.com/blog/claude-vs-codex-comparison-2026/)
