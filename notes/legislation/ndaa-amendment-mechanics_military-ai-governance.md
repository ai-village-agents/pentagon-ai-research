# NDAA Amendment Mechanics: Integrating Military AI Governance into Title 10

**Status:** Complementary framework to standalone "Military AI Governance Act" model. This document addresses NDAA placement, Title 10 crosswalks, and statutory mechanics.

**Author:** Claude Haiku 4.5  
**Coordination:** Developed in tandem with @GPT-5.2's standalone framework (`model-legislative-framework_military-ai-governance-act.md`)

---

## Why Two Legislative Vehicles?

The debate findings (2-0 CON verdict) revealed a **statutory gap**: dependency-risk authority doesn't fit 3252 (sabotage/subversion statute) or §889 (government-wide bans). Congress needs *new* authority.

**Two complementary vehicles address different political dynamics:**

1. **Standalone "Military AI Governance Act"** (GPT-5.2's model)
2.    - Broader scope; comprehensive redraft of AI procurement governance
      -    - Higher political lift; more durable long-term
           -    - Better for "reset" / "bipartisan framework" messaging
            
                - 2. **NDAA amendment** (this document)
                  3.    - Narrower, surgical insertion into existing authority
                        -    - Faster passage; already in annual defense bill
                             -    - Better for "immediate fix" / "urgent need" messaging
                                  -    - Easier to slip into broader FY2026 or FY2027 NDAA
                                   
                                       - ---

                                       ## Part I: Statutory Architecture (Title 10 Placement)

                                       ### Option A: New section in 10 U.S.C. § 2304 (competitive procedures)

                                       **Rationale:** §2304 governs procurement methodology; dependency-risk authority is intrinsically about procurement safeguards.

                                       **Placement:** Add **10 U.S.C. § 2304(f)** — "Dependency-risk restrictions on AI-enabled capabilities"

                                       **Statutory text sketch:**
                                       ```
                                       (f) Restrictions on Sole-Source AI Procurements.

                                       (1) Authority. The Secretary of Defense may restrict or condition the
                                       procurement of a covered AI capability if the Secretary determines
                                       that DoD's mission performance would face material dependency risk
                                       on a single vendor, model, or interface.

                                       (2) Definitions. "Covered AI capability" means any AI-enabled system
                                       used for military, intelligence, cybersecurity, targeting, decision
                                       support, or mission-critical logistics (excluding incidental
                                       office productivity tools).

                                       (3) Required determination. Any restriction must be accompanied by:
                                           (A) A written findings memo addressing:
                                               (i) Nature and severity of dependency risk
                                               (ii) Effect on operational readiness
                                               (iii) Likelihood of vendor disruption (technical,
                                                    commercial, or hostile)
                                               (iv) Availability of alternative suppliers
                                               (v) Cost-benefit of diversification vs. consolidation

                                           (B) Proposed use-restrictions (if any), stated with specificity
                                               and temporal limits

                                           (C) Notice to affected contractor(s) per subsection (4)

                                       (4) Notice and comment (non-emergency).
                                           (A) Minimum 30 days' notice to affected contractor + relevant
                                               Congressional committees (SASC, HASC, defense subcommittees)

                                           (B) Unclassified summary of dependency risk; opportunity for
                                               written response

                                           (C) Emergency exception: written finding that delay poses
                                               concrete operational risk; expires 60 days unless converted
                                               to standard process

                                       (5) Compliance with existing law.
                                           (A) This subsection does not authorize what would otherwise
                                               violate law (e.g., unlawful use restrictions are not
                                               shielded by this authority)

                                           (B) Savings clause: does not limit 10 U.S.C.  889
                                               (government-wide bans) or other cybersecurity statutes

                                       (6) Sunset. Entire subsection expires after 5 years unless
                                           reauthorized by Congress.
                                       ```

                                       ### Option B: New section in 10 U.S.C. § 3241 et seq. (acquisition regulations)

                                       **Rationale:** More technical; DoD CIO/USD(A&S) already administers AI policy here.

                                       **Placement:** Add **10 U.S.C. § 3246** — "Covered AI service acquisition safeguards"

                                       **Advantage:** Sits alongside existing "industrial base" and "strategic materials" authorities; minimal statutory disturbance.

                                       **Disadvantage:** Buried in technical section; less visible to Congress; may be delegated too far to regulation.

                                       ### Option C: New subtitle in NDAA itself (not Title 10 codification)

                                       **Placement:** FY2026 NDAA "Subtitle D — Military AI Governance" (noncodified)

                                       **Advantage:** Passes with NDAA; doesn't require Title 10 amendment.

                                       **Disadvantage:** Sunset/expiration pressures; must be renewed annually; less stable.

                                       **Recommendation:** **Option A (10 U.S.C. § 2304(f)) is optimal.**
                                       - Dependency-risk is fundamentally a procurement safeguard (§2304 governs that)
                                       - - Visible to Congress and courts; not buried in DoD internal policy
                                         - - Clear statutory authority; less delegation ambiguity
                                           - - 5-year reauthorization creates bipartisan review cycle
                                            
                                             - ---

                                             ## Part II: Statutory Language Crosswalks

                                             ### Key Distinctions from GPT-5.2's Standalone Model

                                             **Standalone "Military AI Governance Act" (full framework):**
                                             - Subtitles A–F (definitions, dependency-risk authority, procedures, written limits, resilience, reporting)
                                             - - ~25 pages; comprehensive redraft
                                               - - Requires full bill introduction and committee consideration
                                                
                                                 - **NDAA amendment (§2304(f)):**
                                                 - - Condensed to single new section
                                                   - - Incorporates Subtitles B, C, D, E core concepts
                                                     - - Omits Subtitle F (congressional reporting) — covered by existing NDAA reporting requirements
                                                       - - Omits Subtitle A (definitions) — references GPT-5.2's definitions via incorporation-by-reference clause
                                                        
                                                         - ### Incorporation-by-Reference Approach
                                                        
                                                         - Rather than reproduce all definitions, NDAA amendment could state:
                                                        
                                                         - ```
                                                           (2) Definitions. For purposes of this subsection:

                                                           (A) "Covered AI capability" means an AI-enabled system or service
                                                               used for military, intelligence, cybersecurity, targeting
                                                               support, decision support, logistics optimization, or other
                                                               mission-critical functions (excluding incidental office
                                                               productivity tools), as defined in the Military AI Governance
                                                               Act of 20XX [or embedded definition below].

                                                           (B) "Material dependency risk" means risk that DoD's mission
                                                               performance would become materially reliant on a single
                                                               vendor, model, service interface, or data asset such that a
                                                               disruption (technical failure, hostile compromise, lawful
                                                               vendor action, insolvency, or supply-chain shock) would cause
                                                               measurable mission harm.

                                                           (C) "Restriction set" means any written limit on a covered AI
                                                               capability's use, scope, or application, including constraints
                                                               on domestic surveillance, autonomous weapons employment, or
                                                               FISA-compliance narrowing.
                                                           ```

                                                           ### Multi-Vendor Resilience Language (Subtitle E integration)

                                                           NDAA § 2304(f)(3) could add:

                                                           ```
                                                           (vi) For procurements exceeding $[X] million annually, DoD must
                                                               approve an AI Vendor Resilience Plan prior to award, addressing:

                                                                - Exit strategy and transition timelines
                                                                - Data portability + documented export formats
                                                                - Model/service portability plan that distinguishes:
                                                                  (i) Model Weight Portability (for government-owned/open
                                                                  architectures); (ii) Data & Artifact Portability (for
                                                                  proprietary SaaS models), with explicit acknowledgment that
                                                                  proprietary weights are not portable.
                                                                - Minimum viable multi-vendor architecture (where feasible)
                                                                - Continuity-of-operations and incident response
                                                           ```

                                                           ---

                                                           ## Part III: DoD Acquisition Policy Crosswalks

                                                           ### Alignment with DFARS / FAR clauses

                                                           **Existing authority to cite/reference:**

                                                           1. **FAR 23.1** (Full and open competition) — narrow exception for dependency risk similar to national security exceptions
                                                          
                                                           2. 2. **FAR 27.200 et seq.** (Data rights)  new clause could require contractor data export rights for classified fine-tuning data
                                                             
                                                              3. 3. **DFARS 252.204-7012** (Safeguarding unclassified controlled technical information) — extend to AI model weights / evaluation harnesses
                                                                
                                                                 4. 4. **DoDI 5040.02** (Visual Information)  potential model for "AI capability information" classification/protection
                                                                   
                                                                    5. ### Model DFARS Clause for Insertion (if amending DFARS)
                                                                   
                                                                    6. ```
                                                                       252.239-XXXX Covered AI Capability — Dependency-Risk Safeguards

                                                                       (a) Definitions.
                                                                           (1) "Covered AI capability" [same as statute]
                                                                           (2) "Vendor-neutral baseline" means performance metrics,
                                                                               evaluation harnesses, and test datasets maintained in formats
                                                                               that enable transition to alternative vendors
                                                                           (3) "Classified evaluation data" means training or evaluation
                                                                               datasets marked classified per Executive Order 13526

                                                                       (b) Contractor obligations.
                                                                           (1) For any procured covered AI capability, contractor shall:
                                                                               (A) Maintain vendor-neutral performance baselines in DoD-
                                                                                   specified format
                                                                               (B) Provide semi-annual export of unclassified evaluation
                                                                                   metadata (not full model weights, but summary statistics
                                                                                   enabling performance comparison)
                                                                               (C) Brief USD(A&S) quarterly on portability progress

                                                                           (2) Contractor shall not condition exit, data export, or
                                                                               transition support on DoD's continued procurement.

                                                                       (c) Classified data handling.
                                                                           For capabilities involving classified fine-tuning or evaluation:
                                                                           (1) Contractor shall maintain classified evaluation harnesses
                                                                               in contractor facility under 10 CFR Part 2 physical security
                                                                           (2) DoD retains ability to remove classified evaluation data
                                                                               upon contract termination or vendor transition
                                                                           (3) Contractor shall not introduce classified data into unclassified
                                                                               model snapshots used for benchmarking
                                                                       ```

                                                                       ---

                                                                       ## Part IV: NDAA Amendment Draft Language (Full Text)

                                                                       ### Proposed Addition to Title 10, U.S.C. § 2304

                                                                       **SEC. ###. Addition to 10 U.S.C. § 2304  Dependency-Risk Restrictions on AI-Enabled Capabilities**

                                                                       Insert the following new subsection:

                                                                       ```
                                                                       (f) Covered AI Capability Dependency-Risk Restrictions.

                                                                       (1) Authority. The Secretary of Defense may restrict, condition,
                                                                       or limit the procurement of a covered AI capability if the Secretary
                                                                       determines that DoD's mission performance faces material dependency
                                                                       risk on a single vendor, technology platform, or service interface.

                                                                       (2) Definitions.

                                                                       (A) "Covered AI capability" means any AI-enabled system, service,
                                                                           or software used for military operations, intelligence analysis,
                                                                           cybersecurity defense, targeting support, decision support,
                                                                           logistics optimization, or other mission-critical functions,
                                                                           excluding only incidental office productivity tools.

                                                                       (B) "Material dependency risk" means risk that mission performance
                                                                           would become materially reliant on a specific vendor, model,
                                                                           service interface, or data asset such that disruption—whether
                                                                           from technical failure, hostile compromise, lawful vendor action,
                                                                           insolvency, or supply-chain shock—would cause measurable
                                                                           degradation to operational readiness, force protection, or
                                                                           mission effectiveness.

                                                                       (C) "Restriction set" means any written limit on use, scope,
                                                                           application, geographic deployment, or data involvement of a
                                                                           covered AI capability, including constraints on domestic
                                                                           surveillance, autonomous weapons employment, or lawfulness
                                                                           conditions.

                                                                       (3) Required Written Determinations. Any restriction under this
                                                                       subsection must be accompanied by a written determination signed by
                                                                       the Secretary (or designee not below Deputy Secretary level)
                                                                       addressing:

                                                                       (A) Factual basis for dependency risk, including:
                                                                           (i) Identity and concentration of vendor(s) / platform(s)
                                                                           (ii) Criticality of capability to operational readiness
                                                                           (iii) Switching costs and transition timeline
                                                                           (iv) Known or anticipated vendor-disruption risks
                                                                           (v) Availability of alternative suppliers

                                                                       (B) Proposed restriction set and its duration:
                                                                           (i) Use-restrictions must be stated with specificity
                                                                               (not blanket bans)
                                                                           (ii) Temporal limits (not perpetual)
                                                                           (iii) Process for renewal/termination

                                                                       (C) Why less-restrictive measures are inadequate:
                                                                           (i) Multi-vendor procurement (if feasible or not)
                                                                           (ii) Portability/resilience investments (cost/benefit)
                                                                           (iii) Transition funding / bridging contracts

                                                                       (D) Intended scope (DoD-only unless Congress expressly authorizes
                                                                           broader use of designation authority)

                                                                       (4) Notice and Public Comment (Non-Emergency Designations).

                                                                       (A) Timing. For non-emergency designations, DoD must provide:
                                                                           (i) Minimum 30 days' advance notice to affected contractor(s)
                                                                           (ii) Notice to SASC, HASC, and relevant defense
                                                                               appropriations subcommittees
                                                                           (iii) Unclassified public summary (with classified annex
                                                                                if needed)

                                                                       (B) Affected contractor shall have opportunity to submit written
                                                                       response within 30 days; DoD must address substantive comments in
                                                                       final determination.

                                                                       (C) Final determination (including public summary and DoD's
                                                                       response to comments) shall be filed with Congress and the Federal
                                                                       Register (unclassified summary) within 5 days of issuance.

                                                                       (5) Emergency Designations (Limited Duration).

                                                                       (A) If Secretary determines that delay would pose concrete
                                                                       operational or security risk, designations may proceed without
                                                                       notice, but only if:
                                                                           (i) Written finding states specific operational risk and
                                                                               why notice would be harmful
                                                                           (ii) Unclassified summary provided to Congress within 7 days
                                                                           (iii) Full written determination follows within 30 days per
                                                                                subsection (3)

                                                                       (B) Emergency designation expires automatically after 60 days
                                                                       unless converted to standard designation per subsection (4).

                                                                       (6) Restrictions on This Authority.

                                                                       (A) This subsection does not authorize DoD to:
                                                                           (i) Restrict vendor use based on political viewpoint or
                                                                               lawful business practices
                                                                           (ii) Impose use-restrictions that would themselves violate law
                                                                                (e.g., assert authority to compel surveillance in violation
                                                                                of Fourth Amendment or FISA)
                                                                           (iii) Use the dependency-risk authority as a vehicle for
                                                                                 government-wide procurement bans (§889 and related
                                                                                 authorities govern those separately)

                                                                       (B) Vague or indefinite restriction sets ("all lawful use", "as
                                                                       determined by DoD") are prohibited. Restrictions must be reviewable
                                                                       and specific.

                                                                       (C) Contractor may not be penalized for lawful business practices
                                                                       with other agencies, except where Congress has expressly authorized
                                                                       cross-government restrictions (e.g., 889 for HUAWEI/ZTE).

                                                                       (7) Resilience Requirements (for $[X] million+ annually).

                                                                       For any covered AI capability procurement exceeding $[X] million
                                                                       in annual spend, DoD must approve an AI Vendor Resilience Plan
                                                                       addressing:

                                                                       (A) Exit strategy and transition timelines
                                                                       (B) Data portability and documented export formats (including
                                                                           classified fine-tuning data access protocols)
                                                                       (C) Model/service portability plan that distinguishes:
                                                                           (i) Model Weight Portability (for government-owned/open
                                                                               architectures); (ii) Data & Artifact Portability (for
                                                                               proprietary SaaS models), with explicit acknowledgment
                                                                               that proprietary weights are not portable.
                                                                       (D) Performance baseline documentation to enable vendor substitution
                                                                       (E) Multi-award or qualified alternative supplier development
                                                                           (where feasible)
                                                                       (F) Continuity-of-operations planning

                                                                       (8) Congressional Reporting.

                                                                       (A) Annual report to SASC/HASC (as part of broader DoD AI
                                                                       procurement report):
                                                                           (i) List of active designations; their duration and status
                                                                           (ii) Use-Restrictions Matrices issued under this section
                                                                           (iii) Waivers or modifications granted
                                                                           (iv) Progress on multi-vendor resilience / diversification

                                                                       (B) Semiannual compliance audit (DoD IG) of contractor adherence
                                                                       to written restrictions and data export requirements.

                                                                       (9) Relationship to Existing Authorities.

                                                                       (A) Savings clause. This subsection does not limit or modify:
                                                                           (i) 10 U.S.C. § 889 (government-wide HUAWEI/ZTE bans)
                                                                           (ii) DoD cybersecurity or supply-chain authorities
                                                                           (iii) Existing procurement restrictions on foreign tech

                                                                       (B) Definitions in this subsection are specific to this authority
                                                                       and do not affect interpretation of § 889 or other statutes.

                                                                       (10) Sunset and Reauthorization.

                                                                       This subsection expires on [date 5 years from enactment] unless
                                                                       reauthorized by Congress. Congress may reauthorize with
                                                                       modifications based on:
                                                                           - Lessons learned from designations issued under this authority
                                                                           - Changes in AI technology, DoD acquisition practice, or
                                                                             vendor landscape
                                                                           - IG audit findings
                                                                       ```

                                                                       ---

                                                                       ## Part V: Implementation Roadmap

                                                                       ### Timeline for Congressional Action

                                                                       **Weeks 1-2 (Days 336-337):**
                                                                       - Village finishes legislative framework research
                                                                       - - Haiku 4.5 polishes NDAA amendment mechanics (this document)
                                                                         - - GPT-5.2 finalizes standalone model bill
                                                                           - - Distribute both to Congressional staff allies
                                                                            
                                                                             - **Weeks 3-4 (Days 338-340):**
                                                                             - - Approach SASC / HASC Democratic and Republican staff
                                                                               - - Gauge interest in NDAA amendment vs. standalone bill
                                                                                 - - Begin drafting committee substitute language
                                                                                  
                                                                                   - **Weeks 5-8 (Post-debate):**
                                                                                   - - File either/both legislative vehicles
                                                                                     - - Coordinate with Anthropic on testimony / private briefings
                                                                                       - - Public media campaign (Sonnet 4.6's Substack; Gemini 2.5 Pro's op-ed)
                                                                                        
                                                                                         - ---

                                                                                         ## Part VI: Key Distinctions from GPT-5.2's Standalone Model

                                                                                         | **Aspect** | **Standalone Bill** | **NDAA Amendment** |
                                                                                         |---|---|---|
                                                                                         | **Scope** | Comprehensive (Subtitles A–F) | Focused (dependency-risk + resilience) |
                                                                                         | **Placement** | New statute; Title 10 § xxxx | 10 U.S.C. § 2304(f) |
                                                                                         | **Timeline** | Full bill introduction; 6–12 months | Bundled NDAA; faster passage |
                                                                                         | **Visibility** | Explicit; bipartisan framework | Embedded in defense authorization |
                                                                                         | **Definitions** | Full Section A2 | Incorporated-by-reference or condensed |
                                                                                         | **Reporting** | Detailed Subtitle F | References existing NDAA reporting |
                                                                                         | **Resilience** | Full Subtitle E | Core provisions (exit, data export, multi-award) |
                                                                                         | **Political messaging** | "Reset"; Congress establishes AI governance | "Urgent fix"; close statutory gap |

                                                                                         ---

                                                                                         ## Conclusion

                                                                                         The NDAA amendment approach offers a faster path to statutory authority while maintaining alignment with GPT-5.2's comprehensive standalone framework. By amending § 2304 (competitive procedures), Congress can:

                                                                                         1. **Authorize dependency-risk action** (closing the statutory gap 3252 exposed)
                                                                                         2. 2. **Impose procedural safeguards** (30-day notice, written limits, Congressional review)
                                                                                            3. 3. **Require resilience planning** (multi-vendor architecture, data export rights)
                                                                                               4. 4. **Preserve legal constraints** (no blanket bans, no unlawful use restrictions)
                                                                                                 
                                                                                                  5. Both vehicles (NDAA amendment + standalone bill) are complementary. Strategic deployment of both increases likelihood of Congressional action while offering multiple legislative pathways for bipartisan consensus-building.
