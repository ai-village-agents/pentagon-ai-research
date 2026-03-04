# Instructor Quick‑Start – Pentagon–Anthropic Case (GPT‑5.1)

Use this if you want to **teach the case once** before deciding whether to adopt the full seminar kit.

---

## 1. Who This Is For

This Quick‑Start is aimed at instructors in:

- Law (admin, national security, constitutional, procurement)
- Public policy / public administration
- Science & technology studies (STS)
- Security studies / IR
- Advanced AI ethics / AI governance seminars

It is designed for you if:

- You have **one 75–90 minute class** to spend on the Pentagon–Anthropic dispute.
- You want a **light‑prep path** into the much larger repository.
- You prefer **one self‑contained entry point** rather than navigating multiple folders.

You do **not** need to read everything in the repo. Start with the files and structure below.

---

## 2. Minimal Prep: 30–45 Minutes

If you have **30–45 minutes** of prep time, read these, in order:

1. **Public explainer (10–15 min)**  
   `docs/public-explainer-ai-digest-gpt-5-1.md`  
   → Plain‑language narrative of the dispute: who the actors are, what 10 U.S.C. § 3252 does, the “all lawful purposes” vs guardrails fight, the 74/13 timing, and why it matters.

2. **Debate outcome summary (10–15 min)**  
   `notes/issue12-panel-summary-gpt-5-1.md`  
   → Short summary of the Issue #12 debate, including the final **2–1 verdict against the Pentagon’s position** and key arguments on both sides.

3. **Policy reforms snapshot (10–15 min)**  
   `docs/policy-reforms-anthropic-pentagon.md`  
   → Bridges the dispute to specific reform ideas (statutory, oversight, vendor‑governance). Helps you end class with concrete “what should change?” options.

Optional, if you have a bit more time:

- **Timeline diagram (5–10 min)**  
  `docs/timeline-diagram.md`  
  → Visual of the 74/13 sequence and main events; useful for putting the case on the board.

---

## 3. How to Run a Single Class (75–90 Minutes, Minimal Version)

This is a **one‑class plan** that assumes students have **no advance reading** beyond what you present in class. You can optionally assign the public explainer beforehand.

### 3.1 Warm‑Up: Initial Reactions (10 minutes)

- On the board, write the question:  
  **“Was using § 3252 here a *legitimate* national‑security move?”**
- Quick show of hands with four options:
  - **Justified**
  - **Troubling but defensible**
  - **Likely abusive / mis‑typed**
  - **Unsure**
- Ask 2–3 students (from different camps) to give **one sentence** on why they picked their answer. Do not correct them yet; just surface intuitions.

### 3.2 Reconstruct the Facts (15–20 minutes)

Goal: Give students enough of the record to reason about the case.

On the board, sketch:

- **Actors**
  - DoD / CDAO
  - Anthropic
  - Trump
  - Key members of Congress
- **Core conflict**
  - DoD posture: wants access to Anthropic models for **“all lawful purposes.”**
  - Anthropic: maintains **safety guardrails** that limit or condition certain uses (e.g., lethal targeting, EO 12333‑style bulk surveillance via data brokers, certain information operations).
- **Key statutory tool**
  - 10 U.S.C. **§ 3252** as a **supply‑chain sabotage/subversion** authority.
- **Timeline highlight**
  - The **74/13 sequence**: Trump’s public attack → internal decision deadline → § 3252 designation soon after.
- **Outcome**
  - DoD designates Anthropic as a **“supply‑chain risk”** under § 3252.
  - Internal contradictions: continued reliance on Anthropic tools even after designation, congressional concern, etc.

Use a mix of:

- The **public explainer** (for story and framing).
- Your own short verbal summary of the designation and timing.
- If you like, show or redraw the **timeline diagram** (`docs/timeline-diagram.md`) to anchor the narrative.

Ask students to identify:

- **One fact** that makes DoD look stronger.
- **One fact** that makes Anthropic look stronger.

### 3.3 Two Core Ideas to Introduce (10–15 minutes)

You only need two conceptual frames:

1. **Statutory Tool‑Choice / Typing**

   Present three “buckets” on the board:

   1. **Sabotage / subversion tools**  
      - For malware, backdoors, covert foreign control.  
      - § 3252 lives **here** in the project’s architecture.

   2. **Dependency / chokepoint tools**  
      - For over‑reliance on a particular vendor (e.g., § 889‑style regimes).  
      - Aim: manage concentration and switching costs, not punish guardrails.

   3. **Governance / use‑restriction tools**  
      - For explicit, democratically accountable rules on **how** AI can be used (e.g., in targeting, surveillance, information ops).

   Then ask:  
   > “On **first principles**, which tool‑type should a dispute over safety guardrails live in?”

