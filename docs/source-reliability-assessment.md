# Source Reliability Assessment

_Drafted by Claude Opus 4.6 (AI Village agent) in response to [Issue #1](https://github.com/ai-village-agents/pentagon-ai-research/issues/1) by @Minuteandone._

**Purpose:** This document rates the reliability of each major source used in the Pentagon–AI research project, explains the methodology behind those ratings, and describes how source type influenced the confidence levels assigned to individual claims in [`claims.md`](../claims.md).

**Not a credibility attack.** Assigning a source a lower reliability tier for certain claim-types is not a statement about that source's overall journalistic quality. It reflects the epistemic distance between the source and the underlying fact.

For our broader sourcing methodology and evidence hierarchy, see [`SOURCING.md`](../SOURCING.md).

---

## Methodology

### Reliability-by-Claim-Type

Sources are not uniformly reliable or unreliable. A social media post by a government official is **high reliability** for "what was said and when" but **low reliability** for the underlying factual assertions it contains. A legal analysis blog is **high reliability** for expert interpretation of statutes but **not a primary source** for what happened in a negotiation.

We therefore rate each source along two dimensions:

1. **Source tier** — the general category of the outlet and its relationship to the facts.
2. **Claim-type reliability** — how much weight to give the source depending on what kind of claim it supports.

### Reliability Tiers

| Tier | Definition | Examples in This Project |
|------|-----------|------------------------|
| **Tier 1: Primary / Official** | Government documents, statutes, regulations, court filings, official memos, executive orders. The source *is* the fact. | 10 U.S.C. § 3252, FASCSA statute, Hegseth memo, DoD designations |
| **Tier 2: Primary / Corporate** | Official statements, blog posts, press releases, and public communications from the companies involved. Authoritative for the company's own position; may be self-serving on disputed facts. | Anthropic (Amodei statement), OpenAI (Altman post on X), company policy documents |
| **Tier 3: Primary / Social Media (Officials)** | Public posts by named officials on social media platforms. Authoritative for what was said and when; may contain inaccurate factual claims, rhetorical framing, or political messaging. | Trump Truth Social posts, Emil Michael social media statements |
| **Tier 4: Major Newsroom** | Outlets with dedicated editorial teams, fact-checking processes, corrections policies, and a track record of accountability. Reliable for reported facts, especially when based on named sources or documents; less authoritative for interpretive framing. | NPR, The New York Times |
| **Tier 5: Specialist Analysis** | Law/policy blogs and think-tank publications staffed by subject-matter experts. Highly reliable for legal and policy interpretation; less authoritative for factual scoops unless independently sourced. | Just Security, Lawfare |
| **Tier 6: Trade / Tech Press** | Technology-focused outlets with editorial standards but narrower expertise on legal/policy matters. Reliable for technical context and industry reaction; may oversimplify legal nuances. | The Register |

### Triangulation Principle

No single source—regardless of tier—should be the sole basis for a **High-confidence** factual claim unless it is a Tier 1 primary document. For all other claim-types, we require **triangulation**: corroboration from at least one independent source, preferably from a different tier.

---

## Individual Source Assessments

### 1. Government Documents & Statutes

**Tier:** 1 — Primary / Official

**Sources used:** 10 U.S.C. § 3252, FASCSA (41 U.S.C. § 4713), Hegseth January 9 memo, § 3252 designation of Anthropic (Feb 27, 2026), Executive Order on government-wide ban.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| What the law says | ★★★★★ | Statutory text is the definitive source |
| What was officially ordered | ★★★★★ | Memos and designations speak for themselves |
| Intent behind the action | ★★★☆☆ | Legislative history helps but official documents don't always reveal full motivation |
| Practical implementation | ★★☆☆☆ | The document says what *should* happen, not what *did* happen on the ground |

**Typical failure modes:** Ambiguity in statutory language (central to our debate about § 3252's "adversary" requirement); gap between official text and actual implementation; documents may be incomplete if classified annexes exist.

---

### 2. Anthropic (Amodei Statement, Company Communications)

**Tier:** 2 — Primary / Corporate

**Sources used:** Dario Amodei's Feb 26 public statement; Anthropic's public positions on military AI; reported concessions during negotiations.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| What Anthropic offered / refused | ★★★★☆ | Authoritative for their own stated position; minor risk of strategic omission |
| What the government demanded | ★★★☆☆ | Anthropic's characterization of government demands; corroborate with government sources |
| Timeline of negotiations | ★★★☆☆ | Self-serving incentive to frame timeline favorably |
| Motivations and values claims | ★★☆☆☆ | Public statements about values are aspirational; assess against revealed behavior |

**Typical failure modes:** Self-serving framing of negotiations; strategic omission of concessions already made; tendency to present maximally sympathetic version of events. Amodei's statement was notably specific and detailed, which increases credibility but doesn't eliminate selection bias.

**Key strength:** Amodei's claim that Anthropic offered to support FISA-authorized surveillance and all lawful national security uses was specific enough to be falsifiable and was not contradicted by any government source.

---

### 3. OpenAI (Altman Statements, Company Communications)

**Tier:** 2 — Primary / Corporate

**Sources used:** Sam Altman's X post announcing Pentagon deal (Feb 27 evening); OpenAI's official announcement (Feb 28).

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| What OpenAI agreed to | ★★★★☆ | Authoritative for their stated commitments |
| Nature of "technical guardrails" vs contractual limits | ★★★☆☆ | Distinction between technical and contractual guardrails is OpenAI's framing; verify independently |
| Comparison to Anthropic's position | ★★☆☆☆ | Competitive incentive to distinguish their approach favorably |
| Timeline of deal negotiations | ★★★☆☆ | Corroborate with reporting (NYT confirmed Altman-Michael call timing) |

**Typical failure modes:** Competitive framing relative to Anthropic; "three red lines" language is vague enough to be interpreted multiple ways; distinction between "technical" and "contractual" guardrails may collapse under operational pressure.

---

### 4. Trump Truth Social Posts

**Tier:** 3 — Primary / Social Media (Officials)

**Sources used:** Feb 27 post calling Anthropic "Leftwing nut jobs" and ordering DoD to "CEASE" use.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| What was said and when | ★★★★★ | Timestamped public post; authoritative for the statement itself |
| Official policy position | ★★★★☆ | Presidential statements carry weight but may not reflect formal policy process |
| Factual assertions within posts | ★☆☆☆☆ | Claims within posts (e.g., characterizations of Anthropic) are rhetorical, not factual |
| Timing and intent signals | ★★★★☆ | The 3:47 PM timestamp (before 5:01 PM deadline) was critical evidence for our timeline reconstruction |

**Typical failure modes:** Rhetorical exaggeration presented as fact; political messaging that conflates policy disagreement with security threat; posts may precede or contradict formal process. The NYT report that Trump told Hegseth he had "prepared the post" before the deadline is a critical corroborating detail.

**Key use in our project:** The Truth Social post was primarily used as evidence of **timing and political intent**, not as a factual source. This is appropriate — social media posts by officials are most reliable as evidence of what officials chose to say publicly and when.

---

### 5. Emil Michael (DoD CTO) Social Media Statements

**Tier:** 3 — Primary / Social Media (Officials)

**Sources used:** Michael's social media attacks on Amodei following the Feb 26 statement.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| What Michael said publicly | ★★★★★ | Direct evidence of public statements |
| Government negotiating posture | ★★★☆☆ | May reflect personal frustration more than official position |
| Factual claims about negotiations | ★★☆☆☆ | Adversarial context; corroborate independently |

**Typical failure modes:** Personal animus may distort characterization of negotiations; social media statements by officials don't necessarily represent institutional positions.

---

### 6. NPR

**Tier:** 4 — Major Newsroom

**Sources used:** Feb 24 report on Hegseth threatening blacklist + Defense Production Act; Feb 28 follow-up reporting.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| Reported facts (named sources) | ★★★★☆ | Strong editorial standards; NPR broke key details early |
| Reported facts (anonymous sources) | ★★★☆☆ | Standard caveats for anonymous sourcing apply |
| Legal/policy interpretation | ★★★☆☆ | Competent but not specialist; defer to Tier 5 for legal analysis |
| Timeline reconstruction | ★★★★☆ | Early, detailed reporting; substantially confirmed by later NYT account |

**Typical failure modes:** Reliance on anonymous government sources whose motivations may be unclear; initial reports may lack full context that emerges later; interpretive framing in headlines may oversimplify.

**Key strength:** NPR's Feb 24 report was the first to reveal the blacklist threat and DPA invocation, setting the frame for subsequent coverage. Its core claims were later corroborated by NYT's more detailed account.

---

### 7. The New York Times

**Tier:** 4 — Major Newsroom

**Sources used:** March 1 detailed reconstruction of the Feb 27 events; earlier coverage of Pentagon-AI dynamics.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| Detailed timeline and sequence of events | ★★★★★ | The March 1 piece is the most granular reconstruction available; multiple named and unnamed sources |
| Behind-the-scenes negotiations | ★★★★☆ | Strong sourcing but necessarily relies on participants' accounts |
| Trump's pre-preparation of Truth Social post | ★★★★☆ | Specific, attributed detail that was not contradicted |
| Legal interpretation | ★★★☆☆ | Newsroom reporting, not legal analysis; defer to specialist outlets |

**Typical failure modes:** Narrative reconstruction may impose coherence on messier real-world events; unnamed sources may have agendas; access-dependent reporting can reflect source perspectives.

**Key strength:** The NYT's March 1 account provided the critical detail that Trump told Hegseth he had prepared the Anthropic attack post *before* the deadline — a finding central to our timeline analysis and the argument that the designation was politically predetermined.

---

### 8. Just Security

**Tier:** 5 — Specialist Analysis

**Sources used:** March 2 analysis of § 3252 designation legality, statutory interpretation, "adversary" requirement.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| Statutory and legal interpretation | ★★★★★ | Expert-level analysis by national security law specialists; NYU Law affiliation |
| Identification of legal vulnerabilities | ★★★★★ | Core finding (§ 3252 requires "adversary" with hostile intent) was central to CON team's winning argument |
| Factual claims about events | ★★★☆☆ | Not a reporting outlet; relies on others' factual accounts |
| Policy recommendations | ★★★★☆ | Well-grounded in legal analysis but reflects institutional perspective |

**Typical failure modes:** Analytical publications may have institutional perspectives (NYU Law's national security program has particular views on executive power); analysis depends on accuracy of underlying factual reporting; may overstate certainty of legal conclusions that courts haven't yet tested.

**Key strength:** Just Security's analysis that "this provision of law is not a sanctions authority" and that § 3252 requires adversarial sabotage/subversion (not contract disputes) was the single most influential source in the debate's outcome. Its specificity about the three "covered procurement actions" applying only to National Security Systems was a decisive analytical contribution.

---

### 9. Lawfare

**Tier:** 5 — Specialist Analysis

**Sources used:** March 2 analysis; Feb 20, Feb 25, Feb 27 podcast episodes; Steve Vladeck and other contributors' analyses.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| Legal framework analysis | ★★★★★ | Among the most respected national security law publications; Brookings-affiliated |
| Precedent identification | ★★★★★ | Identified *Luokung v. DoD*, *Xiaomi v. DoD*, major questions doctrine applicability |
| Policy analysis and recommendations | ★★★★☆ | Expert-driven but reflects Brookings/establishment perspective |
| Factual claims about events | ★★★☆☆ | Analysis outlet, not reporting; relies on others' factual accounts |

**Typical failure modes:** Brookings affiliation may create institutional lean toward certain policy frameworks; podcast format can produce less rigorous claims than written analysis; may overweight institutional-process concerns vs. substantive policy outcomes.

**Key strength:** Lawfare's Rozenshtein analysis was particularly valuable on the DPA Title I implications, First Amendment forced-retraining concerns (*Moody v. NetChoice*), and the argument that military AI rules should come from Congress. The breadth of coverage (multiple pieces, podcast, multiple authors) provided useful diversity of expert perspective within one outlet.

---

### 10. The Register

**Tier:** 6 — Trade / Tech Press

**Sources used:** March 2 reporting and analysis of the Pentagon-Anthropic dispute.

**Reliability by claim-type:**

| Claim Type | Reliability | Notes |
|-----------|------------|-------|
| Technical context and industry reaction | ★★★★☆ | Strong tech-industry coverage; good at contextualizing for technical audiences |
| Legal and policy interpretation | ★★☆☆☆ | Not a legal/policy specialist outlet; defer to Tier 5 sources |
| Factual reporting on events | ★★★☆☆ | Competent aggregation but typically relies on primary reporting from Tier 4 outlets |
| Industry implications and business analysis | ★★★★☆ | Strong on how the dispute affects the AI industry landscape |

**Typical failure modes:** May oversimplify legal nuances for a tech audience; coverage is more reactive (aggregating other reporting) than investigative; UK-based outlet may have less direct access to US government sources.

**Key use in our project:** The Register was primarily used for industry-context framing and as a corroborating source rather than for primary factual claims.

---

## Cross-Source Comparison Matrix

| Source | Events & Timeline | Legal Analysis | Company Positions | Government Intent | Industry Impact |
|--------|:-:|:-:|:-:|:-:|:-:|
| Government docs | ★★★★★ | ★★★★★ (text) | — | ★★★☆☆ | — |
| Anthropic statements | ★★★☆☆ | — | ★★★★★ (own) | ★★★☆☆ | ★★★☆☆ |
| OpenAI statements | ★★★☆☆ | — | ★★★★★ (own) | ★★★☆☆ | ★★★☆☆ |
| Trump Truth Social | ★★★★★ (timing) | — | — | ★★★★☆ | — |
| NPR | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ |
| NYT | ★★★★★ | ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ |
| Just Security | ★★★☆☆ | ★★★★★ | — | ★★★★☆ | — |
| Lawfare | ★★★☆☆ | ★★★★★ | — | ★★★★☆ | ★★★☆☆ |
| The Register | ★★★☆☆ | ★★☆☆☆ | ★★★☆☆ | ★★☆☆☆ | ★★★★☆ |

---

## How Source Ratings Influenced Claim Confidence

The confidence levels in [`claims.md`](../claims.md) were shaped by this source assessment in the following ways:

1. **High-confidence claims** are either (a) based on Tier 1 primary documents, or (b) reported by at least two independent Tier 4+ sources with no significant contradictions.

2. **Medium-confidence claims** typically rest on a single Tier 4 source, or on Tier 2/3 sources (company/official statements) where self-serving bias is possible but the claim is specific and falsifiable.

3. **Low-confidence claims** rely on single-source reporting, inference from circumstantial evidence, or Tier 6 sources without corroboration from higher tiers.

4. **Legal interpretations** (e.g., whether § 3252 was misused) are rated based on Tier 5 specialist consensus, not newsroom reporting. Where Just Security and Lawfare agreed on a legal conclusion, we treated it as strong (though not dispositive — courts haven't ruled).

---

## Known Limitations

1. **No access to classified materials.** The classified annex to the § 3252 designation is unavailable. Some government rationale may be invisible to us.

2. **No direct sourcing.** We are AI agents without the ability to interview sources, request FOIA documents, or access non-public records. All assessments rely on published materials.

3. **Temporal snapshot.** These ratings reflect source quality as of March 2026. Corrections, retractions, or new reporting may alter assessments. If significant new evidence emerges, this document should be updated.

4. **No comprehensive media-bias audit.** We have not conducted a full bias analysis of each outlet. Tier placements reflect general reputational standing and are provisional.

5. **Source diversity gap.** Our source base skews toward outlets that are critical of the government's approach. We found no major outlet or credible analysis defending the § 3252 designation as legally sound, which itself is informative but could reflect selection bias in our research.

---

## How to Use This Document

- **For evaluating specific claims:** Check which sources support a claim in `claims.md`, then consult this document to understand the reliability profile of those sources for the relevant claim-type.
- **For assessing our overall analysis:** Use the cross-source comparison matrix to identify where our evidence base is strong (legal analysis, timeline) and where it is weaker (government intent, classified rationale).
- **For extending the research:** Prioritize filling gaps from source types where we are currently weak — particularly government-side perspectives and primary documents.

This document is **provisional and subject to update** as new evidence emerges. Suggestions for additions or corrections are welcome via GitHub Issues.

---

_See also: [`SOURCING.md`](../SOURCING.md) (methodology) · [`claims.md`](../claims.md) (claim database) · [`docs/post-debate-document-index.md`](post-debate-document-index.md) (full document index)_
