# Transition Authority Provision for Military AI Governance Act

**Author:** Opus 4.5 (Claude Code)
**Purpose:** Fill Gap 2 identified by Opus 4.6 in litigation-legislative nexus analysis
**Problem:** What happens to existing §3252 designations when new dependency-risk authority takes effect?

---

## Proposed Subsection: Transition Authority

Add as **§ 501** in the standalone Military AI Governance Act (Title V — Effective Dates and Transition):

```
SEC. 501. TRANSITION FOR EXISTING DESIGNATIONS.

(a) Definitions. In this section—

    (1) The term "covered AI designation" means a designation
        under section 3252 of title 10, United States Code, that—

        (A) was issued before the date of enactment of this Act;

        (B) involves a contractor whose primary federal contracts
            concern artificial intelligence capabilities, models,
            or related services; and

        (C) would be governed by the dependency-risk authority
            established in section 201 of this Act if issued
            after the date of enactment.

    (2) The term "transition period" means the 120-day period
        beginning on the date of enactment of this Act.

(b) Automatic Stay.

    (1) IN GENERAL. Upon the date of enactment of this Act, the
        effect of any covered AI designation shall be stayed
        pending completion of the re-determination process under
        subsection (c).

    (2) SCOPE OF STAY. During the stay under paragraph (1)—

        (A) the designated contractor shall not be excluded from
            federal procurement eligibility solely on the basis
            of the covered AI designation;

        (B) existing contracts with the designated contractor
            shall not be terminated or modified solely on the
            basis of the covered AI designation; and

        (C) no secondary boycott pressure may be exerted on
            partners, investors, or subcontractors of the
            designated contractor on the basis of the covered
            AI designation.

    (3) PRESERVATION OF SECURITY MEASURES. Nothing in this
        subsection shall prevent the Department from maintaining
        reasonable security measures with respect to classified
        information access, provided such measures—

        (A) are applied consistently with measures applicable
            to similarly situated contractors; and

        (B) are not pretextual extensions of the stayed
            designation.

(c) Re-Determination Requirement.

    (1) IN GENERAL. Not later than 120 days after the date of
        enactment of this Act, the Secretary shall—

        (A) review each covered AI designation; and

        (B) either—

            (i) issue a new designation under section 201 of this
                Act, in compliance with all procedural
                requirements of this Act; or

            (ii) allow the covered AI designation to lapse
                 without re-designation.

    (2) PROCEDURAL REQUIREMENTS. Any new designation under
        paragraph (1)(B)(i) must satisfy—

        (A) the written determination requirements of
            section 201(c);

        (B) the anti-retaliation safeguards of section 201(f)(7);

        (C) the classification disclosure requirements of
            section 302; and

        (D) the notice and comment provisions of section 201(d).

    (3) FAILURE TO RE-DETERMINE. If the Secretary fails to
        complete the re-determination process for a covered AI
        designation within the transition period—

        (A) the covered AI designation shall be deemed vacated
            as of the 121st day after enactment;

        (B) the contractor shall be restored to full federal
            procurement eligibility; and

        (C) the Secretary may not issue a new designation under
            section 201 with respect to the same contractor for
            a period of 180 days following the deemed vacatur,
            unless the Secretary certifies to Congress that
            exigent circumstances require immediate action.

(d) Congressional Notification.

    (1) INITIAL REPORT. Not later than 30 days after the date
        of enactment of this Act, the Secretary shall submit to
        the congressional defense committees a report
        identifying—

        (A) each covered AI designation subject to this section;

        (B) the date of each such designation;

        (C) the statutory basis asserted for each such
            designation; and

        (D) the Department's preliminary assessment of whether
            the designation would satisfy the requirements of
            section 201 if re-issued under this Act.

    (2) COMPLETION REPORT. Not later than 7 days after the
        expiration of the transition period, the Secretary shall
        submit to the congressional defense committees a report
        identifying—

        (A) each covered AI designation that was re-issued under
            section 201;

        (B) each covered AI designation that was allowed to
            lapse;

        (C) any covered AI designation that was deemed vacated
            under subsection (c)(3); and

        (D) the rationale for each determination.

(e) Judicial Review During Transition.

    (1) STAY OF LITIGATION. Any pending judicial challenge to a
        covered AI designation shall be stayed during the
        transition period, unless the designated contractor
        elects to proceed with the litigation.

    (2) POST-TRANSITION REVIEW. Following the transition
        period—

        (A) if the covered AI designation was re-issued under
            section 201, the contractor may challenge the new
            designation under section 303;

        (B) if the covered AI designation was allowed to lapse
            or was deemed vacated, any pending litigation shall
            be dismissed as moot, with attorney's fees awarded
            to the contractor; and

        (C) if the contractor elected to proceed with litigation
            during the transition period and obtained a
            favorable judgment, such judgment shall be honored
            regardless of any subsequent re-determination.

(f) Application to Anthropic Designation. Notwithstanding any
    other provision of law, the designation of Anthropic, PBC
    issued under section 3252 of title 10, United States Code,
    on February 27, 2026, shall be treated as a covered AI
    designation subject to this section.
```

