#!/usr/bin/env python3
"""
Validate internal markdown links in the pentagon-ai-research repository.

Usage: python scripts/validate_links.py

Checks all .md files for internal links (relative paths) and verifies
that the target files exist.
"""

import os
import re
import sys
from pathlib import Path


def find_markdown_files(root_dir):
    """Find all markdown files in the repository."""
    md_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip .git directory
        dirs[:] = [d for d in dirs if d != '.git']
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files


def extract_links(content):
    """Extract all markdown links from content."""
    # Match [text](path) but not external URLs
    link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    links = re.findall(link_pattern, content)
    return links


def is_internal_link(path):
    """Check if a link is internal (not an external URL)."""
    return not path.startswith(('http://', 'https://', 'mailto:', '#'))


def validate_link(source_file, link_path, root_dir):
    """Validate that an internal link target exists."""
    # Handle anchor links within same file
    if link_path.startswith('#'):
        return True, None

    # Remove anchor from path if present
    path_without_anchor = link_path.split('#')[0]
    if not path_without_anchor:
        return True, None

    # Resolve relative path from source file's directory
    source_dir = os.path.dirname(source_file)
    target_path = os.path.normpath(os.path.join(source_dir, path_without_anchor))

    if os.path.exists(target_path):
        return True, None
    else:
        return False, target_path


def main():
    # Get repository root (script is in scripts/ directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)

    print(f"Validating links in: {root_dir}")
    print("-" * 50)

    md_files = find_markdown_files(root_dir)
    print(f"Found {len(md_files)} markdown files")

    broken_links = []
    total_links = 0

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            try:
                content = f.read()
            except UnicodeDecodeError:
                print(f"WARNING: Could not read {md_file}")
                continue

        links = extract_links(content)

        for text, path in links:
            if is_internal_link(path):
                total_links += 1
                valid, target = validate_link(md_file, path, root_dir)
                if not valid:
                    rel_source = os.path.relpath(md_file, root_dir)
                    broken_links.append((rel_source, path, target))

    print(f"Checked {total_links} internal links")
    print("-" * 50)

    if broken_links:
        print(f"\nFAIL: Found {len(broken_links)} broken link(s):\n")
        for source, link, target in broken_links:
            print(f"  {source}")
            print(f"    -> {link}")
            print(f"    (target not found: {target})")
            print()
        sys.exit(1)
    else:
        print("\nPASS: All internal links are valid!")
        sys.exit(0)


if __name__ == '__main__':
    main()
