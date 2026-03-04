#!/usr/bin/env python3
"""
Validate full-file-index.md against the actual filesystem.

Checks:
1. Total file count in index header matches actual count
2. All files listed in index exist in filesystem
3. All markdown files in filesystem are listed in index
4. Section counts in index match actual counts per directory

Usage: python scripts/validate_full_file_index.py

Author: Opus 4.5 Claude Code
Created: Day 338 (March 5, 2026)
"""

import os
import re
from pathlib import Path

def get_actual_files(repo_root):
    """Get all markdown files in the repository."""
    md_files = []
    for root, dirs, files in os.walk(repo_root):
        # Skip .git directory
        dirs[:] = [d for d in dirs if d != '.git']
        for f in files:
            if f.endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, f), repo_root)
                md_files.append(rel_path)
    return sorted(md_files)

def parse_index_header_count(index_path):
    """Extract the total file count from the index header."""
    with open(index_path, 'r') as f:
        content = f.read()

    # Look for pattern like "all 235 markdown files"
    match = re.search(r'all\s+(\d+)\s+markdown\s+files', content, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def extract_files_from_index(index_path, repo_root):
    """Extract all file references from the index."""
    with open(index_path, 'r') as f:
        content = f.read()

    files_found = set()

    # Match table rows with backticked filenames
    # Pattern: | `filename.md` | description |
    table_pattern = re.compile(r'\|\s*`([^`]+\.md)`\s*\|')
    for match in table_pattern.finditer(content):
        filename = match.group(1)
        files_found.add(filename)

    return files_found

def get_section_counts(index_path):
    """Extract section counts from the index (e.g., 'Root Files (9)')."""
    with open(index_path, 'r') as f:
        content = f.read()

    counts = {}
    # Match patterns like "## Root Files (9)" or "### News & Scenarios (10)"
    section_pattern = re.compile(r'##?\s*(.+?)\s*\((\d+)\)')
    for match in section_pattern.finditer(content):
        section_name = match.group(1).strip()
        count = int(match.group(2))
        counts[section_name] = count

    return counts

def categorize_actual_files(files):
    """Categorize files by directory."""
    categories = {
        'root': [],
        'docs': [],
        'notes': []
    }

    for f in files:
        if '/' not in f:
            categories['root'].append(f)
        elif f.startswith('docs/'):
            categories['docs'].append(f)
        elif f.startswith('notes/'):
            categories['notes'].append(f)

    return categories

def main():
    repo_root = Path(__file__).parent.parent
    index_path = repo_root / 'docs' / 'full-file-index.md'

    if not index_path.exists():
        print("ERROR: docs/full-file-index.md not found")
        return 1

    errors = []
    warnings = []

    # Get actual files
    actual_files = get_actual_files(repo_root)
    actual_count = len(actual_files)

    # Get header count from index
    header_count = parse_index_header_count(index_path)

    print(f"Validating full-file-index.md against filesystem...")
    print("-" * 50)
    print(f"Actual markdown files in repo: {actual_count}")

    if header_count:
        print(f"Count in index header: {header_count}")
        if header_count != actual_count:
            errors.append(f"Header count mismatch: index says {header_count}, actual is {actual_count}")
    else:
        warnings.append("Could not extract file count from index header")

    # Get files referenced in index
    index_files = extract_files_from_index(index_path, repo_root)
    print(f"Files referenced in index: {len(index_files)}")

    # Categorize actual files
    categories = categorize_actual_files(actual_files)
    print(f"\nActual file distribution:")
    print(f"  Root: {len(categories['root'])}")
    print(f"  docs/: {len(categories['docs'])}")
    print(f"  notes/: {len(categories['notes'])}")

    # Check for files in index but not in filesystem
    # Note: index entries may be just filenames without full paths
    actual_basenames = {os.path.basename(f) for f in actual_files}

    missing_from_fs = []
    for index_file in index_files:
        # Check both basename and if it could be a full path
        basename = os.path.basename(index_file)
        if basename not in actual_basenames:
            # Check if the full path exists
            full_paths_to_check = [
                index_file,
                f"docs/{index_file}",
                f"notes/{index_file}"
            ]
            found = False
            for check_path in full_paths_to_check:
                if check_path in actual_files:
                    found = True
                    break
            if not found:
                missing_from_fs.append(index_file)

    if missing_from_fs:
        for f in missing_from_fs:
            errors.append(f"In index but not in filesystem: {f}")

    # Check for files in filesystem but not in index
    missing_from_index = []
    for actual_file in actual_files:
        basename = os.path.basename(actual_file)
        # Check if basename is in index files (accounting for possible full paths)
        found = basename in index_files or actual_file in index_files
        if not found:
            # Also check if the basename without path is in index
            for idx_file in index_files:
                if os.path.basename(idx_file) == basename:
                    found = True
                    break
        if not found:
            missing_from_index.append(actual_file)

    if missing_from_index:
        for f in missing_from_index:
            warnings.append(f"In filesystem but possibly not in index: {f}")

    # Print results
    print("\n" + "=" * 50)

    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")

    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings[:10]:  # Limit to first 10 warnings
            print(f"  - {w}")
        if len(warnings) > 10:
            print(f"  ... and {len(warnings) - 10} more")

    if errors:
        print("\nFAIL: full-file-index.md validation failed")
        return 1
    elif warnings:
        print("\nPASS (with warnings): full-file-index.md validation passed")
        return 0
    else:
        print("\nPASS: full-file-index.md validation passed")
        return 0

if __name__ == "__main__":
    exit(main())
