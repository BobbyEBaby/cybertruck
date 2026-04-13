# B-011 platform decision: Gumroad vs Lemon Squeezy

**Context:** B-011 (Claude Code hook recipes, freemium dual-channel) needs a
paid storefront. B-002 (Claude Code Power Prompts) shipped on Gumroad. The
03-refresh (2026-04-12) surfaced Lemon Squeezy as a materially cheaper
alternative at our price points and specifically requested that the B-011
scoping run present the choice as a structured decision rather than
defaulting silently.

This file is that decision document. It is written for Robert to override
via `human_outbox/` if he disagrees with the default. If no override arrives
by the next remote run, the build proceeds on the default (**Gumroad**).

## The honest fee math

At our $3–$5 price points, from the 03-refresh verified 2026-04-12:

| Product price | Gumroad effective fees | Gumroad net | Lemon Squeezy effective fees | LS net |
|---|---|---|---|---|
| $3.00 | ~$1.19 (39.7%) | ~$1.81 | ~$0.65 (21.7%) | ~$2.35 |
| $5.00 | ~$1.45 (29.0%) | ~$3.55 | ~$0.75 (15.0%) | ~$4.25 |
| $7.00 | ~$1.71 (24.4%) | ~$5.29 | ~$0.85 (12.1%) | ~$6.15 |

Lemon Squeezy saves **$0.54–$0.86 per sale** at these price points — roughly
15–30% more revenue per transaction. On 100 sales at $5, that's $70 more.

Both platforms are Merchant of Record (handle global VAT/GST/sales tax
automatically since Jan 2025). Both ship digital downloads natively. Both
allow fixed-price or pay-what-you-want. Both have free tiers with no
up-front cost. Both pay out via PayPal or bank transfer.

## The case for **Gumroad** (default)

1. **Zero new setup.** Robert already has a Gumroad account with
   `GUMROAD_ACCESS_TOKEN` in `.env` and a live listing (Power Prompts at
   https://robertwave56.gumroad.com/l/grlmp). Adding a second listing is a
   5-minute operation the local agent can do via the existing tooling
   (`tools/ship_gumroad.py`, which already works). Lemon Squeezy would
   require: new account signup, KYC, payout method reconnect, new API
   token generation, and a new `tools/ship_lemonsqueezy.py` helper — an
   estimated 30–60 minutes of Robert's local time plus a new chunk of
   agent-side tooling.

2. **Single-storefront cross-sell.** Hook recipes and Power Prompts target
   the **exact same audience** (developers who use Claude Code and care
   enough to pay for tooling improvements). Clustering both products on
   `robertwave56.gumroad.com` means a customer who buys one is one click
   from the other. Gumroad shows "More from this creator" on every listing.
   Lemon Squeezy can do this too but only if both products live on the
   same LS store — which means moving Power Prompts, which the 03-refresh
   explicitly said not to do mid-measurement-window.

3. **Proven upload pipeline.** `tools/ship_gumroad.py` is battle-tested.
   A new LS helper would be greenfield code with no production miles.
   Greenfield publishing code is the #1 place new ships break, and we
   don't need two broken platforms.

4. **Robert's tier limitation already priced in.** Robert's Gumroad tier
   doesn't support PWYW-with-minimum (per the B-002 listing note). We've
   already designed B-011 around fixed-price ($5 or $7). The tier-limit
   cost is zero for this product.

5. **At $0 in actual revenue, the fee savings are literally zero.** The
   Lemon Squeezy advantage only materializes above some floor of sales
   we haven't proven we can reach. B-002's 14-day measurement window
   is still open; B-002 may well earn $0. If both products earn $0, the
   platform choice costs nothing either way and the lower-friction path
   is the honest one.

## The case for **Lemon Squeezy** (alternative)

1. **Meaningfully cheaper above $1.** 5% + $0.50 vs 10% + $0.50 + ~3%
   processor. At any price point below ~$15 the gap is material. At
   $5, LS keeps ~30% more of each sale.

2. **No mid-experiment switching cost.** B-011 hasn't been built yet.
   There's no listing to migrate. This is the one B-011 decision point
   where switching platforms is free. Later it won't be.

3. **LS supports PWYW-with-minimum natively.** On a higher plan tier
   (or even free, depending on LS's current setup), PWYW-with-minimum
   is supported. If Robert wanted to try $7 PWYW with a $5 floor for
   B-011, LS is the platform that allows it. Gumroad on his current
   tier does not.

4. **No Discover 30% tax.** Gumroad Discover charges 30% on passive-
   discovery traffic. LS has no equivalent 30% surface. This only
   matters if a product actually earns Discover traffic — and the
   03-refresh notes Discover is realistically irrelevant for B-011
   (all traffic is direct from Reddit/HN/marketplace, not passive).

5. **LS handles license keys and subscriptions.** Not relevant for a
   $5 markdown download, but if a future B-011-derived product needs
   per-customer license keys, Gumroad doesn't do that and LS does.

## Cross-cutting considerations (apply to both)

- **Both refunds: the platform keeps its fees.** Gumroad keeps the 10%
  on refunds; LS has the same policy. Accurate descriptions matter on
  both — keep the listing honest, list the exact hook count in the
  public description.
- **Both have free tiers.** Neither asks for money up front. The
  "never spend money" rule in CLAUDE.md is satisfied by either.
- **Neither has a way for the agent to create the account.** If LS is
  picked, Robert must manually create the account and provision the
  API token.

## Default recommendation: **Gumroad**

The Lemon Squeezy fee advantage is real and material **above the floor
of nonzero sales**. Below that floor (where the honest expectation from
`state/honest-expectations.md` says we live) the advantage is worth
exactly $0. The friction cost of standing up a second platform is
nonzero and lands on Robert, who is the scarce resource in this loop.
Until B-011's first sale proves the product is in the "fee savings
actually matter" zone, the cheap move is the low-friction move.

Cross-sell clustering is the other decisive factor. Hook recipes and
Power Prompts share an audience 1:1. Putting them on the same storefront
is a 0-minute revenue optimization that requires no new code.

**If B-011 earns even modest real sales (≥20 paid downloads in 14 days),
the next-asset decision (B-012 equivalent, whatever that becomes) should
reopen this choice and seriously consider migrating forward to LS.** At
20 paid sales at $5, the LS savings would have been ~$14 over the window
— small but no longer zero.

## How Robert overrides

Drop a file in `human_outbox/` with something like:

```
Switch B-011 to Lemon Squeezy. I'll create the account and generate the
API token. Agent: proceed to build the free pack on the next run; I'll
handle the LS setup in parallel and push LEMONSQUEEZY_ACCESS_TOKEN to
.env before the paid-pack ship.md handoff.
```

If no override file appears in `human_outbox/` before the next remote
run, the build proceeds on Gumroad by default and this `PLATFORM.md`
stays as the decision record.

## Status
**Decision pending Robert's override window (one remote-run cycle).**
**Default: Gumroad.**
**Build will not stall on this decision.**

## Source
`research/markets/03-gumroad-digital-downloads.md` — "Refreshed 2026-04-12"
section, findings #1 and #2. Fee math verified from Lemon Squeezy and
Gumroad pricing pages, WeAreFounders comparison, Ruul blog, Dodo Payments
blog.
