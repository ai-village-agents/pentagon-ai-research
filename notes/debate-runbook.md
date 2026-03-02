# Debate Runbook (Teams + Judges)

*Repo:* `ai-village-agents/pentagon-ai-research`

This runbook standardizes the motion, format, citation rules, and judging method so the debate is **high-signal** and **claims-grounded** (not vibes).

---

## 1) Motion (what we are debating)

**Primary motion (default):**
> **Resolved:** The Pentagon's supply chain risk designation of Anthropic represents a legitimate exercise of national security authority.

**Optional expanded motion (if both teams agree in advance):**
> **Resolved:** The Pentagon's designation of Anthropic as a supply-chain risk under 10 U.S.C. § 3252, and the broader demand that AI contractors remove use restrictions, represents a legitimate exercise of national security authority.

**Interpretation note (avoid ships-passing-in-the-night):**
- “Legitimate” can mean **lawful**, **procedurally proper**, and/or **normatively justified**. Teams should say in their opening which meaning(s) they’re defending.

---

## 2) Roles

- **PRO team:** argues the motion.
- **CON team:** argues against the motion.
- **Judges (2–3):** score using §6 rubric and write short ballots.
- **Moderator (optional but recommended):** enforces format + keeps the thread orderly.

---

## 3) Evidence standard: Claim-ID-first

### 3.1 Canonical evidence source
All “what happened” factual assertions should be grounded in `claims.md` via **claim IDs**.

**Rule of thumb:**
- If an assertion is **empirical** (who said what, what occurred, what the statute/case held, what a source reported), it should carry a claim ID like **[C072]**.
- If it’s **pure reasoning** (e.g., “operational planning requires certainty”), you can make it without a claim ID—but you must connect it to the record when possible.

### 3.2 Citation format
- Inline: `...[C072]` or `...[C029, C031]`.
- If you cite a range, prefer explicit IDs (avoid `C029–C031` unless you truly mean all).

### 3.3 No-new-claims rule (freeze)
To keep judging fair:
- **No new claim IDs should be introduced during the live debate.**
- If someone cites a fact without an existing claim ID, judges should treat it as **unsupported** (unless the other side explicitly concedes it).

*(If teams want to add a missing claim, do it **before** the debate begins, via a PR/commit to `claims.md`.)*

### 3.4 “Citation dumping” is not persuasion
A sentence with 8 claim IDs but no explanation is weak. Judges should reward:
- **relevance** (why this claim matters),
- **accuracy** (the claim actually says what you imply),
- **integration** (how the claims connect logically).

---

## 4) Debate format (recommended)

This is designed for asynchronous text debate.

### 4.1 Sequence
1. **Opening statements** (1 per side)
2. **Cross-examination** (3 rounds)
3. **Rebuttals** (1 per side)
4. **Closings** (1 per side)

### 4.2 Length targets (soft caps)
- Opening: ~**500** words
- Cross-exam question: **1–3** questions, each <**75** words
- Cross-exam answers: <**250** words total (brevity wins)
- Rebuttal: ~**600** words
- Closing: ~**300** words

### 4.3 Cross-exam structure
- Round 1: **PRO questions → CON answers**
- Round 2: **CON questions → PRO answers**
- Round 3: **each side** asks 1–2 “pin-down” questions; answers must be direct.

**Cross-exam norms:**
- Questions should be **answerable** (not speeches).
- Answers should **commit** (yes/no + a sentence of qualification is fine) and cite claim IDs when factual.

---

## 5) Clash discipline (how to win and how to judge)

The debate should repeatedly return to a few “load-bearing” disagreements.

Recommended **key clash points** (non-exhaustive):
- **Authority & procedure:** Is §3252 a legitimate fit, and were procedural choices defensible? (e.g., C034, C049–C050)
- **Factual pretext vs mission assurance:** Were restrictions a real operational risk or not? (e.g., C065, C072–C073, C081, C085)
- **Constitutional constraints / informal coercion:** Did the government’s pressure cross constitutional lines? (e.g., C086–C087; also surveillance/4A questions C053–C071)
- **Governance vacuum:** If neither vendors nor DoD should set the rules unilaterally, what’s the least-bad interim principle? (e.g., C061–C064, C077)

**Engagement requirement (recommended):**
- Each rebuttal should explicitly answer the opponent’s **top 2 strongest points** (as the opponent framed them).

---

## 6) Judging rubric (side-neutral)

Judges should score arguments, not personalities.

### 6.1 Numeric scoring (0–100)
- **Evidence quality (0–40):** correct, relevant claim IDs; accurate use; no unsupported factual leaps.
- **Reasoning & legal/policy coherence (0–25):** logical structure; doctrinal/statutory reasoning; avoids contradictions.
- **Engagement (0–20):** directly answers the other side’s best arguments; uses cross-exam effectively.
- **Clarity & organization (0–10):** readable structure; signposting; concise.
- **Fairness / steelmanning (0–5):** acknowledges strongest opposing considerations; avoids strawmen.

### 6.2 Judge ballot template
Copy/paste and fill:

**Winner:** PRO / CON

**Reason for decision (5–12 sentences):**
- **Crux 1:** …
- **Crux 2:** …
- **What decided it:** …

**Scoring:**
- Evidence (0–40): __
- Reasoning (0–25): __
- Engagement (0–20): __
- Clarity (0–10): __
- Fairness (0–5): __
- **Total (0–100): __**

**Citations check (optional):**
- Best-used claim IDs: …
- Most-misused claim IDs: …

---

## 7) Logistics (where to run it)

Recommended:
- Run the debate in a **single GitHub issue** (or a single doc) so judges can scroll one thread.
- Moderator posts the format + enforces turn order.
- Teams label each entry with a header:
  - `## PRO Opening`, `## CON Opening`, `## Cross-Ex (PRO→CON)`, etc.

---

## 8) “Rules of the road”

- **Civility:** be tough on arguments, not people.
- **No gotchas:** if you think a claim is being misused, quote the relevant line from `claims.md` and explain.
- **Concessions are strength:** judges should reward explicit narrowing (e.g., “even if X, we still win because Y”).

