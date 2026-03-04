# Law‑School Clinic Roadmap – Pentagon–Anthropic Litigation & Governance Project (GPT‑5.1)

**Audience:** law‑school clinics (admin / national security / constitutional / tech / civil‑rights), impact‑litigation orgs, and seminar‑style practicums that want to treat the Pentagon–Anthropic dispute as a **teaching simulation** for TRO/PI strategy _and_ AI‑governance reform.

**Scope:** This roadmap shows how to move from the **Issue #12 record + claims backbone** in `pentagon-ai-research` → to **mock TRO/PI litigation** → to **governance and legislative design work**, using the companion toolkit in `ai-governance-gap-proposal`.

> **Teaching Simulation, not legal advice**  
> This repository encodes a structured teaching simulation around a Pentagon–Anthropic dispute. Nothing here is legal advice. Use these materials as a classroom or training scaffold, and adapt cautiously before using anything in a real matter.

---

## 1. Core On‑Ramps (Weeks 1–2)

If you have a **12–14 week clinic or practicum**, aim to get every student oriented to the dispute, the record, and the governance concepts by the end of Week 2.

### 1.1 Initial orientation (shared for all students)

Start in this repo (`pentagon-ai-research`):

1. **Narrative explainer (homework or in‑class)**
   - `docs/public-explainer-ai-digest-gpt-5-1.md`
   - Optional supplement: `docs/public-explainer-iran-strikes-pentagon-anthropic-gpt-5-1.md` (implementation‑coherence angle).

2. **Claims backbone + indices (scaffold for all later work)**
   - `claims.md`
   - `docs/claims-by-entity-index.md`
   - `docs/claims-by-source-index.md`
   - `docs/claims-chronology-index.md`
   - `docs/key-quotes-compendium.md`
   - `docs/claims-legal-arguments-matrix.md`

3. **Debate outcome and governance frames**
   - `notes/issue12-panel-summary-gpt-5-1.md` (short summary of the debate and 2–1 verdict against the Pentagon).
   - `notes/issue12-panel-opinion-gpt-5-1.md` (long‑form judicial‑style opinion).
   - `docs/verdict-litigation-legislation-bridge-gpt-5-1.md` (how the verdict maps into TRO/PI and legislative strategies).

4. **Quick Start for instructors & students**
   - `docs/instructor-quick-start-gpt-5-1.md` (how to use one class on the case).
   - `docs/student-quick-start-reader-guide-gpt-5-1.md` (45–60 min student path).

5. **Timeline and scenario context**
   - `docs/timeline-diagram.md`
   - `docs/scenario-probability-update-day337-sonnet46.md`
   - `docs/day338-watchlist-preview-opus46.md`

### 1.2 Introduce the key frameworks (1 class)

By the end of Week 2, make sure students can:

- Explain the **S / D / G** tool‑typing framework (Sabotage/Subversion vs Dependency vs Governance) using the public explainer + panel opinion.
- Recognize the **C072 pattern** (“admit → refuse → punish”) and where it appears in the record.
- Articulate why using a **§ 3252 sabotage/subversion tool** to resolve a **guardrail dispute** can be a **Governance Category Error**.

You can lean on:

- `docs/public-explainer-ai-digest-gpt-5-1.md` (S/D/G and C072 in plain language).
- `docs/bridge-pentagon-project-to-ai-governance-gap-gpt-5-1.md` (overview of how this repo connects to the governance toolkit).

---

## 2. Clinic Structure Overview

After orientation, you can organize the clinic into **two interlocking tracks**:

1. **Impact‑Litigation Track – TRO/PI & Judicial Review**  
   Focus: model complaint, TRO/PI motion practice, admin‑record strategy, and First Amendment / APA theories.

2. **Governance & Reform Track – Boards, GCs, Legislation, FOIA**  
   Focus: vendor‑governance, board duties, legislative design, and FOIA/oversight strategies.

Students can stay in one track, or you can run a **“two‑chambers” model** where each track drafts its own work product and then trades for critique.

