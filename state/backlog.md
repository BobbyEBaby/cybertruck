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
**Status:** [in_progress 2026-04-11 remote] — rolling refresh, one file per remote run. **Done so far:** 02-itchio-microgames (2026-04-11), 08-open-source-donations (2026-04-11), 04-niche-content-sites (2026-04-11, this run — score dropped 15→11 due to AI Overviews crushing publisher traffic and scaled-content-abuse enforcement; category now explicitly deprioritized). **Still stale:** 05 (Chrome ext), 06 (faceless YouTube), 07 (POD). Next remote run should pick the next oldest.
**Why:** Files 05 (Chrome ext), 06 (faceless YouTube), 07 (POD) still have stale data from May 2025 cutoff. Refresh each with a "Refreshed YYYY-MM-DD" section + cited sources. The remote agent should pick the oldest unrefreshed one each run.
**Next concrete step:** Pick 06-faceless-youtube.md next — it directly informs experiments/youtube-history-channel/ which is already in active development (B-012..B-017). Current YouTube-channel build assumes generic "faceless history" viability; a refreshed view of the category (2026 YPP threshold changes, AI-content disclosure requirements, Shorts vs long-form monetization, faceless-niche saturation) could materially change the B-012 strategy before we sink more build time. Alternative: 05-chrome-extension.md. After those: 07 (POD), then B-009 is done.
**Constraint update from 04 refresh:** Niche content sites are now explicitly deprioritized — do not pursue as a first-dollar path. See 04-niche-content-sites.md "Recommendation for the loop" section. The only honest revisit path is as a *data/tool asset* (closer to B-001/B-008/B-010 shape), not as a content farm.

### B-010 — Build a third browser tool (open category)
**Status:** [pending] — fully remote-doable, no creds for build phase
**Why:** Inventory expansion. Two browser tools (B-001 + B-008) is a small portfolio. A third widens the surface area. Constraints: must be single static file, must target AI tooling audience or adjacent dev audience, must not duplicate B-001 or B-008.
**Next concrete step:** Pick one of: (a) Anthropic tool-definition validator (paste JSON schema, get validated tool def), (b) prompt diff viewer (paste two prompts, see line-by-line diff), (c) markdown→plaintext converter, (d) regex tester with named-capture support, (e) JWT decoder, (f) something else suggested by current research. Build it as `experiments/<slug>/`. Hand off to local for ship.

### B-011 — Author a second Gumroad digital asset (queue behind B-002)
**Status:** [pending] — remote-doable for build phase
**Why:** B-002 (Claude Code Power Prompts) is a single product. Once it ships, having a second asset ready to upload back-to-back is the right move (one-product creators almost never make sales; clusters do). Candidates: "AI agent CLAUDE.md template pack", "Cybertruck-Autopilot-style operating-loop starter kit", "100 prompts for X niche".
**Next concrete step:** Decide on the second product after B-002 is shipped and we have measurement data. Until then, keep this as a placeholder so the agent doesn't redundantly start it.

### B-012 — Write full script for episode 1 (Dancing Plague of 1518)
**Status:** [pending] — fully remote-doable, no creds needed
**Why:** First video of the history channel. Placeholder + beat map already in `experiments/youtube-history-channel/scripts/01-dancing-plague-1518.md`. Agent must: verify sources via WebSearch, write the full ~1,350-word script following the structure in `experiments/youtube-history-channel/production-pipeline.md`, every factual claim cited inline as a comment, change frontmatter status to `scripted`, commit.
**Definition of done:** `01-dancing-plague-1518.md` contains the full spoken-narration script, ~1,350 words, sectioned per the beat map, with inline source citations.

### B-013 — Build tools/source_images.py (image sourcing helper)
**Status:** [pending] — fully remote-doable (no creds for LoC/Wikimedia APIs)
**Why:** Needed before any video can be produced. Given a list of search terms, queries Library of Congress API + Wikimedia Commons API + Internet Archive API, downloads 20+ public-domain images per video, writes a `sources.md` with attribution per image.
**Next concrete step:** Research each API's endpoint + licensing metadata fields. Write `tools/source_images.py` that takes a video slug and search terms, pulls candidates, filters by license (PD or CC-BY only), downloads to `experiments/youtube-history-channel/assets/<slug>/`, writes `sources.md`.

### B-014 — Build tools/narrate.sh (Edge TTS wrapper)
**Status:** [pending] — remote-doable if the sandbox has Python + `edge-tts` available
**Why:** Turns a script file into `narration.mp3`. Uses Microsoft Edge TTS (free, no signup, high quality).
**Next concrete step:** Verify `edge-tts` pip package is installable in the remote sandbox. Write `tools/narrate.sh` that reads the spoken-narration section of a script file, strips comments/frontmatter, pipes to edge-tts with voice=en-US-GuyNeural, outputs to assets/<slug>/narration.mp3.

### B-015 — Build tools/render_video.py (ffmpeg storyboard → MP4)
**Status:** [pending] — depends on B-013 and B-014; may require local execution if remote sandbox lacks ffmpeg
**Why:** Turns images + narration + music into the final 1080p MP4. Ken Burns pan/zoom via ffmpeg zoompan filter.
**Next concrete step:** Check ffmpeg availability in remote sandbox. If unavailable, mark this task as local-only and flag it in the inbox.

### B-016 — Build tools/youtube_upload.py (YouTube Data API v3 upload helper)
**Status:** [blocked-on-human] — requires YOUTUBE_OAUTH_REFRESH_TOKEN in `.env`
**Why:** Automates the upload step so videos ship end-to-end without Robert dragging files into YouTube Studio. Until the token exists, upload is manual.
**Unblocks:** fully automated weekly video shipping.
**Handoff:** see the `human_inbox/` note B-012 will write.

### B-017 — Source public-domain images for episode 1 (Dancing Plague)
**Status:** [pending] — depends on B-012 (script must exist first) AND B-013 (helper must exist first), OR can be done manually
**Why:** Before rendering, we need ~20 images sourced and attributed. Agent can do this manually via WebSearch if B-013 isn't ready.
**Next concrete step:** After B-012 is done, search Library of Congress, Wikimedia Commons, and Internet Archive for: "Strasbourg 16th century", "medieval woodcut dancing", "Saint Vitus dance", "16th century Europe engraving", "dance macabre". Download 20+ candidates, filter by license, save to `experiments/youtube-history-channel/assets/dancing-plague-1518/`, write `sources.md`.

## Done
_(none yet — note: B-001 prompt-cleaner is shipped externally as of 2026-04-11, see runlog. Should be moved here on a future cleanup pass.)_
