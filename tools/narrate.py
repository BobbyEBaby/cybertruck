#!/usr/bin/env python3
"""tools/narrate.py — multi-voice Edge TTS narrator for Popular Uprisings episodes.

Usage:
    python tools/narrate.py <video-slug>

Reads the spoken body of an episode script (## Script + ## Thematic analysis
+ ## Why it matters now sections; skips metadata sections like theme
intensities and Pollinations prompts), strips [HUMAN_*] markers, splits
into logical segments by section/paragraph cluster, generates per-segment
MP3s with rotating voices to create tonal variation (hedge against the
'flat TTS' inauthentic-content signal), and writes segments.json.

Voice rotation:
    narrator   = en-US-GuyNeural      (warm male baritone, default)
    thematic   = en-US-JennyNeural    (clear female, used for analysis)
    outro      = en-US-AriaNeural     (distinct female, used for outro/CTA)
"""

from __future__ import annotations

import asyncio
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "experiments" / "youtube-history-channel" / "scripts"
ASSETS_DIR = ROOT / "experiments" / "youtube-history-channel" / "assets"

# Sections of the script that are spoken narration (in order).
# Any other ## section is treated as metadata and skipped.
SPOKEN_SECTIONS = [
    "Script",
    "Thematic analysis",
    "Why it matters now",
    "Why it matters",
    "Outro",
]

# Sections explicitly skipped (metadata for the pipeline, not spoken).
SKIP_SECTIONS = [
    "Theme intensities",
    "Pollinations prompts",
    "Sources",
    "Beat map",
    "Status",
    "Why this topic first",
    "Must-cite facts",
    "Hard no's",
    "Metrics to track",
]

VOICE_NARRATOR = "en-GB-RyanNeural"   # older British gentleman, thoughtful
VOICE_THEMATIC = "en-GB-RyanNeural"   # same voice for narrative cohesion
VOICE_OUTRO = "en-GB-RyanNeural"      # same voice for consistency
# Slow pace + natural intonation. -15% rate creates a thoughtful cadence
# without being ponderous. Edge TTS honors punctuation for pauses, and
# the script uses em-dashes, ellipses, and short sentences for additional
# natural phrasing breaks.
NARRATION_RATE = "-15%"
NARRATION_PITCH = "-2Hz"  # slightly lower pitch for older-gentleman feel


def find_script(slug: str) -> Path:
    candidates = list(SCRIPTS_DIR.glob(f"*{slug}*.md"))
    if not candidates:
        sys.exit(f"error: no script for '{slug}' in {SCRIPTS_DIR}")
    if len(candidates) > 1:
        sys.exit(f"error: multiple candidates: {candidates}")
    return candidates[0]


