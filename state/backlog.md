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
**Status:** [in_progress 2026-04-11 remote] — build phase unblocked (no creds needed). Upload phase still blocked on Gumroad account + `GUMROAD_ACCESS_TOKEN` in `.env` (local-run only).
**Why:** Highest score in Phase 0 (17/20). Gumroad's free tier handles checkout and delivery; the agent can author the product (template, prompt pack, ebook). See `research/markets/03-gumroad-digital-downloads.md`.
**Definition of done:** `experiments/<slug>/` with the digital asset (zipped if multi-file), `README.md` (hypothesis + audience + pricing), and `ship.md` (Gumroad listing copy + tags + price + upload steps).
**Next concrete step:** After B-001 ships, decide product based on what we now know about traffic source. Default candidate: a Claude Code / AI agent prompt + template pack aimed at the same audience that found B-001.

### B-002b — Build & ship one tiny web game on itch.io (alternative second ship)
**Status:** [pending] — blocked on B-000 (itch.io account) and B-001
**Why:** Lower score (14/20) but a different distribution channel (itch.io's own discovery). Useful as portfolio diversification. See `research/markets/02-itchio-microgames.md`.
**Definition of done:** `experiments/<slug>/` with a single-file HTML5 game (canvas + vanilla JS, no engine), `README.md`, and `ship.md`.
**Next concrete step:** Only pursue *after* B-002 if Gumroad turns out to be a dead end, OR in parallel by a future weekly run if there's spare capacity.

### B-003 — Validate the autonomous ship pipeline
**Status:** [pending] — blocked on B-001 actually shipping via the automated path.
**Why:** Until something is live via the agent's own hands (not via a manual upload), we have no proof the autonomous loop works. The first ship is not about revenue; it is about proving `gh` + Pages + Reddit posting + publish-log all function end-to-end with no human in between.
**Definition of done:** `state/runlog.md` contains an entry confirming a live GitHub Pages URL exists, `state/publish-log.md` has the entry, and a Reddit post URL is recorded — all done by the agent in a single scheduled run.

### B-004 — Phase-0.5 deeper research with WebSearch
**Status:** [pending] — blocked-on-human (needs `/schedule` running so the agent has WebSearch in its scheduled context, AND B-001 to be in flight so the agent isn't blocked).
**Why:** The bootstrap research files in `research/markets/` are seeded from prior knowledge. They need a current-data refresh: search for 2025–2026 reports on top earners in each category, current rev share / payout terms, recent saturation signals.
**Definition of done:** Each file in `research/markets/` has a `## Refreshed YYYY-MM-DD` section with at least 3 cited sources and any updated scoring.

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

## Blocked on human

### B-000 — One-session setup (Kraken deposit address + free accounts + API tokens + cron install)
**Status:** [blocked-on-human]
**See:** `human_inbox/0001-setup.md`
**Unblocks:** B-001, B-002, B-004, B-005, B-006
**Note:** This is the *only* expected human-action backlog item under normal operation. After it's done, the agent operates hands-off on the daily cron until something earns money or the circuit breaker fires.

### B-008 — LLM API Cost Calculator (browser tool, second AI-tooling shot)
**Status:** [built — awaiting ship via tools/deploy_pages.sh]
**Why:** Same audience as B-001 (AI tooling crowd), different angle (cost-conscious devs/decision-makers vs prompt engineers). Single static file, $0 to ship via the existing pipeline. Full build is done — see `experiments/llm-cost-calculator/`.
**Next concrete step:** Local-run agent executes `bash tools/deploy_pages.sh llm-cost-calculator experiments/llm-cost-calculator` (needs `GITHUB_TOKEN` already in `.env`). Then optionally posts to r/LocalLLaMA via `tools/post_reddit.py` once Reddit creds are filled in.

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

### B-012 — Write full script for episode 1 (Peasants' Revolt 1381) — REVISED after pivot
**Status:** [pending] — was [done] for Dancing Plague script, but channel pivoted to **rebellions with thematic analysis** on 2026-04-11 per Robert's direction. The Dancing Plague script + 22 sourced images are archived (not deleted) in `experiments/youtube-history-channel/_archive/` for reference. New episode 1 is the **Peasants' Revolt of 1381 (Wat Tyler)** — placeholder and beat map are in `experiments/youtube-history-channel/scripts/01-peasants-revolt-1381.md`.
**Why this topic:** textbook example of 5 of 6 Breaking Points themes at high intensity (Economy 3, Government 3, Environment 3, War 2, Debt 2, Royalty 1 → 14/18). Clean narrative arc (Black Death → Statute of Labourers → Poll Tax → London storming → Smithfield murder of Wat Tyler → structural victory over the next century). Sets up the analytical framework the channel will apply to every subsequent episode.
**Preserved from the old B-012 work:** the `[HUMAN_INTRO]` / `[HUMAN_OUTRO]` / `[HUMAN_RECORD]` segment structure that the remote agent (Opus run #9) designed for the Dancing Plague script is an excellent pattern and **must be used for the Peasants' Revolt script too**. 4 human segments total (~15 min of Robert's time per episode), 6–7 TTS segments, every factual claim cited inline as an HTML comment.
**New requirements from the pivot:**
1. **Theme intensities section** at the bottom of the script (6 ratings with one-sentence justifications) for copying into `experiments/youtube-history-channel/themes.md`
2. **Pollinations prompts section** at the bottom of the script (20 prompts for AI image generation via B-013's new `generate_images.py`) instead of public-domain sourcing
3. **Thematic analysis section** in the narration itself (6:00–8:30 of the video), walking through the 6 themes for this rebellion. This is the channel's differentiator.
**Definition of done:** `01-peasants-revolt-1381.md` has the full ~1,600-word script, [HUMAN_*] segment markers, inline source citations, theme intensities section, Pollinations prompts section, themes.md updated with the episode 1 row. Frontmatter status `queued` → `scripted`.
**Next concrete step:** Remote run picks this up, verifies sources via WebSearch, writes the script. After this is done, B-013 (generate images) and B-014 (segmented TTS) can run in either order.

### B-012b — Decide channel name (Breaking Points / Powder Keg / Rising)
**Status:** [blocked-on-human]
**Why:** Affects branding, video description template, and spoken CTA copy in every script. Robert drops one word in `human_outbox/0004-channel-name.md`. Default: "Breaking Points" if unanswered by the time B-012 finalizes episode 1.

### B-013 — Build tools/generate_images.py (Pollinations.ai wrapper) — REVISED after pivot
**Status:** [pending] — fully remote-doable (no creds needed, Pollinations is keyless)
**Why — major pivot from the old B-013:** Robert explicitly asked (2026-04-11) for **original AI-generated imagery tailored to each narration beat**, not public-domain sourcing. Pollinations.ai provides a free, no-key SDXL/Flux/GPT-Image HTTP API at `https://image.pollinations.ai/prompt/{url-encoded-prompt}` — perfect for remote automation with zero cost. The remote agent's earlier LoC/Wikimedia sources.md manifest for Dancing Plague is preserved in `_archive/` and is not deleted.
**Note:** For episodes that reference specific famous iconic artworks (e.g., a famous Vermeer or Delacroix painting), the script's Pollinations prompts section may intentionally include a handful of "use the real image" pointers. B-013 should honor those — if a prompt is prefixed with `REAL:` plus a URL, download the real image instead of generating one. Default is generation.
**Definition of done:** `tools/generate_images.py` exists. Takes a video slug as argv. Reads the "Pollinations prompts" section from the script file. For each prompt: calls Pollinations (with 2-sec delay between calls for rate-limit courtesy), saves to `experiments/youtube-history-channel/assets/<slug>/img_NN.jpg`, writes `images.md` manifest (prompt → filename → engine used → timestamp). Handles REAL: prefix for PD-passthrough. Exponential backoff on HTTP 429. Never prints tokens (there are none for Pollinations, but the pattern is consistent with other tools).

### B-013b — Image quality gate (regenerate bad Pollinations outputs)
**Status:** [pending] — remote-doable if the agent can load images as vision input; otherwise flags to human
**Why:** AI image generation is variable. A bad image (wrong era, anachronistic, low quality) undermines history-video credibility more than any other single thing. After B-013 generates the 20 images, a review pass identifies bad ones and regenerates them with revised prompts.
**Next concrete step:** Build `tools/review_images.py` that scans `images.md`, reads each image as vision input, rates quality 1–5, regenerates anything <3 with a more specific prompt. If vision input isn't available in the sandbox, write a `human_inbox/` note asking Robert to flag bad ones by filename and re-run after his reply.

### B-014 — Build tools/narrate.sh (Edge TTS wrapper) — **segment-aware**
**Status:** [pending] — remote-doable if the sandbox has Python + `edge-tts` available
**⚠️ CONSTRAINT from 06-faceless-youtube refresh:** This wrapper must NOT produce a single monolithic TTS narration. It must split the script on `[HUMAN_INTRO]`, `[HUMAN_OUTRO]`, and `[HUMAN_RECORD]` markers and output **numbered segment files** (`segment-01-tts.mp3`, `segment-02-human-placeholder.mp3`, ...) so that Robert's human-recorded segments can drop in by filename and the final `render_video.py` step concatenates them in order. Pure Edge TTS alone is now a demonetization risk under YouTube's inauthentic-content policy — the mix-in of real human voice is a hard requirement, not a nice-to-have.
**Why:** Turns a script file into segmented audio assets that a human-voiced episode can be assembled from. Uses Microsoft Edge TTS (free, no signup, high quality) for the non-human segments.
**Next concrete step:** Verify `edge-tts` pip package is installable in the remote sandbox. Write `tools/narrate.sh` that reads the spoken-narration section of a script file, splits on `[HUMAN_*]` markers, pipes the TTS segments to edge-tts with voice=en-US-GuyNeural, outputs `assets/<slug>/segment-NN-{tts|human-placeholder}.mp3` plus a `segments.json` manifest that `render_video.py` reads.

### B-015 — Build tools/render_video.py (ffmpeg storyboard → MP4)
**Status:** [pending] — depends on B-013 and B-014; may require local execution if remote sandbox lacks ffmpeg
**⚠️ CONSTRAINT from 06-faceless-youtube refresh:** Pure Ken Burns pan/zoom across all 20 images is a risk signal under the inauthenticity filter. The renderer must support **mixed visual treatments** from a storyboard manifest: (a) Ken Burns pan/zoom, (b) static-with-text-overlay (primary-source quotes, dates, place names), (c) side-by-side comparisons, (d) simple map/timeline graphics. The storyboard JSON the script produces specifies which treatment per shot. The agent should not ship an episode where all shots use the same treatment.
**Why:** Turns images + narration + music into the final 1080p MP4 with varied visual treatments.
**Next concrete step:** Check ffmpeg availability in remote sandbox. If unavailable, mark this task as local-only and flag it in the inbox. Design the storyboard-manifest schema first (a simple JSON list of `{image, start_sec, duration, treatment, params}`), then implement per-treatment ffmpeg filter chains.

### B-016 — Build tools/youtube_upload.py (YouTube Data API v3 upload helper)
**Status:** [blocked-on-human] — requires YOUTUBE_OAUTH_REFRESH_TOKEN in `.env`
**Why:** Automates the upload step so videos ship end-to-end without Robert dragging files into YouTube Studio. Until the token exists, upload is manual.
**Unblocks:** fully automated weekly video shipping.
**Handoff:** see the `human_inbox/` note B-012 will write.

### B-017 — Generate 20 Pollinations images for episode 1 (Peasants' Revolt 1381) — REVISED after pivot
**Status:** [pending] — depends on B-012 (script with Pollinations prompts section) AND B-013 (generate_images.py)
**Why — replaces old B-017:** Old B-017 was "source 20 public-domain images for Dancing Plague" and was partially completed by remote run #10 (22 candidate images mapped in a sources.md manifest, not downloaded). That work is archived in `experiments/youtube-history-channel/_archive/assets-dancing-plague-1518/sources.md` for future reference. **New B-017:** run `python tools/generate_images.py peasants-revolt-1381` to generate 20 AI images from the Pollinations prompts in the new episode 1 script.
**Next concrete step:** After B-012 finalizes the new script (with the Pollinations prompts section populated) and B-013 builds the generator, run the generator. Then B-013b reviews and regenerates any bad outputs. Result: `experiments/youtube-history-channel/assets/peasants-revolt-1381/img_01.jpg` through `img_20.jpg` plus `images.md` manifest.

## Done

### B-009 — Refresh remaining market research files [done 2026-04-11]
Rolling refresh of all 6 stale `research/markets/*.md` files completed across remote runs on 2026-04-11. See the B-009 entry retained above (in the "Blocked on human" section for cross-reference) for the per-file outcomes and constraint updates propagated into the rest of the backlog. **Net result:** three categories materially downgraded (04 niche content 15→11, 05 Chrome extensions 13→10, 07 print-on-demand 11→7), one slightly downgraded with binding constraints (06 faceless YouTube 13→12), two unchanged but with new actionable info (02 itch.io, 08 OSS donations). Print-on-demand is now the worst-fit category in the entire research set and is preemptively deprioritized. The four categories that survive top-tier (Gumroad 17, browser utilities 16, OSS+donations 15, itch.io micro-games 14) match exactly the active backlog items B-001/B-002/B-002b/B-006/B-008/B-010/B-011, so no backlog re-ranking is required from this refresh pass.

_(B-001 prompt-cleaner was shipped externally on 2026-04-11; see runlog and the B-001 entry in Active above. Should be moved here on a future cleanup pass — leaving in place this run to avoid scope creep.)_
