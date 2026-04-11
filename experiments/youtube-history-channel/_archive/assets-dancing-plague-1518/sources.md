---
episode: 01-dancing-plague-1518
title: "The Dancing Plague of 1518"
sourced_on: 2026-04-11
sourced_by: remote run #10 (Opus)
sourced_via: WebSearch + Wikimedia Commons category browsing (no files downloaded this run — remote sandbox is network-read-only for arbitrary file downloads; see "How to use this file" below for the local-run handoff)
image_count_target: 20
image_count_recorded: 22
licenses_used: public-domain-old (PD-old-100, PD-US, PD-Art), CC0
---

# Public-domain image sources for episode 1 — The Dancing Plague of 1518

## Purpose
This file maps every beat of `scripts/01-dancing-plague-1518.md` to 1–3 candidate **public-domain images** hosted on Wikimedia Commons, the Library of Congress Free to Use and Reuse collection, the Internet Archive, and the Public Domain Review. It is the input that `tools/source_images.py` (B-013) or a local-run agent should use to actually **download** the image files into this directory before `tools/render_video.py` (B-015) runs.

## How to use this file
1. For each numbered entry, resolve the **File page URL** on Wikimedia Commons (or LoC / Archive.org).
2. On the file page, right-click the original-resolution image and save to `experiments/youtube-history-channel/assets/dancing-plague-1518/NN-<short-slug>.<ext>` where `NN` matches the numbering below.
3. If a specific numbered file page is unresolvable (link rot / rename), fall back to the **Category URL** and pick a comparable image from that category — all images in the listed categories are either PD-old-100, PD-US, or PD-Art. If a CC-BY image is substituted, add a line to the attribution block below. **Never substitute a file without a clear public-domain or CC-BY license tag.**
4. After downloading, append the actual chosen filename + resolution + exact license tag to the "Downloaded files" table at the bottom.
5. `render_video.py` reads this file's front matter and downloaded-files table; the storyboard manifest then picks from the downloaded files by slug.

## Licensing note (copy-paste for YouTube description credits)
All 20+ images used in this episode are in the public domain under one of:
- **PD-old-100** (author died more than 100 years ago) — applies to all 16th–17th-century engravings and woodcuts.
- **PD-Art** (Bridgeman v. Corel — faithful photographic reproductions of PD works are themselves PD in the U.S.) — applies to museum scans of the above.
- **PD-US** (published in the U.S. before 1929) — applies to Wellcome L-series scans republished via Wikimedia.
- **CC0** (public domain dedication) — applies to LoC Free to Use & Reuse set.

No image in this list is fair-use, watermarked commercial stock, or AI-generated. Per CLAUDE.md and the binding constraints from `research/markets/06-faceless-youtube.md` (faceless-YouTube refresh 2026-04-11), **no AI-generated historical visuals are allowed in this production**.

---

## Image candidates by script beat

Map each image to a target duration range in the script. Runtime numbers match the beat map in `01-dancing-plague-1518.md`.

### A. `[HUMAN_INTRO]` (0:00–0:13) — title card / establishing shot
Visual treatment (from production-pipeline storyboard): **static-with-text-overlay**.

1. **Matthäus Merian — Strasbourg panoramic view** (c. 1644, copper engraving from *Topographia Alsatiae*)
   - Artist: Matthäus Merian the Elder (1593–1650)
   - Source: Wikimedia Commons, Category:Topographia_Alsatiae_(Merian) — 232 files total
   - Category URL: https://commons.wikimedia.org/wiki/Category:Topographia_Alsatiae_(Merian)
   - Specific candidate file: https://commons.wikimedia.org/wiki/File:Topographia_Alsatiae_(Merian)_081.jpg
   - License: PD-old-100
   - Notes: Merian's Strasbourg views are the canonical "this is how Strasbourg looked in the early-modern period" images. Filmable at 4K from Wikimedia.

### B. Hook (0:13–0:33) — the dancing itself
Visual treatment: **Ken Burns pan/zoom** (single hero image, slow zoom on the central dancing figures).