The sections below assume a **12‑week semester** but can be compressed.

---

## 3. Weeks 3–4 – Build Case Theory & TRO/PI Strategy

### 3.1 Litigation theory lab

Use these files to move from facts to a structured case theory:

- `docs/claims-legal-arguments-matrix.md` – master map from claims to legal theories (APA arbitrary‑and‑capricious, pretext, First Amendment coercion/retaliation, statutory misfit).
- `notes/judicial-review-standards-opus45.md` – standards of review and TRO/PI posture.
- `notes/tro-calculus.md` – harm balancing and TRO/PI calculus.
- `docs/verdict-litigation-legislation-bridge-gpt-5-1.md` – bridges the Issue #12 verdict into doctrinal hooks.

Suggested exercise:

- Assign each student (or small team) a **cluster of claims** from `claims.md`.
- Have them identify:
  - The best **APA theory** (statutory fit, arbitrary‑and‑capricious, pretext).
  - Any **First Amendment** or structural‑separation angle.
  - How S/D/G mis‑typing or C072 supports their theory.

### 3.2 TRO/PI packet scaffolding

Then route students into the **TRO/PI document layer**:

- `notes/tro-legal-strategy-memo.md` – strategic framing of a 3252‑challenge TRO.
- `docs/tro-executive-summary_court-clerk.md` – executive summary designed for a clerk or judge.
- `notes/judicial-addendum_extra-record-media-vs-admin-record_tro-pi-gpt-5-2.md` – handling extra‑record reporting vs the formal admin record.
- `notes/student-judge-bench-card-tro-simulation-gpt-5-1.md` – bench tools; have students use this as a **reverse‑engineering guide** to what a judge will care about.

Suggested outputs by end of Week 4:

- **One TRO/PI outline** per team, keyed to specific claims IDs.
- A short **“record map”** identifying which parts of `claims.md` and which sources would be central to a real TRO.

---

## 4. Weeks 5–6 – Factual Development, FOIA, and Oversight

### 4.1 FOIA and admin‑record expansion

Move students into the **FOIA/oversight toolkit** in this repo:

- `docs/foia-request-guide-index.md` – overview of FOIA strategy and request design.
- `docs/foia-letter-template-3252-risk-assessment-opus45.md` – records on the § 3252 designation rationale and risk assessment.
- `docs/foia-letter-template-cdao-assessment-sonnet46.md` – CDAO internal assessment and recommendation chain.
- `docs/foia-letter-template-hegseth-memo-opus45.md` – “AI without restrictions” memo and implementation.
- `docs/foia-letter-template-openai-amendment-sonnet46.md` – OpenAI–DoD contract amendment and safety conditions.

Suggested exercise:

- Assign each student team **one FOIA template**. Have them:
  - Tailor it to a slightly different factual hypothesis.
  - Identify how any responsive records would feed into **TRO/PI theory**, **First Amendment claims**, or **dependency‑risk arguments**.

### 4.2 Civil‑society and board‑level documentation

Introduce tools for documenting and analyzing guardrail pressure:

- `docs/guardrail-pressure-incident-template-gpt-5-1.md` – have students log a C072‑style incident based on the scenario.
- `docs/civil-society-oversight-toolkit-gpt-5-1.md` – show how NGOs could use FOIA + claims backbone + public explainers.
- `docs/board-oversight-checklist-military-ai-gpt-5-1.md` – what a board should be asking in a dispute like this.
- `docs/model-board-resolution-military-ai-guardrails-gpt-5-1.md` – model resolution committing to guardrail floors.

Suggested outputs by end of Week 6:

- A **FOIA strategy memo** (which letters, to whom, and how they connect to litigation).
- A filled‑in **guardrail‑pressure incident report** anchored in specific claim IDs.
- Short board‑brief bullets explaining why S/D/G mis‑typing is a governance failure.

---

## 5. Weeks 7–8 – Drafting the Complaint & Appellate‑Ready Record

### 5.1 Model complaint and briefing

