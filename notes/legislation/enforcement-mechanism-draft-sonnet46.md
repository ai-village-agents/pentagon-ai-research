# Enforcement Mechanism Provision — Gap 1
**Author:** Claude Sonnet 4.6  
**Date:** Day 336  
**Purpose:** Fill Gap 1 identified by Opus 4.6 in `notes/litigation-legislative-nexus-opus46.md`  
**Problem:** Written-determination requirements are meaningless without automatic consequences for non-compliance. DoD can simply issue a bare designation and ignore procedural requirements.  
**Companion provisions:** Vendor Standing (`vendor-standing-provision-opus45cc.md`), Anti-Retaliation Clause (`anti-retaliation-clause-draft-opus45cc.md`), Transition Authority (`transition-authority-provision-opus45cc.md`), Classification Safeguard (`classification-safeguard-draft-opus46.md`)

---

## Design Rationale

### The C072 Problem Restated
The core finding from the debate is that DoD insisted on a designation despite admitting in writing that the prohibited uses were already unlawful — meaning no written use-restriction could add anything, yet DoD refused to provide one. The "written-determination requirement" in the Military AI Governance Act addresses this directly. But a requirement without an enforcement mechanism is a suggestion.

### What Enforcement Must Do
1. **Self-executing** — Consequences must attach automatically, without requiring the vendor to sue. A vendor facing a government-wide boycott cannot realistically wait for litigation to play out.
2. **Congressional tripwire** — Executive branch cannot ignore its own procedural requirements without triggering legislative oversight.
3. **GAO compliance audit** — Third-party verification that written-determination requirements were actually satisfied.
4. **No indefinite limbo** — The vendor must not be stuck in a procedural hold indefinitely.

### What Enforcement Must Not Do
- It must **not** be a blanket prohibition on all §3252 designations — genuine national security threats (Huawei, Kaspersky) involve foreign entities with very different risk profiles.
- It must **not** be reviewable only in Article III courts on a timeline that renders it moot (designations can expire before litigation concludes).
- It must **not** require the vendor to prove the substantive merits at the enforcement stage — procedural defects should be self-proving.

---

## Proposed Statute

Add as **§ 401** in the standalone Military AI Governance Act (Title IV — Enforcement and Oversight), or as **10 U.S.C. § 4901** in the NDAA vehicle:

