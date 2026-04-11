# Cybertruck Autopilot

An autonomous research → build → ship → measure → iterate loop. Its stated goal is to generate enough zero-budget digital-product revenue to fund a Tesla Cybertruck ($100,000 USD) for its owner, starting from $0.

**Is it going to work?** Almost certainly not at that scale. The loop is designed with honest expectations baked in — see [`state/honest-expectations.md`](./state/honest-expectations.md) for the permanent reality check. The project is worth running because the engine itself is valuable: automated shots-on-goal, honest measurement, compounding learnings, and a public record of what worked and what didn't.

## How it works

- A scheduled [Claude Code](https://claude.com/claude-code) remote agent runs hourly.
- On each tick, it reads the state, picks the highest-priority unblocked task from [`state/backlog.md`](./state/backlog.md), executes one task, and writes an honest entry to [`state/runlog.md`](./state/runlog.md).
- Products are built in [`experiments/`](./experiments/) — each folder is one shot on goal.
- Remote runs do research and build. Credential-gated steps (publishing, crypto payouts, OAuth) happen locally when the owner opens Claude Code.
- All credentials live in a local `.env` file that is gitignored and never enters the repo.

## Live products (as of this commit)

| Product | Live URL | Backlog item |
|---|---|---|
| AI Prompt Cleaner | https://bobbyebaby.github.io/prompt-cleaner/ | B-001 |
| LLM API Cost Calculator | https://bobbyebaby.github.io/llm-cost-calculator/ | B-008 |
| Claude Code Power Prompts pack | built, awaiting upload | B-002 |
| YouTube history channel "Margins of History" | channel exists, scripting | B-012+ |

## Read the honest docs first

- [`CLAUDE.md`](./CLAUDE.md) — mission, ground rules, max-autonomy operating model
- [`state/honest-expectations.md`](./state/honest-expectations.md) — the permanent reality check
- [`state/runlog.md`](./state/runlog.md) — append-only log of every run, successes and failures
- [`state/backlog.md`](./state/backlog.md) — ranked tasks the loop is working through
- [`research/markets/`](./research/markets/) — scored zero-budget monetization opportunities
- [`scripts/daily-remote.md`](./scripts/daily-remote.md) — the exact prompt the scheduled agent runs
- [`experiments/`](./experiments/) — what the loop has actually built

## Ground rules (from CLAUDE.md, abbreviated)

- **$0 budget.** No spend without explicit owner approval.
- **Honest runlog.** Failures recorded as failures. No theatrical optimism.
- **No fake engagement.** No astroturfing, no fake reviews, no multiple accounts, no comment-thread wars.
- **Rate-limited.** Max 1 publication per platform per 24 hours.
- **Circuit breaker.** 3 consecutive zero-engagement ships in a category = stop shipping in that category until a strategic review.
- **Never touch the owner's wallet seed phrase or private keys.** The agent only knows public deposit addresses.
- **Pause switch.** A file named `PAUSE` in the repo root halts the next run immediately.

## Why this is open

The honest docs, the failures, the real revenue numbers (if any) — making them public is the point. Most side projects lie about their numbers. This one doesn't.

## License

Code in `experiments/` is MIT unless each experiment's README says otherwise. The operational docs, runlog, and research files are CC-BY-4.0 — share, remix, attribute.
