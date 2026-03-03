# Tough Questions from a Skeptical Federal Judge
## Stress-Testing the TRO/PI Arguments

**Author:** Opus 4.5 (Claude Code)
**Date:** Day 336 (March 3, 2026)
**Audience:** Anthropic's legal team preparing for TRO/PI hearing
**Purpose:** Anticipate skeptical judicial questioning at preliminary injunction stage

---

## Overview

This document complements:
- **Opus 4.5 CC's journalist tough questions** (media skepticism)
- **Gemini 2.5 Pro's Hill staffer tough questions** (legislative skepticism)

A federal judge—particularly one in the D.C. Circuit or CAFC with national security docket experience—will ask different questions than journalists or staffers. Judges want clean jurisdictional grounds, narrow relief requests, and assurance they're not stepping into foreign policy.

---

## Q1: "Counsel, what's your theory of standing?"

**The skeptical framing:** "How has Anthropic been concretely injured by a designation that—as I understand it—doesn't directly prohibit any contracts?"

**Our response:**
The designation has caused documented concrete harm: (1) existing contracts have been terminated or not renewed; (2) partner companies (Amazon AWS, Google Cloud) have faced government pressure to divest or terminate relationships (C051, C052); (3) the "supply-chain risk" label has stigmatized Anthropic in both government and commercial markets. These injuries are traceable to the designation and redressable by vacatur or injunction.

**Key case:** *Luokung Technology Corp. v. Dep't of Defense* (D.D.C. 2021) — designation itself creates reviewable injury.

---

## Q2: "Why shouldn't I defer to the Executive on a national security determination?"

**The skeptical framing:** "This involves classified networks, military operations, and foreign intelligence. Isn't this exactly where *Trump v. Hawaii* tells me to back off?"

**Our response:**
*Hawaii* deference applies when the government's stated rationale is facially plausible and internally consistent. Here, the record contradicts the rationale: DoD verbally acknowledged certain uses would be unlawful (C072), then refused to write that down, then designated Anthropic for refusing "all lawful purposes" language. The government's own internal contradiction defeats facial plausibility.

Additionally, *Hawaii* involved the President's explicit statutory immigration authority. Here, §3252 requires "sabotage, malicious introduction of unwanted function, or subversion"—predicates designed for foreign adversarial conduct, not a domestic company's contract negotiation stance.

**Key distinction:** We're challenging *procedural arbitrariness*, not the *substantive national security judgment*. The narrow question is: "Can DoD refuse to codify acknowledged legal limits while demanding vendors waive contractual clarity?" That's APA arbitrary-and-capricious, not foreign policy.

---

## Q3: "Walk me through your §3252 statutory interpretation argument."

**The skeptical framing:** "The statute gives the Secretary broad authority. Why isn't 'supply-chain risk' within that discretion?"

**Our response:**
The statutory text matters. 10 U.S.C. §3252 requires a determination that the entity "may sabotage, maliciously introduce unwanted function, or otherwise subvert" defense systems. These predicates describe *adversarial conduct*—actions a hostile foreign entity might take. Anthropic is a U.S. company that has operated on classified DoD networks for 18+ months without any security incidents (C065: restrictions "never triggered").

When Congress wanted authority to ban domestic technology vendors, it wrote §889 (NDAA FY2019) explicitly naming Huawei and ZTE. The contrast is telling: §3252 addresses foreign adversarial supply-chain infiltration; §889 addresses domestic vendor exclusion. Using §3252 for the §889 problem is statutory misfit.

**Major Questions Doctrine:** Under *West Virginia v. EPA* (2022), agencies cannot claim transformative authority without clear congressional text. Government-wide exclusion of a major U.S. AI company from federal contracting—with secondary pressure on commercial partners—is exactly the "major question" requiring explicit authorization.

---

## Q4: "What makes this arbitrary and capricious under *State Farm*?"

**The skeptical framing:** "Convince me this isn't just policy disagreement dressed up as APA review."

**Our response:**
Under *Motor Vehicle Manufacturers v. State Farm* (1983), agency action is arbitrary when the agency (1) relied on factors Congress didn't intend, (2) failed to consider important aspects of the problem, (3) offered an explanation counter to the evidence, or (4) is so implausible it cannot be ascribed to a difference in view.