def strip_markers_and_comments(text: str) -> str:
    # Strip HTML comments (used for inline source citations)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Strip [HUMAN_*] markers entirely — they indicate voice changes
    # but for now we route everything through TTS with section-based
    # voice rotation instead of per-marker voice assignment
    text = re.sub(r"\[HUMAN_[A-Z_]*\]", "", text)
    # Strip markdown headers at ANY level — TTS engines read literal "#"
    # as "hash hash hash" which is obviously wrong. Drop entire header
    # lines so section titles don't get read at all. Critical bug fix
    # after v3 XTTS upload had the narrator saying "hash hash hash
    # introduction" out loud.
    text = re.sub(r"^#+\s+.*$", "", text, flags=re.MULTILINE)
    # Strip bold/italic markdown so TTS doesn't say "star star"
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    # Strip markdown link syntax: [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    # Strip Obsidian wiki-link syntax: [[target|text]] -> text, [[target]] -> target
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    # Collapse multiple blank lines that header stripping may have left
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def parse_sections(script_text: str) -> list[tuple[str, str]]:
    """Return list of (section_title, body) for each ## section."""
    # Strip frontmatter
    script_text = re.sub(r"^---\n.*?\n---\n", "", script_text, count=1, flags=re.DOTALL)
    # Strip the # top-level title (episode title)
    script_text = re.sub(r"^#\s+.*?\n", "", script_text, count=1)

    sections: list[tuple[str, str]] = []
    # Find all ## headers and their bodies
    pattern = re.compile(r"^##\s+(.+?)\n(.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
    for m in pattern.finditer(script_text):
        title = m.group(1).strip()
        body = m.group(2).strip()
        sections.append((title, body))
    return sections


def section_kind(title: str) -> str | None:
    """Return 'narrator' | 'thematic' | 'outro' | None (skip)."""
    t = title.lower()
    for spoken in SPOKEN_SECTIONS:
        if spoken.lower() in t:
            if "thematic" in t:
                return "thematic"
            if "matters" in t or "outro" in t:
                return "outro"
            return "narrator"
    return None  # metadata section, skip


def split_into_chunks(body: str, max_chars: int = 1800) -> list[str]:
    """Split a long section body into narration-friendly chunks at
    paragraph boundaries, targeting up to max_chars per chunk (Edge TTS
    handles longer but shorter chunks give cleaner pacing and can be
    mixed back together with fewer artifacts)."""
    paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    for p in paragraphs:
        plen = len(p)
        if current and current_len + plen > max_chars:
            chunks.append("\n\n".join(current))
            current = [p]
            current_len = plen
        else:
            current.append(p)
            current_len += plen + 2
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def build_segment_plan(script_text: str) -> list[dict]:
    """Return ordered list of {index, role, voice, text} segments."""
    sections = parse_sections(script_text)
    plan: list[dict] = []
    for title, body in sections:
        kind = section_kind(title)
        if kind is None:
            continue
        body = strip_markers_and_comments(body)
        body = body.strip()
        if not body:
            continue
        chunks = split_into_chunks(body)
        for chunk in chunks:
            chunk = chunk.strip()
            if not chunk:
                continue
            if kind == "thematic":
                voice = VOICE_THEMATIC
            elif kind == "outro":
                voice = VOICE_OUTRO
            else:
                voice = VOICE_NARRATOR
            plan.append({
                "section": title,
                "role": kind,
                "voice": voice,
                "text": chunk,
            })
    # Assign indexes
    for i, seg in enumerate(plan, 1):
        seg["index"] = i
    return plan


async def synthesize(text: str, voice: str, out_path: Path) -> None:
    import edge_tts  # type: ignore
    communicate = edge_tts.Communicate(
        text, voice, rate=NARRATION_RATE, pitch=NARRATION_PITCH
    )
    await communicate.save(str(out_path))


async def run_plan(plan: list[dict], out_dir: Path) -> list[dict]:
    manifest: list[dict] = []
    for seg in plan:
        idx = seg["index"]
        role = seg["role"]
        voice = seg["voice"]
        filename = f"segment_{idx:02d}_{role}.mp3"
        out_path = out_dir / filename
        char_count = len(seg["text"])
        print(f"  [{idx:02d}] {role:<10} voice={voice} section={seg['section'][:30]!r} ({char_count} chars)")
        await synthesize(seg["text"], voice, out_path)
        manifest.append({
            "index": idx,
            "role": role,
            "voice": voice,
            "section": seg["section"],
            "file": filename,
            "char_count": char_count,
        })
    return manifest


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: narrate.py <video-slug>")
    slug = sys.argv[1]

    script_path = find_script(slug)
    plan = build_segment_plan(script_path.read_text(encoding="utf-8"))
    if not plan:
        sys.exit("error: no spoken sections found")

    out_dir = ASSETS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    # Wipe prior segment files so old broken ones don't confuse the renderer
    for old in out_dir.glob("segment_*.mp3"):
        old.unlink()

    print(f"Script: {script_path.name}")
    print(f"Segments in plan: {len(plan)}")
    print(f"Output dir: {out_dir}\n")

    manifest = asyncio.run(run_plan(plan, out_dir))

    segments_json = out_dir / "segments.json"
    segments_json.write_text(
        json.dumps({
            "slug": slug,
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "segments": manifest,
        }, indent=2),
        encoding="utf-8",
    )
    print(f"\nmanifest: {segments_json}")
    print(f"segments written: {len(manifest)}")


if __name__ == "__main__":
    main()
