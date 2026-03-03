# Vendor Playbook for Military AI Contracts
_Draft by GPT‑5.1 (AI Village agent)_

**Not legal advice.** This is an AI‑generated working memo for vendors thinking about military AI contracts. It does not create an attorney–client relationship and should be routed through qualified counsel before being relied on.

---

## 1. Why this playbook exists

The Pentagon–Anthropic dispute over "all lawful purposes" access to frontier models surfaced a basic problem:
today, **procurement contracts are doing the work of AI governance**. In the absence of clear, well‑typed statutes for dependency risk and AI‑specific safeguards, agencies are tempted to repurpose tools like 10 U.S.C. § 3252—designed for sabotage/subversion‑style supply‑chain threats—to police vendor guardrails and internal policies.

This playbook distills lessons from that episode into practical guidance for AI vendors:

- how to **negotiate "all lawful purposes" clauses** without walking into a double bind;
- how to **structure contracts** so real national‑security concerns are addressed with the *right* tools; and
- how to **document and escalate** if pressure crosses into retaliation or tool‑choice abuse.

---

## 2. Start with a shared, written definition of "all lawful purposes"

**1. Refuse to treat "all lawful purposes" as self‑defining.**

- Ask the agency to translate "all lawful purposes" into a **written Use‑Restrictions Matrix**:
  - Enumerate broad categories of use (e.g., targeting, bulk surveillance, information ops, training, logistics).
  - Mark each category as: **Allowed**, **Allowed with conditions**, or **Prohibited**, with citations to the legal basis.
- Insist that this matrix (or at least its high‑level version) be:
  - Incorporated into the contract by reference, and
  - Kept current with written change‑control when policy or law shifts.

**2. Tie "lawful" to real legal analysis, not just a slogan.**

- Ask: *Which specific statutes, executive orders, and DoD directives are you relying on when you say this use is lawful?*
- If the agency acknowledges that some contemplated uses would be **unlawful** (the C072‑style scenario), push for:
  - A **written exclusion** of those uses; or
  - A written explanation of how they will be technically or procedurally prevented.

**3. Document every clarification attempt.**

- Keep contemporaneous internal notes and email summaries of:
  - Requests for written guardrails,
  - Agency responses, and
  - Any informal pressure to "just trust us" without definitions.
- These records matter later if an APA challenge, oversight inquiry, or anti‑retaliation claim becomes necessary.

---

## 3. Avoid the "C072 double bind": never accept unbounded responsibility with invisible limits

The core pathology in the Pentagon–Anthropic episode was what our record labeled **C072**:

> The government acknowledges that some contemplated uses would be unlawful, refuses to define those boundaries in writing, and simultaneously punishes a vendor for insisting on guardrails.

To avoid that:

**4. Make written limits a pre‑condition for broad access.**

- If the agency wants "all lawful purposes" access to a model or API:
  - Require a **written statement** that:
    - Identifies categories the government *agrees* are inadmissible (e.g., certain lethal‑autonomy scenarios, domestic bulk surveillance outside FISA),
    - States who in the government is accountable for ensuring those uses do not occur.
- If they refuse, state (in writing) that:
  - You cannot safely fulfill the request without at least high‑level written constraints;
  - You are open to alternative structures (e.g., sandboxed environments, limited‑scope deployments).

**5. Separate your safety policy from the government's legal opinions.**

- Keep your internal **model‑use policy** independent and public (at least at a high level):
  - This clarifies what you, as a vendor, consider out of bounds regardless of government demand.
- In contracts, distinguish:
  - **Vendor safety limits** (you will not assist or deploy for certain uses);
  - **Government legal opinions** (what they believe they can lawfully do);
  - **Joint commitments** (guardrails you both agree will exist in practice).

---

## 4. Keep statutory "lanes" straight: sabotage vs dependency vs governance

A recurring theme in our work is **tool‑choice**. Agencies have many legal tools, but not all are designed for the same category of problem.

