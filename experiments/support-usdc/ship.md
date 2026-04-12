# ship.md — experiments/support-usdc/

Four phases. Only Phases 1 and 2 are needed to mark **B-006** as shipped;
Phases 3 and 4 are rail extensions.

## Pre-flight checklist

- [ ] You are on Robert's local machine with `.env` present and
      `GITHUB_TOKEN` populated.
- [ ] `tools/deploy_pages.sh` is the secret-safe (`GIT_ASKPASS`-based)
      version from commit 3112667 — not the older `-c http.extraheader`
      version, which leaks the token into `ps`.
- [ ] `state/publish-log.md` does NOT already have a github-pages entry for
      `support-usdc` within the last 24 hours (per the CLAUDE.md max-autonomy
      rule of 1 publication per platform per 24 hours — note that other
      github-pages deploys are counted separately per-experiment, so this
      should be fine unless another run already pushed).

## Phase 1 — Deploy the static page (one command)

```bash
tools/deploy_pages.sh support-usdc experiments/support-usdc
```

Then confirm:

1. `https://bobbyebaby.github.io/support-usdc/` loads. (May take ~30s after
   first deploy while GitHub provisions the Pages site.)
2. The displayed address matches `EQwtTPe3GfcAGAiQAh3AxmCZ1WAyCviDsNnBmfCaQwf7`
   exactly — same as `state/accounts.md` and `.env`. **A one-character typo in
   a crypto address = funds lost forever.** Do not edit `index.html` without
   re-verifying this.
3. The copy button works (paste into a scratch doc and confirm the full
   address, not a truncated or ellipsized version).
4. The Solscan link opens to the right account.
5. The Ko-fi link works.

Append to `state/publish-log.md`:

```
## YYYY-MM-DD HH:MM
- platform: github-pages
- url: https://bobbyebaby.github.io/support-usdc/
- experiment: support-usdc
- repo: https://github.com/BobbyEBaby/support-usdc
```

## Phase 2 — Cross-link from the live tools (5 min)

The support page is useless without distribution. Add a one-line footer link
to each live tool below its existing Ko-fi footer. Drop-in HTML snippet:

```html
<p style="text-align:center;font-size:0.85em;opacity:0.75;margin:0.35em 0 0">
  Crypto tip? <a href="https://bobbyebaby.github.io/support-usdc/">Send USDC on Solana →</a>
</p>
```

Files to edit:

- [ ] `experiments/prompt-cleaner/index.html` — insert below the existing
      Ko-fi footer line.
- [ ] `experiments/llm-cost-calculator/index.html` — same.
- [ ] `experiments/claude-md-linter/index.html` — same (whenever B-010
      ships via `human_inbox/0005-ship-claude-md-linter.md`).
- [ ] `experiments/flipline/index.html` — footer doesn't exist yet; add a
      minimal footer in the same deploy (whenever B-002b ships via
      `human_inbox/0006-ship-flipline-to-itchio.md`).

For each tool already live, redeploy:

```bash
tools/deploy_pages.sh prompt-cleaner experiments/prompt-cleaner
tools/deploy_pages.sh llm-cost-calculator experiments/llm-cost-calculator
```

Verify each tool's live URL now shows the "Send USDC on Solana →" line under
the Ko-fi line.

Append a second publish-log entry per redeployed tool (github-pages rate
limit is per-platform but the individual repo deploys are each a distinct
publication for tracking purposes — see the prior 2026-04-11 entries for
format).

## Phase 3 — Polar.sh (primary paid-tier rail, OPTIONAL)

Per the 2026-04-11 refresh of `research/markets/08-open-source-donations.md`,
Polar.sh is the default primary rail for the OSS donation experiment shape
in 2026. Merchant-of-record model (handles EU VAT / US sales tax), 4%+$0.40
per transaction, supports paid access to private GitHub repos, paid Discord
roles, file downloads, license keys, subscriptions. This is the rail that
converts from "tool exists" to "tool earns" for a no-name maintainer — pure
tip jars rarely do.

Human steps:

1. Go to https://polar.sh/ and create an account (free).
2. Connect the `BobbyEBaby` GitHub account (and any org you want to use).
3. Generate an API token at https://polar.sh/settings/tokens with the
   minimum scope needed for product creation and order listing.
4. Add it to `.env` as:
   ```
   POLAR_ACCESS_TOKEN=<token>
   ```
   (Never commit `.env`. Never echo this token in any runlog, inbox note,
   or response. It stays inside subprocesses only.)
5. Add a row to `state/accounts.md` under "Active accounts":
   ```
   - platform: Polar.sh
     username: bobbyebaby
     profile_url: https://polar.sh/bobbyebaby
     payout_method: <whatever Polar offers in your region>
     notes: Merchant of Record since launch. 4% + $0.40 per transaction,
       +1.5% international card, +0.5% subscription. Supports paid repo
       access / file downloads / subscriptions.
   ```
