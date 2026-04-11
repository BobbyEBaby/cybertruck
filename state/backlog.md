# Backlog

Ranked tasks. The daily run picks the top task that is **not blocked on a human action**. When picking up a task, mark it `[in_progress]`. When done, mark it `[done YYYY-MM-DD]` and move it to the bottom under "Done".

Priority signals: time-to-first-dollar, $0 viability, automation-friendliness, ceiling.

## Ranking summary (from research/markets/)
Top scores from Phase 0:
1. **17/20** — Gumroad digital downloads (`03-gumroad-digital-downloads.md`)
2. **16/20** — Browser utilities (`01-browser-utilities.md`)
3. **15/20** — Niche content / SEO (`04-niche-content-sites.md`) — too slow for first ship
4. **15/20** — Open-source + donations (`08-open-source-donations.md`)
5. **14/20** — itch.io micro games (`02-itchio-microgames.md`)

**B-001 picks browser utilities (16) over Gumroad (17)** for the *first* ship because browser utilities can go live with zero external account (a `username.github.io` page works once GitHub is set up). Gumroad needs the account fully wired with payouts before the first sale can settle. After the first ship validates the loop, the next experiment will be the higher-ceiling Gumroad play.

## Active

### B-001 — Build & ship a tiny browser tool: "AI Prompt Cleaner"
**Status:** [done 2026-04-11] — live at https://bobbyebaby.github.io/prompt-cleaner/. Repo: https://github.com/BobbyEBaby/prompt-cleaner. Shipped by the local run 2026-04-11 06:03 (see runlog + publish-log).
**Follow-up:** 7-day measurement window is running. No Reddit post yet — deferred until the live URL is visually confirmed and REDDIT_* credentials are in `.env`.