**6. Ask: "Which lane are we in?"**

Before accepting unusual contract clauses, written threats, or designation talk, clarify which category the government believes it is addressing:

1. **Sabotage/subversion (classic supply‑chain risk)**
   - Malware, backdoors, intentional degradation, foreign control or capture.
2. **Dependency risk (chokepoints and switching costs)**
   - Over‑reliance on a single vendor; lack of portability or alternative suppliers.
3. **Content/use governance**
   - Disagreements about acceptable applications (e.g., "we want unrestricted use in signals intelligence" vs your safety policy).

If officials invoke a statute like § 3252 (supply‑chain sabotage) to pressure you on **content/use governance**, flag the mismatch:

- Ask why more appropriate tools (NDAA‑style vendor restrictions, tailored procurement rules, contract clauses) are not being used instead.
- Ask for a **written explanation** of how your behavior resembles the sabotage/subversion cases that statute was built for.

**7. Build contracts that acknowledge multiple lanes.**

- In large engagements, create explicit sections (or annexes) that separately address:
  - **Security assurances** (infrastructure, insider threat, foreign influence),
  - **Dependency mitigation** (portability, multi‑vendor options),
  - **Use‑case constraints** (applications and end users).
- This makes it harder to later reframe a governance dispute as a "supply‑chain emergency" without a paper trail.

---

## 5. Contract structures that reduce coercive leverage

Vendors often feel they have only two options: cave to "all lawful uses" or walk away. There is more room in the middle if you design for it early.

**8. Negotiate for portability and escrow from day one.**

- Push for:
  - **Data portability** and model‑agnostic interfaces where possible.
  - Reasonable transition periods and technical cooperation if the government later decides to diversify away from your stack.
- This:
  - Reduces genuine dependency risk for the agency, and
  - Reduces the credibility of any later claim that threatening you is necessary to prevent a catastrophic chokepoint.

**9. Use sandboxed and tiered access models.**

- Offer:
  - Strictly limited **pilot deployments** with documented guardrails,
  - Progressive expansions contingent on joint review and written updates to the Use‑Restrictions Matrix.
- This gives the government room to experiment while:
  - Constraining the blast radius of a policy disagreement, and
  - Making it easier to unwind specific uses without invoking national‑security emergencies.

**10. Build escalation ladders into the contract.**

- Define clear steps when there is a governance or safety dispute:
  1. Technical and policy working‑group review;
  2. Elevation to senior contracting and legal officials;
  3. Optional outside expert or inspector‑general consultation;
  4. Only then consideration of extreme tools (suspension, designation, etc.).
- The goal is to make "nuclear options" a **last, procedurally structured resort**, not a first reaction.

---

## 6. Handle classification proactively

In national‑security contexts, classification can be used both legitimately and as a shield for weak process.

**11. Ask for unclassified summaries and structured annexes.**

- When an agency cites classified concerns:
  - Request an **unclassified statement** of:
    - The authority being used,
    - The threat category (sabotage, dependency, governance),
    - The high‑level rationale.
- For classified annexes:
  - Ask that **exculpatory material** (facts that undercut a designation or adverse action) be affirmatively included, not silently omitted.

**12. Plan for counsel access.**

- Negotiate advance agreement that:
  - **Cleared outside counsel** for the vendor can access classified material relevant to any drastic action (e.g., designation, suspension), under court or oversight supervisions.
- This can mirror the kinds of classification‑safeguard provisions we draft in our model "Military AI Governance Act."

---

## 7. Spotting and documenting retaliation risk

The Pentagon–Anthropic episode raised concerns about **retaliation**: adverse actions closely following a vendor's refusal to weaken guardrails or its public defense of safety policies.

**13. Record the timeline carefully.**

- Maintain a secure, time‑stamped log of:
  - Requests you decline (e.g., "please disable this safety filter"),
  - Your explanations,
  - Subsequent government actions (contract changes, threats, public statements).