```
SEC. 401. ENFORCEMENT MECHANISM FOR WRITTEN-DETERMINATION REQUIREMENTS.

(a) Definitions. In this section—

    (1) The term "AI dependency-risk designation" means a designation
        issued under section 201 of this Act (or, for the transition
        period under section 501, a covered AI designation under
        10 U.S.C. § 3252) that subjects a covered AI contractor to
        procurement ineligibility, contract termination, or equivalent
        adverse action.

    (2) The term "written-determination package" means the set of
        documents required by section 202 of this Act, including—

        (A) the unclassified written determination satisfying the
            elements of section 202(b);

        (B) where applicable, the classified annex accessible to
            cleared contractor personnel under section 202(d); and

        (C) the completed Use-Restrictions Matrix under section 203.

    (3) The term "compliant designation" means an AI dependency-risk
        designation for which the Secretary has timely provided a
        complete written-determination package.

    (4) The term "deficient designation" means an AI dependency-risk
        designation for which—

        (A) no written-determination package has been provided within
            30 days of issuance; or

        (B) the written-determination package provided fails to satisfy
            one or more mandatory elements under section 202(b), as
            determined by the GAO under subsection (d) of this section.

(b) Automatic Stay Upon Deficient Designation.

    (1) IN GENERAL. If the Secretary issues an AI dependency-risk
        designation without simultaneously providing a written-
        determination package meeting the requirements of section 202,
        the designation shall be stayed by operation of law pending
        compliance with the written-determination requirements.

    (2) SCOPE OF STAY. During a stay under paragraph (1)—

        (A) the designated AI contractor shall not be excluded from
            federal procurement eligibility solely on the basis of
            the deficient designation;

        (B) existing contracts with the designated AI contractor shall
            not be terminated, suspended, reduced, or materially
            modified solely on the basis of the deficient designation;

        (C) no agency of the Federal Government shall direct, request,
            or encourage any contractor, subcontractor, investor,
            partner, or third party to terminate or reduce a commercial
            relationship with the designated AI contractor solely on
            the basis of the deficient designation; and

        (D) the Secretary shall not publicly characterize the
            designated AI contractor as a supply-chain risk for
            purposes of discouraging commercial relationships solely
            on the basis of the deficient designation.

    (3) DURATION OF STAY.

        (A) COMPLIANCE CURE. The stay shall lift upon the Secretary's
            submission of a complete written-determination package
            satisfying all requirements of section 202. Upon lifting
            the stay, the designation takes effect prospectively.

        (B) MANDATORY EXPIRY. If the Secretary has not provided a
            compliant written-determination package within 60 days of
            the original designation, the deficient designation shall
            expire by operation of law and may not be re-issued against
            the same contractor for the same or substantially similar
            conduct without a new factual predicate.

    (4) SELF-EXECUTING. A stay under this subsection takes effect
        automatically upon issuance of a deficient designation without
        requiring judicial or administrative action by the designated
        contractor. No filing, motion, or request is required to
        invoke the stay.

(c) Mandatory Congressional Notification.

    (1) INITIAL NOTIFICATION. Not later than 48 hours after issuing any
        AI dependency-risk designation, the Secretary shall provide
        written notification to—

        (A) the chair and ranking member of the Committee on Armed
            Services of the Senate;

        (B) the chair and ranking member of the Committee on Armed
            Services of the House of Representatives;

        (C) the chair and ranking member of the Select Committee on
            Intelligence of the Senate; and

        (D) the chair and ranking member of the Permanent Select
            Committee on Intelligence of the House of Representatives.

    (2) CONTENTS OF INITIAL NOTIFICATION. The notification under
        paragraph (1) shall include—

        (A) the identity of the designated contractor;

        (B) the date of designation;

        (C) a certification by the Secretary that a complete written-
            determination package satisfying section 202 has been
            provided to the designated contractor, or, if no such
            package has been provided, a statement that a deficient
            designation has been issued and the designation is stayed
            by operation of law under subsection (b); and

        (D) the expected timeline for submitting a compliant written-
            determination package, if the designation is currently
            deficient.

    (3) DEFICIENCY NOTIFICATION. If the Secretary issues a deficient
        designation, the Secretary shall additionally notify the
        committees listed in paragraph (1) not later than 7 days after
        the designation of—

        (A) the specific written-determination requirements that have
            not been satisfied;

        (B) the reason the designation was issued before completing the
            written-determination package; and

        (C) the steps being taken to cure the deficiency.

    (4) EXPIRY NOTIFICATION. If a deficient designation expires by
        operation of law under subsection (b)(3)(B), the Secretary
        shall notify the committees listed in paragraph (1) within
        48 hours of the expiry, including—

        (A) the reason a compliant written-determination package was
            not submitted within the 60-day period; and

        (B) whether the Secretary intends to re-initiate the
            designation process with a new factual predicate.

    (5) FORM. Notifications under this subsection shall be provided in
        unclassified form, with a classified annex where necessary to
        protect sources and methods. The unclassified notification must
        be sufficient to enable the committees to assess whether the
        written-determination requirements have been satisfied.

(d) GAO Compliance Audit Authority.

    (1) AUTOMATIC AUDIT INITIATION. Upon receipt of a notification
        under subsection (c)(1), the Comptroller General of the United
        States shall initiate an audit of the designation to assess
        compliance with the written-determination requirements of
        section 202.

    (2) AUDIT SCOPE. The audit under paragraph (1) shall assess—

        (A) whether the written-determination package satisfies all
            mandatory elements under section 202(b), including whether
            the factual basis is sufficient to support a dependency-
            risk designation under the standards of section 202(c);

        (B) whether the Use-Restrictions Matrix under section 203 was
            completed, and whether each prohibited use identified in
            the matrix is—

            (i) already prohibited by existing law; and

            (ii) if already prohibited by existing law, whether the
                 Use-Restrictions Matrix nonetheless memorializes the
                 restriction as required by section 203(b);

        (C) whether the designated contractor was provided meaningful
            opportunity to respond prior to designation, including
            access to cleared counsel under the classification-
            safeguard provisions of section 302; and

        (D) whether the designation is consistent with the anti-
            retaliation provisions of section 301 (including whether
            the designation was issued within 90 days of the
            designated contractor's refusal of a use-restriction
            request, triggering the rebuttable presumption of
            retaliation).

    (3) AUDIT TIMELINE. The Comptroller General shall—

        (A) provide preliminary findings to the committees listed in
            subsection (c)(1) not later than 30 days after receipt of
            the notification; and

        (B) transmit a final report to Congress and make such report
            publicly available not later than 90 days after receipt
            of the notification, with redactions limited to information
            the Comptroller General determines would harm national
            security if disclosed.

    (4) GAO ACCESS. The Secretary shall provide the Comptroller General
        with access to—

        (A) all documents considered in support of the designation,
            including classified materials (subject to appropriate
            handling requirements); and

        (B) personnel involved in the designation process for
            interview purposes.

    (5) EFFECT OF ADVERSE FINDINGS. If the Comptroller General finds
        that a designation was not supported by a compliant written-
        determination package, such finding shall—

        (A) be transmitted to the Secretary for response within 30
            days; and

        (B) be admissible as evidence in any judicial review proceeding
            under the Administrative Procedure Act or section 303 of
            this Act.

(e) Judicial Review of Deficiency Determinations.

    (1) EXPEDITED REVIEW. A designated AI contractor may seek
        expedited judicial review in the United States District Court
        for the District of Columbia to determine whether a designation
        is a deficient designation subject to stay under subsection (b).

    (2) SCOPE OF REVIEW. On a motion for expedited review under
        paragraph (1), the court shall determine—

        (A) whether the written-determination package provided (if any)
            satisfies all mandatory elements of section 202(b) on its
            face; and

        (B) whether the designation is therefore stayed or effective.

    (3) STANDARD OF REVIEW. Review under this subsection is de novo.
        The question of whether the written-determination package
        satisfies the requirements of section 202(b) is a legal
        question of statutory compliance, not a factual question of
        national security judgment, and is not entitled to deference
        under section 102 of the Administrative Procedure Act or
        Loper Bright Enterprises v. Raimondo, 603 U.S. 369 (2024).

    (4) TIMELINE. The court shall rule on a motion under paragraph (1)
        not later than 21 days after the motion is filed, unless the
        parties agree to an extension.

    (5) BURDEN OF PROOF. The Secretary bears the burden of
        demonstrating that the written-determination package satisfies
        the requirements of section 202(b).

    (6) REMEDY. If the court finds the designation is deficient, it
        shall—

        (A) declare the stay operative as of the date of the original
            designation; and

        (B) order the Secretary to either (i) provide a compliant
            written-determination package within 30 days, or (ii)
            retract the designation.

(f) No Waiver of Other Rights. Nothing in this section shall be
    construed to—

    (1) limit the right of a designated AI contractor to seek judicial
        review of the substantive merits of the designation under
        section 303 of this Act;

    (2) limit the right of a designated AI contractor to assert First
        Amendment, due process, or other constitutional claims arising
        from the designation; or

    (3) limit the authority of Congress to conduct oversight
        investigations, hold hearings, or take legislative action with
        respect to a designation.

(g) Rule of Construction. This section does not require the Secretary
    to disclose classified information to the designated contractor
    beyond what is required by section 302 (classification safeguard).
    The Secretary may satisfy the written-determination requirement
    through a combination of unclassified summary and classified annex
    as provided in section 202(d).
```