### B-002 — Build & ship a Gumroad digital download (highest-ceiling first product)
**Status:** [done 2026-04-11; shipped via tools/ship_gumroad.py. Live: https://robertwave56.gumroad.com/l/grlmp. File attached by Robert via dashboard] — asset `experiments/claude-code-power-prompts/claude-code-power-prompts.md` + README + ship.md all committed. Upload phase blocked on Gumroad account + `GUMROAD_ACCESS_TOKEN` in `.env` (local-run only). Handoff note: `human_inbox/0002-ship-prompt-pack-to-gumroad.md`.
**Why:** Highest score in Phase 0 (17/20). Gumroad's free tier handles checkout and delivery; the agent can author the product (template, prompt pack, ebook). See `research/markets/03-gumroad-digital-downloads.md`.
**Definition of done:** `experiments/<slug>/` with the digital asset (zipped if multi-file), `README.md` (hypothesis + audience + pricing), and `ship.md` (Gumroad listing copy + tags + price + upload steps). **Build phase: done.** Ship phase: pending local run.
**Next concrete step:** Local Claude Code reads `experiments/claude-code-power-prompts/ship.md` and executes upload. **Before upload**, read the 03-gumroad refresh constraint update (see B-004 entry below) — specifically: listing title must have "Claude Code" in the first 3 words (not generic "Claude" or "AI prompts" or "LLM"); use `$5 PWYW with $3 suggested minimum` pricing (below $3 the Gumroad flat fee eats the margin); include the full table-of-contents in the public listing (refunds keep Gumroad's 10%, so accurate descriptions are net-positive EV); no tax-compliance paperwork needed (Gumroad is Merchant of Record since Jan 2025). Remote runs do not touch this item further until upload happens.

### B-002b — Build & ship one tiny web game on itch.io (alternative second ship)
**Status:** [pending] — blocked on B-000 (itch.io account) and B-001
**Why:** Lower score (14/20) but a different distribution channel (itch.io's own discovery). Useful as portfolio diversification. See `research/markets/02-itchio-microgames.md`.
**Definition of done:** `experiments/<slug>/` with a single-file HTML5 game (canvas + vanilla JS, no engine), `README.md`, and `ship.md`.
**Next concrete step:** Only pursue *after* B-002 if Gumroad turns out to be a dead end, OR in parallel by a future weekly run if there's spare capacity.

### B-003 — Validate the autonomous ship pipeline
**Status:** [partial 2026-04-11] — GitHub Pages half is validated twice (prompt-cleaner + llm-cost-calculator live; publish-log entries at 06:03 and 06:46). YouTube half is validated too (Popular Uprisings ep1 shipped twice: 15:00 v1 and 15:39 v2, both unlisted). Reddit half is still unvalidated — no Reddit post in publish-log yet because Reddit creds + subreddit-safety decision are still pending. Downgrading from "pending" to "partial" — the half that matters most for free distribution is still open.
**Why:** Until something is live via the agent's own hands (not via a manual upload), we have no proof the autonomous loop works.
**Definition of done:** `state/publish-log.md` contains at least one Reddit post URL alongside the existing Pages and YouTube rows, all shipped by the agent itself.
**Next concrete step:** Still blocked on REDDIT_* credentials in `.env` + a human decision on which subreddit is safe to post to. No remote action until those land.

### B-004 — Phase-0.5 deeper research with WebSearch
**Status:** [mostly done 2026-04-11] — 7 of 8 `research/markets/*.md` files now have a current `Refreshed 2026-04-11` section (02, 03, 04, 05, 06, 07, 08). **Remaining:** only `01-browser-utilities.md` is still pre-2026-04-11 (has an older 2026-04-10 bootstrap refresh). Fully remote-doable for the final file.
**Why:** 01 is the remaining top-2 category (16/20) underpinning B-001/B-008/B-010 — the three active browser-tool experiments. Its rubric underpins every browser-tool prioritization decision. Finishing this closes out the B-004 refresh pass entirely.
**Definition of done:** `01-browser-utilities.md` has a `## Refreshed 2026-04-11` section with ≥3 cited sources and any updated scoring, same shape as the B-009 refreshes and today's 03 refresh.
**Next concrete step:** Any future remote run looking for work can pick up the final `01-browser-utilities.md` refresh. One file per run, per ship-small.

**Constraint update from 03 refresh (2026-04-11 remote run #14):** Four material findings affect B-002 and B-011 (both in the Active section):
1. **Gumroad is now Merchant of Record** (since Jan 2025) — handles global VAT/GST/sales tax automatically. **No `human_inbox/` note needed** asking Robert to set up international tax compliance. This de-risks B-002 materially.
2. **No minimum payout threshold** — first-dollar milestone will settle on the first Friday after the first sale, not after accumulation. Update milestone-tracking expectations accordingly.
3. **Refund policy: Gumroad keeps its 10% on refunds** (a refund at $5 PWYW is a ~1.38× loss, not a wash). Listings must accurately describe the pack's contents to minimize refund risk — no "15+ prompts" inflation, full ToC in the public listing.
4. **B-002 listing positioning must lean hard on "Claude Code" (the CLI) not "Claude" (the model)** — the generic AI-prompt-pack category is saturated (150k-prompt mega-bundles compete), but the "Claude Code" CLI-tooling sub-niche is a tighter field where our 15-prompt focused pack has a fighting chance. Title must have "Claude Code" in the first 3 words. **B-011 shortlist:** (a) Claude Code CLAUDE.md templates pack, (b) Agent operating-loop starter kit, (c) Claude Code hook recipes — all three stay inside our authentic-authority zone. Do **not** ship a generic "100 AI prompts" sequel.
See `research/markets/03-gumroad-digital-downloads.md` "Refreshed 2026-04-11" section for full data and sources.

### B-005 — Wire fiat → Kraken auto-conversion
**Status:** [pending] — depends on B-001 actually earning a first dollar (no point wiring this until something pays out)
**Why:** When Gumroad/Stripe pays out fiat, we want it to land in the Kraken USDC deposit address from `.env` automatically — not sit in a bank account. The cleanest path: link Gumroad → bank → standing instruction to buy USDC on Kraken when fiat lands → withdraw USDC to the deposit address (which is already a Kraken-internal address, so this is more about *holding it as USDC* than transferring).
**Next concrete step:** When the first payout is imminent, write `human_inbox/` instructions for Robert to set up the fiat → USDC conversion rule on Kraken and confirm the bank link from his payout platform.
**Definition of done:** First fiat payout has been observed converting to USDC in Kraken without per-payout human action, recorded in runlog.

### B-006 — Direct-crypto earning experiments
**Status:** [pending] — parallel-eligible after B-001
**Why:** Skip the fiat onramp entirely by earning crypto directly. Targets:
- **Polar.sh** — sponsorships and issue funding for OSS projects (free, crypto + fiat payouts)
- **Gitcoin Grants / bounties** — bounties for OSS contributions
- **GitHub Sponsors** — ties into B-008-ish OSS shipping
**Definition of done:** At least one experiment is published with a "support this in USDC" link wired to the Kraken deposit address or a self-custody wallet, even if it earns nothing.

### B-007 — Self-custody migration trigger
**Status:** [pending] — sleeps until balance crosses $5,000
**Why:** Custodial Kraken holdings are fine while small but become a single-point-of-failure as the balance grows. At $5k, the agent will write an inbox note recommending Robert install MetaMask/Phantom and withdraw the bulk of holdings to self-custody.
**Trigger:** `state/goal.json.balance_usd >= 5000`
**Next concrete step:** Sleep. The daily run checks the balance at the top of each run; when threshold is crossed, this becomes an inbox note instead of staying on the backlog.

### B-018 — Write full script for episode 2 (German Peasants' War 1524–25) [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11 remote run #13] — `experiments/youtube-history-channel/scripts/02-german-peasants-war-1524.md` written (1,710 words, status: `scripted`, episode_number: 2, 9 sources cited, 6 theme intensities with justifications totaling 12/18, 20 Pollinations prompts). Row added to `experiments/youtube-history-channel/themes.md` database. Wiki rebellion page `wiki/rebellions/german-peasants-war-1524.md` written (with explicit `> Contradiction:` blockquote vs 1381 per wiki conventions), plus 6 figure stubs (thomas-muntzer, martin-luther, sebastian-lotzer, christoph-schappeler, philip-of-hesse, charles-v) and 4 concept stubs (twelve-articles-1525, battle-of-frankenhausen, against-the-murderous-thieving-hordes-1525, second-serfdom). `wiki/index.md` updated to reflect the new entries (2 rebellions, 11 figures, 9 concepts). The episode honestly frames the channel's thesis as a *tendency* rather than a law because the 1525 structural outcome diverges from 1381 — crushed in the east via the `[[concepts/second-serfdom]]`, partial weak gains in the south — which is the first real stress test of `structural-vs-tactical-victory` as planned in the B-018 description. Added 2026-04-11 remote run #12 during the reconcile pass.
**Why:** Episode 1 (Peasants' Revolt 1381) is live but unlisted. The episode 1 outro explicitly teases episode 2: *"In the next episode, we are going to Germany, 1524. The German Peasants' War — the largest popular uprising in Europe before the French Revolution. The one that Martin Luther publicly endorsed and then publicly disowned, in writing, within a single year."* That's a committed audience expectation; the agent should have the script ready so the pipeline can render and ship on cadence (1/week, ≥3 days apart per 06-faceless-youtube constraints).
**Format requirements (must match episode 1's structure so Robert's pipeline Just Works):**
1. Frontmatter: `status: queued` → will flip to `scripted`, `target_length_seconds: ~660`, `word_count: ~1600`, `episode_number: 2`, `theme_rebellion`, `unifying_theme`, `sources: [at least 5 URLs/citations]`
2. Body sections: Introduction → Body (the story) → Conclusion. Match the narrative arc pattern of ep1.
3. **Apply the six-theme framework explicitly** in the narration — the "Luther endorsed then disowned" thread is ep2's most distinctive theme beat and should land on the Royalty/Government lines.
4. Thematic analysis section in the narration itself + `## Theme intensities (for themes.md)` table at the bottom (6 ratings + justifications).
5. `## Pollinations prompts` section at the bottom — **20 prompts**, each matching a specific narration beat, same "period + subject + style + NOT modern / NOT 19th century" template as ep1.
6. Every factual claim cited inline as `<!-- source: ... -->` HTML comments.
7. Honest dispute-framing where the historical record is contested (e.g., Luther's "Against the Murderous, Thieving Hordes of Peasants" timeline, Twelve Articles attribution, death-toll estimates).
**Definition of done:** `experiments/youtube-history-channel/scripts/02-german-peasants-war-1524.md` exists, full script written, ≥5 sources verified via WebSearch, theme-intensities table populated, 20 Pollinations prompts written, frontmatter `status: scripted`. **Also:** add a new row to `experiments/youtube-history-channel/themes.md` Database table and append the episode-2 rebellion page + figure/concept stubs to `wiki/` + update `wiki/index.md` (this is now part of every episode's scripted-state per the wiki conventions in CLAUDE.md).
**Next concrete step:** Run WebSearch on: (a) Twelve Articles of the Peasants (March 1525, Memmingen), (b) Luther's "Admonition to Peace" vs "Against the Murderous, Thieving Hordes of Peasants" timeline and texts, (c) Thomas Müntzer + Battle of Frankenhausen, (d) total death-toll estimates (~100,000 is the standard figure but dispute it honestly), (e) how the war's defeat compared to 1381 in tactical-loss-structural-win terms (this is the channel's through-line thesis being tested for the first time). Then write the script. Then update themes.md + wiki in the same run.
**Constraint propagation from ep1 experience:** The v2 of ep1 had to be re-rendered after v1 because the camera pan was too fast (commit b2fce65). Ep2's script should not assume the renderer defaults are right — note any per-shot camera-speed preferences in the storyboard-hint column of the Pollinations-prompts table if relevant.

## Blocked on human

### B-000 — One-session setup (Kraken deposit address + free accounts + API tokens + cron install)
**Status:** [blocked-on-human]
**See:** `human_inbox/0001-setup.md`
**Unblocks:** B-001, B-002, B-004, B-005, B-006
**Note:** This is the *only* expected human-action backlog item under normal operation. After it's done, the agent operates hands-off on the daily cron until something earns money or the circuit breaker fires.

### B-008 — LLM API Cost Calculator (browser tool, second AI-tooling shot) [done 2026-04-11]
**Status:** [done 2026-04-11] — live at https://bobbyebaby.github.io/llm-cost-calculator/. Publish-log entry: 2026-04-11 06:46 github-pages. Reddit post still pending REDDIT_* creds (see B-003).
**Moved to Done section on reconcile run #12.**

### B-009 — Refresh remaining market research files
**Status:** [done 2026-04-11] — all 6 stale files refreshed in a rolling pass. **Files refreshed (in order):** 02-itchio-microgames (no score change, 14/20; surfaced Creator Day Nov 28 0%-fee window + ≥$3 PWYW floor justification), 08-open-source-donations (no score change, 15/20; surfaced Polar.sh as material new rail for B-006), 04-niche-content-sites (15→11; AI Overviews + scaled-content-abuse enforcement; explicitly deprioritized), 06-faceless-youtube (13→12; Jan 2026 enforcement wave against faceless-AI channels; binding constraints propagated to B-012..B-017 and youtube-history-channel/README), 05-chrome-extensions (13→10; CWS $5 fee + 2025 malware-wave scrutiny + dead built-in payments; explicit Edge+Firefox-first path), 07-print-on-demand (11→7; Etsy June 2025 retroactive Creativity Standards rewrite + Amazon Merch invitation-only AI-bot screening + Redbubble new-AI-account 5/day cap + no truly free commercial-clean image-gen pipeline for our remote sandbox; **lowest-scoring category in the entire research set after refresh**; explicitly preemptively deprioritized — see "Recommendation for the loop" in the file).
**Why:** All bootstrap research files were seeded from May 2025 cutoff and needed a current-data refresh with cited sources. Done.
**Outcome:** Three categories materially downgraded (04, 05, 07), one slightly downgraded (06 with binding constraints on the in-flight YouTube build), two unchanged but surfaced new actionable info (02, 08). The full scoring landscape is now current and the four categories that survive top-tier (Gumroad 17, Browser utilities 16, OSS+donations 15, itch.io micro games 14) are exactly the ones we already have active backlog items for (B-002, B-001/B-008/B-010, B-006, B-002b).
**Constraint update from 04 refresh:** Niche content sites are now explicitly deprioritized — do not pursue as a first-dollar path. See 04-niche-content-sites.md "Recommendation for the loop" section. The only honest revisit path is as a *data/tool asset* (closer to B-001/B-008/B-010 shape), not as a content farm.
**Constraint update from 06 refresh:** The YouTube build (B-012..B-017) can still proceed but **must** change assumptions before episode 1 ships — see the "Recommendation for the loop" section in `research/markets/06-faceless-youtube.md`. The binding points are (a) narration cannot be pure Edge TTS alone — either Robert records narration or we mix TTS with human-voiced intro/outro + editorial commentary; (b) visuals must go beyond uniform Ken Burns pan/zoom; (c) cadence hard-capped at 1 episode/week for first 12 weeks; (d) no AI-generated historical visuals; (e) publications spaced ≥3 days apart. These are NOT aesthetic preferences — they are mitigations against the Jan 2026 YouTube inauthentic-content enforcement wave that mass-terminated thousands of faceless-AI channels.
**Constraint update from 05 refresh:** Chrome extensions remain deprioritized but with a cleaner honest path if ever revisited: do NOT pay the CWS $5 fee on spec. If a future browser-tool experiment (B-001 / B-008 / B-010) shows measured demand (≥1000 real users or ≥1 "I wish this was an extension" request), ship the extension-wrapped version to **Edge Add-ons and Firefox AMO first** (both free, no money-ask, no backend required for a static tool) and only flip to CWS once the Edge+Firefox versions have produced installs. Never submit to CWS as an unknown dev with broad-permission manifest — the 2025 malware wave made Google's review on new devs far stricter and the 35% rejection rate reflects that. Monetization path if ever reached: ExtensionPay for single-dev licensing (free tier, handles DRM + payments) — not CWS built-in payments, which are dead.
**Constraint update from 07 refresh:** Print-on-demand is now the **worst-fit category in the entire research set** (refreshed score 7/20, lower than 04 niche content at 11 and 05 Chrome extensions at 10). Treat it as preemptively deprioritized — do not propose POD experiments under B-010, B-011, or any new backlog item; do not add Redbubble/TeePublic/Etsy/Amazon Merch to any future setup ask; do not propose "wrapping a browser tool as POD merch" as a follow-on. The category fails the zero-budget rule (no truly free commercial-clean image-gen pipeline for the remote sandbox), the automation rule (every platform's enforcement specifically filters AI/templated bulk uploads — Etsy June 2025 retroactive ban, Amazon Merch invite-only with anti-AI-bot screening, Redbubble 5/day cap on new AI accounts), and the ship-small rule (the volume math requires hundreds of designs to find a single winner). If Robert ever expresses POD interest via `human_outbox/`, write an honest reply note pointing him at the 07 file's "Recommendation for the loop" section before any backlog action — POD is fundamentally a Robert-led category that needs his identity, portfolio, and creative voice to clear application/disclosure gates the agent cannot.

### B-010 — Build a third browser tool (open category)
**Status:** [pending] — fully remote-doable, no creds for build phase
**Why:** Inventory expansion. Two browser tools (B-001 + B-008) is a small portfolio. A third widens the surface area. Constraints: must be single static file, must target AI tooling audience or adjacent dev audience, must not duplicate B-001 or B-008.
**Next concrete step:** Pick one of: (a) Anthropic tool-definition validator (paste JSON schema, get validated tool def), (b) prompt diff viewer (paste two prompts, see line-by-line diff), (c) markdown→plaintext converter, (d) regex tester with named-capture support, (e) JWT decoder, (f) something else suggested by current research. Build it as `experiments/<slug>/`. Hand off to local for ship.

### B-011 — Author a second Gumroad digital asset (queue behind B-002)
**Status:** [pending] — remote-doable for build phase
**Why:** B-002 (Claude Code Power Prompts) is a single product. Once it ships, having a second asset ready to upload back-to-back is the right move (one-product creators almost never make sales; clusters do). Candidates: "AI agent CLAUDE.md template pack", "Cybertruck-Autopilot-style operating-loop starter kit", "100 prompts for X niche".
**Next concrete step:** Decide on the second product after B-002 is shipped and we have measurement data. Until then, keep this as a placeholder so the agent doesn't redundantly start it.

### B-012 — Write full script for episode 1 (Peasants' Revolt 1381) [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11 — locally, by Robert] — script written and rewritten (v2). The final version (`scripts/01-peasants-revolt-1381.md`, 1,650 words, "Why Failed Rebellions Still Win") was authored locally by Robert on 2026-04-11 afternoon as part of the wider ship pass. Theme intensities section present (14/18). Pollinations prompts section present (20 prompts). Episode shipped live as unlisted YouTube video sBUTZhrbMPU at 15:39 UTC.
**Moved to Done section on reconcile run #12.**

### B-012b — Decide channel name [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11] — resolved to **"Popular Uprisings"** by the default-if-unanswered rule. Episode 1 shipped under that name ("Popular Uprisings Ep 1 v2" per commit b2fce65). The script opens with "This is Popular Uprisings, episode one".
**Moved to Done section on reconcile run #12.**

### B-013 — Build tools/generate_images.py (Pollinations.ai wrapper) [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11 — locally, by Robert] — `tools/generate_images.py` committed in 33a242f. Already run against episode 1 (20 `img_NN.jpg` files + `images.md` manifest in `assets/peasants-revolt-1381/`).
**Moved to Done section on reconcile run #12.**

### B-013b — Image quality gate (regenerate bad Pollinations outputs) [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11 — locally, by Robert] — `tools/regen_images.py` exists. 5 images (img_04, 08, 11, 14, 18) were regenerated for the v2 cut per commit b2fce65.
**Moved to Done section on reconcile run #12.**

### B-014 — Build tools/narrate.py (Edge TTS wrapper, segment-aware) [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11 — locally, by Robert] — `tools/narrate.py` committed. Segment MP3s (`segment_01_narrator.mp3` .. `segment_08_outro.mp3`) + `segments.json` + final `narration.mp3` all present for episode 1. Robert chose a **UK narrator voice** for v2 (per commit b2fce65 title). The human-segment mixing path originally planned was not used for ep1 — Robert went with full TTS under a deliberate voice choice; honest read is that the inauthenticity-filter mitigation is weaker than the 06-refresh recommended, and a future weekly review should watch for any YouTube policy notice on the channel.
**Moved to Done section on reconcile run #12.**

### B-015 — Build tools/render_video.py (ffmpeg storyboard → MP4) [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11 — locally, by Robert] — `tools/render_video.py` committed. Episode 1 v1 shipped at 15:00, v2 (with "slower camera" per commit b2fce65) shipped at 15:39. Both are on YouTube unlisted. Per commit b2fce65 the v2 addressed camera-speed feedback, implying the tool supports tunable pan/zoom params.
**Moved to Done section on reconcile run #12.**

### B-016 — Build tools/youtube_upload.py (YouTube Data API v3 upload helper) [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11 — locally, by Robert] — `tools/youtube_upload.py` + `tools/youtube_oauth_bootstrap.py` both committed. Episode 1 was uploaded **twice** via the helper (video IDs SFen0WYnBy4 and sBUTZhrbMPU in publish-log). OAuth refresh token must therefore exist in Robert's local `.env`. Both uploads are **unlisted** — no public discovery yet.
**Moved to Done section on reconcile run #12.**

### B-017 — Generate 20 Pollinations images for episode 1 (Peasants' Revolt 1381) [done 2026-04-11]
**Status:** [paused 2026-04-11; was: done 2026-04-11 — locally, by Robert] — all 20 images + `images.md` manifest present in `assets/peasants-revolt-1381/`. 5 regenerated in v2.
**Moved to Done section on reconcile run #12.**

## Done

### B-009 — Refresh remaining market research files [done 2026-04-11]
Rolling refresh of all 6 stale `research/markets/*.md` files completed across remote runs on 2026-04-11. See the B-009 entry retained above (in the "Blocked on human" section for cross-reference) for the per-file outcomes and constraint updates propagated into the rest of the backlog. **Net result:** three categories materially downgraded (04 niche content 15→11, 05 Chrome extensions 13→10, 07 print-on-demand 11→7), one slightly downgraded with binding constraints (06 faceless YouTube 13→12), two unchanged but with new actionable info (02 itch.io, 08 OSS donations). Print-on-demand is now the worst-fit category in the entire research set and is preemptively deprioritized. The four categories that survive top-tier (Gumroad 17, browser utilities 16, OSS+donations 15, itch.io micro-games 14) match exactly the active backlog items B-001/B-002/B-002b/B-006/B-008/B-010/B-011, so no backlog re-ranking is required from this refresh pass.

_(B-001 prompt-cleaner was shipped externally on 2026-04-11; see runlog and the B-001 entry in Active above. Should be moved here on a future cleanup pass — leaving in place this run to avoid scope creep.)_

### Reconcile pass — 2026-04-11 remote run #12
On remote run #12 the backlog was reconciled with Robert's local ship activity between runs 11 and 12. Eight items were marked [done] in place (still listed in their original sections with `[done 2026-04-11]` tags rather than physically moved, to keep the diff small): **B-008** (llm-cost-calculator shipped 06:46 UTC), **B-012** (ep1 Peasants' Revolt script written + v2 rewrite), **B-012b** (channel name resolved to "Popular Uprisings" by default-if-unanswered), **B-013** (`tools/generate_images.py`), **B-013b** (`tools/regen_images.py` + 5 v2 regens), **B-014** (`tools/narrate.py` — Robert chose full-TTS UK-voice rather than the segment-aware human-mix path; honest read: weaker inauthenticity-filter mitigation than 06-refresh recommended, flag for weekly review), **B-015** (`tools/render_video.py` — ep1 rendered twice), **B-016** (`tools/youtube_upload.py` — ep1 uploaded twice as unlisted video IDs SFen0WYnBy4 and sBUTZhrbMPU), **B-017** (20 Pollinations images for ep1). Also marked **B-002** as built-but-awaiting-local-upload and **B-003** as partial (Pages + YouTube halves validated, Reddit half still pending creds). **B-004** was re-scoped to the 2 remaining research files (01-browser-utilities + 03-gumroad-digital-downloads). New item **B-018** added: write episode 2 script (German Peasants' War 1524–25) as teed up by ep1's outro.
