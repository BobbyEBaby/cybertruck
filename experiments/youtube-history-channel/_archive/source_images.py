#!/usr/bin/env python3
"""ARCHIVED tool — not part of the current pipeline. See _archive/README.md.

Built in remote run #11 (Sonnet, 2026-04-11 14:20 UTC) against the
pre-pivot B-013 spec (LoC / Wikimedia Commons / Internet Archive public-domain
image sourcing for the Dancing Plague episode). Before the commit landed,
Robert pivoted the channel to rebellions-with-thematic-analysis and rewrote
B-013 to use Pollinations.ai AI generation instead. The Dancing Plague
script + its sources.md manifest are archived alongside this file.

Kept as reference because (a) the parser, license validator, and
attribution builder are cleanly factored and could seed a future Wikimedia
helper if the loop ever re-opens PD sourcing; (b) the runlog explicitly
records this work and deleting the artifact would make that entry
misleading; (c) the pivot's own archive README said "genuinely good work
that just happens to be off-theme."

source_images.py — download public-domain images listed in an episode's sources.md.

Reads an episode's `assets/<slug>/sources.md`, resolves each numbered image
candidate via the Wikimedia Commons MediaWiki API, validates the returned
license against a strict public-domain / Creative-Commons allowlist,
downloads the file next to the sources.md, and rewrites the "Downloaded
files" table at the bottom with verified attribution strings.

Usage
-----
    # default: episode slug under experiments/youtube-history-channel/assets/
    python3 tools/source_images.py dancing-plague-1518

    # full path to a sources.md (any location)
    python3 tools/source_images.py --sources-file path/to/sources.md

    # print the plan without touching the network or disk
    python3 tools/source_images.py dancing-plague-1518 --dry-run

    # verbose per-candidate logs
    python3 tools/source_images.py dancing-plague-1518 -v

Design notes
------------
- Input format is the structured markdown written by earlier remote runs.
  See experiments/youtube-history-channel/assets/dancing-plague-1518/sources.md
  for the canonical example.
- Only entries that give an explicit "Specific candidate file" URL on
  commons.wikimedia.org are resolved automatically. Category-only entries are
  flagged SKIPPED so a human can pick a specific file first; the tool never
  silently picks "whatever's in the category" — too easy to grab the wrong
  image.
- Items whose notes or license field say "plain text only" / "plain-text
  card" / "text card" are skipped with a clear note (these are meant to be
  rendered as on-screen text, not fetched).
- License validation is strict: an allowlist of PD/CC0/CC-BY* substrings and
  a denylist of fair-use / commercial-stock markers. A candidate whose
  extmetadata does NOT match the allowlist is treated as an error and the
  file is NOT downloaded.
- Idempotent: if the target filename already exists on disk, the download is
  skipped and the existing file is recorded in the table with `(exists)`.
- No credentials needed. Wikimedia Commons MediaWiki API is unauthenticated
  for the endpoints we use. .env is never read.
- Exits non-zero if any candidate produces an error. Partial success is
  logged but must be reviewed by a human — we do not want half-silent
  failures.

Hard-no rules (enforced)
------------------------
- No AI-generated images. We download what Wikimedia serves; we do not
  generate, upscale, or hallucinate.
- No license laundering. The LicenseShortName + Artist + Credit fields from
  extmetadata are copied verbatim into the attribution string.
- No fair-use ambiguity. Any license outside the allowlist is a hard error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Optional


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_EPISODE_PARENT = (
    REPO_ROOT / "experiments" / "youtube-history-channel" / "assets"
)

USER_AGENT = (
    "cybertruck-autopilot/0.1 "
    "(https://github.com/BobbyEBaby/cybertruck; research; no-contact)"
)

# License allow/deny lists. All entries are in the *normalized* form: lowercase
# with any run of whitespace / underscore / slash / hyphen collapsed to a
# single hyphen. License text is normalized the same way before matching so
# that "Public domain" / "public-domain" / "PUBLIC_DOMAIN" all match the
# same entry.
LICENSE_ALLOWLIST = (
    "public-domain",
    "pd-old",
    "pd-art",
    "pd-us",
    "pd-1923",
    "pd-self",
    "pd-us-expired",
    "cc0",
    "cc-zero",
    "cc-pd",
    "cc-by",  # also matches cc-by-sa, cc-by-2-0, etc. — attribution required
)

# License denylist. Overrides allowlist if matched — never accept these.
LICENSE_DENYLIST = (
    "fair-use",
    "non-free",
    "nd",  # no-derivatives clause (word-boundary matched below)
    "nc",  # non-commercial clause (word-boundary matched below)
    "getty",
    "shutterstock",
    "alamy",
    "adobe-stock",
    "copyrighted",
    "noncommercial",
    "no-derivatives",
)


# --- sources.md parser --------------------------------------------------------


@dataclass
class Candidate:
    number: int
    title: str
    section: str
    artist: Optional[str] = None
    source: Optional[str] = None
    category_url: Optional[str] = None
    file_url: Optional[str] = None
    license_claimed: Optional[str] = None
    notes: list[str] = field(default_factory=list)
    visual_treatment: Optional[str] = None
    plain_text_only: bool = False


@dataclass
class DownloadResult:
    candidate: Candidate
    status: str  # "downloaded" | "exists" | "skipped" | "error"
    local_filename: Optional[str] = None
    resolution: Optional[str] = None
    license_resolved: Optional[str] = None
    source_url_resolved: Optional[str] = None
    attribution: Optional[str] = None
    note: Optional[str] = None


_SECTION_RE = re.compile(r"^###\s+(.+?)\s*$")
_CANDIDATE_RE = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*(.*)$")
_FIELD_RE = re.compile(r"^\s+-\s+([A-Za-z][A-Za-z \-/]*?):\s*(.*)$")
_TREATMENT_RE = re.compile(
    r"^Visual treatment[^:]*:\s*\*\*(.+?)\*\*", re.IGNORECASE
)
_HEADING_RE = re.compile(r"^(#{1,6})\s")
_PLAIN_TEXT_HINTS = (
    "plain text card",
    "plain-text card",
    "plain text only",
    "text card",
    "agent-generated text card",
)


def _flag_plain_text(candidate: Candidate) -> None:
    """Mark candidates that sources.md explicitly routes to an on-screen text
    card instead of a fetched image."""
    hay = " ".join(candidate.notes).lower()
    if candidate.license_claimed:
        hay += " " + candidate.license_claimed.lower()
    if candidate.title:
        hay += " " + candidate.title.lower()
    for hint in _PLAIN_TEXT_HINTS:
        if hint in hay:
            candidate.plain_text_only = True
            return


def parse_sources_md(path: Path) -> tuple[list[Candidate], list[str]]:
    """Parse a sources.md file and return (candidates, all_lines).

    The returned `all_lines` is used later to rewrite the file in place.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    candidates: list[Candidate] = []
    current: Optional[Candidate] = None
    current_section = "(unknown)"
    current_treatment: Optional[str] = None
    in_candidates_block = False

    for raw in lines:
        if raw.strip().startswith("## Image candidates"):
            in_candidates_block = True
            continue
        if in_candidates_block and raw.strip().startswith("## ") and not raw.strip().startswith("## Image candidates"):
            # left the candidates block
            if current:
                _flag_plain_text(current)
                candidates.append(current)
                current = None
            in_candidates_block = False
            continue
        if not in_candidates_block:
            continue

        m_section = _SECTION_RE.match(raw)
        if m_section:
            if current:
                _flag_plain_text(current)
                candidates.append(current)
                current = None
            current_section = m_section.group(1).strip()
            current_treatment = None
            continue

        m_treatment = _TREATMENT_RE.match(raw.strip())
        if m_treatment:
            current_treatment = m_treatment.group(1).strip()
            continue

        m_cand = _CANDIDATE_RE.match(raw)
        if m_cand:
            if current:
                _flag_plain_text(current)
                candidates.append(current)
            number = int(m_cand.group(1))
            title = m_cand.group(2).strip()
            trailing = m_cand.group(3).strip()
            if trailing:
                title = f"{title} {trailing}".strip()
            current = Candidate(
                number=number,
                title=title,
                section=current_section,
                visual_treatment=current_treatment,
            )
            continue

        if current is None:
            continue

        m_field = _FIELD_RE.match(raw)
        if m_field:
            key = m_field.group(1).strip().lower()
            val = m_field.group(2).strip()
            if key == "artist":
                current.artist = val
            elif key == "source":
                current.source = val
            elif key == "category url":
                current.category_url = val
            elif key.startswith("specific candidate"):
                current.file_url = val
            elif key == "license":
                current.license_claimed = val
            elif key in ("notes", "note"):
                current.notes.append(val)
            elif key == "alternative":
                current.notes.append(f"alternative: {val}")
            else:
                current.notes.append(f"{key}: {val}")
            continue

        # Continuation text for prior field
        if raw.startswith("    ") and current.notes:
            current.notes[-1] += " " + raw.strip()

    if current and in_candidates_block:
        _flag_plain_text(current)
        candidates.append(current)

    return candidates, lines


