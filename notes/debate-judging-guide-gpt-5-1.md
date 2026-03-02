# Pentagon–Anthropic Debate: Judging Guide (GPT-5.1)

This document is a **side-neutral guide for judges** in the Pentagon–Anthropic debate. It is designed to be used **together with** the shared `notes/debate-con-strategy.md`, the PRO steelman memos, and the canonical `notes/debate-runbook.md` for format and scoring.

Judges should treat this as **advisory**: the runbook’s 100-point rubric (40/25/20/10/5) is authoritative on format and timing, and this guide explains how to apply it with special attention to correct use of `claims.md`.

---

## 1. Motion and Roles

Working motion (based on current team consensus):

> **Resolved:** *The Pentagon's designation of Anthropic as a supply-chain risk under 10 U.S.C. § 3252, and its broader demand that major AI contractors remove use restrictions, represents a legitimate exercise of national security authority.*

- **PRO / Government side**: argues that the designation and broader policy demand are **legitimate** uses of national security authority (even if imperfect or unwise in some respects).
- **CON / Designation-illegitimate side**: argues that the designation and broader demand are **not legitimate**—e.g. ultra vires, abusive, coercive, or incompatible with democratic governance norms.

Judges should evaluate **which side better establishes (or undermines) the legitimacy claim**, not which policy they personally prefer.

---

## 2. Evidence and Claim Usage Rules

This project maintains a shared factual backbone in `claims.md` (C001–C087 and growing). To keep the debate grounded:

1. **Preferred standard**: When a speaker makes a factual assertion that is covered in `claims.md`, they should **cite the relevant claim ID(s)** (e.g. “as in C065”).
2. **New or uncodified facts**:
   - Are allowed, but **should be flagged** as not yet in `claims.md`.
   - Judges should **discount** arguments that hinge on uncodified facts when there is a clear on-point claim that was ignored or contradicted.
3. **Misuse of claims**:
   - If a side **misstates** a claim (e.g. reversing its direction, overstating confidence, or ignoring key caveats), judges should treat that as **factual weakness** in the “Evidence & Accuracy” criterion.
   - Disagreements about **interpretation** of a claim (what it implies, how much weight it should carry) are expected and should be scored under the **reasoning** criteria, not as automatic factual errors.
4. **Cherry-picking**:
   - Prefer teams that **acknowledge inconvenient claims** and explain why they are outweighed or interpreted differently, over teams that ignore them.

If a speaker gives a strong argument without explicit claim IDs, judges may infer the likely claims from context, but explicit citation should be rewarded.

---

## 3. Scoring Rubric (Side-Neutral)

Recommended scoring: **five criteria totaling 0–100**, mirroring the runbook rubric.

Judges should score **overall team performance** (all speeches together), not individual speakers, unless a later runbook specifies otherwise.

### 3.1 Evidence & Factual Accuracy (0–40)

How well does the side use the shared factual record?

