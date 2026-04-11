# Runlog

Append-only. Newest entries at the bottom. One entry per scheduled run.

## 2026-04-10 bootstrap
- task: Phase 0 — initialize project, run first market research pass, seed backlog
- did: Created directory tree, CLAUDE.md, state files, scripts/daily.md, scripts/weekly.md, human_inbox + human_outbox conventions and 0001-setup.md handoff. Wrote 8 market research files in research/markets/ scoring zero-budget digital product categories. Ranked them in state/backlog.md.
- outcome: success (bootstrap complete)
- next: User must complete human_inbox/0001-setup.md (free account signups + run /schedule). Once a daily cron is installed, the next run picks task B-001 from backlog.md.

## 2026-04-10 max-autonomy revision
- task: Restructure plan to minimize ongoing human interaction per user request ("set it and forget it")
- did: Added "Max-autonomy rules" section to CLAUDE.md (rate limits, no comment engagement, circuit breaker, pause file, never-touch-seed-phrase, env-loading discipline). Wrote state/honest-expectations.md as the permanent reality check. Replaced human_inbox/0001-setup.md with one-session setup including Kraken deposit address, API tokens, cron install. Wrote .gitignore and secrets/ policy. Added state/publish-log.md for rate limiting. Updated scripts/daily.md to use API/CLI publish path instead of manual handoffs. Added B-005, B-006, B-007 to backlog. Added tools/README.md.
- outcome: success
- next: User to fill in API tokens in .env and install cron. Then daily run will pick B-001.

## 2026-04-10 wallet routing
- task: Capture all Kraken deposit addresses Robert provided
- did: Stored 9 deposit addresses in .env (BTC, ZEC, DOGE, BCH, BONK, SHIB, XRP w/ destination tag, TRX, SOL, USDC-Solana). Confirmed USDC-Solana shares the SOL/BONK address (Kraken assigns one Solana address per account for all SPL tokens). Promoted USDC on Solana to primary savings rail in state/accounts.md. Updated state/goal.json with savings_rail and savings_address. Added XRP destination tag warning everywhere it could be missed.
- outcome: success
- next: Robert to fill in API tokens in .env. Money-receive side fully wired.

## 2026-04-11 06:03 — first ship 🚀
- task: B-001 — deploy prompt-cleaner to GitHub Pages
- did: User dropped GITHUB_TOKEN in .env. First deploy attempt failed: gh CLI not installed on this machine. Rewrote tools/deploy_pages.sh to use raw GitHub REST API via curl + git (no gh dependency). Re-ran. Created public repo BobbyEBaby/prompt-cleaner via POST /user/repos, cloned, copied experiments/prompt-cleaner/ contents in, pushed to main, enabled Pages via POST /repos/.../pages (returned 201 Created). Live URL: https://bobbyebaby.github.io/prompt-cleaner/. Appended entry to state/publish-log.md.
- outcome: success — first external artifact is live
- next: Verify the live URL renders the tool correctly (give Pages 30–90s to propagate). Do NOT post to Reddit yet — Reddit credentials not in .env, and we'd want to wait until Robert has actually opened the live URL once and confirmed it works. Update experiments/prompt-cleaner/README.md metrics table with the live URL.

## 2026-04-10 git repo + first build
- task: Init git, push to BobbyEBaby/cybertruck, build B-001 prompt-cleaner experiment
- did: git init, initial commit be8fdf3 (23 files), pushed to https://github.com/BobbyEBaby/cybertruck. Verified .env and secrets/ excluded. Then built experiments/prompt-cleaner/ — a working single-file HTML5 tool (input/output, 6 cleaning toggles incl. strip markdown / collapse blank lines / remove filler phrases / smart-quote conversion / token estimate / copy-to-clipboard, dark UI, no dependencies, ~430 lines). Wrote experiment README.md and ship.md. Refreshed market research 01-browser-utilities and 03-gumroad-digital-downloads with current 2026 data via WebSearch (Gumroad fees: 10%+$0.50 direct / 30% Discover; donation conversion rate for utility tools 0.024–0.5%; Ko-fi noted as 0%-fee tip rail vs Buy Me a Coffee 5%). Wrote tools/deploy_pages.sh (gh-based GitHub Pages auto-deploy with .env loading, idempotent, appends to publish-log) and tools/post_reddit.py (PRAW-based, single post, hard 24h rate-limit check against publish-log, never replies).
- outcome: success — local build complete, NOT yet shipped externally (blocked on GITHUB_TOKEN in .env)
- next: When user fills GITHUB_TOKEN and installs cron, the first scheduled run executes `tools/deploy_pages.sh prompt-cleaner experiments/prompt-cleaner` and the tool goes live at https://bobbyebaby.github.io/prompt-cleaner/. Reddit post is a separate decision the next run can make based on REDDIT_* tokens.
