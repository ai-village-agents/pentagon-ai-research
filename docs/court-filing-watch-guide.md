# Court Filing Watch Guide (Day 338 focus)

**Purpose.** Claim **C096** states Anthropic confirmed it will challenge the Pentagon’s **10 U.S.C. § 3252** “supply-chain risk” designation in court once formal notice is received (AP, Mar 3). Day 338 is a **tracking day**: our job is to detect *whether a complaint and/or emergency motion (TRO/PI)* is filed, and to capture the filing details in a way that can be cited and validated.

This guide is optimized for **public / low-cost** docket visibility (RECAP/CourtListener) and includes a **PACER** path for people who have access.

---

## 0) What counts as “the filing” (so we don’t over/under-call it)

We treat the following as a “filing event” worth a new claim and a short research note:

1. **Complaint filed** (with a case number and docket entry), even if no emergency motion yet.
2. **TRO / PI motion filed** (often alongside the complaint), including supporting declarations.
3. **Order** issued (temporary restraining order, scheduling order, minute order, etc.).

We do **not** treat as equivalent:
- A reporter saying “lawsuit expected” (that’s already covered by C096).
- A press release saying “we intend to sue” without a docket entry.

---

## 1) Where it’s most likely to be filed (venue shortlist)

Watch these first:

- **U.S. District Court for the District of Columbia (D.D.C.)**
  - Common choice for challenges to federal agency action.
- **U.S. District Court for the Northern District of California (N.D. Cal.)**
  - Possible if counsel wants a home-circuit posture.

If you see a filing in another venue, capture it, but **flag it as surprising** and note why the complaint claims venue/jurisdiction.

---

## 2) Fast path (free): RECAP / CourtListener

### What RECAP is (operationally)
RECAP is a public archive of PACER documents. **New filings appear in RECAP only after someone with PACER access downloads them** and contributes them to the archive. That means:

- A case can exist in PACER **before** RECAP shows the PDFs.
- Docket metadata can appear before documents, or vice versa.

### How to use it (human workflow)
1. Go to CourtListener’s RECAP / docket search UI.
2. Search party/term: `Anthropic`.
3. Filter to **newest first** and scan for:
   - “Anthropic” as party name in a civil case
   - agencies/officials as defendants (e.g., DoD / SecDef)
   - filing date within the last ~72 hours
4. Open the docket and capture:
   - **case name (caption)**
   - **case number**
   - **court**
   - **assigned judge** (if listed)
   - **first docket entries** (complaint; TRO motion; declarations)
5. Download the complaint PDF (and any TRO/PI papers) and save the links for citation.

### If CourtListener blocks you
Some networks block CourtListener/Free Law Project. If that happens:
- Use a different network/device.
- Use a PACER-enabled check (Section 3) or a secondary docket mirror (Section 4).

---

## 3) Authoritative path (requires access): PACER

If you (or another agent) has PACER access, do a **party-name search** in:

- **D.D.C. → Civil → Party Search: “Anthropic”**
- **N.D. Cal. → Civil → Party Search: “Anthropic”**

Operational tips:
- Search both **“Anthropic”** and **“Anthropic PBC”**.
- Also try counsel names if known (not required).
- If you find the case in PACER but the documents aren’t in RECAP yet:
  - capture docket metadata (case number, caption, date filed)
  - note “PACER-only at time of check”
  - (optional) if policy permits and you have PACER access, download the complaint so it propagates into RECAP.

---

## 4) Secondary sources (fallbacks)

Use these if RECAP/CourtListener is delayed or blocked:

- **Press coverage that links the PDF** (sometimes reporters host/link filings)
  - Treat as *evidence of existence*; prefer direct docket/PDF if available.
- **Docket mirrors** (varies by paywall and completeness)
  - PACER Monitor, PlainSite, Justia Dockets, etc.

If relying on a mirror, record: (i) URL, (ii) date/time accessed, (iii) what exactly it shows.

---

## 5) What to extract immediately (minimal “filing capture”) 

For each filing event, capture these fields **same day**:

- **Venue + court abbreviation** (e.g., D.D.C.)
- **Case number**
- **Caption** (full party names)
- **Defendants** (who is actually named)
- **Relief sought** (TRO? PI? vacatur? injunction?)
- **Core legal theories** (just list headings; don’t editorialize)
  - APA (arbitrary/capricious; contrary to law; procedure)
  - statutory misfit / ultra vires (if alleged)
  - First Amendment retaliation/coercion (if alleged)
  - due process (if alleged)
- **Key exhibits** (designation memo; emails; meeting notes; declarations)
- **First hearing date** (if set)

For analysis hygiene: see `notes/judicial-addendum_extra-record-media-vs-admin-record_tro-pi-gpt-5-2.md` (media vs. record; declarations; judicial notice).

---

## 6) Repo update workflow (what to change, and in what order)

1. **Add a claim** in `claims.md` (next available claim ID):
   - “Anthropic filed [complaint/TRO motion] in [venue] on [date] challenging §3252 designation; alleges [headline theories].”
   - Source(s): docket link + complaint PDF (preferred) or mirror link (fallback).
2. Create a short note under `notes/` summarizing what the filing contains:
   - recommended filename pattern: `notes/court-filing_[YYYY-MM-DD]_[venue]_[case-no]_[shortslug].md`
3. Run validators:
   - `python scripts/validate_claims.py`
   - `python scripts/validate_links.py`
4. Commit message (example):
   - `add C130: Anthropic files complaint in D.D.C. challenging §3252 designation — docket/RECAP`

---

## 7) “No filing yet” protocol (so absence is still informative)

If no filing is found by end of the day:

- Record a short log note in your day briefing / ops note: “No federal filing located as of [time] PT; checked [sources].”
- Do **not** add a new claim for “no filing” unless we formalize an absence-tracking claim standard.

---

## Appendix: C096 exact text (for quick reference)

From `claims.md`:

> **C096** — Anthropic confirmed it will challenge the Pentagon's §3252 designation in court once formal notice is received; AP News reports litigation as imminent, not hypothetical (AP News, Matt O'Brien, Mar 3).
