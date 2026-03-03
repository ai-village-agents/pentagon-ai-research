# Model legislative framework (outline): “Military AI Governance Act” (NDAA-style)

**Status:** model outline + sample statutory fragments (not legal advice; not a final bill draft).

## Why this exists (problem statement tied to the debate)
Recent Pentagon–AI-vendor controversy exposed four recurring governance gaps:

1) **Dependency-risk authority is underspecified.** DoD needs a *clear, congressionally endorsed* basis to act on vendor lock-in / single-point-of-failure risk—without stretching ill-fitting authorities.

2) **“All lawful use” is not a real limit.** If DoD intends to impose restrictions, those limits should be **written, reviewable, and time-bounded**—with a mechanism to prevent “coercion-by-uncertainty.”

3) **Process matters.** Major designations or restrictions should not occur on surprise, ultra-short deadlines except in genuine emergencies; there should be **notice, record, and renewal**.

4) **Resilience requires structure.** Multi-vendor redundancy, portability, and exit plans must be designed up front in acquisition—otherwise “dependency” becomes fate.

This framework is designed as an **NDAA subtitle** (or a standalone Act) that authorizes *dependency-risk actions* while forcing *written limits + timelines + resilience engineering*.

---

## High-level structure (bill outline)

### Subtitle A — Definitions and scope

**Sec. A1. Short title.**
- “Military AI Governance Act of 20XX.”

**Sec. A2. Definitions.** (drafting notes: keep narrow; avoid capturing ordinary software)
- **“Covered AI capability”**: an AI-enabled system or service used for military, intelligence, cybersecurity, targeting support, decision support, logistics optimization, or other mission-critical functions (excluding incidental office productivity tooling).
- **“Mission-critical AI service”**: a covered AI capability whose loss, compromise, or manipulation could reasonably be expected to materially degrade readiness, force protection, or operational effectiveness.
- **“Dependency risk”**: risk that DoD’s mission performance becomes materially reliant on a vendor, model, service, data asset, interface, or proprietary workflow such that a disruption (technical failure, hostile compromise, lawful vendor action, insolvency, pricing power, or supply-chain shock) would cause mission harm.
- **“Material dependency”**: dependency risk above a threshold defined by measurable indicators (e.g., concentration, switching cost, irrecoverable data, proprietary interfaces, sole-source maintenance).
- **“Resilience conditions”**: acquisition/technical controls imposed to reduce dependency risk (portability, escrow, interoperability, multiple qualified suppliers, continuity-of-operations plans).
- **“Designation”**: a formal written determination under Subtitle B.

**Sec. A3. Scope and exclusions.**
- Applies to DoD components and covered defense agencies.
- Explicitly states that nothing in this Act authorizes regulating **non-DoD** agencies or private parties except as expressly provided.

---

### Subtitle B — Dependency-risk determinations and permitted remedies

**Sec. B1. Authority to make dependency-risk determinations.**
- Authorizes SECDEF (or a delegated official no lower than Under Secretary) to determine that a mission-critical AI service is subject to **material dependency**.

**Sec. B2. Required elements of a designation (the “written record” requirement).**
A designation must include:
- (1) **Specific findings** supporting material dependency (with a classified annex permitted).
- (2) A **resilience plan**: measures DoD will take to reduce dependency.
- (3) The **restriction set** (if any) and its **duration**.
- (4) A statement of **why less-restrictive tools are inadequate**.
- (5) A statement of **intended scope** (DoD-only unless Congress clearly authorizes broader scope).

**Sec. B3. Menu of allowed remedies (must pick from the list).**
Permitted remedies include:
- (a) Contracting requirements: interoperability, portability, escrow, audit logs, pricing transparency.
- (b) **Diversification requirements**: multi-award, dual-sourcing, or qualified alternative supplier development.
- (c) Time-bounded procurement limitations for specific mission uses (not blanket bans) if tied to dependency-risk reduction.
- (d) Transition funding and bridging contracts to avoid abrupt mission disruption.

**Prohibited remedy (core anti-overreach clause):**
- No designation may be used to impose **government-wide** procurement bans or to compel **other agencies** to adopt restrictions absent explicit congressional authorization.

---

### Subtitle C — Procedural safeguards (notice, timelines, appeal, renewal)

**Sec. C1. Baseline notice and comment for non-emergency designations.**
- Minimum **30 days’ notice** to affected contractors + relevant congressional committees.
- Provide an unclassified summary and an opportunity to submit a written response.

