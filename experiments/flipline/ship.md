# ship.md — Flipline

**Read this file top to bottom before running any commands.** The local agent (or Robert) executes this ship; the remote agent cannot, because publishing needs `BUTLER_API_KEY` + an authorized itch.io account, neither of which exist in the remote sandbox.

## Pre-flight

1. **itch.io account exists.** Robert has an itch.io account (username should already be in `state/accounts.md`'s "Active accounts" section). If not, this ship is blocked on B-000 — create the account first, add the username to `state/accounts.md`, then return here.
2. **`BUTLER_API_KEY` is in `.env`.** The key comes from https://itch.io/user/settings/api-keys — "Generate new API key", name it "cybertruck-autopilot". Paste it into `.env` under the line `BUTLER_API_KEY=...`. Never print, echo, log, or commit this key. `.env` is already in `.gitignore`.
3. **`butler` CLI is installed.**
   ```bash
   which butler || echo "NOT INSTALLED — see https://itch.io/docs/butler/installing.html"
   ```
   On linux: download from https://broth.itch.zone/butler/linux-amd64/LATEST/archive/default, unzip, put in `~/.local/bin/`. On macOS: `brew install --cask butler` is a common path but it's not official — the official path is the direct download.
4. **Game is playable locally.**
   ```bash
   python3 -m http.server --directory experiments/flipline 8080
   ```
   Then open http://localhost:8080 in a real browser (not a headless test). Verify:
   - Title screen shows "FLIPLINE" on a dark background.
   - Press space → obstacles start scrolling in from the right.
   - Press space again → gravity flips, player moves to ceiling.
   - Hit an obstacle → game-over screen with score and best.
   - Press space → restart works.
   - Reload the page → "BEST" score persists (localStorage).
5. **Cover art decision** — choose ONE path before listing:
   - **Path A (recommended, agent-friendly):** use a screenshot of the title screen itself (300×250 or similar) as the cover. Programmer-art aesthetic. Honest.
   - **Path B (human-required):** Robert opens any free vector editor (Figma free tier, Excalidraw, etc.) and makes a 630×500 cover with the word FLIPLINE and a simple gradient. 10 minutes.
   - **Do NOT** generate AI art for the cover — itch.io's policy on AI-generated visuals is tightening and we don't want the listing flagged.

## Butler upload commands

Assume the game target is `robertwave56/flipline` (adjust to Robert's actual itch.io username — check `state/accounts.md`).

```bash
# 1. Authenticate butler (one-time; idempotent if already done)
set -a; source .env; set +a
butler login

# 2. Zip the game directory (butler accepts zip or raw dir; raw dir is simpler)
# Butler uploads only the files actually used by the running game:
#   index.html (the entire game, single file)

# 3. First-time push — channel name "html" tags this as an HTML5 browser game
butler push experiments/flipline ${ITCH_USERNAME:-robertwave56}/flipline:html \
    --userversion "$(date +%Y%m%d.%H%M)"

# 4. Verify
butler status ${ITCH_USERNAME:-robertwave56}/flipline:html
```

**After the first push**, the game's storefront page still needs manual configuration in the itch.io web dashboard — butler uploads the build but cannot set the store metadata. Go to https://itch.io/game/edit — new game — fill in the fields from the section below.

## itch.io storefront metadata

Paste verbatim into https://itch.io/game/edit when creating the game entry. Do not paraphrase.

- **Title:** `Flipline`
- **Project URL:** `flipline` (gives `https://robertwave56.itch.io/flipline`)
- **Short description / tagline:** `A one-button gravity-flip arcade dodger. Single HTML file. No tracking.`
- **Classification:** Games
- **Kind of project:** HTML
- **Release status:** Released
- **Pricing:** **Free**. Do NOT enable paid / PWYW on first launch — see the 02-itchio-microgames refresh (PWYW minimum < $3 loses the majority of revenue to per-transaction fees). If measurement after 14 days shows ≥ 1 organic play request for a tip rail, then flip to PWYW with **$3 suggested / $1 minimum** in a follow-up ship. For now the tip rail is Ko-fi (see "Tip rail" below), not itch's native payment.
- **Uploads:** upload the butler-pushed HTML build. Set "This file will be played in the browser" for `index.html`. Viewport: **800 × 450**. Check "Enable scrollbars" off. Check "Fullscreen button" on. Check "Mobile-friendly" on. Orientation: any.
- **Description (Markdown source below):**

```md
# Flipline

A one-button gravity-flip arcade dodger.

**Controls:** Space / click / tap to flip gravity. Dodge the red bars. Survive as long as you can.

**Plays in your browser.** Single HTML file. No installation. No accounts. No tracking. No ads. Your high score is saved locally in your browser.

Built as part of the [Cybertruck Autopilot](https://github.com/BobbyEBaby/cybertruck) project — a public log of an automated indie dev loop that ships small, honest things and documents every failure. Flipline is the first game in that portfolio.

If you enjoyed this enough that a dollar-sized nudge wouldn't feel weird, [Ko-fi is here](https://ko-fi.com/) (Robert — replace with your Ko-fi URL before publishing). Tips are 100% optional — the game is free.

## How it works

Flipline is ~250 lines of vanilla JavaScript in one HTML file. No engine, no framework, no dependencies. You can read the whole source by clicking "View Source" in your browser. It is deliberately small because the goal is to ship, measure, and learn — not to build another unfinished project.

## What's next

If this game finds even a tiny audience, the next version adds: a single audio cue on flip, a second obstacle type, and a small difficulty curve tuning pass. If it finds zero audience, it stays live as a free thing anyone can play and the project moves on to other experiments.
```

- **Genre:** `Action`
- **Tags (up to 10, all lowercase, comma-separated):** `one-button`, `arcade`, `gravity`, `endless`, `minimalist`, `html5`, `browser`, `mobile`, `no-ads`, `single-file`
- **App store links:** leave all blank
- **Custom noun:** "game" (default)
- **Community:** off (we do not engage in comments per CLAUDE.md)
- **Visibility & access:** **Public**. Do not mark as restricted or draft.

## Distribution checklist (post-launch)

Per CLAUDE.md: max 1 publication per platform per 24h, no replies, no multi-account, no DMs.

- [ ] `state/publish-log.md` — append a row with platform=`itch.io`, URL, date.
- [ ] **r/WebGames post** — ONE post, honest title like "Flipline — one-button gravity dodger, single HTML file, plays in browser". Body: three lines describing what it is + link. Post on a weekday afternoon PT. Do NOT reply to comments. Do NOT crosspost. *Blocked on Reddit credentials + r/WebGames account warm-up; use `tools/post_reddit.py` if available, otherwise skip Reddit this launch and note it in the runlog as "reddit step deferred".*
- [ ] **r/incremental_games** — skip. It's an idle-game community; Flipline is arcade, not idle. Wrong audience.
- [ ] **Ko-fi link** — if Robert has a Ko-fi account, update the `[Ko-fi is here](https://ko-fi.com/)` placeholder in the description above to the real URL before publishing the store page. If not, delete the sentence — do not leave a dead link.
- [ ] **USDC-Solana tip address** — optional follow-up ship once a tip rail is validated. For the first launch, Ko-fi-or-nothing keeps the description clean.
- [ ] **Do NOT** submit to a jam on first launch (per 02-itchio-microgames refresh point 3: establish baseline discoverability first).
- [ ] **Do NOT** pay for any boosted listing or itch.io Creator Day ad slot. Creator Day participation is free — if the next Creator Day is within the 14-day measurement window, toggle the game's participation on in the dashboard (free, zero spend). If not, ignore.

## Rollback

If anything goes wrong post-upload (game won't run in itch's iframe, store page broken, etc.):

```bash
# Depublish by marking the game as "draft" in the web dashboard (no butler command for this).
# Alternatively, delete the upload:
butler wipe robertwave56/flipline:html
```

Never delete the game entry itself without also removing it from `state/publish-log.md`.

## Day-14 decision rule

Read `README.md` → "Measurement window" for the thresholds. The decision gate is binary: **alive / soft zero / hard zero**. Write the outcome into `state/backlog.md` B-002b status line and into the runlog.

## Honest note for whichever agent reads this

This game is a small thing. It won't buy a Cybertruck. The point of shipping it is to exercise the itch.io vertical, get measured data on itch.io's organic discovery for single-HTML-file games, and have a second category alive so that our entire portfolio isn't bet on AI-tooling browser utilities. If this ships and gets 3 plays over 14 days, that's a real data point about itch.io's discovery floor — it is not a failure of this run.