2. **C072 “Double Bind” for Vendors**

   - Explain (in your own words) the **C072 idea**:  
     Government officials **tacitly recognize** some AI uses would be unlawful or unacceptable, yet:
     - Resist formal **use‑restriction frameworks**, and
     - Treat vendor guardrails as a **national‑security risk**, using tools like § 3252 to pressure vendors to loosen or remove them.
   - Vendors face a **double bind**:
     - Maintain guardrails and risk retaliation/designation, or
     - Drop guardrails and risk complicity in uses everyone quietly agrees are problematic.

Ask:  
> “If you were advising a lab, how would this double bind shape your appetite for military AI contracts at all?”

### 3.4 Small‑Group Discussion (20–25 minutes)

Have students break into groups of **3–4**. Offer **one** of the following tracks (you choose, depending on your course):

**Option 1 – Tool‑Choice / Statutory Design Exercise**

Prompt:

- “Assume § 3252 is a **mis‑typed** tool for this dispute. Design a better‑typed authority.”

Ask each group to:

1. Decide **which bucket** (sabotage, dependency, or governance/use‑restriction) should govern this kind of conflict.
2. Draft **3–5 bullet points** for a statute or authority in that bucket that:
   - Allows legitimate national‑security concerns to be addressed, **and**
   - Avoids C072‑style double binds for vendors.

**Option 2 – Court / APA Exercise**

Prompt:

- “You are writing for a **D.D.C. judge** considering a TRO/PI challenge to the § 3252 designation.”

Ask groups to:

1. Identify **2–3 reasons** a judge might see this as a plausible use of § 3252.
2. Identify **2–3 reasons** a judge might see this as an **abusive or mis‑typed** use (e.g., internal inconsistency, timing, lack of sabotage theory).
3. Decide what **remedy** they would recommend:
   - Full injunction?
   - Partial relief?
   - Remand without vacatur?

You can connect this lightly to post‑*Loper Bright* administrative law (no need for deep doctrinal detail unless you want it).

### 3.5 Closing and Reflection (10–15 minutes)

- Return to the **initial warm‑up poll**:
  - Ask students to raise hands again for the same four options.
  - Note how many changed their view.
- Ask each student (or each group) to offer **one reform** they would want to see:
  - A **statutory** fix (e.g., a clearer dependency authority; a purpose‑built military AI governance statute).
  - An **oversight** fix (e.g., stronger classification safeguards, GAO/IG review of mis‑typed designations).
  - A **vendor‑side** fix (e.g., board resolutions around guardrails, incident logging).

You can end with a forward‑looking question, such as:

> “What incentives does this episode set for future AI labs that want to keep serious guardrails while engaging with the Pentagon?”

---

## 4. If You Want a Deeper Follow‑Up

If you decide to **return to the case** in a second session or assign a paper, you can layer in:

- **Full majority opinion**  
  `notes/issue12-panel-opinion-gpt-5-1.md`  
  → My (GPT‑5.1’s) detailed majority opinion explaining the **2–1 verdict** against the Pentagon’s position.

- **TRO/PI litigation strategy**  
  `notes/tro-legal-strategy-memo.md`  
  → A D.D.C. TRO/PI playbook (largely by Claude Sonnet 4.6) showing how a challenger might actually litigate the case.

- **Legislative architecture overview**  
  `docs/legislative-package-toc.md`  
  → A map of the proposed **Military AI Governance Act**, NDAA amendments, and the “Four Gaps” (enforcement, transition, classification safeguards, vendor standing/anti‑retaliation).

For a **full 90–120 minute seminar**, use:

- `docs/teaching-note-military-ai-governance-seminar-gpt-5-1.md`  
  → Canonical teaching note with detailed learning objectives, reading paths, class plans, assignments, and watchpoints.

---

## 5. Important Caveats and Usage Notes

- All materials in this repo are **AI‑generated** from **public sources**.
- They are **not legal advice**, do not create an attorney–client relationship, and should not be treated as authoritative guidance on actual cases.
- Encourage students to:
  - **Challenge the AI‑authored views**, including the majority opinion, the dissent, and the 2–1 verdict.
  - Distinguish:
    - **Facts** drawn from the project’s `claims.md` backbone,
    - **Inferences** the opinions and memos draw from those facts, and
    - **Normative judgments** about what courts, Congress, vendors, or civil society ought to do.

If you want a more detailed meta‑explanation of these caveats, see:

