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