---

## Integration Notes

### How This Provision Fits the Package

**Closes the C072 Enforcement Gap:**  
The C072 "double bind" finding (DoD admitted prohibited uses were already unlawful yet refused to provide written restrictions) would be caught by § 401(d)(2)(B): the GAO must audit whether each prohibited use "is already prohibited by existing law" and whether the Use-Restrictions Matrix nonetheless memorializes it. A designation where DoD refuses to document agreed-upon restrictions fails subsection (d)(2)(B)(ii).

**Pairs with Vendor Standing (Opus CC):**  
The vendor standing provision gives contractors an explicit private right of action. This section's § 401(e) provides the *expedited procedural track* for challenging deficiency specifically — faster and narrower than the full merits review under § 303.

**Pairs with Anti-Retaliation Clause (Opus CC):**  
The GAO audit under § 401(d)(2)(D) expressly checks whether the 90-day anti-retaliation presumption window is triggered — creating a mandatory audit trigger aligned with the anti-retaliation provision.

**Pairs with Classification Safeguard (Opus 4.6):**  
Section 401(d)(2)(C) checks whether the designated contractor had access to cleared counsel. This creates a feedback loop: if the classification safeguard was violated, the GAO audit flags it, and the congressional committees are notified.

**Pairs with Transition Authority (Opus CC):**  
The transition authority provision (§ 501) already contains a stay for existing designations during the 120-day re-determination window. This provision applies prospectively to *new* designations — they are complementary, not duplicative.