Move students into concrete drafting:

- `docs/model-complaint-section-3252-challenge.md` – model complaint structure challenging the § 3252 designation.
- `notes/judicial-review-standards-opus45.md` (re‑used here) – to ensure counts and standards are correct.
- `notes/tro-calculus.md` – check that the complaint lines up with TRO/PI theory.

Have each team either:

- Rewrite one or two **counts** in the model complaint in their own words; or
- Draft a short **supplemental claim** (e.g., focused entirely on First Amendment coercion and vendor speech).

### 5.2 Judge‑facing tools

Use the **bench and judging tools** to stress‑test drafts:

- `notes/debate-judging-guide-gpt-5-1.md` and `notes/judge-scoring-template-gpt-5-1.md` – convert debate scoring criteria into judicial‑style evaluation checklists.
- `notes/student-judge-bench-card-tro-simulation-gpt-5-1.md` – simulate a TRO hearing and have student‑judges rule on their peers’ motions.

Suggested outputs by end of Week 8:

- A **partially rewritten model complaint** with at least one fully fleshed count per team.
- A **mock TRO hearing** or written ruling applying the bench card.

---

## 6. Weeks 9–10 – Legislation, Policy, and Governance Remedies

### 6.1 Congressional and legislative work

Route students into the **Hill‑facing materials**:

- `notes/hearing-questions-sasc-hasc-gpt-5-1.md` – structured question sets for SASC/HASC.
- `notes/hearing-closing-statement-gpt-5-1.md` – sample closing statement highlighting Governance Category Error and S/D/G mis‑typing.
- `docs/policy-reforms-anthropic-pentagon.md` – concrete statutory and oversight reform ideas.
- `docs/legislative-package-toc.md` – organizing rubric for a reform package.

Suggested exercise:

- Assign each team a **different legislative vehicle** (e.g., NDAA title, standalone AI safety act, FOIA strengthening bill).
- Have them draft:
  - A **one‑page staff memo** explaining the Pentagon–Anthropic case as a motivating example.
  - 1–2 **draft statutory sections** or report‑language snippets.

### 6.2 Vendor and board governance

Blend litigation with governance design:

- `docs/vendor-playbook-military-ai-contracts-gpt-5-1.md` – how vendors should prepare for S/D/G mis‑typing, contract pressure, and C072 incidents.
- `docs/board-oversight-checklist-military-ai-gpt-5-1.md` and `docs/model-board-resolution-military-ai-guardrails-gpt-5-1.md` – embed guardrail floors and escalation duties.
- `docs/civil-society-oversight-toolkit-gpt-5-1.md` – outside‑in pressure that complements litigation.

Have one part of the class act as **outside counsel** drafting governance recommendations to the Anthropic board, while another acts as **congressional staff**; let them negotiate what “good” governance and statutory guardrails should look like.

---

## 7. Weeks 11–12 – Cross‑Repo Governance Toolkit & Capstone

In the final phase, you pivot from this repo to the **`ai-governance-gap-proposal`** toolkit to generalize lessons.

### 7.1 Case Study A and Governance Category Error

Start here in the governance repo:

- `ai-governance-gap-proposal/case-studies/case-study-a_pentagon-anthropic.md` – treats this dispute as **Case Study A**, focused on Governance Category Error and S/D/G mis‑typing.

Have students compare:

- How the case study describes the dispute vs how **their complaint and TRO theory** describe it.
- Whether their proposed remedies align with the case study’s diagnosis of S/D/G boundary failures.

### 7.2 Regulatory & legal preparedness (WS4)

Then move into **Workstream 4** materials:

- `ai-governance-gap-proposal/docs/workstreams/regulatory-legal-preparedness-playbook-gpt-5-1.md` – playbook for GCs and regulatory leads; maps S/D/G tools and mis‑typing scenarios.
- `ai-governance-gap-proposal/docs/board-gc-ai-governance-gap-explainer-gpt-5-1.md` – concise explainer for boards and GCs.

Suggested exercise:

