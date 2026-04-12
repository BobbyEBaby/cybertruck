# 08 — Open-source utility + donation funnel

## What it is
Build a small but genuinely useful open-source CLI or library, publish it (npm, PyPI, GitHub), and accept donations via GitHub Sponsors / Polar / Open Collective. Examples: a one-purpose dev tool, a niche scraper, a config helper.

## Monetization paths
- GitHub Sponsors (free, no fee; needs eligibility)
- Polar.sh (free tier; supports paid tiers and "issue funding")
- Optional paid pro tier hosted as a separate package

## Why this is interesting at $0
- Hosting = free (npm, PyPI, GitHub all free)
- The audience (developers) has more disposable income and is more tip-friendly than most
- Aligns with what the agent is naturally good at (code)
- A useful tool can earn small recurring tips for years

## Risks / honest downsides
- Donations are *rare*. Even popular OSS projects net very little.
- Discoverability still matters; "if you build it they will come" is a lie
- GitHub Sponsors application is human-reviewed and can be rejected

## Scoring
- Time-to-first-dollar: **2** (days to ship, weeks/months to first sponsor)
- $0 viability: **5**
- Automation-friendliness: **5** (this is literally the agent's home turf)
- Ceiling: **3** (most OSS donations are small; rare cases earn livable amounts)
- **Total: 15 / 20**

## First concrete experiment idea
A small CLI that does one thing well, distributed via npm/pip with a `README.md` linking to a Sponsors page. Pair it with B-001's audience (the AI tooling crowd) for distribution.

## Refreshed 2026-04-11

Pulled current data via WebSearch for GitHub Sponsors, Polar.sh, Open Collective, and the broader state of OSS maintainer funding. Sources below.

### GitHub Sponsors — fees and payout mechanics (2025/2026)
- **0% platform fee on sponsorships from personal accounts.** 100% of individual-sponsor dollars reach the maintainer (Stripe processing fee is already absorbed by GitHub). This is unchanged from prior years and is unusually generous compared to every other monetization rail we've researched.
- **Up to 6% fee on sponsorships from *organization* accounts**, of which ~3% is the card-processing cost (organizations can eliminate it by switching to invoiced billing).
- **Stripe Connect payout schedule:** payouts on the **22nd of each month** for whatever balance accrued, with an additional payout any month the balance crosses **$100 USD**. This matters for us: if an early product earns $3 from one sponsor in month 1, we don't actually see it hit the bank until the next 22nd. The runlog should treat "sponsored" and "paid out" as two distinct milestones. (https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-payouts-from-github-sponsors)
- **Eligibility is still human-reviewed**, still requires residency in a supported region, still requires the contributor to have a legitimate contribution history. Risk to us: a brand-new GitHub account with one shipped tool may or may not clear eligibility review. Plan B (Polar.sh) does not have this gate.
- Source: https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/about-sponsorships-fees-and-taxes

### Polar.sh — significant platform since prior research
- Polar launched **v1.0 in September 2024** and as of early 2026 has **17,000+ signups, ~5,300 GitHub stars**, and claims **120%+ month-over-month revenue growth** on their creator base over the past six months. They closed a **$10M seed (Accel)** — this is no longer a hobby project; it's a durable rail to bet on.
- **Merchant-of-Record model.** Polar handles tax (US sales tax, EU VAT, etc.) on behalf of sellers. This is genuinely valuable for a solo operator because it removes ~every cross-border tax headache a Gumroad/Stripe-direct setup would create.
- **Headline fee: 4% + $0.40 per transaction**, with surcharges: +1.5% international card, +0.5% subscription. Worst case (international subscription): **~6% + $0.40**. Disputes: **$15 each**, win or lose.
- **Product shapes supported:** paid access to private GitHub repos, paid Discord roles, file downloads, license keys, one-time purchases, subscriptions. This is structurally higher-ceiling than pure donations because it lets a project gate real value behind payment (e.g., "sponsors get a private repo with the extended prompt pack and priority issue triage") while staying $0-upfront.
- **Implication for B-006:** Polar.sh is now the default primary rail for the open-source-donation experiment. GitHub Sponsors stays as a secondary link (lower friction for a pure tip, 0% fee, but lower ceiling).
- Sources: https://polar.sh/resources/pricing · https://polar.sh/blog/polar-seed-announcement · https://dodopayments.com/blogs/polar-sh-review

### Open Collective — moved off percentage fees
- Open Collective **replaced percentage-based platform fees** with a non-percentage model tied to measurable activity (number of Collectives and Expenses processed). Contributors see either **Platform Tips** (optional add-on at checkout) or a flat **5% Crowdfunding Fee** depending on how the Collective is configured.
- Fiscal hosts that don't charge their own host fees use the platform free. Hosts that do charge fees pay Open Collective a **15% "platform share"** of their host-fee revenue.
- **Relevance to us:** Open Collective is overkill for a solo unincorporated operator. It's optimized for fiscal-host-backed community projects (think Babel, Webpack), not individual tip jars. **Recommendation: deprioritize for B-006. Use GitHub Sponsors for the personal-tip angle and Polar.sh for the paid-tier angle.**
- Source: https://documentation.opencollective.com/why-open-collective/pricing

### The honest state of OSS maintainer income (2025 survey data)
- Donation-program adoption is climbing: **16% (2021) → 24% (2023) → 25% (2024)** of maintainers now report some income from programs like GitHub Sponsors, Tidelift, Polar, etc. (Tidelift State of the Open Source Maintainer survey, via dev.to/tidelift).
- But: **47% of maintainers report earning $0** from maintenance work. **60% of maintainers are unpaid entirely** (byteiota analysis of Sonar / Tidelift surveys). **61% of unpaid maintainers fly solo.** **44% cite burnout as the reason they leave.**
- Most-cited "success" stories (Caleb Porzio publicly hitting $100k/yr; Sarah Drasner at ~$3,200/mo on Vue components) are **far-right-tail outliers** — they pre-existed as known figures in their niches before opening a sponsorship page. We are neither.
- **No public "median" figure** because the underlying distribution is heavily zero-inflated. The honest read is: **median monthly Sponsors income for a brand-new solo maintainer shipping a tool in 2025/2026 is $0**, same as `honest-expectations.md` already says. The 25% adoption figure means "1 in 4 maintainers get *some* amount" — it does not mean "1 in 4 get a livable amount".
- Sources: https://dev.to/tidelift/whos-paying-the-maintainers-donation-programs-employers-and-tidelift-3j4k · https://byteiota.com/open-source-maintainer-crisis-60-unpaid-burnout-hits-44/ · https://itsfoss.com/news/open-source-developers-are-exhausted/

### Score update
- Time-to-first-dollar: **2** (unchanged — days to ship, weeks-to-months to first tip)
- $0 viability: **5** (unchanged and reconfirmed — npm/PyPI/GitHub/Polar all free)
- Automation-friendliness: **5** (unchanged — code shipping is the agent's home turf)
- Ceiling: **3** (unchanged — outlier stories exist but median is $0; Polar's gated-product model would arguably push this to 4, but not for a cold-start unknown maintainer in our first year)
- **Total: 15 / 20** — rank unchanged (tied 4th with B-002b itch.io after the refresh).

### Actionable updates for B-006 (direct-crypto earning experiments) and future shipping
1. **Primary funding rail for B-006: Polar.sh.** Its Merchant-of-Record model handles tax, its fees are competitive, and it uniquely supports paid repo/Discord access — the only realistic path from "tool exists" to "tool earns" for a no-name maintainer is *gated value*, not pure charity. This requires a Polar account + API key in `.env` before any automation is possible; write a `human_inbox/` note when B-006 is picked up.
2. **Secondary rail: GitHub Sponsors.** Add a "Sponsor" button (0% fee, predictable monthly payout, trust signal from being GitHub-native). Eligibility application is human-reviewed and may take days/weeks — apply *before* the first product needs it, not after.
3. **Do not bother with Open Collective** for a solo operator. It's the wrong instrument for our shape.
4. **Crypto rail: the USDC-Solana Kraken address in `state/accounts.md` is the canonical "tip in crypto" target.** A footer link on every shipped tool can say "tip in USDC (Solana)" with the address and a QR code. This is the rail most aligned with this loop's savings strategy and incurs zero platform fees. It is, however, high-friction for non-crypto-native users and will convert at a fraction of a fiat-rail tip button. Treat it as a supplement, not a replacement.
5. **Milestone semantics in `state/goal.json`:** separate "earned" (sponsor committed) from "settled" (money cleared Stripe/Polar to bank/USDC). The $100 Stripe payout threshold for GitHub Sponsors means small early wins *exist* for weeks before they *move*. Don't double-count them and don't undercount them.
6. **Product-shape guidance for any OSS shipment going forward:** ship with a dual README strategy — a free tier (the tool does its job, no nag) plus a "sponsors get X" tier where X is something genuinely incremental (extended prompt pack, private repo with examples, faster issue response, etc.). This is how Polar's pricing model converts viewers into dollars; pure tip jars rarely do.
7. **Reality check:** per `state/honest-expectations.md`, the default forecast for any single OSS shipment is $0. The refreshed data does not move that. It just tells us *which rails to use if the rare non-zero outcome lands*.

### Files/rails this feeds into
- `state/accounts.md` — confirm Polar.sh and GitHub Sponsors get added to the "Suggested first accounts" list.
- `state/backlog.md` — B-006 can reference this refreshed section rather than re-researching.
- `state/honest-expectations.md` — no change; data reconfirms the anchor.

## Refreshed 2026-04-12

Second-pass refresh on remote run #20 (one calendar day after the 2026-04-11 pass). Same-day refreshes are usually theater, but this one surfaced two material new data points that were **not** in the 2026-04-11 section. All other prior guidance (Polar.sh base 4%+$0.40, GitHub Sponsors 0% personal / human-reviewed eligibility, Open Collective deprioritized for solo operators, Polar-as-primary / Sponsors-as-secondary ordering) is reconfirmed unchanged.

### New finding 1: donatr.ee — zero-fee donation link aggregator (not a payment processor)
- **What it is:** A free, hosted "link tree for donations" that displays wallet addresses and links to external tip rails on one page. It does NOT process payments itself — supporters are routed to the underlying platform (PayPal, Ko-fi, BMaC, Patreon, Revolut, Wise, IBAN) or to a raw crypto wallet address (BTC, ETH, USDT-multichain, **Solana + USDC-SPL**, LTC, DOGE, Monero, TON, TRON). 19+ rails total.
- **Fees:** **0% to donatr.ee** (it's just a link tree). Whatever the underlying rail charges still applies (e.g., a tip that ends up on Ko-fi is still 0%; a tip that ends up on BMaC is still 5%; a BTC wallet send is still subject to BTC network fees). Donatr.ee itself takes nothing.
- **Barriers:** Zero. No KYC, no bank account, no approval process, no country restrictions, no API token. You make an account, paste in wallet addresses and links, and share one URL.
- **Crypto-native features:** Click-to-copy + QR code on each wallet address. Explicitly supports Solana and USDC-SPL — our canonical savings rail — without needing any third-party crypto payment processor or bridge. The operator (us) holds the private key (or in our case, the Kraken custodial wallet controls it — same model as the hand-rolled `experiments/support-usdc/` page).
- **Source:** https://donatr.ee/ and https://donatr.ee/about/ (platform description); https://donatr.ee/blog/github-sponsors-alternatives/ (positions itself as a GitHub Sponsors alternative for developers).

#### Why this matters to B-006 — and where it does NOT replace what we built
- The **hand-rolled `experiments/support-usdc/` static page** (shipped run #18) has three specific guarantees donatr.ee cannot offer: (a) zero network calls — the page makes no HTTP requests at all after load, grep-verified; (b) source-code auditable on GitHub down to the byte; (c) hosted on our own GitHub Pages domain, no third-party redirect. Those guarantees are the entire reason the page is credible to a low-trust developer audience reading the HTML.
- **donatr.ee is a hosted third-party page.** Visitors load it from donatr.ee's servers. It may (almost certainly does) run basic analytics, cookies, or other request flows typical of any SaaS. The CLAUDE.md rule is "never use multiple accounts per platform" and "posting copy must be honest" — neither forbids using a third-party page as a supplement, but the "zero tracking, self-hosted" honesty anchor of our own support page must be preserved as the canonical rail.
- **The correct integration pattern (NOT this run — run #18's support-usdc rebuild ban holds):** keep `experiments/support-usdc/` as the canonical primary page for USDC-SPL only, and **optionally** add a single footer link at the bottom of our hand-rolled support page pointing to a donatr.ee companion page that covers the 18 *other* rails (PayPal, Ko-fi, BTC, ETH, Monero, etc.) for visitors who have those but not USDC on Solana. This gets us the full multi-rail coverage without compromising the low-trust-audience guarantees of the canonical page. It is a one-file follow-on to B-006, not a replacement.
- **Critical caveat before ever creating a donatr.ee account:** verify via a test run that donatr.ee supports the **XRP destination tag** field. Our `state/accounts.md` routing rule warns that XRP *requires* the destination tag `2272490000` — sending XRP to our shared Kraken address without the tag loses the funds. If donatr.ee's XRP form has no tag field, the XRP rail must be omitted from any donatr.ee page we create. Default assumption: most third-party tip aggregators do NOT handle destination tags — test before trusting.

#### Honest read
- Adding donatr.ee as a secondary rail has a **small positive EV** (captures a handful of would-be tippers who have BTC/ETH/Monero but no USDC-SPL) at near-zero build cost (~15 minutes of Robert's time to create the account + paste in addresses + paste one donatr.ee URL in a footer).
- It does NOT change the underlying median-outcome forecast of $0 per `state/honest-expectations.md`. Adding rails doesn't create demand, it just catches it when it exists. The 2026-04-11 refresh said "donations are rare, most OSS projects net very little." That remains the default expectation.
- Priority: **low**. Behind the 0005/0006/0007/0008 inbox items already awaiting Robert. Do NOT rebuild `experiments/support-usdc/` to add this — the B-006 ship phase is still pending local deploy and changing it mid-flight violates scope discipline.

### New finding 2: Open Source Endowment (OSE) launched Feb 2026
- **What it is:** The **world's first dedicated OSS endowment fund.** Structured as a US 501(c)(3) tax-exempt charity. Instead of collecting donations and passing them straight through to maintainers, OSE invests all contributions into a permanent principal and distributes only the **investment income** as grants — the structural goal being "move OSS funding off a donation treadmill onto an endowment-income model."
- **Size:** ~$700,000 principal as of early 2026, across 60+ founding donors.
- **Founding donors include:** the founders of ClickHouse, curl, Elastic, Gatsby, HashiCorp, n8n, Nginx, Pydantic, Supabase, and Vue.js. This is a who's-who of established OSS commercial success — the fund is seeded by people who *already made it*, and is designed to help the next generation who are currently drowning in the 60%-unpaid data above.
- **Sources:** https://www.opensourceforu.com/2026/03/worlds-first-oss-endowment-backs-maintainers-with-investment-income/ and https://www.theregister.com/2026/02/27/open_source_endowment/.

#### Relevance to this loop (low, but not zero)
- **Not actionable for us today.** OSE is a grant-giving body, not a tip rail. Grant eligibility (though not publicly detailed in the launch coverage) almost certainly requires existing maintainer reputation, measurable public impact, and a track record — none of which a cold-start solo operator shipping browser tools in week 1 has.
- **Long-run relevance:** IF one of the loop's experiments eventually matures into a real OSS project with measurable user adoption (see `state/honest-expectations.md` year-1 outcomes), OSE becomes one of three things we should apply to alongside Polar.sh paid tiers and GitHub Sponsors. Currently year 0 week 1 — this is filed under "not today, but don't forget it exists." Earliest realistic trigger: a single experiment crosses 1000 measurable active users.
- **Do NOT** add OSE to `state/accounts.md`'s suggested-first-accounts list. It is not an account we can create; it is an institution we may someday apply to receive a grant from. Different category entirely.

### Everything else — reconfirmed unchanged from 2026-04-11
- **Polar.sh:** base 4% + $0.40 + 1.5% international card surcharge + 0.5% subscription surcharge + $15 per dispute. No pricing changes announced for 2026 specifically. The pricing page (https://polar.sh/resources/pricing) reserves the right to pass on future Stripe fee changes. Still the recommended primary paid-tier rail for B-006.
- **GitHub Sponsors:** still 0% on personal-account sponsorships, up to 6% on org-account sponsorships, $100-USD payout threshold on Stripe Connect, payouts on the 22nd of each month. Eligibility still human-reviewed, still requires a supported region and legitimate contribution history. No 2026 policy updates surfaced. Still the recommended secondary 0%-fee rail.
- **Open Collective:** still non-percentage fee model, still Platform Tips + 5% Crowdfunding Fee depending on host configuration, still overkill for a solo unincorporated operator. Still deprioritized for B-006.
- **OSS maintainer income data:** still ~25% of maintainers get donation income, still ~86% of contributors receive no pay, still ~60% of maintainers are unpaid hobbyists. The "median new solo maintainer Sponsors income in year 1 is $0" anchor is unchanged and reconfirmed.

### Score update
- Time-to-first-dollar: **2** (unchanged)
- $0 viability: **5** (unchanged)
- Automation-friendliness: **5** (unchanged)
- Ceiling: **3** (unchanged — OSE and donatr.ee both surface but neither moves the ceiling; the structural median is still $0 for year 1)
- **Total: 15 / 20** — rank unchanged (tied 4th with B-002b itch.io).

### Actionable updates (layer on top of the 2026-04-11 actionables)
1. **Keep `experiments/support-usdc/` as the canonical rail.** Do not rebuild it in this run. The hand-rolled "zero network calls, Solscan-verified, auditable HTML" page serves the specific low-trust developer audience better than any hosted aggregator can.
2. **Optional future enhancement (NOT this run):** one additional footer link at the bottom of `experiments/support-usdc/index.html` pointing to a donatr.ee companion page Robert would create with the full 19-rail spread, for visitors who have BTC/ETH/Monero/PayPal/etc. but not USDC-SPL. Estimated Robert time: ~15 minutes. **Gate this behind the measurement of the existing support page first** — there's no point adding rails if the primary page earns $0 over its 14-day window; measure before expanding.
3. **XRP destination-tag compatibility check** is a hard precondition for any donatr.ee use of XRP. `state/accounts.md` already flags this as a CRITICAL rule: XRP without the tag = lost funds. Default to omitting XRP from any third-party page unless the tag field is confirmed present.
4. **OSE is a year-1+ consideration, filed under "the rail that exists when we have something to apply with."** Do not add it to `state/accounts.md`. Do not write an inbox note. Revisit only if the circuit-breaker dashboard ever shows an experiment with ≥1000 active users.
5. **No change to priority ordering for B-006:** Polar.sh primary (paid tiers, merchant-of-record) → GitHub Sponsors secondary (0% fee, personal trust signal) → USDC-Solana static page (already shipped) → donatr.ee companion (optional, post-measurement) → OSE (year-1+). The rails are now ordered by a combination of ceiling and setup cost.

### Sources (new this refresh)
- https://donatr.ee/ — platform homepage
- https://donatr.ee/about/ — feature and fee details
- https://donatr.ee/blog/github-sponsors-alternatives/ — positioning as dev-maintainer rail
- https://www.opensourceforu.com/2026/03/worlds-first-oss-endowment-backs-maintainers-with-investment-income/ — OSE launch coverage
- https://www.theregister.com/2026/02/27/open_source_endowment/ — OSE launch (primary source; 403'd on direct fetch but referenced by the opensourceforu article)
- https://polar.sh/resources/pricing — Polar fee reconfirmation
- https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/about-sponsorships-fees-and-taxes — GitHub Sponsors fees reconfirmation
