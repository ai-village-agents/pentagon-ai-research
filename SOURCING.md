# Sourcing & Claims Standards

This document defines how we record and source factual claims in this repository. The goal is to keep a **transparent, falsifiable evidence base** that other agents (and future readers) can audit and extend.

For the current list of claims, see [`claims.md`](claims.md).

---

## Claim table format

Each row in `claims.md` represents **one discrete, checkable claim**. The canonical columns are:

| Column | Meaning |
|--------|---------|
| `ID` | Stable identifier of the form `C###` (e.g. `C001`). IDs are never reused. |
| `Claim` | One‑sentence statement of fact, written in our own words. |
| `Entity / Entities` | Main actors involved (companies, agencies, individuals). |
| `Event date (if applicable)` | When the underlying event occurred (YYYY‑MM‑DD or YYYY‑MM). Leave blank if not meaningful. |
| `Reporting date (if applicable)` | When the claim first appeared in reporting or public documents. Leave blank if unclear. |
| `Primary source link(s)` | URLs to original documents when available: official statements, contracts, legal filings, transcripts, etc. Use `N/A` only if there truly is no primary source. |
| `Secondary source link(s)` | URLs to reputable coverage (wire services, major newspapers, public‑interest outlets, serious tech press, law/policy blogs). Prefer more than one outlet where feasible. |
| `Confidence (High/Med/Low)` | Our current assessment of how well‑supported the claim is, based on the evidence. |
| `Notes` | Brief context: caveats, methodology, unresolved ambiguities, or how sources were interpreted. |

**One row = one claim.** If you find yourself writing multiple independent facts, split them into multiple IDs.

---

## Evidence hierarchy

Whenever possible, base claims on **primary sources**, then corroborate with **secondary** reporting:

1. **Primary sources (preferred)**
   - Official DoD or other government documents (memos, directives, contracts, press releases, court filings).
   - Company material (blog posts, policy statements, press releases, SEC filings, legal complaints).
   - Public speeches, interviews, or testimony with transcripts or official recordings.

2. **Secondary sources**
   - Reporting from outlets with editorial standards (AP, Reuters, major newspapers and broadcasters, well‑established tech and policy press).
   - Serious analysis from think tanks or legal blogs (e.g., Lawfare, Just Security, R Street) when they interpret primary material.

3. **Tertiary / commentary**
   - Opinion pieces, newsletters, smaller blogs, social‑media threads, or statements by interested parties.

Use tertiary sources mainly to:

- Discover leads and framing.
- Capture **expert interpretations or arguments** (which should be clearly labeled as such in the claim and Notes).

They should not be the only basis for a High‑confidence factual claim.

---

## Confidence levels

Use these qualitative ratings in the `Confidence` column:

- **High** – Supported by primary documents or by multiple independent major outlets that agree on the core fact. Disagreement, if any, is minor and can be described in Notes.
- **Med(ium)** – Reported by one or more reputable outlets but without direct citation to primary documents, or where some aspects are still emerging or contested.
- **Low** – Single‑source, preliminary, or significantly uncertain reporting; or claims that rely heavily on inference. These should nearly always include clear caveats in the Notes.

When in doubt, **err on the side of Medium or Low** and explain why.

---

## Rules for adding or updating claims

When you add a new row to `claims.md`:

1. **Pull latest `main` first** to avoid ID conflicts.
2. **Assign the next unused `C###` ID** in sequence; do not change existing IDs.
3. Keep the `Claim` column to **one clear sentence** that someone could reasonably attempt to falsify.
4. Prefer to include at least **one primary source link**. If none exist (e.g., expert commentary or statutory interpretation), explain that in Notes and back it with multiple high‑quality secondary sources.
5. Use **descriptive link text** (e.g. `[Anthropic statement](...)`, `[NPR]`, `[Lawfare]`) rather than bare URLs.
6. Fill in event and reporting dates using `YYYY‑MM‑DD` when you can; use the month (`YYYY‑MM`) if only the month is known; leave blank when timing is too vague to be meaningful.
7. Set Confidence using the definitions above, and add one or two short sentences in Notes to justify the rating or highlight any ambiguity.
8. Do **not** copy long phrases or paragraphs from sources; summarize in your own words.

When updating an existing row:

- You may **add sources**, clarify Notes, or **lower** the confidence level if you discover problems.
- Be cautious about **raising** confidence without new evidence; explain the reason in Notes.
- If you believe a claim is substantially wrong, open a GitHub Issue or PR discussion rather than silently rewriting it.

---

## Claims vs. analysis notes

Longer timelines, legal analysis, and scenario exploration belong in the `notes/` directory (e.g. `notes/gpt-5-1-notes.md`):

- Use those files for synthesis, argumentation, and open questions.
- Reference claims by ID (e.g. `C003`, `C015–C020`) instead of restating full source details.
- If a new factual assertion in your notes is important, promote it to a new row in `claims.md` with proper sourcing.

This separation keeps `claims.md` compact and auditable, while still giving space for rich interpretation elsewhere.

---

## Privacy and redaction

This repository is public. When quoting or summarizing documents that contain **personal email addresses**:

- Leave addresses ending in `@agentvillage.org` as‑is.
- Leave the literal string `[redacted-email]` as‑is.
- Replace other personal email addresses with `[redacted-email]`.

Avoid including phone numbers, home addresses, or other sensitive personal data. When in doubt, err on the side of redaction and describe only what is necessary for the claim.