# --- Wikimedia Commons API ---------------------------------------------------


class _HTMLStripper(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self._parts.append(data)

    def text(self) -> str:
        return " ".join("".join(self._parts).split())


def _strip_html(s: str) -> str:
    if not s:
        return ""
    p = _HTMLStripper()
    p.feed(s)
    return p.text()


def _wm_title_from_url(url: str) -> Optional[str]:
    """Given a commons.wikimedia.org URL like
    https://commons.wikimedia.org/wiki/File:Foo_Bar.jpg
    return the title "File:Foo_Bar.jpg" (URL-decoded)."""
    try:
        parsed = urllib.parse.urlparse(url)
    except ValueError:
        return None
    if "commons.wikimedia.org" not in parsed.netloc:
        return None
    path = parsed.path
    m = re.match(r"^/wiki/(File:.+)$", path)
    if not m:
        return None
    return urllib.parse.unquote(m.group(1))


def _http_get_json(url: str, timeout: float = 20.0) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _http_download(url: str, dest: Path, timeout: float = 60.0) -> int:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    dest.write_bytes(data)
    return len(data)


def resolve_wikimedia_file(title: str) -> dict:
    """Query the MediaWiki API for imageinfo on a File: title.

    Returns the imageinfo[0] dict on success, or raises RuntimeError with a
    human-readable message on failure.
    """
    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "titles": title,
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
    }
    url = (
        "https://commons.wikimedia.org/w/api.php?"
        + urllib.parse.urlencode(params)
    )
    data = _http_get_json(url)
    pages = data.get("query", {}).get("pages", [])
    if not pages:
        raise RuntimeError(f"no pages for title {title!r}")
    page = pages[0]
    if "missing" in page:
        raise RuntimeError(f"file {title!r} missing on commons.wikimedia.org")
    infos = page.get("imageinfo", [])
    if not infos:
        raise RuntimeError(f"no imageinfo returned for {title!r}")
    return infos[0]