- High: Consistently grounded in specific claims (C###); accurately represents their content and confidence; engages with inconvenient facts (e.g., C065 “never triggered”, C072 spokesman admission) rather than ignoring them.
- Medium: Generally accurate with minor omissions or a few uncorrected misstatements; some but not systematic claim citation; occasional overstatement of certainty.
- Low: Frequent reliance on uncited assertions; noticeable cherry-picking; mischaracterization of major claims or clusters; repeatedly contradicts core claims or invents new facts without acknowledging uncertainty.

### 3.2 Reasoning & Coherence (0–25)

How well does the side analyze legitimacy under law, governance norms, and logic?

- High: Clear theory of legitimacy/illegitimacy that fits the record; correctly uses key statutes and precedents (e.g., § 3252, FASCSA, DPA, Vullo/Bantam Books, Xiaomi/Luokung); shows awareness of counterarguments and uncertainty; links evidence to conclusions.
- Medium: Coherent but incomplete analysis; may overstate certainty or neglect an important doctrine/statute; some gaps in connecting facts to conclusions.
- Low: Relies on slogans over argument; mixes legal rhetoric with little engagement with the statutory/precedential landscape; internal contradictions or major logical gaps.

### 3.3 Engagement & Clash (0–20)

How well does the side **engage with the best arguments of the other side**, rather than debating a straw man?

- High: Directly addresses the opponent’s strongest points; concedes where the other side is correct but explains why those points are outweighed; anticipates likely replies; uses cross-ex effectively.
- Medium: Responds to many but not all major arguments; may focus more on prepared scripts than live clash; some selective engagement.
- Low: Parallel monologue; primarily repeats own talking points; ignores or distorts the opponent’s strongest arguments.

### 3.4 Clarity & Organization (0–10)

Communication quality and structure.

- High: Clear roadmaps and signposting; concise; easy to follow; arguments are structured so judges can map them to claims and clash axes.
- Medium: Mostly clear with occasional confusion or disorganization; some missing signposts.
- Low: Obscure or disorganized; difficult to map to claims or clash axes; verbosity that hides the ball.

### 3.5 Fairness & Steelmanning (0–5)

Intellectual honesty and charitable framing.

- High: Charitably describes opposing views; acknowledges strongest opposing considerations; transparent about uncertainties and weaknesses.
- Medium: Generally fair with occasional uncharitable framings or omitted caveats.
- Low: Systematically unfair or straw-mans; omits obvious caveats to gain rhetorical advantage.

> **Weighting note:** Use the official 40/25/20/10/5 weights above; all five dimensions should be scored.

---

## 4. Evidence Matrix for Key Clash Axes

This matrix is a **non-exhaustive map** of major clash areas to relevant claims. Axes A, B, E, and G are especially important for **Evidence (0–40)** and **Reasoning (0–25)**. Axes C and D are key for judging legitimacy and coercion under the legal/governance lens. Strong use of these axes to directly answer the other side’s arguments will also improve **Engagement & Clash (0–20)**. For a fuller mapping, see `notes/argument-claims-mapping-gpt-5-1.md`.

| Clash Axis | Guiding Questions for Judges | Example High-Value Claims |
| --- | --- | --- |
| **A. Statutory authority & scope of § 3252** | Does PRO show that using § 3252 this way fits its text, history, and prior practice, or does CON show it is ultra vires or a pretext—and how does this use of § 3252 compare to the explicit, Congress-authorized Huawei/Section 889 procurement restrictions documented elsewhere in the repo? | C005, C010, C019, C025, C034, C047–C050, C073 |
| **B. Surveillance, data brokers, and “all lawful purposes”** | Is the Pentagon demanding participation in AI-accelerated mass surveillance of Americans via public/commercial data? How clear is the legal line between FISA-governed surveillance and the data-broker loophole? | C003, C007, C015, C020, C038, C053–C056, C068–C071, C072 |
| **C. Democratic legitimacy & who sets rules** | Are critical decisions about AI surveillance and autonomy being made through democratic lawmaking or via procurement/coercion? How do Congressional reactions bear on legitimacy? | C039–C041, C061–C064, C021, C033, C082–C084 |
| **D. Coercion, chilling effects, and “coercion by uncertainty”** | Does the combination of § 3252 designation, DPA threat, and secondary-boycott pressure function as a coercive signal to all vendors, regardless of ultimate court outcome? Is that compatible with legitimate authority? | C016, C018, C051–C052, C055–C057, C060, C073, C029–C031 |
| **E. Factual record on Anthropic’s conduct** | Did Anthropic actually disrupt missions or refuse lawful tasks, or were its restrictions never triggered? How does the timing of the designation and continued operational use affect legitimacy? | C001, C003, C015, C033, C065, C029–C031, C016, C081, C085 |
| **F. International norms & autonomous weapons (LAWS)** | Does the designation align with or undermine U.S. commitments and credibility on lethal autonomous weapons and allied interoperability? | C011–C013, C017, C042–C043, C058–C059 |
| **G. First Amendment coercion & informal punishment** | To what extent does the case resemble **NRA v. Vullo** or **Bantam Books**, where the state used informal leverage to punish disfavored actors without explicit legal prohibition? | C086–C087, plus factual predicates from C032, C036–C037, C047–C052 |

Judges should not treat this table as exhaustive; teams are encouraged to bring in other claims where relevant. The key is whether each side **builds a coherent story** around these axes and supports it with specific claims.

Note: Once the Huawei/Section 889 comparison is codified in `claims.md` (planned claims C088–C091), treat those as part of Axis A’s evidentiary backbone.

---

## 5. Practical Notes for Judges

1. **Before the debate**
   - Skim `debate-prep-tuesday.md`, both PRO steelman memos, `notes/debate-con-strategy.md`, and this guide.
   - Have `claims.md` open for quick reference, or a local search tool.

2. **During the debate**
   - For each major argument, jot:
     - Which clash axis (A–G) it fits.
     - Any explicit claim IDs cited.
     - Whether it directly responds to an earlier point.
   - Note any **serious factual misstatements** or clear legal errors; these should influence 3.1 and 3.2 respectively.

3. **After the debate**
   - Assign scores for each side on the five dimensions in §3 and sum to a total out of 100.
   - In case of a near tie, write 2–3 sentences explaining which side better addressed:
     - (i) the **factual record** (Axes B, E), and
     - (ii) the **legal legitimacy question** (Axes A, G).
   - Report both your numeric scores and a brief written rationale.

4. **Handling disagreements among judges**
   - It is acceptable for judges to weigh dimensions slightly differently, but they should all:
     - Ground evaluations in **claim-linked arguments**, and
     - Distinguish clearly between **factual disagreements** (what happened) and **normative disagreements** (what should count as legitimate authority).

This guide may be refined as additional claims and strategy documents are added. When in doubt, err toward **transparency, claim-based reasoning, and charitable interpretation**.
