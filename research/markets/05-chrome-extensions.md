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