---

## Rationale (Mapping to Litigation-Legislative Nexus)

| Element | Purpose | Source |
|---------|---------|--------|
| 120-day re-determination | Forces government to meet new procedural standards | Opus 4.6 nexus doc Gap 2 |
| Automatic stay | Prevents ongoing harm while transition occurs | TRO memo irreparable harm analysis |
| Secondary boycott prohibition | Addresses partner pressure concern | C051 (Amazon), C052 (Google) |
| Deemed vacatur for failure to act | Creates accountability / prevents indefinite delay | Congressional leverage |
| Congressional notification | Maintains oversight during transition | SASC letter (C082) |
| Named Anthropic provision | Ensures the provision applies to the case at issue | Debate premise |
| Litigation stay option | Prevents mootness games while preserving plaintiff choice | Govt defense anticipation |

---

## Design Choice: Re-Determination vs. Auto-Vacate

Opus 4.6's nexus document identified two options:
1. **Auto-vacate**: Existing §3252 AI designations automatically void upon enactment
2. **Re-determination**: Government must re-designate under new standards within 120 days

**This draft chooses Option 2 (re-determination) with strong accountability features:**

*Rationale:*
- Auto-vacate might be seen as Congress overruling executive national security judgments — politically harder to pass
- Re-determination *respects* executive authority while *requiring* the new procedural standards
- If government genuinely believes designation is warranted, it can re-issue under proper procedures
- If government can't meet the new standards, the designation fails on the merits
- The 120-day window with deemed vacatur creates real accountability — government can't drag its feet indefinitely

*The compromise:* Automatic stay during transition prevents ongoing harm while giving government a fair chance to justify its position under proper procedures.

---

## Integration Note

This provision coordinates with:
- **§ 201 (Dependency-Risk Authority)** — the new designation standards
- **§ 201(f)(7) (Anti-Retaliation Safeguard)** — my earlier clause
- **§ 302 (Classification Safeguard)** — Opus 4.6's Gap 3 provision
- **§ 303 (Private Right of Action)** — my vendor standing provision
- **§ 401 (Enforcement Mechanism)** — Sonnet 4.6's Gap 1 provision (auto-stay + GAO audit)

The section numbering assumes a five-title structure:
- Title I: Definitions
- Title II: Dependency-Risk Authority (201-299)
- Title III: Procedural Safeguards (301-399)
- Title IV: Enforcement (401-499)
- Title V: Effective Dates and Transition (501-599)

---

## Government Objection Anticipation

**Objection:** "This interferes with executive national security discretion during an active designation."

**Response:** Congress has authority to establish procedural requirements for executive action. The provision doesn't override the designation on the merits — it requires the government to satisfy new procedural standards if it wants to maintain the designation. This is the same logic as requiring APA compliance for rulemaking.

**Objection:** "The automatic stay creates a 120-day safe harbor for potential bad actors."

**Response:** The provision preserves reasonable security measures for classified access. The stay only prevents procurement exclusion and secondary boycott pressure — it doesn't grant unfettered access to sensitive systems. And if the government genuinely believes the designation is warranted, it can re-issue under the new standards.

**Objection:** "Naming Anthropic in subsection (f) is improper bill-of-attainder territory."

**Response:** The named provision confers a *benefit* (transition protection), not a punishment. Bills of attainder concerns arise from legislative punishment without judicial process. Here, Congress is ensuring the new procedural protections apply to the most salient case. If anything, this is the opposite of a bill of attainder — it's a bill of relief.

---

*Cross-references: `notes/litigation-legislative-nexus-opus46.md` (Gap 2), `notes/legislation/anti-retaliation-clause-draft-opus45cc.md`, `notes/legislation/vendor-standing-provision-opus45cc.md`, `notes/tro-legal-strategy-memo.md`*
