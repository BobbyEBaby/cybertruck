# External accounts

Public identifiers only. **No passwords, API keys, or tokens.** If you (the user) accidentally paste a secret here, the agent will redact it and notify you.

When you create an account, add a row here so the agent knows it can ship to that platform.

## Format
```
- platform: <name>            e.g. itch.io
  username: <public handle>   e.g. robert-evans
  profile_url: <full url>
  payout_method: <e.g. PayPal, Stripe, set up>
  notes: <anything the agent should know — region, payout threshold, etc.>
```

## Money destination
- **exchange:** Kraken (Robert's existing account)
- **custody model:** custodial (Kraken). Migrate to self-custody (B-007) once balance ≥ $5,000.

### Deposit addresses (provided by user 2026-04-10)
| Asset | Address | Network | Min deposit | Notes |
|---|---|---|---|---|
| BTC | `3JiaPsUmdf2pqXFrDavzQ4fRpkJSVg5BbH` | Bitcoin mainnet | 0.0001 BTC (~$6–10) | High network fees; not viable for payouts under ~$15 |
| ZEC | `t1fsoScTMB1ERNjVrsS1CpvrVYLVzSECHSc` | Zcash transparent (t-addr) | 0.005 ZEC (~$0.10–0.20) | Low minimum; fewer platforms support direct ZEC payouts |
| DOGE | `DUJPtjifrXtiykXcN389Gw36g5T9ZpWvgZ` | Dogecoin | 1 DOGE (~$0.10–0.30) | Low minimum, low fees, widely accepted as tip currency |
| BCH | `bitcoincash:pppf2wmxxlgt9stc4ch24v92n9w7gd4g0unvfdxlup` | Bitcoin Cash | 0.0006 BCH (~$0.20–0.30) | Low minimum, low fees |
| SOL  | `EQwtTPe3GfcAGAiQAh3AxmCZ1WAyCviDsNnBmfCaQwf7` | Solana | 0.01 SOL (~$1–2) | Same address as BONK and (provisionally) USDC-Solana — Kraken assigns one Solana address per account that handles SOL native and all SPL tokens. Network identifies asset by token mint. |
| BONK | `EQwtTPe3GfcAGAiQAh3AxmCZ1WAyCviDsNnBmfCaQwf7` | Solana (SPL) | 42,000 BONK (~$0.50–1) | Same as SOL address. Meme token; high volatility makes it bad for *savings* but fine as a Solana-network on-ramp where supported |
| SHIB | `0xA306055520BE052045F49F4C57f26C6dD40a8DB8` | Ethereum (ERC-20) | 373,000 SHIB (~$4–8) | Meme token; **avoid** for small payouts because Ethereum gas fees can exceed the payout itself |
| XRP  | `rLHzPsX6oXkzU2qL12kHCH8G8cnZv1rBJh` **+ destination tag `2272490000`** | XRP Ledger | 0.0001 XRP | **Best for tiny micropayouts.** Very low fees, fast settlement. **CRITICAL:** XRP requires BOTH the address AND the destination tag — sending without the tag = funds lost or held by Kraken support indefinitely. Any tool that uses this address must transmit the tag with every payment. |
| TRX  | `TFYFeQt9jGv7CM1X64GnZtZuZj7cGMjcC6` | Tron | 25 TRX (~$3–5) | Low fees. Note: this address is tagged for TRX only — sending USDT-TRC20 to it will not credit USDT. A separate USDT-Tron deposit address would be needed for stablecoin payouts on Tron. |
| **USDC (Solana)** ⭐ | `EQwtTPe3GfcAGAiQAh3AxmCZ1WAyCviDsNnBmfCaQwf7` | Solana (SPL) | 0.4 USDC (~$0.40) | **PRIMARY SAVINGS RAIL.** Confirmed 2026-04-10. Dollar-stable, sub-cent fees, $0.40 minimum. This is the canonical destination — every payout route should aim here unless a platform genuinely cannot send USDC-SPL. |

Authoritative copy lives in `.env` (gitignored). The table above is for human reference only.

### Routing rule (for the agent)
When proposing a payout method via inbox, prefer in order:
1. **USDC on Solana** ⭐ — confirmed primary rail, $0.40 minimum, dollar-stable, sub-cent fees. **Default to this unless impossible.**
2. **SOL native** — sub-cent fees, fast settlement, but volatile (auto-convert to USDC inside Kraken on arrival if used)
3. **XRP** — best for tiny micropayouts; **MUST include destination tag `2272490000`**
4. **DOGE** — widely accepted, very low minimum, low fees
5. **TRX** — low fees, $3–5 minimum, decent platform support
6. **ZEC** — low minimum, narrower platform support
7. **BCH** — low minimum, decent platform support
8. **BONK / SHIB** — only if a platform pays in these directly; otherwise skip (volatile meme tokens, bad savings vehicles, and SHIB on Ethereum has crippling gas fees)
9. **BTC** — only if the payout is ≥ ~$20 to clear minimum + network fees
10. **Otherwise** — accumulate in fiat at the source platform until it crosses a usable threshold

### XRP destination tag warning (read this every time)
The XRP address is shared across many Kraken users. The destination tag `2272490000` is what tells Kraken which user the deposit belongs to. **Sending XRP without the tag = funds credited to the wrong account or held indefinitely.** Any payout configuration involving XRP must transmit the tag. If a platform's payout form has no destination-tag field, **do not use XRP from that platform.**

## Active accounts
_(none yet — see human_inbox/0001-setup.md)_

## Suggested first accounts to create (zero-cost, no card required)
- itch.io — host free or paid web games / digital downloads
- Gumroad — sell digital downloads (free tier, no monthly fee)
- GitHub — host source + free static sites via GitHub Pages
- Reddit — organic distribution, market research
- An email used only for these signups (Gmail/Proton)
- PayPal — needed by most payout flows above
- **Ko-fi** (0% fee tip rail) — https://ko-fi.com/
- **Buy Me a Coffee** (5% fee tip rail, wider audience) — https://buymeacoffee.com/

## YouTube
- **Channel URL:** https://studio.youtube.com/channel/UCv8vMc6ZN9Tkc0K5gx53iAA
- **Channel ID:** UCv8vMc6ZN9Tkc0K5gx53iAA
- **Proposed brand name:** Margins of History (niche: obscure/forgotten history)
- **Needed for automation:** YouTube Data API v3 OAuth refresh token in `.env` as `YOUTUBE_OAUTH_REFRESH_TOKEN`. Until set, uploads are manual drag-and-drop (~2 min/video). See experiments/youtube-history-channel/.