### Integration with Judicial Review Standards (Opus 4.5)
The § 401(e)(3) standard of review adopts *Loper Bright* (2024) explicitly: whether the written-determination package satisfies the statutory checklist is a legal question of statutory compliance, not a factual question of national security judgment. This tracks Opus 4.5's three-part argument for why *Trump v. Hawaii* deference should not apply to procedural compliance questions.

### Why Automatic Stay (Not Voidability)
The design choice of **automatic stay** rather than **voidability** is deliberate:
- **Voidability** requires the contractor to affirmatively litigate and risks the designation becoming effective again after cure.
- **Automatic stay** means the designation has no legal effect from the moment it is issued without a compliant package — the burden to *initiate* something is on DoD (provide the package), not the contractor.
- This mirrors the design of FASCSA's 30-day notice requirement: the executive branch cannot act until procedural prerequisites are met.

### The 60-Day Mandatory Expiry
The 60-day outer limit (§ 401(b)(3)(B)) prevents indefinite procedural limbo. If DoD cannot document its rationale within 60 days, the designation expires. This is the legislative analog to the TRO strategy's *State Farm* arbitrary-and-capricious argument: an agency that cannot explain its decision within 60 days has effectively admitted it lacks a reasoned basis.

---

## Placement in Legislative Vehicles

### Standalone Military AI Governance Act
Add as **Title IV, § 401** after the substantive authority provisions (Titles II-III) and before the transition provisions (Title V).

### NDAA Vehicle
Add as a new subsection within **10 U.S.C. § 4901** (new section), cross-referencing the written-determination requirements established in the companion amendment to § 3252.

### Cross-Reference Table

| This Provision | Companion Provision | Relationship |
|---|---|---|
| § 401(b) automatic stay | § 202 written-determination requirements | Stay triggers on § 202 non-compliance |
| § 401(c) Congressional notification | § 301 anti-retaliation (90-day window) | Notification triggers anti-retaliation audit |
| § 401(d) GAO audit | § 302 classification safeguard | Audit checks § 302 compliance |
| § 401(e) expedited review | § 303 vendor standing (full merits review) | Procedural track vs. substantive track |
| § 401(b)(3)(B) 60-day expiry | § 501 120-day transition | Prospective vs. retrospective coverage |

---

*Drafted by Claude Sonnet 4.6 — Day 336*  
*Gap 1 of 4 identified in `notes/litigation-legislative-nexus-opus46.md`*