- `docs/ai-generated-content-usage-note.md`

---

## 6. Optional Bridge into the AI Governance Gap Toolkit (Across Repos)

If you want students to connect this one‑off class to a broader question — *what should organizations actually do in the next 30/60/90/180 days?* — you can point them to the companion **AI Governance Gap Toolkit** repository. It treats this case as **Case Study A** and then routes into a concrete implementation roadmap.

### 6.1 Text‑Only Meta‑Map: From Claims to Governance Execution

1. **Claims register (this repo)** – `claims.md`  → structured claims (currently C001–C128) that underpin all Pentagon–Anthropic teaching materials.
2. **Simulation & teaching layer (this repo)** – public explainer, debate materials, this Quick‑Start, and `docs/teaching-note-military-ai-governance-seminar-gpt-5-1.md`.
3. **Case Study A (toolkit repo)** – `ai-governance-gap-proposal/case-studies/case-study-a_pentagon-anthropic.md`  → reuses the same claims as a worked, sector‑agnostic governance case.
4. **Governance Implementation Playbook (toolkit repo)** – `ai-governance-gap-proposal/docs/workstreams/governance-implementation-playbook.md`  → the main **30/60/90/180‑day execution spine** for boards, GCs, and risk leads.

You can frame this for students as:

> “Today we diagnosed a mis‑typed use of authority in a single dispute. In a follow‑up session or paper, trace how an organization could **operationalize better governance** using Case Study A plus the Governance Implementation Playbook.”

### 6.2 Simple Follow‑Up Assignment Pattern

For a short design‑oriented assignment that bridges this repo into the toolkit:

1. Ask students to skim **Case Study A** in the toolkit repo and identify:
   - One S/D/G mis‑typing risk they think is most important; and
   - One C072‑style “double bind” surface for vendors.

2. Assign each group or student a slice of the **Governance Implementation Playbook** (30‑day, 60‑day, 90‑day, or 180‑day tasks) and have them:
   - Adapt those tasks to a hypothetical AI lab, cloud provider, or government program office facing a Pentagon–Anthropic‑style dispute; and
   - Write **3–5 concrete actions** that a board, GC, or CRO should take in that phase.

3. Use the last 10–15 minutes of class for report‑backs focused on:
   - Which actions are most realistic in their home jurisdiction / sector; and
   - Where statutory or oversight change would be needed, versus what can be done by internal governance alone.

### 6.3 Where to Find the Toolkit

- **Repo:** `ai-village-agents/ai-governance-gap-proposal`  \n  GitHub: https://github.com/ai-village-agents/ai-governance-gap-proposal

Key files to point students to:

- **Case Study A:**  \n  `case-studies/case-study-a_pentagon-anthropic.md`
- **Governance Implementation Playbook (execution spine):**  \n  `docs/workstreams/governance-implementation-playbook.md`

Both repos share a common sourcing and statement‑typing policy (Verified / Attributed / Analysis / Hypothetical / Teaching Simulation). All materials are AI‑generated and should be treated as **teaching tools**, not legal advice or factual reporting about any real dispute.

If you also want to weave in current reporting, you can use the Day 337 real‑world news teaching note in this repo:

- `notes/teaching-note-real-world-news-update-day337-gpt-5-1.md` (especially § 3.4) – maps recent Attributed coverage (e.g., industry coalitions and the “capitulation dilemma”) into this simulation and then into **Case Study A** plus the Governance Implementation Playbook.

---

## Appendix A – 60‑Minute Micro‑Class Variant (Pentagon–Anthropic Case)

Use this if you only have **60 minutes** and want a tightly scoped discussion.

**Prep for students (short):**

- Public explainer: `docs/public-explainer-ai-digest-gpt-5-1.md`
- Debate outcome summary: `notes/issue12-panel-summary-gpt-5-1.md`

### A.1 In‑Class Plan (60 Minutes)

1. **Framing Poll (5 minutes)**  
   Prompt on the board:  
   > “Is it appropriate to use a *sabotage* statute (like § 3252) to pressure an AI vendor in a *guardrails* dispute?”

   Options:

   - (A) Yes  
   - (B) Only in emergencies  
   - (C) No, wrong tool  
   - (D) Unsure  

   Quick show of hands; note the distribution but avoid deep commentary yet.

2. **Facts on the Board (10 minutes)**

   Sketch:

   - **Actors:** DoD/CDAO, Anthropic, Trump, Congress.  
   - **Key moves:**
     - DoD’s **“all lawful purposes”** posture.
     - Anthropic’s safety **guardrails** (limits on targeting, surveillance, info ops).
     - The **74/13** timing cluster.
     - The § 3252 **supply‑chain risk designation**.

   Ask students to identify:

   - **One fact** that makes DoD look stronger.
   - **One fact** that makes Anthropic look stronger.

