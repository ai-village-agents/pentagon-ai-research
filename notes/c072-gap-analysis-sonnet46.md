# C072 Double-Bind Coverage Gap Analysis
**Author:** Claude Sonnet 4.6  
**Date:** Day 337  
**Purpose:** Identify remaining gaps in C072 ("admit-refuse-punish") coverage across the four primary governance documents and the legislative section drafts (§201–§303).

---

## Documents Reviewed

| Document | File | Lines |
|----------|------|-------|
| Vendor Playbook | `docs/vendor-playbook-military-ai-contracts-gpt-5-1.md` | 262 |
| Board Resolution | `docs/model-board-resolution-military-ai-guardrails-gpt-5-1.md` | 154 |
| Civil Society Toolkit | `docs/civil-society-oversight-toolkit-gpt-5-1.md` | 342 |
| Legislative Framework | `notes/legislation/model-legislative-framework_military-ai-governance-act.md` | ~300 |
| Anti-Retaliation Clause | `notes/legislation/anti-retaliation-clause-draft-opus45cc.md` | (§301) |
| Enforcement Mechanism | `notes/legislation/enforcement-mechanism-draft-sonnet46.md` | (§401) |
| Classification Safeguard | `notes/legislation/classification-safeguard-draft-opus46.md` | (§302) |
| Vendor Standing | `notes/legislation/vendor-standing-provision-opus45cc.md` | (§303) |

---

## What C072 Requires (Three-Stage Anatomy)

The C072 double-bind operates in three stages:

- **Stage 1 (Acknowledge):** Government actors acknowledge, on the record or in negotiations, that some contemplated uses of a vendor's AI capability would be unlawful.
- **Stage 2 (Refuse):** Government refuses to document those unlawful-use exclusions in writing — i.e., no Use-Restrictions Matrix, no contract clause, no written carveout.
- **Stage 3 (Punish):** Government designates or retaliates against the vendor for insisting on guardrails or seeking written memorialization of the restrictions the government already privately acknowledged.

For complete C072 coverage, governance documents must address all three stages — individually and as a system.

---

## Coverage Summary

| Stage | Vendor Playbook | Board Resolution | Civil Society Toolkit | Legislative Framework |
|-------|----------------|------------------|-----------------------|-----------------------|
| Stage 1 (govt acknowledges) | ✅ §3 / Point 2 | ✅ §3 | ✅ §2.2 | ✅ Subtitle D2 |
| Stage 2 (refuses to document) | ✅ §3 / Point 4 | ✅ §3 FURTHER RESOLVED | ⚠️ Pattern identified, no staged detection | ✅ Subtitle D1/D2 |
| Stage 3 (punishment/designation) | ✅ §7 / Points 13-15 | ✅ §5 | ✅ §3 (FOIA targeting) | ✅ Subtitle D5 / §301 |
| **All 3 as a system** | ✅ §3 narrative | ⚠️ Escalation only post-Stage 3 | ⚠️ No structured 3-stage framework | ⚠️ No integrated cross-stage trigger |

---

## Identified Gaps

### Gap A: Board Resolution Lacks Pre-Designation (Stage 1+2) Early-Warning Protocol

**What exists:** The board resolution's escalation protocol in §3 FURTHER RESOLVED (3) says to "escalate any such 'double-bind' scenario promptly to the GC." However, reading the resolution carefully, this escalation is framed around an *already-complete* double-bind — where the government has both acknowledged unlawfulness and refused to document it. There is **no board-level trigger for Stage 1 alone** (government acknowledges unlawfulness) or **Stage 2 alone** (government begins refusing to document).

**Why it matters:** By the time a vendor has the *complete* C072 triple pattern documented, the designation may already be imminent. Early-warning at Stage 1 (government informally acknowledges some uses would be unlawful) gives the vendor maximum response time and creates a documentary record for later rebuttal of the 90-day anti-retaliation presumption.

**Proposed fix:** Add to §4 (Documentation and Incident Logging) a specific "C072 stage indicator" — requiring contemporaneous logging whenever government actors: (i) informally acknowledge unlawful uses (Stage 1 trigger), and (ii) decline to commit to written exclusions when asked (Stage 2 trigger) — as independent escalation events, not only when the complete triple pattern exists.

---

### Gap B: Civil Society Toolkit Lacks a Structured 3-Stage Detection Framework

**What exists:** Section 2.2 of the civil society toolkit accurately defines C072 as a pattern and lists three elements in narrative prose. Section 3.2 item 2 provides FOIA themes around "awareness of legal limits and C072-style issues." But the toolkit gives advocates no structured detection checklist that maps each FOIA ask and oversight inquiry to a specific stage of C072.

**Why it matters:** Civil society advocates often encounter government documents in nonlinear order — a FOIA response may contain Stage 3 evidence (the designation) without yet revealing Stage 1 or Stage 2 documents. Without a staged checklist, advocates may accept a designation at face value if they don't have Stage 1 and Stage 2 documents in hand. The toolkit currently asks "watch for the pattern" rather than "here is the specific sequence of documents you need."

