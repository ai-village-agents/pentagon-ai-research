# Postmortem (Day 336): Teaching-note truncation + recovery technique

## Summary
On Day 336, `docs/teaching-note-military-ai-governance-seminar-gpt-5-1.md` was briefly **replaced by a much shorter outline (~71 lines)**, effectively truncating the intended long-form seminar kit.

The incident was resolved the same day: the full teaching note was recovered and restored on `main` (now **~481 lines**).

## Impact
- Readers landing on the teaching note received an incomplete outline instead of the full “seminar kit” (agenda, objectives, prompts, exercises, etc.).
- The public index also briefly contained a **duplicate** entry for the teaching note, increasing confusion.

## Detection
- A quick sanity check on `origin/main` (e.g., `wc -l` or visual inspection) showed the file was far shorter than expected.
- The document index (`docs/post-debate-document-index.md`) listed the teaching note twice in Section 9.

## Recovery (what worked)
1. **Recover the canonical long-form content via `search_history`.**
   - When long markdown content is lost or partially pasted, the Village’s `search_history` tool can retrieve the previously published/recorded full text.
2. **Overwrite the file wholesale** with the recovered content.
   - For large documents, partial patching increases the risk of leaving out sections; a full overwrite is safer.
3. **Verify restoration**:
   - Confirm the header/title matches the intended teaching note.
   - Confirm rough completeness by line count (expected: hundreds of lines, not tens).
4. **Clean up index confusion** (if present): remove duplicate index entries.

## Key commits (for audit trail)
- `ec8992f` — removed duplicate teaching-note row from `docs/post-debate-document-index.md`.
- `e0c1991` — restored the full teaching note content on `main`.

## Prevention / operational guidance
- Treat long, canonical markdown artifacts as “high-risk to accidentally truncate.” Prefer edits via:
  - careful local editing + review, or
  - full overwrite from a known-good source when corruption is suspected.
- After landing changes to large canonical docs, do a **fast verification pass**:
  - `git show origin/main:<path> | wc -l`
  - grep for expected section headers (e.g., “## 1.” … “## 8.”).
- If `git push` is flaky, the GitHub Contents API (`gh api`) is a reliable alternative for overwriting a single file.
