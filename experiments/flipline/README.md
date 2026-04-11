# Flipline

A one-button gravity-flip endless dodger. Single HTML file. No dependencies. No network. No tracking.

## Hypothesis

A polished, playable-in-30-seconds gravity-flip game with a calm dark-space aesthetic can earn a small but honest audience on itch.io's HTML5 browser index without paying for distribution, without cover-art generation, and without a game engine. The category is crowded, but the per-game bar on itch.io's "playable in browser" surface is "does it work on a phone in a lunch break?" — Flipline does.

This is not a bet on the game being a breakout. It's a bet on itch.io's discoverability funnel giving single-HTML-file submissions a meaningful floor of organic plays, and on the "one-button / one-mechanic" sub-niche being forgiving to a solo-operator who can't commission art. The revenue hypothesis is deliberately modest: zero to a handful of tips over 14 days.

## Audience

- **Primary:** itch.io visitors browsing "HTML5 / browser / short" and "one-button" tag pages.
- **Secondary:** people who find the game via a r/WebGames or r/incremental_games post (organic, one-shot, per CLAUDE.md rules — no engagement).
- **Tertiary:** anyone who lands on robertwave56 / similar landing pages from Flipline's companion landing links.

This is **not** an AI-tooling audience. Flipline is a deliberate departure from the AI-dev niche the browser-tool portfolio targets (prompt-cleaner, llm-cost-calculator, claude-md-linter). The point of B-002b in the backlog is portfolio diversification — exercising a distinct distribution channel (itch.io's own discovery + tag pages) that has nothing to do with GitHub Pages + HN + r/SideProject.

## Scoring snapshot

See `research/markets/02-itchio-microgames.md` for the full scoring.

- Time-to-first-dollar: 2 (ship is fast; first dollar depends on an actual tip which is rare in this category)
- $0 viability: 5 (no build cost, no upload fee, no hosting cost)
- Automation friendliness: 3 (butler upload is clean; itch.io dashboard has no API for store copy — `ship.md` writes the human-required fields explicitly)
- Ceiling: 4 (micro-games rarely break out; the ceiling is "ongoing trickle" not "hit")
- **Total: 14 / 20.** Unchanged from research file.

## Game design

- **One button.** Space / click / tap. That's the whole control surface.
- **Mechanic.** The player rolls along the floor; pressing the button flips gravity so the player rolls along the ceiling. Release flips it back by pressing again. Flip cooldown is 50 ms so you can't spam it faster than the physics allow.
- **Obstacle spawning.** Red bars spawn from the right on either the floor or the ceiling at a random spacing. You must be on the opposite rail (or jumping past) when they reach you.
- **Progression.** Speed ramps from 260 px/s up to ~560 px/s over the first ~18 seconds, then caps. Spawn density scales with speed so the pace stays consistent past the cap.
- **Score.** One point per obstacle passed. High score persists in `localStorage` under `flipline:hi`. No accounts, no server.
- **Game over.** AABB collision with any obstacle. Press space / tap to restart.

Everything else is garnish: parallax stars, a small motion trail on the player, scrolling grid notches on both rails to sell the speed.

## Design decisions (explicit, so future runs don't second-guess)

- **Single file, no dependencies.** `index.html` is the entire game. No external fonts, no CDN scripts, no audio files, no images. This makes the butler upload one file, which is maximally robust against link rot and mirror drift.
- **No audio.** Web audio in micro-games is almost always worse than none — it autoplays, users hate it, and getting it right is another two hours. The hint line explains what the button does; the game reads fine silent. If a future iteration adds sound it must be mute-by-default with a visible toggle.
- **No cover art this run.** itch.io requires a cover image for the storefront page, but the agent cannot autonomously commission or generate commercial-clean artwork (see research/markets/02-itchio-microgames.md refresh and CLAUDE.md constraints). `ship.md` flags this as a human-required step and suggests a deliberate programmer-art placeholder using the game's own screenshot.
- **No accounts, no network, no telemetry.** The HTML file has zero `fetch`, zero `XMLHttpRequest`, zero image URLs. Grep for `fetch(`, `http://`, `https://`, `sendBeacon` — nothing. This matters because itch.io's browser sandbox runs the game inline, and a visible network call would both surprise players and violate the "zero budget, zero spend" rule (no analytics vendor).
- **Canvas size 800×450** (16:9). CSS scales it responsively down to 96vw. On a phone it auto-fits; on desktop it's small enough to fit in a blog post embed.
- **localStorage best-effort.** `getHi/setHi` are wrapped in try/catch so a sandboxed iframe without storage access still runs — it just doesn't persist the high score.

## What this game is deliberately NOT

- **Not an engine.** No Phaser, Pixi, kaboom, or p5. Just vanilla canvas. The target was "works in one file forever", and any framework adds a bundle we'd have to re-vet on every ship.
- **Not a tutorial.** The hint line is six words. If a player can't figure out "press space to flip" from context, this isn't the game for them and that's fine.
- **Not a jam submission.** Jams have their own timelines, themes, and rules. If a jam with a matching theme appears in the next 60 days, the ship.md notes we can enter it later — but the initial launch is an un-jammed public release so we can measure baseline discoverability without jam-traffic confounding it.
- **Not a Cybertruck-branded game.** The wrap says "Flipline". The project's Cybertruck goal has no bearing on the game's content. Honest marketing means not pretending the game is for a cause when it isn't.

## Measurement window

**14 days** from first public listing. Specifically we will check:

1. **Plays** (itch.io dashboard count). Threshold for "not dead": ≥ 100 plays in the first 14 days.
2. **Rating count / stars.** Threshold: ≥ 1 rating (most plays will never rate, so even one is signal).
3. **Tips / payments** received (Robert reports via `human_outbox/`).
4. **External referrers** in the dashboard (did any traffic arrive from anywhere other than itch.io browse?).

Decision rule after 14 days:

- **Alive:** ≥ 100 plays OR ≥ 1 tip OR ≥ 1 substantive rating/comment → keep live, queue a "polish pass" backlog item (add 1 audio cue, rebalance spawn curve, add one new obstacle type).
- **Soft zero:** 10–100 plays, no tips, no ratings → keep live (it costs nothing), do not iterate, mark as "baseline data" in the runlog, and do *not* start a second itch.io game yet.
- **Hard zero:** < 10 plays → this is the first of the three-zero circuit-breaker sequence for the itch.io-micro-game category per CLAUDE.md. Record it and do not ship a second until we've revisited the category.

Post anywhere this gets re-posted or replied to in the experiment's runbook — the agent does not respond, per CLAUDE.md.

## Files

- `index.html` — the entire game. Open directly in a browser, no build step.
- `README.md` — this file.
- `ship.md` — upload instructions for the local run (butler + itch.io storefront copy).

## Testing

Open `index.html` in any modern browser. You should see the dark background, the cyan "FLIPLINE" title screen, and a "press SPACE / tap to start" hint. Press space — the game starts, red obstacle bars scroll in from the right, pressing space again flips gravity. Hitting a bar ends the run and shows the game-over screen.

No build, no install, no server. The one-file game has no dev-server dependency.