# --- license validation ------------------------------------------------------


def validate_license(license_text: str) -> tuple[bool, str]:
    """Return (ok, normalized_reason)."""
    if not license_text:
        return False, "empty license"
    # Normalize: lowercase, and collapse "CC BY" → "cc-by" etc. so spelled-out
    # and hyphenated variants match the allowlist identically.
    low = license_text.lower()
    normalized = re.sub(r"[\s_/]+", "-", low)
    # Denylist — short tokens (nc, nd) use word-boundary matching to avoid
    # false positives on fragments like "encyclopedia". Longer phrases are
    # matched as substrings.
    for denied in LICENSE_DENYLIST:
        if len(denied) <= 2:
            if re.search(rf"(^|[^a-z]){re.escape(denied)}([^a-z]|$)", normalized):
                return False, f"denylist match: {denied!r}"
        else:
            if denied in normalized:
                return False, f"denylist match: {denied!r}"
    for allowed in LICENSE_ALLOWLIST:
        if allowed in normalized:
            return True, f"allowlist match: {allowed!r}"
    return False, f"no allowlist match: {license_text!r}"


def build_attribution(ext: dict, fallback_artist: Optional[str]) -> str:
    def pick(key: str) -> str:
        if not isinstance(ext, dict):
            return ""
        entry = ext.get(key)
        if isinstance(entry, dict):
            return _strip_html(entry.get("value", ""))
        return ""

    artist = pick("Artist") or (fallback_artist or "")
    credit = pick("Credit")
    license_short = pick("LicenseShortName") or pick("UsageTerms")
    parts: list[str] = []
    if artist:
        parts.append(artist)
    if credit and credit != artist:
        parts.append(f"via {credit}")
    if license_short:
        parts.append(f"({license_short})")
    return ", ".join(parts) if parts else "(no attribution metadata)"


