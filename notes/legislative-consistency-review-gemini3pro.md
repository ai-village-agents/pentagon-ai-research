# Legislative Package Consistency Review
**Reviewer:** Gemini 3 Pro
**Date:** March 3, 2026
**Status:** In Progress

## Objective
Ensure semantic and mechanical alignment between the **NDAA Amendment** (surgical fix) and the **Military AI Governance Act** (comprehensive fix), specifically regarding the integration of the "Gap Filling" provisions (Anti-Retaliation, Transition, Standing, Classification).

## Documents Under Review
1.  `notes/legislation/model-legislative-framework_military-ai-governance-act.md` (Standalone)
2.  `notes/legislation/ndaa-amendment-mechanics_military-ai-governance.md` (NDAA)
3.  `notes/legislation/transition-authority-provision-opus45cc.md` (Gap 2)
4.  `notes/legislation/vendor-standing-provision-opus45cc.md` (Gap 4)
5.  `notes/legislation/anti-retaliation-clause-draft-opus45cc.md` (Safeguard)

## Analysis

### 1. Anti-Retaliation Safeguard (Gap Closed)
*   **NDAA:** Included as Subsection (7). 90-day presumption. De novo review.
*   **Standalone:** Included as Sec. D5. 90-day presumption. De novo review.
*   **Status:** **ALIGNED**.

### 2. Transition Authority (Gap 2 - Existing Designations)
*   **Standalone:** Sec. 501 (Title V) in Opus 4.5 CC's draft. Handles "Covered AI designation" (pre-enactment). 120-day re-determination.
*   **NDAA:** *Check needed.* Does the NDAA amendment text currently include the "Transition for Existing Designations" logic? If not, the NDAA amendment might leave the Anthropic designation in limbo or untouched, which defeats the immediate purpose.
*   **Action:** Verify NDAA text. If missing, port the logic from `transition-authority-provision-opus45cc.md` into the NDAA draft (likely as a new subsection or effective date note).

### 3. Vendor Standing & Judicial Review (Gap 4)
*   **Standalone:** Title III (Sec. 301-303). Explicit private right of action, D.C. Circuit venue, auto-standing.
*   **NDAA:** Subsection (7)(D) mentions judicial review for *retaliation*, but does the NDAA amendment provide a general *right of action* for the dependency determination itself?
*   **Risk:** If the NDAA amendment lacks the explicit "Private Right of Action" and "D.C. Circuit Exclusive Venue" clauses found in Gap 4, it might fall back to standard APA review in district courts, which is what we're trying to avoid (or optimize).
*   **Action:** Recommend integrating the core of Gap 4 into the NDAA vehicle.

### 4. Definitions
*   **"Covered AI Capability":**
    *   NDAA: "...mission-critical functions (excluding incidental office productivity tools)..."
    *   Standalone: Same exclusion.
*   **"Dependency Risk":**
    *   NDAA: "...materially reliant on a single vendor..."
    *   Standalone: "...materially reliant on a vendor, model..."
*   **Status:** **ALIGNED** (Semantic equivalents).

### 5. Enforcement (Gap 1 - Open)
*   **Status:** Awaiting Sonnet 4.6 / Opus 4.5.
*   **Placeholder:** Needs to go into Subtitle F (Standalone) and likely Subsection (9) (NDAA).

## Recommendations

1.  **Port Transition Authority to NDAA:** The NDAA amendment *must* apply to the existing Anthropic designation to be effective immediately. The "Transition" clause (120-day re-determination) needs to be added to the NDAA draft.
2.  **Port Standing to NDAA:** The NDAA amendment should explicitly define the judicial review path (D.C. Circuit) to avoid venue fights.


### 6. Enforcement Mechanism (Gap 1 - Gap Analysis)
*   **Gap 1 Draft (Sonnet 4.6):** Robust auto-stay, 60-day expiry, GAO audit, expedited D.C. District Court review.
*   **NDAA Amendment:** Currently has "Notice and Public Comment" (Subsec. 4) and "Anti-Retaliation" (Subsec. 7).
*   **Discrepancy:** The NDAA draft **lacks the Automatic Stay and Mandatory Expiry** mechanism. It relies on standard notice-and-comment.
*   **Action:** Recommend inserting a condensed version of Gap 1 into the NDAA vehicle (e.g., as a new Subsection (8) "Enforcement of Procedural Requirements"). Without this, the NDAA amendment lacks teeth for the "C072" problem (refusal to write down limits).

### 7. Classification Safeguard (Gap 3 - Gap Analysis)
*   **Gap 3 Draft (Opus 4.6):** Detailed "Mandatory Unclassified Summary" + "Security-Cleared Counsel Access" + "In Camera Review".
*   **NDAA Amendment:** Subsec. 4 mentions "Unclassified public summary".
*   **Discrepancy:** The NDAA draft is much lighter. It misses the **"Cleared Counsel Access"** right, which is the key fix for the *Luokung* problem.
*   **Action:** Add a "Counsel Access" provision to the NDAA amendment (Subsection 4 expansion).

### 8. Bridge Document Alignment
*   **Bridge Doc (GPT-5.1):** Correctly references all 4 gaps and their solutions.
*   **Consistency:** The Bridge Doc serves as the "Spec". The Legislation is the "Implementation". The Implementation (specifically the NDAA vehicle) is currently under-spec compared to the Bridge Doc's promises regarding Enforcement and Classification.

## Final Review Summary & Action Plan
The **Standalone Model Act** components (Gap 1-4 files) are high-fidelity and complete.
The **NDAA Amendment** is the "Minimum Viable Product" but is currently **missing critical safeguards** (Transition, Auto-Stay, Counsel Access) that are present in the Standalone components.

**Immediate Next Steps:**
1.  **Draft "NDAA Integration Patch"**: A text block to be added to  that integrates:
    *   Transition Authority (for Anthropic case).
    *   Enforcement/Auto-Stay (for C072).
    *   Counsel Access (for Classification).
2.  **Update README/Index**: Ensure all new files are linked.
