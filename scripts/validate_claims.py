#!/usr/bin/env python3
"""Validate claims.md table formatting.

Checks:
- Table header exists.
- Each claim row has an ID of the form C###.
- No duplicate IDs.
- Each row has the expected number of columns.
- Confidence is one of High/Med/Low.

This script is intentionally strict on structure (to keep claims auditable) but
not strict about sequential numbering (gaps are allowed if claims are removed).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from collections import defaultdict

EXPECTED_COLUMNS = [
    "ID",
    "Claim",
    "Entity / Entities",
    "Event date (if applicable)",
    "Reporting date (if applicable)",
    "Primary source link(s)",
    "Secondary source link(s)",
    "Confidence (High/Med/Low)",
    "Notes",
]
ALLOWED_CONF = {"high", "med", "low"}


def fail(msgs: list[str]) -> int:
    print("FAIL: claims.md validation")
    for m in msgs:
        print(f" - {m}")
    return 1


def main() -> int:
    p = Path(__file__).resolve().parents[1] / "claims.md"
    if not p.exists():
        return fail([f"Missing {p}"])

    lines = p.read_text(encoding="utf-8").splitlines()

    # Find header
    header_idx = None
    for i, l in enumerate(lines):
        if l.strip() == "| " + " | ".join(EXPECTED_COLUMNS) + " |":
            header_idx = i
            break

    errors: list[str] = []

    if header_idx is None:
        errors.append("Missing canonical table header row")
    else:
        if header_idx + 1 >= len(lines) or not lines[header_idx + 1].lstrip().startswith("|----"):
            errors.append("Missing table separator row after header")

    row_re = re.compile(r"^\|\s*(C\d{3})\s*\|")
    ids: list[tuple[str, int]] = []

    for lineno, l in enumerate(lines, 1):
        if not l.startswith("| C"):
            continue
        m = row_re.match(l)
        if not m:
            errors.append(f"Line {lineno}: row starts with '| C' but ID is not C###")
            continue

        cid = m.group(1)
        pipe_count = l.count("|")
        # For 9 columns, markdown table rows have 10 pipes: leading + between + trailing
        if pipe_count != 10:
            errors.append(f"Line {lineno} ({cid}): expected 10 '|' characters (9 columns), found {pipe_count}")

        # Extract columns (naive split; OK because we disallow '|' in cells)
        cols = [c.strip() for c in l.strip().split("|")[1:-1]]
        if len(cols) != 9:
            errors.append(f"Line {lineno} ({cid}): expected 9 columns, parsed {len(cols)}")
        else:
            conf = cols[7].strip().lower()
            if conf not in ALLOWED_CONF:
                errors.append(f"Line {lineno} ({cid}): invalid Confidence '{cols[7]}' (expected High/Med/Low)")

        ids.append((cid, lineno))

    seen = defaultdict(list)
    for cid, lineno in ids:
        seen[cid].append(lineno)
    for cid, locs in sorted(seen.items()):
        if len(locs) > 1:
            errors.append(f"Duplicate ID {cid} at lines {locs}")

    if errors:
        return fail(errors)

    print("PASS: claims.md validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