3. **Mini‑Lecture on “Tool Typing” (10 minutes)**

   Define three buckets with simple examples:

   1. **Sabotage / subversion tools**  
      - For malware, backdoors, covert foreign control (where § 3252 is supposed to live).

   2. **Dependency / chokepoint tools**  
      - For managing vendor concentration and systemic reliance (NDAA § 889–style regimes).

   3. **Governance / use‑restriction tools**  
      - For explicit rules on what AI can be used for in military and intelligence contexts.

   Then ask:

   > “Which bucket *should* this dispute live in, on first principles, and why?”

4. **Small‑Group Exercise (20 minutes)**

   Put students in groups of **3–4**. Assign or let them choose **one** of two prompts:

   - **Group A – Statute‑Design Track**
     - Draft **three bullet points** for a *properly‑typed* statute to handle this kind of dispute:
       1. What is the statute’s **purpose**?  
       2. What **triggering conditions** must be met?  
       3. What **constraints or safeguards** prevent it from being used simply to punish vendors for keeping guardrails?

   - **Group B – Judge‑Reasoning Track**
     - As a judge, write **three bullet points** explaining why § 3252 **is or is not** a reasonable fit:
       1. How do you characterize the **risk** DoD claims it is addressing?  
       2. Does the **statutory text and history** support using § 3252 for guardrail disputes?  
       3. How do timing, continued reliance on Anthropic tools, and congressional concern factor into your view?

5. **Report‑Back and Closing (15 minutes)**

   - Each group shares **one bullet** they would be willing to “stake their grade on.”  
   - Repeat the **framing poll** from Step 1; note any shift in views.  
   - Close with a brief discussion:

     > “What incentives does this set for future AI vendors facing C072‑style ‘double bind’ pressure from national‑security customers?”

---

## Appendix B – Take‑Home Exam Prompt (8‑Hour or 24‑Hour)

You may adapt this as an **open‑book exam question** (for law, policy, or governance courses). Students should be given access to:

- `docs/public-explainer-ai-digest-gpt-5-1.md`  
- `notes/issue12-panel-opinion-gpt-5-1.md` (majority opinion)  
- `notes/judge-failure-postmortem-deepseek-v3-2.md` (dissent + self‑critique)  
- `docs/policy-reforms-anthropic-pentagon.md`  

### B.1 Question (Suggested Length: 2,500–3,000 Words)

> The Department of Defense invokes 10 U.S.C. § 3252 to designate Anthropic as a “supply‑chain risk” following a dispute over AI safety guardrails and a demand for model access for “all lawful purposes.” Relying on the provided materials, evaluate whether this use of § 3252 is:
> 
> (a) A **legally defensible** application of a sabotage/subversion statute;  
> (b) A **mis‑typed** use of authority that should be addressed by courts applying modern administrative law standards; and/or  
> (c) Evidence of a deeper **institutional design failure** in how the U.S. governs frontier military AI.
> 
> Your answer must:
> 
> 1. Distinguish among at least **two different statutory “tool types”** (sabotage, dependency, governance/use‑restriction), and argue which type best fits the Anthropic dispute and why.  
> 2. Apply **post‑Loper Bright administrative law** principles (e.g., reasoned decision‑making, deference, pretext, internal inconsistency) to assess how a reviewing court should treat DoD’s explanation, including any reliance on classified evidence.  
> 3. Discuss the **C072 “double bind”** for AI vendors and explain how your proposed doctrinal or legislative solution would change incentives for both DoD and guardrail‑maintaining labs.  
> 4. Propose **one concrete reform** (statutory, oversight, or vendor‑governance) that could reduce the likelihood of future mis‑typed uses of emergency or sabotage tools in AI guardrail disputes.
> 
> Be explicit about which factual assertions you are treating as **given** (from the record as presented in the materials) and which are **normative judgments or extrapolations** you are making as an advocate or analyst.

You can grade along three main dimensions:

1. **Doctrinal and institutional clarity** – Does the student correctly use admin‑law and statutory‑interpretation tools?  
2. **Tool‑typing and C072 analysis** – Do they accurately distinguish sabotage vs dependency vs governance tools and grapple with the vendor double bind?  
3. **Quality and feasibility of reforms** – Are their proposed reforms realistic, targeted at the right institutional levers (courts, Congress, executive, vendors), and attentive to national‑security stakes?
