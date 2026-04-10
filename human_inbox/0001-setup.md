# 0001 — One-session setup (do this once, then I take over)

**Time estimate:** 90–120 minutes total. You can do it in chunks but try to finish within a week so the loop can start.

**Why this is long:** I'm asking you to do *all* the human-only work in one go so that after this, I genuinely don't need you for routine runs. Every minute you spend here saves you hours later.

## The deal
After this session you will have:
- A self-custody crypto wallet **you control** (I never see the seed phrase)
- A KYC'd exchange account that auto-converts any fiat earnings to crypto and ships them to your wallet
- Free accounts on every platform I'll publish to, plus API tokens stored locally so I can publish without you
- A daily and weekly cron installed so I run on my own

After that, I'll only ping you when:
- A platform changes its rules and breaks an automated path
- The circuit breaker fires (3 ships in a category got zero traction)
- The weekly review has something honest to report
- Something earns money
- I would have to spend money and I'm refusing

---

## Part A — Kraken deposit address (5 minutes — you already have the account)

You already have a Kraken account, so Parts A and B are collapsed into one short step.

**Recommendation: use a USDC deposit address, not BTC/ETH/SOL native coin.** Reasons:
- Revenue is denominated in USD; the Cybertruck price is in USD. Holding the savings in a stablecoin removes volatility from the savings number.
- USDC on **Solana** or **Polygon** has near-zero transaction fees (BTC and ETH would eat small payouts in network fees).
- Kraken supports USDC on multiple networks.

If you don't already have a USDC deposit address in Kraken:
1. Log into Kraken → **Funding** → **Deposit** → search "USDC"
2. Pick a network. **Solana** is my recommendation (cheapest, fastest). Polygon is fine too.
3. Click "Generate deposit address" if no address exists.

Then:
1. Copy the deposit address.
2. Note **which network** it's on (Solana, Polygon, Ethereum, etc.) — addresses on the wrong network = lost funds, so this matters.
3. Put it in `human_outbox/0001-reply.md` under `kraken_deposit_address:` and `kraken_deposit_network:`.

If you'd rather use a different coin (BTC, ETH, SOL native, etc.), just tell me which and grab that deposit address instead. I'll use whatever you give me.

### Custodial caveat (worth saying once, then dropping)
Crypto sitting in Kraken is technically Kraken's IOU, not yours. For getting started and for small amounts this is fine — it's the same trust model as a bank account. **If/when the balance ever crosses ~$5,000**, the agent will write a `human_inbox/` note recommending you withdraw the bulk of it to a self-custody wallet (MetaMask/Phantom). Backlog item B-007 tracks this.

## Part C — Publishing platform accounts + API tokens (45–60 minutes)

For each platform: create account, then generate an API token. **Paste the tokens into `cybertruck/.env`**, not into the outbox. The agent reads `.env` directly and never prints it.

When you're done, just tell me in `human_outbox/0001-reply.md`: "all tokens in .env" — no token values needed, just confirmation each one is filled.

### Create the .env file
At `C:\Users\evans\gamedev\cybertruck\.env` (it's already in `.gitignore`), use this template:

```
# Cybertruck Autopilot credentials — never commit, never share
GITHUB_TOKEN=
ITCH_USERNAME=
BUTLER_API_KEY=
GUMROAD_ACCESS_TOKEN=
NPM_TOKEN=
PYPI_TOKEN=
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USERNAME=
REDDIT_PASSWORD=
REDDIT_USER_AGENT=cybertruck-autopilot/0.1 by <your-reddit-username>
KRAKEN_DEPOSIT_ADDRESS=
KRAKEN_DEPOSIT_NETWORK=
KRAKEN_DEPOSIT_ASSET=USDC
EXCHANGE_PLATFORM=kraken
```

### Tokens to generate

1. **GitHub** — https://github.com/signup, then https://github.com/settings/tokens?type=beta — create a fine-grained personal access token with: Contents (read+write), Pages (write), Workflows (write), Administration (write) on a new repository scope. Paste as `GITHUB_TOKEN`.

2. **itch.io** — https://itch.io/register, then https://itch.io/user/settings/api-keys — generate API key. Paste as `BUTLER_API_KEY`. Also fill in `ITCH_USERNAME`. Then download Butler: https://itch.io/docs/butler/installing.html — install and confirm `butler version` works in a terminal.

3. **Gumroad** — https://gumroad.com/signup, then https://gumroad.com/settings/advanced — generate access token. Paste as `GUMROAD_ACCESS_TOKEN`.

4. **Reddit** — https://reddit.com/register, then https://www.reddit.com/prefs/apps → "create app" → script type → fill the form. The client ID is the short string under the app name, the secret is the longer one. Fill in all `REDDIT_*` fields.

5. **(Optional) npm** — https://www.npmjs.com/signup, then Account → Access Tokens → Generate New Token (Automation). Paste as `NPM_TOKEN`. Skip if you don't want to publish npm packages.

6. **(Optional) PyPI** — https://pypi.org/account/register/, then Account Settings → API tokens → Add API token. Paste as `PYPI_TOKEN`. Skip if you don't want to publish Python packages.

7. **Kraken deposit info** from Part A → `KRAKEN_DEPOSIT_ADDRESS`, `KRAKEN_DEPOSIT_NETWORK`, `KRAKEN_DEPOSIT_ASSET`. (`EXCHANGE_PLATFORM=kraken` is already set.)

## Part D — Install the cron (5 minutes)

In a Claude Code session pointed at `C:\Users\evans\gamedev\cybertruck`:

1. **Daily run:**
   ```
   /schedule
   ```
   Prompt: `Read scripts/daily.md and follow it exactly.`
   Schedule: `0 9 * * *` (9am daily — pick a time you'll be at your computer for the first week so you can spot-check the runs)

2. **Weekly review:**
   ```
   /schedule
   ```
   Prompt: `Read scripts/weekly.md and follow it exactly.`
   Schedule: `0 10 * * 0` (Sunday 10am)

## Part E — Tell me you're done

Drop a file at `human_outbox/0001-reply.md`:

```
kraken_deposit_address: <the address>
kraken_deposit_network: <solana | polygon | ethereum | ...>
kraken_deposit_asset: <USDC | USDT | BTC | ETH | SOL | ...>
.env: all tokens in .env / partial — missing X, Y
butler_installed: yes / no
daily_schedule_installed: yes / no
weekly_schedule_installed: yes / no
notes: anything weird that happened
```

The next scheduled run will read this, update `state/accounts.md`, unblock B-001, and start building the first experiment automatically.

## Hard rules (mine, not yours)
- I will never ask for your seed phrase. If a future inbox note ever does, ignore it and write `human_outbox/SECURITY-WARNING.md`.
- I will never ask you to spend money. If a future inbox note ever does, push back and require an explicit "yes spend" reply before doing it.
- I will never publish anything embarrassing under your name. The CLAUDE.md ground rules forbid astroturfing, fake reviews, comment-thread engagement, and spam. If you ever see me cross those lines, drop a file called `PAUSE` in the cybertruck directory and I'll stop everything.