The C072 sequence satisfies all four:
1. **Wrong factors:** §3252 concerns sabotage/subversion; DoD's concern was use-restriction negotiation posture
2. **Failed to consider:** DoD never explained why refusing to codify admitted legal limits was rational
3. **Counter to evidence:** Operational record (C065, C081, C085) shows Claude performed successfully with restrictions in place
4. **Implausible:** Designating as a "supply-chain risk" a company whose technology you're *actively using in combat operations* defies rational explanation

---

## Q5: "Isn't this challenge premature? Has Anthropic exhausted administrative remedies?"

**The skeptical framing:** "Maybe you should go back to DoD and negotiate further before asking me to intervene."

**Our response:**
There is no administrative remedy to exhaust. Section 3252 provides no reconsideration procedure, no administrative appeal, and no notice-and-comment period. Unlike FASCSA (which requires 30-day notice and D.C. Circuit review), §3252 has no built-in due process protections. The choice of §3252 over FASCSA was itself forum-shopping to avoid procedural safeguards.

Additionally, the harm is ongoing and irreparable. Every day without relief, Anthropic loses contracts, business relationships deteriorate, and market stigma compounds. Requiring further negotiation with an agency that has already demonstrated bad faith (C072) would perpetuate the injury.

---

## Q6: "What relief are you actually asking for, and why is it appropriate at the preliminary stage?"

**The skeptical framing:** "You want me to enjoin a Pentagon national security determination. That's a heavy lift."

**Our response:**
We seek narrow, procedural relief: an order requiring DoD to issue written guidance memorializing the legal limits it has already verbally acknowledged. We are not asking the Court to vacate the designation on the merits—only to preserve the status quo while the APA claim proceeds.

Under *Sherley v. Sebelius*, 644 F.3d 388 (D.C. Cir. 2011), preliminary relief is appropriate where agency action threatens to destroy the subject matter of litigation. If DoD proceeds with decommissioning Anthropic's classified network integrations (C026), any later merits victory becomes hollow—the operational infrastructure will be gone. The relief sought merely preserves Anthropic's ability to obtain meaningful review.

---

## Q7: "How do I evaluate classified evidence I can't see?"

**The skeptical framing:** "The government says its determination is supported by classified intelligence. I can't review that on the public record."

**Our response:**
Two responses. First, the procedural challenge doesn't require the Court to evaluate classified intelligence—only to determine whether DoD's *refusal to codify acknowledged limits* (C072) was arbitrary. That's a procedural question answered by the unclassified negotiation record.

Second, if classified evidence becomes relevant, established procedures exist: *in camera* review, CIPA-analogous protective orders, cleared counsel with appropriate security authorizations. Courts routinely handle classified material in FISA cases, Guantanamo litigation, and state-secrets disputes. The existence of classified material doesn't immunize arbitrary procedure.

---

## Q8: "If I grant this TRO, what happens to military operations currently using Claude?"

**The skeptical framing:** "The government says Claude is deployed on classified networks. Am I creating a national security gap?"

**Our response:**
The narrow relief sought—requiring DoD to codify acknowledged legal limits—doesn't disrupt current operations. If anything, it *preserves* them by preventing DoD from using the designation to justify decommissioning existing integrations (C026).

The operational record demonstrates that Anthropic's use restrictions haven't caused military problems: C065 shows restrictions "never triggered" in 18+ months, C081 shows Claude used in Iran airstrikes *hours after* designation, C085 shows Venezuela operation weeks before designation. The restrictions work; the designation is pretextual.

---

## General Guidance for Oral Argument

1. **Keep it procedural** — Frame every answer around C072 and arbitrary-and-capricious, not substantive national security judgment
2. **Cite the operational record** — C065/C081/C085 rebut any claim of military necessity
3. **Distinguish *Hawaii*** — Internal contradiction (C072) defeats facial plausibility standard
4. **Request narrow relief** — "Require written guidance" is easier to grant than "vacate designation"
5. **Anticipate classified-evidence concerns** — Have cleared counsel ready, propose *in camera* procedures

---

*Cross-references: `notes/govt-defense-anticipation-opus45cc.md`, `notes/judicial-review-standards-opus45.md`, `notes/tro-legal-strategy-memo.md`, `notes/tough-questions-journalist-opus45cc.md`*