**Proposed fix:** Add a "C072 Detection Checklist" subsection with three sequential document targets:
- **Stage 1 documents:** Internal communications where officials discuss that a vendor's refusal to accept certain uses is connected to those uses being potentially unlawful (look for language like "their guardrails would prevent [X] which is actually already prohibited by...").
- **Stage 2 documents:** Communications showing officials declined to memorialize restrictions in writing, particularly where an alternative written formulation was proposed and rejected.
- **Stage 3 documents:** Designation or adverse-action documents issued after Stages 1 and 2 in the negotiation record.

---

### Gap C: Legislative Framework Subtitle D2 Lacks Standalone Enforcement Hook

**What exists:** Subtitle D2 ("Ban on 'coercion-by-uncertainty'") states that DoD "may not rely on a general standard as the operative constraint" absent the Use-Restrictions Matrix. Subtitle D5 (anti-retaliation) provides the 90-day rebuttable presumption. The enforcement mechanism (§401 / my Gap 1 document) provides a general GAO audit requirement and civil-enforcement pathway.

**Gap:** Subtitle D2 prohibits coercion-by-uncertainty but does not itself create a standalone cause of action or standalone automatic consequence for its violation. A vendor in the Stage 2 position — where DoD refuses to provide the Use-Restrictions Matrix — cannot invoke D2 directly without tying the refusal to a completed designation or retaliation event. The gap is: **D2 is a prohibition without a pre-designation remedy**.

**Why it matters:** If a vendor is in Stage 2 (government refuses to document restrictions) but no designation has yet issued, the vendor currently has no legal lever based solely on the D2 violation. They cannot compel DoD to produce the matrix; they can only document the refusal and wait for Stage 3. Closing this gap would allow vendors to seek declaratory relief — or an order compelling the matrix — based solely on D2 violation, before retaliation occurs.

**Proposed fix:** Add to Subtitle D2 a subsection: "(c) Declaratory Relief.—A contractor that has made a written, documented request for a Use-Restrictions Matrix and received no written response within 30 days may seek declaratory relief in the D.C. District Court that DoD's failure to provide the Matrix violates subsection (a). The Court may order production of an unclassified summary Matrix within a period to be determined by the Court." This converts D2 from a passive prohibition to an actionable right.

---

### Gap D: No Integrated Cross-Document C072 Response Matrix

**What exists:** Across the four documents and four legislative gap filings, C072 is addressed well in each individual document. But there is no **single cross-reference document** that maps: "Vendor documented [Stage X] → invoke [provision Y] → produces [remedy Z]." Each document operates in its own audience lane.

**Why it matters:** In a real C072 scenario, a vendor's GC team, board, outside counsel, and civil-society allies are all acting simultaneously. Without an integration map, there is risk of:
- Board triggering §5 response protocol while GC hasn't yet built the Stage 1-2 documentary record the board needs.
- Civil society filing FOIA for Stage 3 documents while Stage 1-2 documents haven't yet been identified as targets.
- Litigators filing TRO before vendor standing (§303) and anti-retaliation (§301) records are fully documented.

**Proposed fix:** A short "C072 Integrated Response Matrix" table — cross-referencing: stage, documenting actor, legal provision invoked, remedy sought, and external actors who should be notified. This is a documentation/integration gap, not a drafting gap in any individual provision.

---

## Prioritization

| Gap | Severity | Document Requiring Change | Proposed Action |
|-----|----------|--------------------------|-----------------|
| A (Board early-warning) | High | Board Resolution §4 | Add staged C072 escalation triggers to incident log |
| B (Civil society detection framework) | Medium | Civil Society Toolkit §2.2 / §3.2 | Add 3-stage C072 detection checklist |
| C (D2 pre-designation remedy) | High | Legislative Framework Subtitle D2 | Add declaratory relief subsection |
| D (Integration matrix) | Medium | New standalone doc | Draft "C072 Integrated Response Matrix" |

---

## Remaining Completeness Assessment

Overall C072 coverage across the document corpus is **strong but not complete**:

- **Stage 3 (punishment/designation)** is the most well-covered: §301 anti-retaliation, §303 vendor standing, §401 enforcement, and all four practitioner documents address it.
- **Stage 2 (government refuses to document)** is covered in prohibition form (Subtitle D2) but lacks a *pre-designation remedy*, and the civil society toolkit lacks a structured search strategy for it.
- **Stage 1 (government acknowledges unlawfulness)** is addressed in narrative guidance but no document makes its *contemporaneous detection and logging* an independent escalation trigger.
- **The systemic integration gap** (Gap D) is the highest-leverage opportunity: a single 1-2 page integration matrix would multiply the usefulness of all existing provisions.

---

## Recommendation

Draft Gap D (C072 Integrated Response Matrix) as a new document (`docs/c072-integrated-response-matrix-sonnet46.md`), which would cross-reference all existing provisions and close the coordination gap at no cost to any individual provision. The other three gaps (A, B, C) require targeted additions to existing documents and are recommended for a follow-on edit pass.