2. **Hendrik Hondius — "Dancing mania on a pilgrimage to the church at Sint-Jans-Molenbeek"** ⭐ PRIMARY
   - Artist: Hendrik Hondius the Elder (1573–1650), engraved in 1642 **after** a 1564 drawing by Pieter Bruegel the Elder
   - Source: Wikimedia Commons, Category:Dancing_mania (also indexed under Category:Hendrik_Hondius_I)
   - Category URL: https://commons.wikimedia.org/wiki/Category:Dancing_mania
   - License: PD-old-100 (1642 engraving, 1564 original drawing — both authors died >100 years ago)
   - Notes: **This is the canonical dancing-plague image** used in virtually every academic write-up (Waller 2008, Public Domain Review essay, Wikipedia's own article). Hero image for the whole episode.

3. **Pieter Bruegel the Younger — "A depiction of dancing mania, on the pilgrimage of epileptics to the church at Molenbeek"** (painting, c. 1564 after elder's drawings)
   - Artist: Pieter Brueghel the Younger (1564–1638)
   - Source: Wikimedia Commons (search "Dancing mania Brueghel the Younger")
   - License: PD-old-100 (PD-Art for the museum scan)
   - Notes: Use as a color/secondary variant if the Hondius engraving reads too dark on a smartphone thumbnail.

### C. Context (0:33–1:42) — Strasbourg in 1518
Visual treatment: **mixed** — one Ken Burns over a city view, two static-with-text overlays for dates/place names.

4. **Sebastian Münster's *Cosmographia* — Strasbourg woodcut view** (1544 / 1550 editions)
   - Artist: Sebastian Münster (1488–1552), woodcutters incl. Hans Rudolf Manuel Deutsch
   - Source: Wikimedia Commons, Category:Illustrations_of_Cosmographia_(Münster) — 214 files
   - Category URL: https://commons.wikimedia.org/wiki/Category:Illustrations_of_Cosmographia_(M%C3%BCnster)
   - Alternative full-book scan (for finding the exact Strasbourg plate): Internet Archive `https://archive.org/details/cosmographiabesc00muns`
   - License: PD-old-100
   - Notes: Münster's Cosmographia is the contemporaneous German-language atlas and its Strasbourg city-view woodcut is period-correct for 1518.

5. **Strasbourg Cathedral interior/exterior — medieval views from Wikimedia Commons**
   - Source: Wikimedia Commons, Category:Cathédrale_Notre-Dame_de_Strasbourg ("Historic views" section includes Merian 1644 and 1663 engravings)
   - Category URL: https://commons.wikimedia.org/wiki/Category:Cath%C3%A9drale_Notre-Dame_de_Strasbourg
   - License: PD-old-100 for all pre-1900 engravings
   - Notes: Establish place. Strasbourg Cathedral was the tallest building in Europe in 1518 — a visual anchor the viewer will recognize.

6. **"Famine and peasant hardship" — Hans Holbein / David Kandel woodcut** (first half of 16th c.)
   - Source: Wikimedia Commons — Category:Woodcuts_by_Hans_Holbein_the_Younger OR the Münster Cosmographia category above (David Kandel's peasant vignettes)
   - License: PD-old-100
   - Notes: Period-correct visualization of the 1517 famine year that the script cites.

### D. Beat 1 — Frau Troffea (1:42–3:18)
Visual treatment: **mixed** — one Ken Burns on Frau Troffea figure interpretation, one static-with-text for the growth-numbers overlay, one side-by-side (single → crowd).

7. **Hondius 1642 engraving — crop on the lead female dancer** (same file as #2 above, cropped)
   - Re-use file from entry #2. `render_video.py` can zoom into the central female figure as a "Frau Troffea" interpretive shot. Inline on-screen text should say: *"Interpretation: Frau Troffea as imagined by Bruegel and Hondius — no contemporary portrait exists."* — **be honest that this is an interpretation, not a likeness.**

8. **Strasbourg city council chronicle — 16th-century manuscript page**
   - Source: Wikimedia Commons, Category:Medieval_manuscripts (filter to "Strasbourg" or "Alsace")
   - Alternative: Public Domain Review — https://publicdomainreview.org/essay/the-dancing-plague-of-1518 — which reproduces the Strasbourg chronicle pages.
   - License: PD-old-100
   - Notes: Static shot with an on-screen callout: *"Strasbourg city council minutes, summer 1518"*. Grounds the "we know this happened because" argument visually.

9. **16th-century woodcut crowd scene** (for the "~30 in the first week, ~400 by end of month" growth beat)
   - Source: Wikimedia Commons, Category:16th-century_woodcuts (search "crowd", "peasants", "dance")
   - License: PD-old-100
   - Notes: Mass-of-people visual. On-screen overlay: *"End of first week: ~30. End of first month: ~400."*

### E. Beat 2 — Council response (3:36–5:02)
Visual treatment: **mixed** — one Ken Burns, one static-with-text-overlay for the "clear the guild halls, build a stage, hire musicians" beat, one side-by-side comparison.

10. **16th-century guild hall interior / market building**
    - Source: Wikimedia Commons, Category:Guild_halls — pre-1800 engravings + Category:Sebastian_Münster_engravings
    - License: PD-old-100
    - Notes: Establish the physical setting where the dancers were gathered.

11. **Medieval / early-modern musicians (drums, horns, pipes)**
    - Source: Wikimedia Commons, Category:Medieval_musicians OR Category:Renaissance_musicians (woodcuts + manuscript illuminations)
    - License: PD-old-100
    - Notes: The script says the council "hired pipers and drummers and horn players" — we need a period-correct image of those instruments. Holbein's *Dance of Death* contains several useful woodcuts of musicians.

12. **Hans Holbein the Younger — *Dance of Death* series, "The Musician" or "The Countess"** (1538 first publication, designed 1523–1525)
    - Artist: Hans Holbein the Younger (1497/8–1543), engraved by Hans Lützelburger
    - Source: Wikimedia Commons, Category:Danse_Macabre_(Holbein) — the 41-woodcut series is fully public domain
    - Category URL: https://commons.wikimedia.org/wiki/Category:Danse_Macabre_(Holbein)
    - Public Domain Review collection page: https://publicdomainreview.org/collection/hans-holbeins-dance-of-death-1523-5
    - License: PD-old-100
    - Notes: Thematically aligned ("dancing → death" visual rhyme), period-correct (1520s, same decade as the plague), and one of the highest-resolution PD woodcut sets available. Use 2 plates total across beats 2 and 3.

13. **Collapsing dancer / exhausted figure** (for the "men hired to hold collapsing dancers upright" line)
    - Source: Wikimedia Commons, Category:Dancing_mania (rarer) OR crop from the Hondius engraving (#2)
    - License: PD-old-100

### F. Beat 3 — Pilgrimage to the Saint Vitus shrine (5:20–6:32)
Visual treatment: **mixed** — one Ken Burns over pilgrimage imagery, one static-with-text for the "red shoes / holy water / Latin prayers" ritual beats, one static map/timeline.

14. **Saint Vitus — medieval/Renaissance altarpiece or panel painting**
    - Source: Wikimedia Commons, Category:Paintings_of_Saint_Vitus
    - Category URL: https://commons.wikimedia.org/wiki/Category:Paintings_of_Saint_Vitus
    - License: PD-old-100 / PD-Art
    - Notes: Hero image of the saint the pilgrims were travelling to. Pick one with clear iconography (boy with palm branch, cauldron, rooster — standard Vitus attributes per the christianiconography.info reference at https://www.christianiconography.info/vitus.html).

15. **Martyrdom of Saint Vitus — woodcut or engraving**
    - Source: Wikimedia Commons, Category:Martyrdom_of_Saint_Vitus — 49 files, includes "German Martyrdom of Saint Vitus.jpg" and multiple PD woodcuts
    - Category URL: https://commons.wikimedia.org/wiki/Category:Martyrdom_of_Saint_Vitus
    - License: PD-old-100
    - Notes: Grounds the religious authority the shrine carried for a 1518 Strasbourger.

16. **Saverne / Zabern village 17th-century view** (the shrine was in the hills above Saverne)
    - Source: Wikimedia Commons, Category:Topographia_Alsatiae_(Merian) — includes Saverne view
    - License: PD-old-100
    - Notes: Physical location. Static-with-on-screen-text: *"The Saint Vitus shrine stood in the hills above Saverne."*

17. **Medieval/early-modern pilgrim procession**
    - Source: Wikimedia Commons, Category:Pilgrimages_in_art (pre-1800 prints only)
    - Alternative: Flickr Commons via Library of Congress — https://www.flickr.com/commons — search "pilgrimage engraving"
    - License: PD-old-100
    - Notes: For the red-shoes / ritual beat.

### G. Why it matters (6:50–7:50) — three theories
Visual treatment: **static-with-text-overlay** (each theory gets its own labeled card).

18. **Ergot / Claviceps purpurea botanical illustration** (for the ergot theory)
    - Source: Wikimedia Commons, Category:Claviceps_purpurea_-_botanical_illustrations
    - Known specific file: *First illustration of rye infected by ergot Wellcome L0002215.jpg* (Wellcome Collection, PD-US)
    - Category URL: https://commons.wikimedia.org/wiki/Category:Claviceps_purpurea_-_botanical_illustrations
    - License: PD-Art / PD-US (Wellcome L-series releases)
    - Notes: Pair with on-screen text: *"Theory 1: ergot poisoning. Waller 2008 rejects — no gangrene reports in Strasbourg records; the other known dancing epidemics weren't in rye-eating regions."*

19. **19th-century medical illustration of brain/nervous-system — for mass psychogenic illness**
    - Source: Wikimedia Commons, Category:19th-century_anatomical_illustrations OR Library of Congress Free to Use — https://www.loc.gov/free-to-use/
    - License: PD-old-100 / CC0
    - Notes: On-screen text: *"Theory 2: mass psychogenic illness. Waller's preferred reading: extreme social stress + pre-existing belief in Saint Vitus' power = real, involuntary, contagious motor symptoms."*

20. **Religious trance / ecstatic worship — medieval manuscript illumination**
    - Source: Wikimedia Commons, Category:Medieval_illuminated_manuscripts (filter for ecstatic/trance/religious-dance imagery) OR New York Public Library Digital Collections — https://digitalcollections.nypl.org
    - License: PD-old-100
    - Notes: On-screen text: *"Theory 3: religious trance state (Dance Research 2017). A recognized cross-cultural phenomenon in pre-modern religious crowds."*

### H. `[HUMAN_OUTRO]` (final 60 seconds) — book rec + CTA card
Visual treatment: **static-with-text-overlay**.

21. **John Waller's *A Time to Dance, a Time to Die* (2008) book cover** — use only the book's **cover image** if it's reproducible under fair-use; otherwise substitute a simple text card ("Further reading: John Waller, *A Time to Dance, a Time to Die* (2008); Waller, *The Lancet* 2009 — free online") as the safer PD path.
    - **DO NOT** scrape the publisher's cover image. If we cannot find a PD or CC-licensed cover photograph, ship the plain text card instead. Fair-use is defensible but the faceless-YouTube refresh constraints say we avoid any ambiguity that could trigger the inauthentic-content filter.
    - License: **PREFER plain-text card** — see above.

22. **Ko-fi / Buy Me a Coffee support card** — **plain text only** (agent-generated text card, not an image scrape). Per `video-description-template.md`, episode 1 rotates **Ko-fi** as the primary tip rail. Final on-screen text:
    *"If this was worth your time: ko-fi.com/<TBD>"* (Ko-fi handle pending `human_inbox/0003-youtube-api-and-tips-setup.md` reply).

---

## Downloaded files

Fill this table when images are actually downloaded. Until then, this episode is **sourced but not downloaded** — it cannot be rendered by `tools/render_video.py` yet.

| # | Local filename | Resolution | License | Source URL | Attribution string |
|---|---|---|---|---|---|
| 1 | _(pending)_ | | | | |

## Provenance and integrity rules
- **Never** add an image to this table without a verifiable source URL that a human can click and confirm the license.
- **Never** re-license an image — if the source tags it CC-BY, it stays CC-BY and we include the byline in the video description.
- **Never** substitute an AI-generated image for a missing source. Ship the episode with fewer images instead.
- The `sources_verified_by` line in the manifest must name the specific remote run (or local run) that did the verification. Running `tools/source_images.py` overwrites it; manual downloads must preserve it.

## Remote sandbox limitations (why this file exists instead of downloaded JPGs)
This episode's images were **identified** in remote run #10 (Opus, 2026-04-11) via WebSearch-only reconnaissance. The remote sandbox could not:
- Reach Wikimedia Commons file pages via WebFetch (403 on the commons.wikimedia.org paths) — only category-level and Wikipedia-article-level pages were readable.
- Write arbitrary network downloads to `experiments/youtube-history-channel/assets/dancing-plague-1518/`.
So the artifact this run produces is the **source list with full attribution**, not the image binaries. The next remote or local run that picks up B-013 (`tools/source_images.py`) or the local-run agent should use this file as the download target list. See `state/backlog.md` B-013 and B-017 entries for handoff.

## Hard no's — compliance re-check (matches script file)
- [x] No AI-generated historical visuals (CLAUDE.md + 06-faceless-youtube refresh).
- [x] No copyrighted stock imagery (Getty / Shutterstock / Alamy / Adobe Stock).
- [x] No unlicensed Google Image Search grabs.
- [x] Every proposed image is PD-old-100, PD-Art, PD-US, or CC0.
- [x] No "Frau Troffea portrait" — no such contemporary portrait exists; the script and sources explicitly label the Bruegel/Hondius figure as an interpretation, not a likeness.
- [x] Waller book cover path is the plain-text safer option, not a scrape.
