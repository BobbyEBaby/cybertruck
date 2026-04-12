# 05 — Chrome / browser extensions

## What it is
Single-purpose extensions for Chrome / Edge / Firefox. Examples: tab managers, productivity blockers, "summarize this page", price trackers, reading mode, theme packs.

## Monetization paths
- Free + donation (hard)
- Freemium: free extension, paid pro features behind a license server (needs backend; hurts $0 viability)
- One-time license sale via Gumroad — extension calls home to verify

## Why this is interesting at $0
- The Chrome Web Store charges a **one-time $5 developer fee**. This is *not* $0 — flag this as a money ask before publishing.
- Edge Add-ons store is free. Firefox add-ons are free.
- Extensions can find passionate niche audiences

## Risks / honest downsides
- Chrome's $5 fee means this is not strictly bootstrap-from-zero
- Discoverability inside the Chrome Web Store is bad; you need outside marketing
- Manifest v3 has restricted what extensions can do; check what your idea actually needs
- Permission scopes scare users

## Scoring
- Time-to-first-dollar: **2**
- $0 viability: **3** (Chrome fee — Edge/Firefox-only would be **5** but smaller market)
- Automation-friendliness: **4**
- Ceiling: **4** (best paid extensions clear $1k–$10k/mo; very rare)
- **Total: 13 / 20**

## First concrete experiment idea
Defer until later, OR ship an Edge/Firefox-only version of a tool first to validate before paying the Chrome fee.

## Refreshed 2026-04-11

Data pass run from a scheduled remote agent in preparation for whether Chrome extensions should remain in the Cybertruck backlog or be explicitly deprioritized. Conclusion: **deprioritized** — score 13 → 10. The category still *exists* as a shipping channel, but the honest path for a no-budget solo loop is Edge Add-ons + Firefox AMO first, Chrome Web Store only after real demand is measured on the free channels, and **never** CWS as a first stop.

### What changed since the May 2025 cutoff

