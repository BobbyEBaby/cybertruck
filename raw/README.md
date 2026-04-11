---
kind: raw-root
---

# raw/

Immutable raw sources ingested into the wiki. The agent reads from this directory but never modifies anything in it. This is the source-of-truth layer.

## What goes here

- Articles (PDFs, HTML, plain text)
- Academic papers
- Book chapter notes (yours, or OCR/copy)
- Podcast transcripts
- Primary source chronicles (public domain, no copyright issues)
- Interview notes
- Lecture notes
- Any other source material you want compiled into the [[../wiki/index|wiki]]

## How to ingest

1. Drop the file into `raw/` (subdirectories OK — organize by topic, date, or type, whatever makes sense to you).
2. In your local Claude Code session, tell the agent: *"ingest raw/<filename>"* or *"process the new source in raw/"*.
3. The agent will:
   - Read the source
   - Discuss key takeaways with you (optional — you can also say "ingest silently")
   - Write a source summary page in `../wiki/sources/`
   - Update affected wiki pages (entities, concepts, themes)
   - Update `../wiki/index.md`
   - Append an entry to `../state/runlog.md`

## Conventions

- **File names are stable** once ingested. The wiki source pages reference them by name; renaming breaks the links.
- **Copyrighted material** is fine to keep locally (fair use) but the repo is **public**, so anything committed here is public. If a source is copyrighted and shouldn't be public, add the filename to `.gitignore` before committing.
- **Large files** (multi-MB PDFs, video files): consider adding to `.gitignore` if they'd bloat the repo. The agent can still read local files during ingest even if they're not committed.
- **No private thoughts here.** This folder is for source material, not your journal. If you want a private thinking space, that's a separate concern and we can add one.

## Status

_(no sources ingested yet — this folder is empty)_