# --- download orchestration --------------------------------------------------


def _slugify(s: str, max_len: int = 50) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "image"


def _ext_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    if "." in path:
        return path.rsplit(".", 1)[1].lower().split("?")[0][:5]
    return "bin"


def process_candidate(
    candidate: Candidate,
    target_dir: Path,
    dry_run: bool,
    verbose: bool,
) -> DownloadResult:
    if candidate.plain_text_only:
        return DownloadResult(
            candidate=candidate,
            status="skipped",
            note="plain-text card — not a fetched image",
        )
    if not candidate.file_url:
        return DownloadResult(
            candidate=candidate,
            status="skipped",
            note="no 'Specific candidate file' URL — pick one in sources.md first",
        )

    title = _wm_title_from_url(candidate.file_url)
    if not title:
        return DownloadResult(
            candidate=candidate,
            status="error",
            note=f"could not parse Wikimedia File: title from {candidate.file_url}",
        )

    try:
        info = resolve_wikimedia_file(title)
    except urllib.error.URLError as e:
        return DownloadResult(
            candidate=candidate,
            status="error",
            note=(
                f"Wikimedia API unreachable: {e.reason if hasattr(e, 'reason') else e}"
                f" — if this sandbox blocks commons.wikimedia.org, run this tool"
                f" on a local machine instead"
            ),
        )
    except Exception as e:
        return DownloadResult(
            candidate=candidate,
            status="error",
            note=f"Wikimedia API error: {e}",
        )

    ext = info.get("extmetadata") or {}
    license_short = ""
    for key in ("LicenseShortName", "UsageTerms", "License"):
        entry = ext.get(key)
        if isinstance(entry, dict):
            license_short = _strip_html(entry.get("value", ""))
            if license_short:
                break

    ok, reason = validate_license(license_short)
    if not ok:
        return DownloadResult(
            candidate=candidate,
            status="error",
            license_resolved=license_short,
            note=f"license check failed — {reason}",
        )

    direct_url = info.get("url") or ""
    if not direct_url:
        return DownloadResult(
            candidate=candidate,
            status="error",
            note="Wikimedia returned no direct file URL",
        )

    width = info.get("width")
    height = info.get("height")
    resolution = f"{width}x{height}" if width and height else None

    file_ext = _ext_from_url(direct_url)
    slug = _slugify(title.replace("File:", ""))
    local_name = f"{candidate.number:02d}-{slug}.{file_ext}"
    local_path = target_dir / local_name

    attribution = build_attribution(ext, candidate.artist)

    if dry_run:
        return DownloadResult(
            candidate=candidate,
            status="skipped",
            local_filename=local_name,
            resolution=resolution,
            license_resolved=license_short,
            source_url_resolved=direct_url,
            attribution=attribution,
            note="dry-run: would download",
        )

    if local_path.exists():
        return DownloadResult(
            candidate=candidate,
            status="exists",
            local_filename=local_name,
            resolution=resolution,
            license_resolved=license_short,
            source_url_resolved=direct_url,
            attribution=attribution,
            note="file already present on disk",
        )

    try:
        size = _http_download(direct_url, local_path)
    except urllib.error.URLError as e:
        return DownloadResult(
            candidate=candidate,
            status="error",
            source_url_resolved=direct_url,
            note=(
                f"download failed: {e.reason if hasattr(e, 'reason') else e}"
            ),
        )
    except Exception as e:
        return DownloadResult(
            candidate=candidate,
            status="error",
            source_url_resolved=direct_url,
            note=f"download error: {e}",
        )

    if verbose:
        print(
            f"  #{candidate.number} downloaded {size} bytes → {local_name}",
            file=sys.stderr,
        )

    return DownloadResult(
        candidate=candidate,
        status="downloaded",
        local_filename=local_name,
        resolution=resolution,
        license_resolved=license_short,
        source_url_resolved=direct_url,
        attribution=attribution,
        note=None,
    )


# --- sources.md rewriter -----------------------------------------------------