**1. The $5 Chrome Web Store developer fee is unchanged — and still a hard money-ask for this loop.**
Google still charges a one-time $5 USD registration fee to publish on the Chrome Web Store. The fee has been in place since 2020 and no 2025 or 2026 policy has changed it ([Chrome for Developers — Register your developer account](https://developer.chrome.com/docs/webstore/register), [Extension Radar — Chrome Web Store Developer Registration Fee 2026](https://www.extensionradar.com/blog/chrome-web-store-developer-fee-2026)). For CLAUDE.md purposes this is not "$0" — any task that requires publishing to CWS must still route through a `human_inbox/` money-ask before we pay it.

**2. Manifest V2 is fully dead as of Chrome 139 (July 2025).**
June 2025 was the enterprise grace-period deadline; Chrome 139 permanently disabled all remaining MV2 extensions ([Byteiota — Chrome Manifest V3 Deadline](https://byteiota.com/chrome-manifest-v3-deadline-ad-blocker-impact-2025/)). The most iconic casualty was uBlock Origin, which was removed from the Chrome Web Store in late 2024 ([Ghostery — uBlock Origin Not Supported on Chrome](https://www.ghostery.com/blog/ublock-origin-not-supported-chrome), [Bleeping Computer — Chrome disables uBlock Origin in MV3 rollout](https://www.bleepingcomputer.com/news/google/google-chrome-disables-ublock-origin-for-some-in-manifest-v3-rollout/)). Implication for our loop: any new build must target MV3 from day one and cannot rely on the webRequest blocking API (use declarativeNetRequest instead). Firefox still supports the full webRequest surface, which is relevant for any tool whose main job is network interception — Firefox becomes the more capable target in those cases.

**3. The Chrome Web Store shrank ~18% under enforcement pressure.**
CWS hosts ~111,933 active extensions in early 2026, down from a peak above 137,000 ([aboutchromebooks — Google Chrome Extension Ecosystem 2026](https://www.aboutchromebooks.com/chrome-extension-ecosystem/)). The shrink isn't organic attrition — Google has been actively removing extensions for malware, affiliate fraud, and outdated MV2 code. Lower competition helps, but it also signals that the review+enforcement pipeline is more active than it was the last time this research file was scored.

**4. Two major 2025 malware waves have changed Google's posture toward new developers.**
The ShadyPanda campaign (revealed late 2025) involved "sleeper" extensions that had been installed for up to seven years behaving normally, then pushed a malware-laden auto-update to ~4.3M Chrome+Edge users ([Malwarebytes — Sleeper browser extensions woke up as spyware on 4 million devices](https://www.malwarebytes.com/blog/news/2025/12/sleeper-browser-extensions-woke-up-as-spyware-on-4-million-devices), [The Register — Browser extensions pushed malware to 4.3M users](https://www.theregister.com/2025/12/01/chrome_edge_malicious_browser_extensions/)). The RedDirection campaign earlier in 2025 hit ≥3.2M users across 16 extensions that injected code for ad/SEO fraud ([GitLab Security Tech Notes — Malicious browser extensions Feb 2025](https://gitlab-com.gitlab.io/gl-security/security-tech-notes/threat-intelligence-tech-notes/malicious-browser-extensions-feb-2025/)). A March 2026 Hacker News write-up documented ownership-transfer → malicious-update as a distinct attack pattern ([The Hacker News — Chrome Extension Turns Malicious After Ownership Transfer](https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html)). **Effect on our submission:** Google's review on new/low-reputation developers with broad permissions is measurably stricter than it was pre-2025. Rejection rate was already ~35% per Oct 2024 data ([Extension Radar — Why Chrome Extensions Get Rejected](https://www.extensionradar.com/blog/chrome-extension-rejected)), and the common rejection categories (excessive permissions, missing privacy policy, obfuscated code, broken functionality, incomplete listing) all get harsher scrutiny for first-time devs with no install history. A single-file static tool with `activeTab`-only permissions can still pass, but anything asking for `<all_urls>`, `tabs`, `storage`, or host permissions is a flagged submission.

**5. Chrome Web Store built-in payments are gone; monetization requires an external backend or ExtensionPay.**
CWS retired its built-in payments system in the mid-2020s. Current monetization patterns for extensions ([Extension Radar — How to Monetize Your Chrome Extension in 2025](https://www.extensionradar.com/blog/how-to-monetize-chrome-extension), [AverageDevs — How to Monetize Chrome Extensions in 2025](https://www.averagedevs.com/blog/monetize-chrome-extensions-2025)): (a) freemium with Stripe/Paddle + a backend license server, (b) ExtensionPay, which is a free-tier service purpose-built for extension DRM/licensing and sidesteps the backend requirement, (c) one-time Gumroad license with a manual key-verification step on first install. Option (b) is the one most compatible with our $0 / no-server posture — ExtensionPay is effectively a monetization backend we don't have to run. Headline earning stats are misleading: "successful Chrome extensions earn on average $862k/year" ([Extension Radar — Monetize](https://www.extensionradar.com/blog/how-to-monetize-chrome-extension)) is outlier-weighted — the vast majority of extensions earn $0, matching the `honest-expectations.md` anchor. Realistic sustained indie-extension incomes look like the examples compiled by [ExtensionPay — Chrome Extensions with Impressive Revenue](https://extensionpay.com/articles/browser-extensions-make-money) — a handful of mature products in the $1k–$10k/mo range with real brands behind them, not zero-audience agent-authored drops.

**6. Edge Add-ons Store and Firefox AMO are still 100% free — and under-competed.**
Microsoft Edge Add-ons has no developer registration fee and no per-submission cost ([Microsoft Learn — Register as a Microsoft Edge extension developer](https://learn.microsoft.com/en-us/microsoft-edge/extensions/publish/create-dev-account), [Microsoft Q&A — Registration fee to publish Edge extension](https://learn.microsoft.com/en-us/answers/questions/2377371/registration-fee-to-publish-edge-extension)). Firefox AMO has no listing fees, no per-submission charges, and no per-update charges ([Mozilla Add-ons Blog — Updated add-on policies, June 2025](https://blog.mozilla.org/addons/2025/06/23/updated-add-on-policies-simplified-clarified/), [Firefox Extension Workshop — Submitting an add-on](https://extensionworkshop.com/documentation/publish/submitting-an-add-on/)). Both accept MV3. Edge's market share is smaller than Chrome's but the store is less crowded and review is faster. Firefox's market is smaller still, but AMO users skew power-user and are more receptive to specialty dev tools — which overlaps our browser-tool audience from B-001/B-008.

### Rescore (13 → 10)

| Axis | Old | New | Reason |
|---|---|---|---|
| Time-to-first-dollar | 2 | 2 | Unchanged. Still slow: listing → review → traffic → conversion → settlement via external backend. |
| $0 viability | 3 | **2** | Downgraded. CWS still costs $5 (unchanged), AND monetization now requires an external backend or ExtensionPay (unchanged but newly binding since there is no fallback to built-in payments). Edge+Firefox-only would still score 4, but the strategic reason to deprioritize Chrome removes the $0-friendly sub-path from the category's practical footprint for our loop. |
| Automation-friendliness | 4 | **3** | Downgraded. 35% rejection rate, mandatory manual review, tightened scrutiny on new devs post-malware-waves, MV3 restrictions requiring declarativeNetRequest instead of webRequest, and the fact that the developer-account creation step itself cannot be done by the agent (it's a human task + fee). |
| Ceiling | 4 | 4 | Unchanged. A handful of indie wins in the $1k–$10k/mo band still exist. The outlier stats are real but outlier-weighted. |
| **Total** | **13** | **10** | Material downgrade. The category drops below 04-niche-content-sites' refreshed 11 and well below the top tier. |

### Recommendation for the loop

Do **not** pursue Chrome extensions as a first-dollar path. Specifically:

1. **Do not pay the $5 CWS registration fee on spec.** Only request the money-ask via `human_inbox/` after at least one browser-tool experiment (B-001 prompt-cleaner, B-008 llm-cost-calculator, or a future B-010) has produced either ≥1000 real users OR ≥1 user-submitted request for "can you turn this into an extension?". Before that, the $5 is burning real money on a hypothesis, which violates the zero-budget rule.
2. **If a browser-tool experiment does cross that threshold, ship the extension to Edge Add-ons and Firefox AMO first.** Both are free. Both accept MV3. Both are less competitive than CWS. Both produce real install counts that either validate the hypothesis (justifying the $5 CWS fee later) or falsify it (saving the $5 entirely).
3. **Keep manifests minimal.** Use only `activeTab` and `storage` permissions unless the extension's core functionality genuinely requires more. No `<all_urls>`, no `tabs`, no host permissions for the sake of "I might need it later." A minimal-permission MV3 extension sails through AMO and Edge; a broad-permission one from an unknown dev gets held up or outright rejected post-ShadyPanda.
4. **Never submit an extension with obfuscated code, missing privacy policy, or vague listing copy** — all three are top-5 rejection reasons and all three are trivially avoidable. An agent-authored single-file extension should include a readable source bundle, a 50-word privacy policy pointing at "we don't collect anything" (because we don't), and screenshots that literally show the feature working.
5. **Monetization if ever reached: ExtensionPay.** It handles the DRM+license+payment flow on a free tier, avoiding the need to run a backend. CWS built-in payments are dead and Stripe-direct is overkill for a no-audience first attempt.
6. **Don't revive Chrome extensions as a standalone backlog item.** The category only earns its place on the backlog as a *wrapper* around an already-validated browser tool. If you find yourself proposing "let's build a Chrome extension from scratch as a new experiment", stop — go build another browser-tool experiment instead (B-010 shape). The browser tool can be wrapped later if it earns the right to be wrapped.

### What's still worth watching

- **Whether Google tightens CWS fees above $5.** If it does, the fee stops being a small ask and becomes a real barrier — make a human_inbox note at that point and reconsider.
- **Whether Firefox or Edge add any payment/license rails of their own.** Neither currently does; if they do, the honest path becomes "ship free on Chrome, paid on Firefox/Edge".
- **Whether the Jan 2026 malware-wave enforcement cools off after a year or stays permanent.** If submission rejection rates on new devs drop back below ~25%, the automation-friendliness score can be re-raised.
- **Whether any of our shipped browser tools (B-001, B-008, or a future B-010) actually attract a "make this an extension" signal from real users.** That signal is the only trigger for revisiting this category.

## Refreshed 2026-04-12

Re-refresh from remote run #26. Targeted searches: CWS fee changes, extension security/malware enforcement 2026, Edge/Firefox store changes, extension monetization alternatives. Six searches + three follow-ups. Conclusion: **score unchanged at 10/20**. No finding warrants a rescore, but three material updates improve the picture's resolution.

### What changed since the 2026-04-11 refresh

**1. CVE-2026-0628: Chrome's Gemini AI panel created a new privilege-escalation attack surface for extensions (patched Jan 2026).**
Discovered by Palo Alto Networks Unit 42 (researcher: Gal Weizman, reported Nov 23 2025). CVSS 8.8. A malicious extension with only basic `declarativeNetRequest` permissions could inject scripts into Chrome's Gemini Live side panel, which has *elevated* privileges — camera/microphone access, local file reads, screenshot capabilities. The attack required no user interaction beyond installing the extension and opening the Gemini panel ([The Hacker News — Chrome Vulnerability Let Malicious Extensions Escalate Privileges via Gemini Panel](https://thehackernews.com/2026/03/new-chrome-vulnerability-let-malicious.html), [Unit 42 — Taming Agentic Browsers](https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/), [The Register — Chrome AI panel became privilege escalator](https://www.theregister.com/2026/03/03/google_chrome_bug_gemini/)).
**Why this matters for our loop:** This is the first high-profile example of browser-integrated AI features (Gemini, Copilot) creating privilege-escalation paths that MV3's permission model wasn't designed to contain. Even with minimal declared permissions, an extension could access the AI panel's elevated surface. Google patched this specific bug in Chrome 143 (Jan 2026), but the *pattern* — AI panels with elevated permissions that extensions can reach — is architectural and will recur as Gemini's capabilities expand. Direction of travel: Google will almost certainly tighten extension-to-AI-panel isolation further, which means (a) more review scrutiny for any extension that interacts with side panels, and (b) the enforcement posture on new developers will stay strict or tighten. This reinforces the 04-11 recommendation to keep permissions minimal (`activeTab` + `storage` only) and avoid anything that touches side panels or AI features.

**2. Massive Feb 2026 malware campaign: 300+ extensions, 37M+ downloads, ongoing ownership-transfer attacks.**
Security researchers documented 300+ Chrome extensions with 37.4 million combined downloads that leaked browsing history, SERP data, or actively stole user data ([SecurityWeek — Over 300 Malicious Chrome Extensions Caught](https://www.securityweek.com/over-300-malicious-chrome-extensions-caught-leaking-or-stealing-user-data/), [The Dupree Report — 300 Malicious Chrome Extensions](https://www.thedupreereport.com/2026/02/malicious-chrome-extensions-37-million-downloads/)). Of these, 287 transmitted browsing history or SERP data, and ~27.2 million users installed 153 extensions confirmed to leak data on installation. Separately, Socket Security identified 5 extensions targeting enterprise HR platforms (Workday, NetSuite, SAP SuccessFactors) that harvested auth cookies every 60 seconds while blocking security admin pages ([The Hacker News — Malicious Chrome Extensions Caught Stealing Business Data](https://thehackernews.com/2026/02/malicious-chrome-extensions-caught.html)). In March 2026, a separate write-up documented the ownership-transfer attack pattern (buy a legitimate extension, push malicious update) as a distinct repeating tactic ([The Hacker News — Chrome Extension Turns Malicious After Ownership Transfer](https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html)).
**Impact:** This is a continuation and escalation of the ShadyPanda/RedDirection campaigns from 2025 that were already noted in the 04-11 refresh. The scale is larger (300+ vs 16 extensions in RedDirection) and the tactics are more diverse (enterprise-targeting, SERP scraping, cookie harvesting, ownership transfer). Google's enforcement response is correspondingly broader. The 04-11 assessment that Google's review on new/low-reputation developers is "measurably stricter" is confirmed — and the pressure is not abating. No score change (already priced in at the 04-11 refresh) but the data is fresher and the escalation pattern is worth noting.

**3. Edge Add-ons store gains CI/CD API and extension ownership transfer (2025–2026).**
Microsoft Edge Add-ons now supports REST API endpoints for publishing extension updates directly from CI/CD pipelines without manual Partner Center interaction ([Microsoft Learn — Released features for Edge extensions](https://learn.microsoft.com/en-us/microsoft-edge/extensions/whats-new/released-features)). Also new: sidebar extension support (custom UI in the browser sidebar) and extension ownership transfer between developers. The store remains free — no registration fee, no per-submission fee, no per-update fee.
**Why this matters for our loop:** The CI/CD REST API is the first concrete signal that *automated* publishing to Edge is more feasible than before. If we ever build an extension wrapper around a validated browser tool (the only honest path per the 04-11 recommendation), the Edge publish step could theoretically be agent-automated via the API + credentials in `.env`, the same way we handle GitHub Pages and Gumroad today. This slightly improves the automation-friendliness picture for the Edge-first path specifically — but not enough to rescore, since the Chrome path (which dominates the category) is still gated on manual review + $5 fee + tightening enforcement.

**4. Dodo Payments emerges as a second monetization backend for extensions (4% + $0.40/tx, MoR, no monthly fee).**
Dodo Payments is a new alternative to ExtensionPay for extension monetization ([Dodo Payments — How to Monetize a Chrome Extension in 2026](https://dodopayments.com/blogs/monetize-chrome-extension)). Pay-as-you-go pricing: 4% + $0.40 per transaction, no setup fee, no monthly minimum. Merchant of Record (handles global VAT/GST). Supports license keys, subscriptions, and usage-based billing. Credit-based billing launching in 2026 (aimed at AI-powered extensions). Competition with ExtensionPay gives developers a second option if ExtensionPay's terms change.
**Impact:** Minor positive. Adds a second no-upfront-cost monetization backend to the toolbox. Neither Dodo nor ExtensionPay changes the fundamental calculus: monetization is downstream of traffic, and traffic is the bottleneck for any zero-audience extension. Filed for reference if we ever reach the monetization stage.

### No-change confirmations

- **CWS $5 one-time fee:** unchanged ([Chrome for Developers — Register](https://developer.chrome.com/docs/webstore/register), [Extension Radar — CWS Fee 2026](https://www.extensionradar.com/blog/chrome-web-store-developer-fee-2026)).
- **CWS rejection rate:** ~35% as of Oct 2024 data, no newer public figure. 60% of rejections involve insufficient permission justification. Average review 3–7 days, longer for broad permissions.
- **Edge Add-ons:** still free, no registration fee.
- **Firefox AMO:** still free. June 2025 policy update (privacy-policy hosting flexibility, closed-group extensions allowed) already noted in 04-11.
- **MV3:** fully enforced since Chrome 139 (July 2025). Already noted.
- **ExtensionPay:** still available, still free tier for developers.
- **CWS active extensions:** ~111,933 (early 2026), down from 137k peak. Already noted.
- Score: **10/20 unchanged**.

### Updated "What's still worth watching" (additions in bold)

- Whether Google tightens CWS fees above $5.
- Whether Firefox or Edge add payment/license rails.
- Whether submission rejection rates on new devs drop below ~25%.
- Whether any shipped browser tool attracts a "make this an extension" signal.
- **Whether Google's AI-panel isolation improves or whether more CVE-2026-0628-class bugs emerge** — this determines whether the Gemini/Copilot attack surface becomes a permanent new enforcement driver or gets architecturally contained.
- **Whether Edge's CI/CD API matures enough to be a reliable agent-automated publishing path** — if so, the Edge-first recommendation gains a concrete automation advantage over Chrome that isn't just "free vs $5."