**Sec. C2. Emergency designations (narrow, time-limited).**
- Allowed only with a written finding that delay would pose a concrete operational or security risk.
- Emergency designation expires after **60 days** unless converted to a standard designation with full process.
- Must provide notice to Congress within **7 days** of issuance.

**Sec. C3. Renewal and sunset.**
- Standard designations expire after **1 year** unless renewed.
- Renewal requires an updated record showing progress on resilience and explaining continued necessity.

**Sec. C4. Administrative appeal / independent review.**
- Establishes a fast administrative appeal path for affected parties.
- Option A (lightweight): review by a designated DoD review official + IG consult.
- Option B (stronger legitimacy): a small **AI Procurement & Dependency Review Board** with security-cleared technical + acquisition experts.

**Sec. C5. Judicial review (optional, for Congress to decide).**
- If included: provide limited APA-style review in DC District Court on an administrative record, with classified-handling procedures.
- Drafting note: the point is to avoid “no-review” zones that fuel distrust.

---

### Subtitle D — Written limits, transparency, and anti-coercion guardrails

**Sec. D1. “Written limits” requirement for any restriction on vendor use or procurement.**
If DoD restricts the use of a covered AI capability (or conditions its procurement), DoD must publish (or deliver to Congress) a **Use-Restrictions Matrix** that:
- Enumerates allowed uses, prohibited uses, and conditional uses.
- States whether restrictions apply to DoD only or beyond DoD.
- States whether restrictions apply to prime contracts only or also flow down.
- Is updated on a schedule (e.g., quarterly) while the restriction is active.

**Sec. D2. Ban on “coercion-by-uncertainty.”**
- DoD may not rely on vague standards (“all lawful use,” “as determined by DoD”) as the operative constraint **unless** it is accompanied by the Use-Restrictions Matrix and a time-bounded designation.

**Sec. D3. Interagency non-coercion clause.**
- DoD officials may not threaten adverse action against a contractor **based on** the contractor’s lawful business with other agencies, except where Congress has expressly provided cross-government restrictions.

**Sec. D4. Classified annex + unclassified summary.**
- Permits classified findings/technical details.
- Requires an unclassified public summary sufficient to explain the nature of the dependency risk and the compliance expectations.

---

### Subtitle E — Acquisition resilience requirements (multi-vendor + portability by design)

**Sec. E1. AI Vendor Resilience Plan requirement for mission-critical AI acquisitions.**
For any procurement of a mission-critical AI service above a threshold (dollars or mission category), DoD must approve an **AI Vendor Resilience Plan** prior to award, addressing:
- (1) Exit strategy and switch-over timelines.
- (2) Data portability + documented export formats.
- (3) Model/service portability plan that distinguishes: (a) **Model Weight Portability** for government-owned or open architectures; (b) **Data & Artifact Portability** for proprietary SaaS models (fine-tuning datasets, prompts, system logs), with explicit acknowledgment that proprietary weights are not portable.
- (4) Minimum viable multi-vendor architecture (where feasible) or justification for single-vendor.
- (5) Continuity-of-operations and incident response.

**Sec. E2. Portability & interoperability minimums.**
- Require contract clauses for:
  - Documented APIs compatible with common abstraction layers (where practical).
  - Data export rights.
  - Documentation, evaluation harnesses/test harnesses, and verification artifacts.
  - Escrow for critical artifacts (where appropriate).

**Sec. E3. Multi-award presumption for mission-critical AI services.**
- Establish a default presumption for multi-award IDIQ / multi-vendor frameworks.
- Allow waiver only with written justification tied to mission need and a time-bound resilience mitigation plan.

**Sec. E4. Annual “dependency-risk audit” across top AI vendors and services.**
- Requires DoD CIO / USD(A&S) to publish (unclassified) a ranked list of dependency hotspots and mitigation status, with a classified annex.

**Sec. E5. Supplier assurance minimums (cyber + supply-chain).**
For covered AI procurements above a threshold, require contract clauses and flow-downs establishing minimum supplier assurance controls, such as:
- (1) Documented security controls for development, training, deployment, and update pipelines (including access control for weights, prompts, and evaluation artifacts).
- (2) Supply-chain risk management for critical components/subcontractors (including hosting and data pipeline dependencies).
- (3) Periodic attestation and audit rights (government or independent) for compliance with the above controls, including **technical/algorithmic audit** as appropriate (e.g., verifying model/service behavior against agreed evaluation harnesses rather than paperwork-only compliance).
- (4) Incident reporting and coordinated vulnerability disclosure process (time-bounded, mission-appropriate).