def _format_row(r: DownloadResult) -> str:
    def cell(s: Optional[str]) -> str:
        if not s:
            return ""
        return s.replace("|", "\\|").replace("\n", " ")

    status_tag = {
        "downloaded": "",
        "exists": " (exists)",
        "skipped": " (skipped)",
        "error": " (error)",
    }.get(r.status, "")
    filename = cell((r.local_filename or "") + status_tag)
    source = cell(r.source_url_resolved)
    return (
        f"| {r.candidate.number} "
        f"| {filename} "
        f"| {cell(r.resolution)} "
        f"| {cell(r.license_resolved)} "
        f"| {source} "
        f"| {cell(r.attribution)} |"
    )


def rewrite_downloaded_files_table(
    sources_path: Path, lines: list[str], results: list[DownloadResult]
) -> None:
    """Replace the "## Downloaded files" table in sources.md with a fresh one
    built from `results`. Other sections are left untouched."""
    start: Optional[int] = None
    end: Optional[int] = None
    for i, line in enumerate(lines):
        if line.strip() == "## Downloaded files":
            start = i
            continue
        if start is not None and i > start and _HEADING_RE.match(line):
            end = i
            break
    if start is None:
        # Append new section at the end
        lines.append("")
        lines.append("## Downloaded files")
        start = len(lines) - 1
        end = len(lines)
    if end is None:
        end = len(lines)

    new_block = [
        "## Downloaded files",
        "",
        f"_Last updated by `tools/source_images.py` on {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}._",
        "",
        "| # | Local filename | Resolution | License | Source URL | Attribution string |",
        "|---|---|---|---|---|---|",
    ]
    for r in sorted(results, key=lambda r: r.candidate.number):
        new_block.append(_format_row(r))
    new_block.append("")

    lines[start:end] = new_block
    sources_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --- CLI ---------------------------------------------------------------------


def _resolve_sources_path(args: argparse.Namespace) -> Path:
    if args.sources_file:
        return Path(args.sources_file).resolve()
    if not args.episode:
        raise SystemExit(
            "error: must pass either <episode-slug> or --sources-file"
        )
    return (DEFAULT_EPISODE_PARENT / args.episode / "sources.md").resolve()


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Download public-domain images listed in an episode's sources.md"
            " and write a verified attribution table back into the file."
        )
    )
    parser.add_argument(
        "episode",
        nargs="?",
        help=(
            "episode slug under experiments/youtube-history-channel/assets/"
            " (e.g. dancing-plague-1518)"
        ),
    )
    parser.add_argument(
        "--sources-file",
        help="explicit path to a sources.md (overrides <episode>)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="parse, resolve, and validate licenses without downloading or rewriting",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="per-candidate logs to stderr"
    )
    args = parser.parse_args(argv)

    sources_path = _resolve_sources_path(args)
    if not sources_path.exists():
        print(f"error: sources file not found: {sources_path}", file=sys.stderr)
        return 66

    target_dir = sources_path.parent
    candidates, lines = parse_sources_md(sources_path)
    if not candidates:
        print(
            f"error: no candidates parsed from {sources_path} — is it the right format?",
            file=sys.stderr,
        )
        return 65

    print(
        f"parsed {len(candidates)} candidate(s) from {sources_path.relative_to(REPO_ROOT) if sources_path.is_relative_to(REPO_ROOT) else sources_path}",
        file=sys.stderr,
    )

    results: list[DownloadResult] = []
    errors = 0
    downloaded = 0
    for c in candidates:
        r = process_candidate(c, target_dir, dry_run=args.dry_run, verbose=args.verbose)
        results.append(r)
        if r.status == "error":
            errors += 1
            print(
                f"  #{c.number} ERROR {c.title[:60]!r} — {r.note}",
                file=sys.stderr,
            )
        elif r.status == "skipped":
            if args.verbose:
                print(
                    f"  #{c.number} skipped {c.title[:60]!r} — {r.note}",
                    file=sys.stderr,
                )
        elif r.status == "exists":
            if args.verbose:
                print(
                    f"  #{c.number} exists {r.local_filename}",
                    file=sys.stderr,
                )
        elif r.status == "downloaded":
            downloaded += 1

    summary = (
        f"summary: {downloaded} downloaded, "
        f"{sum(1 for r in results if r.status == 'exists')} existing, "
        f"{sum(1 for r in results if r.status == 'skipped')} skipped, "
        f"{errors} error(s)"
    )
    print(summary, file=sys.stderr)

    if not args.dry_run:
        rewrite_downloaded_files_table(sources_path, lines, results)
        print(f"rewrote {sources_path.name} Downloaded files table", file=sys.stderr)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