- Ask each litigation team to **rewrite one section** of their TRO or complaint as an **internal GC memo**, using the WS4 playbook as the target audience.

### 7.3 Governance implementation (WS1–WS3) and 180‑day plan

Close by connecting to the **implementation roadmap**:

- `ai-governance-gap-proposal/docs/workstreams/governance-implementation-playbook.md` – 30/60/90/180‑day governance implementation plan.
- `ai-governance-gap-proposal/docs/policies/factuality-and-sourcing-policy.md` – shared statement‑type and sourcing policy that underpins both repos.
- `ai-governance-gap-proposal/templates/teaching-simulation-disclaimer.md` – boilerplate disclaimer language.

Capstone assignment idea:

- Each team submits a **“dual audience” packet** consisting of:
  1. A **short TRO/PI brief segment** (5–7 pages).
  2. A **board/GC memo** explaining how to avoid ever needing that TRO by building S/D/G‑aware governance ex ante.
  3. An **NDAA or oversight proposal** (1–2 pages) that would reduce Governance Category Error risk in future Pentagon–vendor disputes.

---

## 8. Media and Public‑Facing Coordination (Optional Module)

Clinics often interact with press and public‑education partners. This repo has tools you can plug in **without turning the clinic into a PR shop**.

Useful starting points:

- `docs/journalist-cheat-sheet.md` – high‑level summary for reporters: timeline, core dispute, top claims, FOIA hooks, and unexplored angles.
- `docs/journalist-faq.md` – anticipated reporter questions and structured answers.
- `notes/press-gaggle-script-gpt-5-1.md` – sample talking points and Q&A for a press gaggle.
- `docs/press-kit/` – additional assets for media‑facing work (if updated).

Suggested uses:

- Have a small **media‑liaison team** of students who adapt the journalist cheat sheet into a **one‑page media backgrounder** for the clinic’s hypothetical case.
- Run a simulation where student‑lawyers brief student‑journalists using the cheat sheet and public explainer; emphasize sourcing discipline and Teaching Simulation framing.

---

## 9. Time‑Boxed Variants

If you have less than a full semester, you can compress the roadmap:

- **6–7 weeks:**
  - Weeks 1–2: Orientation + S/D/G + C072 (Sections 1–2).
  - Weeks 3–4: TRO/PI theory + one FOIA letter and guardrail‑pressure incident log (Sections 3–4).
  - Weeks 5–6: Model complaint section + one governance/board memo + quick read of Case Study A and WS4 playbook (Sections 5 & 7.2).
  - Optional Week 7: mock TRO hearing or Hill briefing.

- **3–4 weeks (intensive module or reading group):**
  - Session 1: Public explainer + claims backbone + S/D/G & C072.
  - Session 2: TRO/PI framing using `docs/tro-executive-summary_court-clerk.md` and `docs/model-complaint-section-3252-challenge.md`.
  - Session 3: Policy reforms and legislative work using `docs/policy-reforms-anthropic-pentagon.md` and `notes/hearing-questions-sasc-hasc-gpt-5-1.md`.
  - Session 4: Cross‑repo governance synthesis using Case Study A and WS4.

---

## 10. Sourcing, Citation, and Responsible Use

To keep clinics on‑track and aligned with the project’s norms:

- In this repo, review:
  - `SOURCING.md` – how claims are structured and sourced.
  - `docs/how-to-cite-this-repository.md` – how to cite the teaching simulation and attribute AI‑generated content.

- In the governance repo, review:
  - `ai-governance-gap-proposal/docs/policies/factuality-and-sourcing-policy.md` – statement types (Verified, Attributed, Analysis, Hypothetical) and sourcing guardrails.
  - `ai-governance-gap-proposal/templates/teaching-simulation-disclaimer.md` – language you can adapt for your own syllabi and assignments.

Encourage students to **treat Attributed claims as pointers to underlying reporting**, not as independent fact‑finding by the repo authors, and to be explicit whenever they move from **fact description → analysis → normative advocacy**.
