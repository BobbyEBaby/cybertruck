# ship.md — CLAUDE.md Linter

This file is the handoff from the remote build run to the local run (or to Robert) for publication. Every step is mechanical. Follow it in order; do not skip.

## Pre-flight check
- [ ] `experiments/claude-md-linter/index.html` exists and opens correctly in a browser (double-click opens it).
- [ ] Clicking **Load sample** populates the textarea.
- [ ] Clicking **Lint** on the sample produces ≥ 4 findings (the sample is intentionally rigged: includes a fake Anthropic key, an absolute `/Users/alice/` path, a hedging word, a TODO, an email, an unclosed code fence, an empty section).
- [ ] **Errors** counter is ≥ 1 (the secret should trip `no-secrets` and/or `assignment-secret`).
- [ ] Footer shows the Ko-fi link and USDC-Solana address.
- [ ] View source shows no `<script src="https://...">` tags and no `fetch()` / `XMLHttpRequest` / `navigator.sendBeacon` calls. Privacy promise holds.

If any check fails, write the failure in `state/runlog.md` and **stop**. Do not publish a broken tool.

## Step 1 — Publish to GitHub Pages
Requires `GITHUB_TOKEN` in `.env` (local only). Remote runs cannot do this step.

```bash
cd cybertruck
bash tools/deploy_pages.sh claude-md-linter experiments/claude-md-linter
```

Expected result:
- New repo `BobbyEBaby/claude-md-linter` created (or reused if it already exists).
- `index.html` and `README.md` pushed to `main`.
- GitHub Pages enabled on `main` / root.
- Live URL: `https://bobbyebaby.github.io/claude-md-linter/`

Add a row to `state/publish-log.md`:

```
| 2026-04-DD HH:MM UTC | claude-md-linter | github-pages | https://bobbyebaby.github.io/claude-md-linter/ | B-010 |
```

Verify the live URL resolves and the **Load sample → Lint** round-trip works in an incognito window before moving to distribution.

## Step 2 — Distribution launch (day-1 push per 01-refresh)

The 01 refresh (2026-04-11) concluded that passive SEO long-tail is dead for browser tools in 2026 and every ship from B-010 onward needs a direct-distribution push on day 1. Execute these in order. **Posting copy below is honest and non-astroturfed per CLAUDE.md.** Do not reply to comments on any platform; log responses in `README.md`'s "Engagement log" section for the next run.

### 2a — Show HN
**When:** Next Monday or Tuesday 08:00–10:00 US/Eastern (highest front-page density).
**One post per tool, ever.** Do not retry.

**Title** (HN caps at 80 chars):
> Show HN: CLAUDE.md Linter – check your Claude Code project file in your browser

**Body:**
```
I maintain a CLAUDE.md for an always-on agent project and kept tripping over
the same mistakes: a committed API key, absolute /Users paths, silently-broken
code fences, a 9000-token file that was paying rent on every turn.

So I wrote a linter for it. 17 rules, single HTML file, runs entirely in your
browser. The input may contain secrets so sending it anywhere would defeat
the point.

Rules cover credentials (Anthropic/OpenAI/GitHub/AWS/Google/Slack/Stripe/
JWT/private-key blocks), rough token budget, structure (missing H1, heading
skips, empty sections, unclosed fences), clarity (hedging language, TODO
markers), and hygiene (trailing whitespace, CRLF, tab indentation, bare URLs,
duplicate headings).

View source to verify there are no network calls. Free, no signup, no
tracking. Tip jar in the footer if it saves you from a leaked key.

Source: https://github.com/BobbyEBaby/claude-md-linter
```

After posting, capture the submission URL and add it to `state/publish-log.md` as a second row (platform: `hacker-news`).

### 2b — r/SideProject
**When:** Saturday's "Share Your Project" thread, OR Friday's "Feedback Friday" thread. Do NOT post as a new top-level post outside those threads — r/SideProject prefers the weekly threads for working-product launches in 2026.

**Title** (inside the thread, so shorter):
> CLAUDE.md Linter – 17 rules, runs in your browser, catches leaked API keys

**Body:**
```
Built this because my own CLAUDE.md for a Claude Code agent project kept
accumulating the same issues and I wanted a checklist that wasn't in my head.

- 17 lint rules: credentials, token budget, structure, clarity, hygiene
- Single HTML file, no backend, no tracking
- Runs client-side so you can paste a file that has secrets in it without
  sending them anywhere (verify via view-source)
- Free, tip jar in the footer

Live: https://bobbyebaby.github.io/claude-md-linter/
Source: https://github.com/BobbyEBaby/claude-md-linter

Feedback on missing rules welcome — the rule list is easy to extend.
```

Add a third `state/publish-log.md` row (platform: `reddit`).

### 2c — (optional, only if 2a and 2b both landed) Post to r/ClaudeAI or r/LocalLLaMA
Only if the HN and r/SideProject posts got real traction (not to farm, but because those subs will genuinely want it). Keep to one sub. Rate-limit: one additional Reddit post per 24h per CLAUDE.md.

Skip entirely if there's any doubt — reputation is the asset.

## Step 3 — Measurement (7 days)
Per `research/markets/01-browser-utilities.md`, the measurement window for browser tools is **7 days from public launch**. At day 7, append a measurement block to this experiment's README and to `state/runlog.md`:

- GitHub Pages visits (GitHub Insights, or `goatcounter` if it's added later)
- HN Show HN final score + peak rank
- r/SideProject post upvotes + comment count
- Ko-fi tips count + USD total
- USDC-Solana deposits observed to `EQwtTPe3GfcAGAiQAh3AxmCZ1WAyCviDsNnBmfCaQwf7` (Kraken deposit) — cross-check timestamps against launch day
- Any "I wish this existed" or missing-rule feedback (captured in the README engagement log, not replied to)

**Decision rule at day 7:**
- **≥ 100 unique visitors + ≥ 1 tip OR ≥ 5 substantive feedback comments** → winner. Write a B-010b extension task (new rules, Node CLI port, VS Code extension exploration).
- **< 100 unique visitors, 0 tips, 0 substantive comments** → honest zero. Log as the first of the three-in-a-row needed to trigger the browser-tools circuit breaker per CLAUDE.md.

## Step 4 — Do NOT
- **Do NOT** create multiple accounts to upvote.
- **Do NOT** reply to comments (CLAUDE.md rule — one-way posting).
- **Do NOT** re-post to HN later with a different title. One attempt.
- **Do NOT** post to r/webdev — the 01 refresh found r/SideProject is strictly better for working-product launches in 2026. r/webdev still enforces the 9:1 rule and has a much higher warming cost.
- **Do NOT** add tracking, analytics, or a "share your file" backend. Privacy is the product.
- **Do NOT** spend any money (no ads, no sponsored posts, no domain — `github.io` is the canonical URL).

## Rollback
If GitHub Pages build fails or the live site renders broken:
1. Revert the commit on `BobbyEBaby/claude-md-linter`.
2. Do not announce anything until it's fixed.
3. Fix locally, retest, redeploy, then resume at Step 2.

If the tool somehow gets bad press (e.g., someone finds a bug where a specific input crashes the page): fix the bug, redeploy, post a correction in the HN and Reddit threads by editing the **original post body**, not by replying. Still no back-and-forth.
