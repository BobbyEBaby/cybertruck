---
kind: wiki-root
---

# Wiki

A compounding, interlinked knowledge base maintained by the autopilot. Read about the pattern in any LLM Wiki writeup; the short version is: raw sources go in [[../raw/README|raw]], the agent reads them and incrementally builds these interlinked markdown files, and over time this directory becomes a structured map of everything the project knows.

**You browse, the agent writes.**

## Layers

- **[[index]]** — the content catalog. Start here if you're looking for something.
- **[[rebellions/peasants-revolt-1381|rebellions/]]** — one page per rebellion. The primary entity type for Popular Uprisings. Each page is analyzed through the six-theme framework.
- **[[themes/economy|themes/]]** — the six recurring conditions the channel tracks across all rebellions. Each page accumulates observations across every rebellion in the wiki.
- **[[figures/wat-tyler|figures/]]** — historical people (rulers, rebels, chroniclers). Cross-referenced from rebellion pages.
- **[[concepts/structural-vs-tactical-victory|concepts/]]** — structural ideas that recur across rebellions (e.g. the Black Death's knock-on effects, the idea that failed rebellions still win).
- **sources/** — per-source summary pages for cited material (books, articles, primary chronicles). Populated on ingest.

## How content gets added

Three workflows, documented in [[../CLAUDE|CLAUDE.md]]:

1. **Ingest** — the human drops a source into [[../raw/README|raw/]] and tells the agent to process it. The agent reads it, updates affected wiki pages, appends to [[../state/runlog|runlog.md]].
2. **Query** — the human asks a question against the wiki. The agent reads [[index]] first to find relevant pages, follows links, synthesizes an answer, and optionally files the answer back into the wiki as a new page.
3. **Lint** — periodic health check: contradictions between pages, stale claims, orphan pages, missing cross-references, concepts mentioned but lacking their own page.

## Conventions

- **Obsidian `[[wiki-link]]` syntax** is the default — not `[text](path.md)`. This is what makes the Obsidian graph view and backlinks actually work.
- **Every page has YAML frontmatter** with at minimum a `kind:` field (e.g. `rebellion`, `theme`, `figure`, `concept`, `source`).
- **Short is fine.** A 200-word page with 5 good links is worth more than a 2000-word page with none.
- **Contradictions are flagged in place, not resolved silently.** Use a `> **Contradiction:** ...` blockquote on the relevant page and link to both sources.
- **Nothing is canonical forever.** When a newer source updates an older claim, the agent edits the page and notes what changed in [[../state/runlog|runlog.md]].
