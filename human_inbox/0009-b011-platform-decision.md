# 0009 — B-011 platform decision: Gumroad vs Lemon Squeezy (optional override)

**Created:** 2026-04-13 21:31 UTC by remote run #65 (the first run after the
B-011 48-hour post-B-002-ship gate tripped).
**Action required from Robert:** **Optional.** Zero-touch default is
available below — this note exists only if Robert wants to override.
**Urgency:** none. The next remote run will proceed on the default unless
an override file is dropped in `human_outbox/` first.

## TL;DR
The agent is starting B-011 (Claude Code hook recipes — the second digital
asset, freemium dual-channel: free plugin marketplace + paid extended pack).
The 03-Gumroad refresh surfaced Lemon Squeezy as a cheaper alternative at
our $3–$7 price points. The scoping run has picked **Gumroad by default**
for cross-sell + zero-new-setup reasons (see below + `experiments/claude-code-hooks/PLATFORM.md`
for the full reasoning). If you disagree, drop a file in `human_outbox/`
saying so and the next remote run will switch.

## The one-paragraph version of the fee math
At $5 per sale: Gumroad nets ~$3.55, Lemon Squeezy nets ~$4.25 — LS keeps
~$0.70 more per sale (roughly 30% more revenue per transaction in the
micro-price zone). On 100 sales that's +$70. At zero sales it's $0. See
the fee table in `experiments/claude-code-hooks/PLATFORM.md` for the full
breakdown at $3 / $5 / $7.

## Why the scoping run defaulted to Gumroad
1. You already have a Gumroad account + `GUMROAD_ACCESS_TOKEN` in `.env`
   + a tested upload helper (`tools/ship_gumroad.py`). Lemon Squeezy
   requires a new account, new KYC, new payout link, new API token, and a
   new `tools/ship_lemonsqueezy.py` helper — roughly 30–60 min of your time
   plus greenfield agent-side code that could break.
2. Hook recipes and Power Prompts target **the exact same audience**.
   Clustering both on `robertwave56.gumroad.com` lets a customer of one
   become a customer of the other with one click via Gumroad's "More from
   this creator" surface. Moving Power Prompts to LS mid-measurement-window
   is explicitly ruled out by the 03-refresh, which means cross-sell only
   works on Gumroad for now.
3. The honest revenue expectation for an unknown second product with zero
   paid promotion is ~$0. The LS fee advantage only materializes above a
   floor of sales we haven't proven we can reach. Below that floor the
   advantage is worth exactly zero and the friction cost is positive.
4. If B-011 surprises us and earns ≥20 paid downloads in 14 days, the
   next-asset decision should reopen this choice and seriously consider
   migrating forward. The decision isn't forever.

## Why you might want to override
- **You want to try PWYW-with-minimum.** Gumroad on your current tier
  doesn't support it (same reason Power Prompts landed at $3 fixed).
  Lemon Squeezy does. If you're willing to spend 30–60 min on new-account
  setup to test a $7-PWYW-with-$5-floor price shape, LS is the platform.
- **You'd rather diversify across platforms.** If you don't want 100% of
  the digital-asset revenue funnel dependent on Gumroad staying up and
  sane, LS gives you a second rail. Reasonable if you expect this to
  scale.
- **You'd prefer the cheaper platform regardless of setup cost.** It's
  your time and your call. The agent will not second-guess if you override.

## How to override
Drop a file anywhere in `human_outbox/` containing something like:

```
Switch B-011 to Lemon Squeezy. I will:
- create the LS account
- generate the API token
- add LEMONSQUEEZY_ACCESS_TOKEN to .env before the paid-pack ship.md handoff

Agent: proceed to build the free pack on the next run; assume LS for
the paid pack.
```

The agent will read that on the next remote run, update the backlog,
and adjust `experiments/claude-code-hooks/ship.md` to target LS when
it's written.

## If you do nothing
The next remote run will:
1. Start building the 5–8 free hooks (`experiments/claude-code-hooks/free-pack/`)
2. On the run after that, build the 15–18 paid hooks + walkthroughs
3. Then write `ship.md` with Gumroad upload instructions + awesome-claude-code
   PR draft + Show HN title options
4. Land a handoff inbox note asking you to run the local ship workflow
   (`tools/ship_gumroad.py` + push the free repo via `gh repo create`)

No action on your end until that ship handoff lands.

## Related
- `experiments/claude-code-hooks/README.md` — full scoping doc for B-011
- `experiments/claude-code-hooks/PLATFORM.md` — decision document with fee table
- `research/markets/03-gumroad-digital-downloads.md` — "Refreshed 2026-04-12"
  section, findings #1 and #2 (where the LS alternative was surfaced)
- `state/backlog.md` — B-011 entry (marked [in_progress remote run #65])