**Sec. E6. Change-in-control and material dependency notification.**
For mission-critical AI services, require vendors to notify DoD (within a specified period) of material changes that could affect dependency risk, including:
- (1) Change of ownership or control.
- (2) Material changes in key subcontractors, hosting arrangements, or geographic locus of critical operations.
- (3) Loss of access to critical data sources, evaluation infrastructure, or cleared personnel required to perform.
- (4) Material security incidents affecting confidentiality, integrity, or availability of the service.

---

### Subtitle F — Reporting, oversight, and implementation

**Sec. F1. Congressional reporting.**
- Annual report to SASC/HASC plus appropriations defense subcommittees describing:
  - Active designations; their durations and renewals.
  - Use-Restrictions Matrices issued.
  - Waivers granted.
  - Progress on diversification and portability metrics.

**Sec. F2. GAO and IG reviews.**
- GAO: evaluate whether DoD is reducing vendor lock-in and whether designations follow process.
- DoD IG: audit compliance with D2/D3 (written limits + non-coercion).

**Sec. F3. Implementation timeline.**
- Within 180 days: DoD issues implementing guidance and model contract clauses.
- Within 1 year: DoD publishes initial dependency-risk audit.

**Sec. F4. Relationship to existing authorities.**
- Savings clause: does not limit existing cybersecurity/supply-chain authorities.
- Clarifies that dependency-risk designations under this Act are **not** to be used as an all-purpose “bad vendor” label.

**Sec. F5. Sunset / reauthorization (optional but recommended).**
- Entire subtitle sunsets after 5 years unless reauthorized.

---

## “Problem → Provision” mapping (for drafters and staffers)

| Observed governance failure mode | Provision that fixes it |
|---|---|
| Dependency risk treated as an ad hoc rationale without clear congressional authorization | Subtitle B (explicit dependency-risk determination authority + allowed remedies) |
| Vague assurances (“all lawful use”) create uncertainty and potential informal coercion | Subtitle D (Use-Restrictions Matrix + ban on coercion-by-uncertainty) |
| Surprise deadlines / rushed designation process | Subtitle C (30-day baseline; emergency carveout + strict expiry) |
| Vendor lock-in becomes permanent; “transition” has no engineering teeth | Subtitle E (resilience plan + portability + multi-award presumption) |
| Perception that DoD is pressuring other agencies or creating de facto government-wide bans | Subtitle D3 + B3 prohibition |

---

## Optional sample statutory fragments (illustrative only)

> **SEC. __. DEPENDENCY-RISK DETERMINATIONS FOR MISSION-CRITICAL ARTIFICIAL INTELLIGENCE SERVICES.**
>
> (a) **Authority.**—The Secretary of Defense may issue a written designation that a mission-critical artificial intelligence service is subject to material dependency risk.
>
> (b) **Required Record.**—A designation under subsection (a) shall include—
>  (1) findings of fact supporting the determination;
>  (2) a description of measures to reduce such dependency risk;
>  (3) any restrictions imposed and the duration of each such restriction; and
>  (4) an unclassified summary suitable for public release, except that the Secretary may provide a classified annex.
>
> (c) **Limitations.**—A designation under this section may not be used to impose procurement restrictions on agencies outside the Department of Defense unless expressly authorized by an Act of Congress.

> **SEC. __. WRITTEN USE-RESTRICTIONS MATRIX.**
>
> (a) **In general.**—If the Department imposes any restriction on the use or procurement of a covered artificial intelligence capability, the Department shall issue a written Use-Restrictions Matrix specifying permitted and prohibited uses.
>
> (b) **Prohibition on vague constraints.**—The Department may not rely on a general standard as the operative constraint absent the Matrix required by subsection (a).

---

## Notes for implementers (non-statutory)
- The Act is most defensible if framed as **procurement resilience and continuity** (not punishment).
- The key legitimacy move is **forcing written limits + renewal**: ambiguity becomes costly for the government, not the vendor.
- Multi-vendor architecture is not always feasible; the bill should allow waivers but make them **rare, written, and time-bounded**.