6. Report back in `human_outbox/` so a future run can scope the first
   Polar product.

Candidate first Polar product: a **sponsor-tier unlock** for the Claude Code
Power Prompts pack (already live on Gumroad at $3). The unlock gives
sponsors access to a private GitHub repo with extended prompts, templates,
and an example CLAUDE.md catalog — leveraging the authentic authority from
running this project, which generic prompt tools cannot match. Scope this
in a future remote run once the `POLAR_ACCESS_TOKEN` is available.

## Phase 4 — GitHub Sponsors (secondary 0%-fee rail, OPTIONAL)

Per the same 08-refresh: GitHub Sponsors is unusually generous (0% platform
fee on personal sponsorships; all dollars reach the maintainer) but the
eligibility application is human-reviewed and may take days or weeks. Apply
before the first product needs it, not after.

Human steps:

1. Go to https://github.com/sponsors and open the application.
2. Link the `BobbyEBaby` GitHub account to a supported payout region.
3. Complete the application honestly — reference this repo
   (`BobbyEBaby/cybertruck`) and the shipped tools (prompt-cleaner,
   llm-cost-calculator, flipline when live, claude-md-linter when live)
   as contribution history.
4. Wait for human review. Do NOT ping or DM the review team — that violates
   the CLAUDE.md "never DM anyone" rule and would damage the reputation
   we are trying to build.
5. Once accepted, set up tiers ($1/$5/$10) and add the `:heart: Sponsor`
   button to the project README (`README.md` at the repo root) and a
   "GitHub Sponsors" section to `experiments/support-usdc/index.html`.
6. Add a `github-sponsors` row to `state/accounts.md`.
7. Report back in `human_outbox/`.

Reality check: per `state/honest-expectations.md`, the realistic GitHub
Sponsors income for a brand-new solo maintainer in year 1 is $0. Applying
is still worth it because the application cost is low, the rail is zero-fee
if anyone ever does sponsor, and being listed on Sponsors is itself a
trust signal.

## Do NOT

- **Do NOT** post this support page to Reddit / Hacker News as a standalone
  "please donate" pitch. That is engagement bait, violates CLAUDE.md honesty
  rules ("no fake reviews, no engagement bait"), and would damage the
  reputation this project treats as its primary asset. Distribution happens
  passively via the tool footers.
- **Do NOT** add analytics, a tracking pixel, or any network call to
  `index.html`. The "zero network calls from this page" guarantee is part
  of the page's value proposition and part of what makes it safe to link
  from every tool.
- **Do NOT** change `EQwtTPe3GfcAGAiQAh3AxmCZ1WAyCviDsNnBmfCaQwf7` to any
  other address without re-verifying it matches `state/accounts.md` AND
  `.env` AND Kraken's deposit-address page for the Solana network. A
  one-character typo in a crypto address = funds lost forever.
- **Do NOT** display or echo the contents of `.env` in any runlog entry,
  inbox note, or commit message — this applies especially to
  `POLAR_ACCESS_TOKEN` once it exists.
- **Do NOT** ship a Cybertruck-themed photoshopped cover image or any asset
  that implies the project has already bought / is about to buy the
  Cybertruck. The only honest visual is the one already on the page
  (nothing; it's text-only).

## Rollback

If Phase 1 goes wrong (page displays the wrong address, page fails to
render, etc.):

1. Do not leave it live with incorrect info.
2. Edit `experiments/support-usdc/index.html` to fix the issue.
3. Run `tools/deploy_pages.sh support-usdc experiments/support-usdc` again.
4. If the problem is catastrophic (e.g. the address is visibly wrong and a
   tip might be lost before a redeploy lands), delete the `support-usdc`
   repo from the `BobbyEBaby` GitHub account to take the page down
   immediately. Then fix and redeploy.

## Decision rule — day 14

On 2026-04-26 (14 days after the Phase 1 deploy date, adjust if Phase 1
happens later), check the Kraken USDC-Solana deposit address for any
incoming transactions:

- **≥ 1 tip received:** B-006 is "alive". Keep the page, add GitHub Sponsors
  and Polar.sh on the same page in a follow-up run to diversify rails.
- **0 tips, Phase 2 complete:** B-006 is "soft-zero". Normal outcome for
  a first 14-day window; do not remove the page, do not conclude the rail
  is dead. A second 14-day window begins automatically.
- **0 tips, Phase 2 NOT complete:** The experiment has not really been
  tested yet. Complete Phase 2 before drawing any conclusion.
- **Three consecutive 14-day windows at 0 tips with Phase 2 complete:**
  Trigger the circuit breaker for the "direct-crypto donation page"
  category. Do not ship a second USDC page. Pivot to Polar.sh as the
  primary rail via Phase 3.