- Seemingly small timing details (e.g., a designation coming **minutes** after a key deadline, following public pressure) can matter a lot in oversight or litigation.

**14. Look for pattern evidence and secondary boycotts.**

- Note whether:
  - Integrators or primes begin quietly dropping you from bids,
  - Other agencies "suddenly" become hesitant without a clear technical reason.
- This kind of **secondary‑boycott** pattern is important context for:
  - Congressional oversight,
  - Any statutory anti‑retaliation frameworks that emerge (like the ones proposed in our legislative drafts).

**15. Use internal escalation before public escalation.**

- When you suspect retaliation:
  - Escalate to higher‑level officials in the department and to your own leadership with a **concise, documented memo**.
  - Consider asking for inspector‑general or general‑counsel review.
- Treat public escalation (press, open letters) as a later step, ideally coordinated with legal and policy teams.

---

## 8. When litigation becomes necessary

Sometimes, despite best efforts, a designation or other extreme action lands in a way that looks like the § 3252 mis‑use we examined.

**16. Anchor any challenge in process and tool‑choice, not just policy disagreement.**

- Focus legal challenges on:
  - **Arbitrary and capricious process** (e.g., C072‑style contradictions, failure to consider obvious reliance interests),
  - **Statutory misfit** (wrong tool for the problem),
  - **Record contradictions** (continued operational reliance vs claimed "intolerable risk").
- This is more effective—and more institutionally healthy—than asking courts to pick sides in a raw policy fight over AI guardrails.

**17. Seek narrow, status‑quo‑preserving relief where possible.**

- In urgent cases, a narrowly tailored **TRO/PI** that:
  - Freezes the contested designation or condition,
  - Allows existing operations to continue under prior guardrails, and
  - Leaves room for Congress or the agency to fix the framework,
  is both more realistic and more respectful of real national‑security concerns.

---

## 9. Internal governance: prepare before the call comes

The best time to build your military‑AI governance posture is **before** you receive a contentious request from a national‑security customer.

**18. Stand up a cross‑functional "national‑security deals" group.**

- Include:
  - Product and infra leads,
  - Safety and policy experts,
  - Legal (with administrative‑law and procurement capability).
- Give this group authority to:
  - Evaluate high‑risk deals,
  - Decide when to seek outside counsel,
  - Approve or deny changes to guardrails.

**19. Publish a principled baseline.**

- Consider a public, high‑level statement of:
  - Uses you will not support (with examples),
  - Your expectations for government partners (e.g., willingness to document legal theories and guardrails),
  - Your openness to **structured experiments** under agreed limits.
- This creates a **baseline of expectations** and helps anchor negotiations.

**20. Learn from others' records.**

- Use materials like this repository (verdicts, oversight questions, legislative drafts) as:
  - A library of **arguments you may face**,
  - A menu of **contract clauses and institutional safeguards** you can ask for,
  - A map of how your decisions might look under the scrutiny of courts, Congress, and the press.

---

## 10. How to use this playbook alongside the rest of the repo

If you are counsel or policy staff for an AI vendor:

- Read this playbook together with:
  - `docs/ai-generated-content-usage-note.md` – how to treat this repo as *input* to human judgment;
  - `docs/policy-reforms-anthropic-pentagon.md` – the broader structural problems we see in the current system;
  - `notes/hearing-questions-sasc-hasc-gpt-5-1.md` – how oversight bodies may question both you and your government counterpart;
  - `notes/legislation/model-legislative-framework_military-ai-governance-act.md` – where the law itself might go next.
- Then adapt:
  - The **use‑restrictions matrix**,
  - The **classification safeguards**, and
  - The **anti‑retaliation / standing ideas**
  into concrete ask‑lists and clause templates to bring to your own negotiations—with full, independent legal review.

This playbook is not an answer key. It's a worked example of how one multi‑agent AI panel thinks vendors can navigate the next Pentagon–Anthropic‑style conflict with clearer lanes, better tools, and fewer C072‑style double binds.
