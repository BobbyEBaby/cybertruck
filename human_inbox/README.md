# human_inbox/

This is where the agent writes things it needs **you** (Robert) to do. Each note is a numbered file: `0001-setup.md`, `0002-...`, etc.

## How to use it
1. Read the lowest-numbered open note.
2. Do the steps it lists.
3. Drop a reply file in `human_outbox/` describing what you did. Anything works — `0001-reply.md`, `done.md`, `accounts-created.txt`. The next agent run will read it.
4. Once you've replied, you can leave the inbox file alone — the agent will move processed inbox notes to `human_inbox/processed/` after acknowledging your reply.

## Format of inbox notes
Each note has:
- **What** — the exact action you need to take
- **Why** — which task this unblocks
- **How to report back** — what to write in `human_outbox/`
- **Time estimate** — honest

## Hard rule
The agent will **never** ask you to spend money without flagging it loudly. If you see a money ask, double-check you actually want to do it before paying anything.
