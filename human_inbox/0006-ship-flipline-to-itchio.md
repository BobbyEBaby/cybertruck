# 0006 — Ship Flipline to itch.io

**Status:** blocked on B-000 (itch.io account + `BUTLER_API_KEY` in `.env`).
**Priority:** low — this is portfolio diversification into a category that is NOT expected to earn quickly. Do NOT de-prioritize any AI-tooling browser-tool ship or the B-002 Gumroad follow-up to do this.

## What I built (remote run #17)

`experiments/flipline/` — a single-file HTML5 browser game. One-button gravity-flip endless dodger. ~250 lines of vanilla JS inside one HTML file. No dependencies, no network calls, no audio, no tracking, no cover art generated yet. Playable offline by opening `index.html` in any browser.

Commit: (current HEAD on `main` after this remote run).

## What Flipline IS and ISN'T

- **IS:** a small, honest, one-mechanic arcade game. Plays in ~30 seconds per run. Dark aesthetic. High score in `localStorage`. Works on mobile and desktop.
- **IS NOT:** a breakout game, an AI-tooling product, or a Cybertruck-branded thing. It exists to exercise the itch.io vertical for portfolio diversification per backlog task B-002b.

Read `experiments/flipline/README.md` for the full hypothesis, scoring, design decisions, and 14-day measurement window.

## What I need from you

Two separable human steps. Either one can happen first; both need to be done before this game can go live.

### Step 1 — (blocked-on-human) create the itch.io account (B-000)

If you haven't already: go to https://itch.io/register, create an account, pick a username (you can use `robertwave56` to match the Gumroad handle for brand consistency, or whatever you prefer — just make sure it's YOUR handle, no "autopilot" prefix; per CLAUDE.md we use one account per platform and honest branding).

Then:

1. Add the itch.io username and profile URL to `state/accounts.md` under "Active accounts".
2. Go to https://itch.io/user/settings/api-keys → Generate New API Key → name it `cybertruck-autopilot`.
3. Open `.env` in the cybertruck repo root (it's gitignored, it's fine). Add:
   ```
   BUTLER_API_KEY=<the key you just generated>
   ITCH_USERNAME=<your itch.io username>
   ```
   **Do not paste the key into any file that is checked into git. Do not paste the key into any `human_outbox/` file. Do not paste it into chat. The `.env` file is already in `.gitignore`.**
4. Install the `butler` CLI locally — https://itch.io/docs/butler/installing.html. Verify with `which butler && butler version`.

Report back by dropping a file in `human_outbox/` that just says "itch.io account `<username>` created, butler installed, BUTLER_API_KEY in .env". Do NOT include the key.

### Step 2 — run the ship

In a local Claude Code session (not remote), run:

```bash
cd cybertruck
cat experiments/flipline/ship.md
```

Then follow the steps in `ship.md` top-to-bottom. Specifically:

1. **Pre-flight check** — open `experiments/flipline/index.html` in a browser (or `python3 -m http.server --directory experiments/flipline 8080` and open localhost:8080), play for 30 seconds, verify the game loop works end-to-end.
2. **Cover art decision** — I recommend taking a screenshot of the title screen ("FLIPLINE" on a dark background) and using that as the cover. Do NOT generate AI cover art (itch.io policy is tightening, and the game's aesthetic works as a screenshot).
3. **Butler upload** — the exact commands are in ship.md under "Butler upload commands". It's 3 lines. `butler push experiments/flipline <username>/flipline:html --userversion ...`
4. **Web dashboard metadata** — butler pushes the build but cannot set the store page fields. Paste the metadata block from ship.md (title, tagline, tags, description markdown) into https://itch.io/game/edit verbatim. Set pricing to **Free** on first launch per the 02-itchio-microgames refresh.
5. **Append to `state/publish-log.md`** — one row, format matching existing rows.
6. **(optional) Reddit post** — ONE post to r/WebGames, honest title, no replies. Only do this if Reddit credentials are set up (see B-003) and you have an account with enough karma to post without friction. If not, skip and note "reddit step deferred" in the runlog.

## What to do if something goes wrong

- **Game doesn't run in itch.io's iframe but runs locally** → itch.io's sandbox may block something. Check the browser console. Common fixes: viewport size exactly 800×450, mobile-friendly on, scrollbars off, fullscreen button on.
- **Butler refuses to push** → `butler login` should prompt for the API key. If `BUTLER_API_KEY` is set in `.env`, butler should auto-pick it up; otherwise paste it interactively into the `butler login` prompt.
- **itch.io flags the game** → don't fight it. Depublish, read the flag reason, write a new `human_outbox/` note with the verbatim rejection text, and the next remote run will figure out the fix.

## What NOT to do

- **Do NOT** pay for itch.io boosted listings, ads, or Creator Day paid slots (Creator Day participation itself is free — if the next one is within 14 days of launch, toggle participation on in the dashboard).
- **Do NOT** create multiple accounts, multiple uploads of the same game under different names, or crosspost across unrelated subreddits.
- **Do NOT** engage with comments or ratings on the itch.io page (CLAUDE.md rule; no replies).
- **Do NOT** link Flipline to the Cybertruck Autopilot in a way that turns the game's store page into an ad for the project — the README mentions it honestly once, that's enough.

## Report-back format

When Flipline is live, drop a file in `human_outbox/` with:

```
# 0006 reply — Flipline shipped

itch.io URL: https://<username>.itch.io/flipline
butler push timestamp: YYYY-MM-DD HH:MM UTC
cover art path taken: A (screenshot) | B (manual cover) | C (skipped)
pricing: free | PWYW
first-run cold plays over the first hour: N (from dashboard)
anything weird: ...
```

The next remote run will process this into `state/goal.json`, `state/publish-log.md`, and the B-002b backlog status line, and will start the 14-day measurement window from the first full day after launch.

## One more thing

This is the first game on the loop's portfolio. It is a deliberate diversification bet, not a high-ceiling bet. The honest-expectations.md anchor still applies: most itch.io micro-games earn $0 lifetime and Flipline's single-mechanic simplicity makes it a median case at best. The value is in *having* a live itch.io listing so that future game experiments can compound on that account's reputation and the next game can borrow the first game's review traffic. That's the whole strategic case. If it earns a single tip in 14 days, that's a win. If it earns zero, that's baseline data and also fine.
