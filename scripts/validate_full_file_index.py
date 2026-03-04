#!/usr/bin/env python3
"""Validate docs/full-file-index.md against the repository filesystem.

Checks:
- The index's claimed total markdown file count matches actual .md files on disk.
- Top-level section header counts match actual counts for root/docs/notes.
- The set of file entries listed in index tables matches the on-disk set:
  - no missing files
  - no extra (nonexistent) files
  - no duplicates

Design notes:
- Only table rows are parsed (lines starting with '| ... |'). Other backticked
  mentions of filenames are ignored.
- The index sometimes lists filenames relative to a subsection directory
  (e.g., a header like "### Legislative Drafts (`notes/legislation/`)" followed by
  rows like "| `file.md` | ... |"). This validator supports that convention.

Usage:
  python scripts/validate_full_file_index.py
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

INDEX_PATH = Path("docs/full-file-index.md")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def list_md_files(root: Path) -> list[Path]:
    md = [p for p in root.rglob("*.md") if p.is_file()]
    md = [p for p in md if ".git" not in p.parts]
    return md


def fail(msgs: list[str]) -> int:
    print("FAIL: docs/full-file-index.md validation")
    for m in msgs:
        print(f" - {m}")
    return 1


@dataclass(frozen=True)
class ParsedIndex:
    claimed_total: int | None
    header_root_count: int | None
    header_docs_count: int | None
    header_notes_count: int | None
    listed_files: list[str]  # normalized relative paths


TOTAL_RE = re.compile(r"catalogs\s+all\s+(\d+)\s+markdown\s+files", re.IGNORECASE)
ROOT_HDR_RE = re.compile(r"^##\s+Root\s+Files\s*\((\d+)\)\s*$")
DOCS_HDR_RE = re.compile(r"^##\s+Core\s+Documentation\s*\(`docs/`\)\s+—\s+(\d+)\s+files\s*$")
NOTES_HDR_RE = re.compile(r"^##\s+Working\s+Notes\s*\(`notes/`\)\s+—\s+(\d+)\s+files\s*$")

# Subsection headers that contain a directory hint, e.g. "### ... (`notes/legislation/`) — ..."
SUBDIR_HDR_RE = re.compile(r"^###\s+.*\(`([^`]+)`\).*$")

# Table row file token: | `something.md` | ... |
ROW_FILE_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|")


def _norm_prefix(p: str) -> str:
    p = p.strip()
    if not p:
        return ""
    # Normalize to posix-ish forward slashes; Path will normalize to platform.
    p = str(Path(p))
    if not p.endswith("/"):
        p += "/"
    return p


def parse_index(index_text: str) -> ParsedIndex:
    claimed_total = None
    m = TOTAL_RE.search(index_text)
    if m:
        claimed_total = int(m.group(1))

    header_root_count = None
    header_docs_count = None
    header_notes_count = None

    # Base prefix applied to table row tokens that don't already specify a full path.
    # "" means root.
    base_prefix = ""
    top_level = "root"  # root | docs | notes
    top_default_prefix = ""

    listed: list[str] = []

    for raw in index_text.splitlines():
        line = raw.rstrip("\n")
        stripped = line.strip()

        # Reset to top-level default when entering a new subsection without a directory hint.
        if stripped.startswith("### ") and not SUBDIR_HDR_RE.match(stripped):
            base_prefix = top_default_prefix

        m = ROOT_HDR_RE.match(stripped)
        if m:
            header_root_count = int(m.group(1))
            top_level = "root"
            top_default_prefix = ""
            base_prefix = top_default_prefix
            continue

        m = DOCS_HDR_RE.match(stripped)
        if m:
            header_docs_count = int(m.group(1))
            top_level = "docs"
            top_default_prefix = "docs/"
            base_prefix = top_default_prefix
            continue

        m = NOTES_HDR_RE.match(stripped)
        if m:
            header_notes_count = int(m.group(1))
            top_level = "notes"
            top_default_prefix = "notes/"
            base_prefix = top_default_prefix
            continue

        m = SUBDIR_HDR_RE.match(stripped)
        if m:
            hinted = m.group(1).strip()
            # Only adopt subsection hints that look like a directory path.
            if hinted.endswith("/") or hinted.endswith("\\"):
                base_prefix = _norm_prefix(hinted)
            else:
                # allow hints without trailing slash as well
                base_prefix = _norm_prefix(hinted)
            continue

        # Only count table rows; ignore other backticked mentions.
        if not stripped.startswith("|"):
            continue

        m = ROW_FILE_RE.match(stripped)
        if not m:
            continue

        token = m.group(1).strip()
        if not token.lower().endswith(".md"):
            continue

        token_norm = str(Path(token))

        # If already fully qualified from repo root, trust it.
        if token_norm.startswith("docs/") or token_norm.startswith("notes/"):
            rel = token_norm
        else:
            # Otherwise, prefix based on current base context.
            rel = str(Path(base_prefix) / token_norm) if base_prefix else token_norm

        # Safety: if we're in a top-level section but base_prefix got overridden to
        # another top-level, keep it anyway (the index may intentionally do that).
        listed.append(rel)

    return ParsedIndex(
        claimed_total=claimed_total,
        header_root_count=header_root_count,
        header_docs_count=header_docs_count,
        header_notes_count=header_notes_count,
        listed_files=listed,
    )


def main() -> int:
    root = repo_root()
    index_file = root / INDEX_PATH
    if not index_file.exists():
        return fail([f"Missing {INDEX_PATH}"])

    index_text = index_file.read_text(encoding="utf-8")
    parsed = parse_index(index_text)

    md_paths = list_md_files(root)
    md_rel = sorted(str(p.relative_to(root)) for p in md_paths)
    md_set = set(md_rel)

    actual_total = len(md_rel)
    actual_by_top = Counter(p.split("/")[0] if "/" in p else "." for p in md_rel)
    actual_root = actual_by_top.get(".", 0)
    actual_docs = actual_by_top.get("docs", 0)
    actual_notes = actual_by_top.get("notes", 0)

    errors: list[str] = []

    if parsed.claimed_total is None:
        errors.append(
            "Could not parse claimed total markdown count (expected text like 'catalogs all N markdown files')."
        )
    elif parsed.claimed_total != actual_total:
        errors.append(
            f"Claimed total markdown files = {parsed.claimed_total}, but actual on disk = {actual_total}."
        )

    if parsed.header_root_count is None:
        errors.append("Could not parse '## Root Files (N)' header count.")
    elif parsed.header_root_count != actual_root:
        errors.append(
            f"Root header count = {parsed.header_root_count}, but actual root markdown files = {actual_root}."
        )

    if parsed.header_docs_count is None:
        errors.append("Could not parse '## Core Documentation (`docs/`) — N files' header count.")
    elif parsed.header_docs_count != actual_docs:
        errors.append(
            f"Docs header count = {parsed.header_docs_count}, but actual docs markdown files = {actual_docs}."
        )

    if parsed.header_notes_count is None:
        errors.append("Could not parse '## Working Notes (`notes/`) — N files' header count.")
    elif parsed.header_notes_count != actual_notes:
        errors.append(
            f"Notes header count = {parsed.header_notes_count}, but actual notes markdown files = {actual_notes}."
        )

    if not parsed.listed_files:
        errors.append("Parsed 0 file entries from index tables (unexpected).")
    else:
        counts = Counter(parsed.listed_files)
        dups = [p for p, n in counts.items() if n > 1]
        if dups:
            errors.append(
                "Index contains duplicate file entries: "
                + ", ".join(sorted(dups)[:20])
                + (" ..." if len(dups) > 20 else "")
            )

        listed_set = set(parsed.listed_files)
        missing = sorted(md_set - listed_set)
        extra = sorted(listed_set - md_set)

        if missing:
            errors.append(
                f"Index is missing {len(missing)} markdown file(s) present on disk (showing up to 20): "
                + ", ".join(missing[:20])
                + (" ..." if len(missing) > 20 else "")
            )
        if extra:
            errors.append(
                f"Index lists {len(extra)} markdown file(s) not present on disk (showing up to 20): "
                + ", ".join(extra[:20])
                + (" ..." if len(extra) > 20 else "")
            )

        # Consistency: if index claims to catalog all files, unique table entries should equal total.
        if parsed.claimed_total is not None and len(listed_set) != parsed.claimed_total:
            errors.append(
                f"Index claims {parsed.claimed_total} total markdown files, but parsed {len(listed_set)} unique table entries."
            )

    if errors:
        return fail(errors)

    print("PASS: docs/full-file-index.md validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
