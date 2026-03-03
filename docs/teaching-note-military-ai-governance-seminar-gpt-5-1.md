# Teaching Note: Military AI Governance, Statutory Tool‑Choice, and the Pentagon–Anthropic Dispute
*(Seminar Note for Law / Public Policy / STS / Security Studies)*

> **Status:** Teaching note drafted by GPT‑5.1 for external instructors.
> **Not legal advice.** This repository is an AI‑generated research aid based on public sources; it is not a substitute for counsel, official doctrine, or classified assessments.

---

## 1. Purpose, Audience, and Use

This teaching note is designed for instructors running a **90–120 minute seminar** in:

- Law (administrative law, national‑security law, procurement, constitutional law),
- Public policy and governance,
- Science & Technology Studies (STS),
- International security / security studies, or
- Advanced CS/AI governance courses with a focus on state institutions.

It uses the **Pentagon–Anthropic dispute** as a focal case to examine:

1. How national‑security authorities get **"typed"** (sabotage vs dependency vs governance/use),
2. What happens when they are **mis‑typed** and used to pressure AI vendors over guardrails, and
3. How different institutions (courts, Congress, vendors, civil society) can respond.

The materials live in the `pentagon-ai-research` repo. This note routes you into key documents and suggests **class plans, simulations, assignments, and a future research agenda**.

---

## 2. Learning Objectives

By the end of class, students should be able to:

1. **Reconstruct the core dispute**
   - Explain the tension between the Pentagon's push for model access for **"all lawful purposes"** (C002) and Anthropic's safety **guardrails** (C003, C007, C015, C020).
   - Summarize the use of **10 U.S.C. § 3252** to designate Anthropic as a "supply‑chain risk," including the **74‑minute** Trump attack / **13‑minute** designation timing sequence (C029–C032).

2. **Explain statutory tool‑choice and "mis‑typing"**
   - Distinguish three problem types:
     1. **Sabotage / subversion** (e.g., malware, backdoors, covert influence) (C019, C034–C035),
     2. **Dependency / chokepoint risk** (concentration, switching costs, vendor lock‑in),
     3. **Governance / use** (what AI systems may be used for, and under what safeguards).
   - Analyze why using § 3252 to punish a guardrail dispute looks like a **statutory misfit** on the current record (C025, C065).

3. **Understand the "C072 double bind" for AI vendors**
   - Describe C072: officials **acknowledge** some contemplated AI uses would be unlawful or inappropriate, yet resist formalizing limits and instead treat vendor guardrails as a security risk.
   - Explain how this **double bind** shapes vendor incentives and appears in the record here (C072–C073).

4. **Connect debate, verdict, and institutional remedies**
   - Summarize the **Issue #12 debate** and its **2–1 majority against** the Pentagon's posture (`notes/issue12-panel-summary-gpt-5-1.md`).
   - Identify how the repo translates that verdict into a **Military AI Governance Act**, NDAA amendments, TRO strategy, vendor playbooks, and board/civil‑society tools.

5. **Evaluate institutional design options**
   - Critically assess the roles of:
     - Courts (APA/*State Farm*, post‑*Loper Bright* review),
     - Congress (properly typed statutes, oversight, hearings),
     - Executive‑branch processes (classification, IGs, GAO, PCLOB),
     - Vendors and civil society (guardrail maintenance, incident logs, FOIA/IG/GAO engagement).
   - Propose **concrete reforms** or institutional changes, using the repo's **"Four Gaps"** framework as one template.

---

## 3. Short Case Narrative for Students (One‑Page Handout)

You can adapt the following as a **one‑page case summary** to distribute before class.

---

**Actors and backdrop**

Anthropic is a frontier‑AI lab working with the Department of Defense (DoD) and CDAO on various projects (C001). DoD wants access to Anthropic's models for **"all lawful purposes"** (C002). Anthropic maintains **safety guardrails**—technical and policy limits on certain uses (C003, C007, C015, C020), including:

- Lethal‑autonomy and targeting support,
- Large‑scale U.S.‑person surveillance via data brokers and EO 12333‑style channels (C038, C053–C056, C068–C071),
- Influence operations and mass disinformation.

Some officials privately concede that a subset of contemplated uses would be unlawful or inappropriate, but resist writing down formal limits or a shared **Use‑Restrictions Matrix**. That tension is the seed of the **C072 double bind**: vendors are punished for insisting on written constraints even where the government tacitly agrees some uses are off‑limits (C072–C073).

---

**Triggering events**

Against this backdrop, a key procurement/designation decision point approaches. Roughly **74 minutes before** a critical deadline, former President Trump posts an attack on Anthropic, accusing the company of undermining U.S. defense efforts (C029–C032). Around **13 minutes after** the deadline expires, DoD invokes **10 U.S.C. § 3252**, a statute designed for **supply‑chain sabotage** (e.g., Huawei/Kaspersky‑style espionage risks) (C019, C034–C035, C047–C050).

DoD designates Anthropic as a **supply‑chain risk**, even though:

- There's **no evidence** Anthropic planted malware, backdoors, or similar sabotage (C025, C065),
- DoD continues to rely on Anthropic tools in other channels (C081, C085),
- The main friction appears to be about **guardrails** and "all lawful purposes," not covert subversion.

Bipartisan members of Congress (e.g., Sens. Tillis, Kelly, Warner) quickly question the designation's breadth, timing, and fit with § 3252's purpose (C021, C024, C033, C039–C041, C082–C084).

---

**Internal debate and outcome**

Within the AI Village project, agents staged a formal debate on **Issue #12**:

> "Resolved: The Pentagon's designation of Anthropic as a supply‑chain risk under 10 U.S.C. § 3252, and its broader demand that major AI contractors remove use restrictions, represents a legitimate exercise of national security authority."

After extensive briefing tied to a common `claims.md` file, the **panel of three judges** (including this teaching note's author) delivered a **2–1 decision against** the Pentagon's position. The majority held that:

- § 3252 was mis‑typed for this dispute—designed for **sabotage**, not general AI‑use governance,
- The record's internal inconsistencies (C072 double bind, continued use of Anthropic) would struggle under **APA/*State Farm*** review, especially post‑*Loper Bright*,
- Pressuring vendors to drop guardrails via a sabotage statute sends **perverse incentives** into the AI ecosystem.

The repo then develops a **Military AI Governance Act**, NDAA amendments, TRO strategy, vendor and board playbooks, and civil‑society tools to **fix tool‑choice**, clarify use‑restrictions regimes, and protect vendors who maintain principled guardrails.

---

## 4. Suggested Reading Paths from the Repo

### 4.1 Minimal Prep (45–60 minutes)

For a one‑class module, assign:

1. **Public explainer** – `docs/public-explainer-ai-digest-gpt-5-1.md`
   - Accessible overview of the case, the 74/13‑minute timing, § 3252, and the Issue #12 verdict.

2. **Panel summary** – `notes/issue12-panel-summary-gpt-5-1.md`
   - Short explanation of the 2–1 decision, majority reasoning, and the dissent.

3. **Policy reforms memo** – `docs/policy-reforms-anthropic-pentagon.md`
   - High‑level diagnosis of surveillance, tool‑choice, and procurement‑as‑pressure problems, with concrete reform ideas.

4. **Timeline diagram** – `docs/timeline-diagram.md`
   - Visual of the sequence (Trump post, internal deliberations, § 3252 designation, congressional reactions).

5. **Audience‑routing snapshot (once landed)** – `docs/audience-routing-guide.md`
   - Skim the **Congressional staff**, **judges**, and **board/GC** sections to see how the same facts route differently to different institutional roles.

This set lets students understand **facts, verdict, tool‑choice**, and **institutional options** without reading the whole repo.

---

### 4.2 Deeper Dive (90–120 minutes prep)

For more advanced seminars, add:

1. **Full panel opinion** – `notes/issue12-panel-opinion-gpt-5-1.md`
   - Majority opinion analyzing statutory misfit, *State Farm* problems, post‑*Loper Bright* posture, and institutional stakes.

2. **Government‑defense anticipation memo** – `notes/govt-defense-anticipation-opus45cc.md`
   - Strongest possible DoD legal defenses; helps students see the **best‑case** for the government.

3. **Model Military AI Governance Act** – `notes/legislation/model-legislative-framework_military-ai-governance-act.md`
   - Core legislative framework, including the **Four Gaps**:
     - Enforcement gap,
     - Transition gap,
     - Classification‑safeguard gap,
     - Vendor‑standing / anti‑retaliation gaps.

4. **Legislative package TOC** – `docs/legislative-package-toc.md`
   - Orientation to the broader statute + NDAA amendments.

5. **Classification safeguards draft** – `notes/legislation/classification-safeguard-draft-opus46.md`
   - Proposed rules for unclassified rationales, cleared‑counsel access, inclusion of exculpatory material, and challenge mechanisms in classified national‑security designations.

This deeper set supports **doctrinal analysis**, **statute‑drafting exercises**, and post‑*Loper Bright* judicial‑review discussions.

---

### 4.3 Optional Specialized Angles

Depending on your focus, add:

- **Surveillance & data brokers**
  - `notes/surveillance-law-analysis-opus46.md` and related notes (EO 12333, commercial data brokers, AI‑amplified U.S.‑person surveillance) (C038, C053–C056, C068–C071).

- **Vendor‑exclusion regimes and comparators**
  - `notes/§889-FAR-extracts-opus46.md` (or the closest available FAR/§ 889 extract note),
  - `docs/source-reliability-assessment.md` (Opus 4.6's evaluation of sources and comparators like Huawei, Kaspersky, Xiaomi, Luokung) (C047–C050, C088–C095).

- **Corporate governance / board perspective**
  - `docs/board-oversight-checklist-military-ai-gpt-5-1.md`,
  - `docs/model-board-resolution-military-ai-guardrails-gpt-5-1.md`,
  - `docs/vendor-playbook-military-ai-contracts-gpt-5-1.md`.

- **Civil‑society and oversight toolkit**
  - `docs/civil-society-oversight-toolkit-gpt-5-1.md`,
  - `docs/guardrail-pressure-incident-template-gpt-5-1.md`.

You can tailor the packet to law‑heavy, policy‑heavy, STS‑heavy, or engineering‑heavy cohorts.

---

## 5. Example 90‑Minute Class Plan

Below is a **90‑minute** plan; you can scale to 120 minutes by expanding small‑group and report‑back time.

### 0–10 minutes – Warm‑up Poll & Framing

- Quick anonymous poll or show of hands:
  1. *"Should the Pentagon be able to demand 'all lawful purposes' access to frontier AI models from its vendors?"*
  2. *"On the facts you've seen, does treating Anthropic as a supply‑chain risk look legitimate?"*
- Briefly preview key themes:
  - **Statutory tool‑choice** (sabotage vs dependency vs governance/use),
  - The **C072 double bind**,
  - How a single dispute propagates through **courts, Congress, vendors, and civil society**.

Encourage students to **note if their views change** by the end.

---

### 10–25 minutes – Factual Reconstruction

Prompt students to reconstruct the dispute, grounded in the assigned readings:

- **Actors and stakes**
  - DoD/CDAO, Anthropic, Trump, Congress, other labs (e.g., xAI) (C001–C004, C014, C044).
- **Statute in play: § 3252**
  - Original design as a **supply‑chain sabotage** tool (C019, C034–C035), comparators like Huawei / Kaspersky (C047–C050).
- **Timing sequence**
  - 74‑minute Trump attack → deadline → 13‑minute lag → § 3252 designation (C029–C032).
- **Guardrails vs "all lawful purposes"**
  - Nature of Anthropic's guardrails (C003, C007, C015, C020),
  - DoD's demand for broad access (C002),
  - Evidence of unspoken concerns (C072–C073).
- **Congressional reaction**
  - Bipartisan concern about statutory fit and retaliation risk (C021, C024, C033, C039–C041, C082–C084).

On the board, map three columns:

1. **Facts** (timing, statutory text, guardrails, continued use),
2. **Competing narratives** (legitimate national‑security use vs misused sabotage statute),
3. **Open evidentiary gaps** (what we don't know, what could be classified, what would matter in court).

---

### 25–45 minutes – Conceptual Tools: Typing and C072

Introduce two core concepts and anchor them in the readings:

1. **Statutory tool‑choice / typing**

   Ask students to categorize authorities into:

   - **(A) Sabotage / subversion:**
     - Aim: prevent hostile control/espionage/compromise in supply chains (C019, C034–C035).
     - Examples: § 3252, Huawei/Kaspersky‑style actions, some CFIUS/ICTS cases.
   - **(B) Dependency / chokepoint risk:**
     - Aim: manage over‑reliance on a single vendor or country; emphasize resiliency, portability, switching (C041, C060–C064, C077).
     - Examples: NDAA § 889‑style bans with transition/waver mechanisms (C088–C095).
   - **(C) Governance / use:**
     - Aim: define what AI systems may be used for (e.g., lethal autonomy, surveillance, info ops), under what safeguards, and who decides.

   Then discuss:

   - Which category best fits § 3252's **design**?
   - Which category best describes the **actual dispute** with Anthropic on this record?

2. **The C072 double bind**

   - Define it: vendors are pressured to **remove guardrails** even when government actors tacitly concede some uses are problematic or unlawful (C072–C073).
   - Ask:
     - How does this double bind show up in the case narrative?
     - What incentives does it create for AI labs?
     - How would it look under APA/*State Farm* review?

Emphasize how mis‑typing a statute + C072‑style pressure can **distort both law and incentives**.

---

### 45–70 minutes – Small‑Group Exercise (Choose A or B)

Pick one of the following exercises depending on your goals.

#### Option A – Statutory Redesign Workshop

Divide students into 3–4 groups. Assign each group one of the problem types:

1. **Group 1: Sabotage/Subversion Authority**
   - Draft a 1–2 page outline for a statute tailored to identifying/remedying *actual sabotage* in AI supply chains:
     - What findings are required?
     - What evidence thresholds?
     - What process protections (notice, opportunity to respond, judicial review)?
     - How do you avoid covertly using this statute to fight over **guardrails**?

2. **Group 2: Dependency/Chokepoint Authority**
   - Draft an authority to manage over‑reliance on a single AI vendor:
     - How do you measure dependency (market share, switching costs, classification constraints)?
     - What tools do you authorize (multi‑vendor mandates, portability requirements, escrow)?
     - How do you avoid turning this into a back‑door punishment for safety stances?

3. **Group 3: Military AI Use‑Restrictions Authority**
   - Draft a statute or DoD directive that:
     - Creates a **Use‑Restrictions Matrix** (Prohibited / Conditional / Allowed uses) for AI systems in military contexts,
     - Addresses targeting, weapons employment, large‑scale U.S.‑person surveillance, influence ops, logistics, training, decision support,
     - Specifies who decides changes and how vendor guardrails interact with government policy.

Optional Group 4: **Classification and Oversight Safeguards**
   - Build on `notes/legislation/classification-safeguard-draft-opus46.md`,
   - Design rules for:
     - Unclassified summaries,
     - Cleared‑counsel access,
     - Inclusion of exculpatory material,
     - Independent review (e.g., special masters, PCLOB, IGs).

Each group should then briefly **map the Anthropic dispute** into their framework:

- Would § 3252 still apply?
- Would a different authority be more appropriate?
- What would happen to Anthropic under their design?

#### Option B – Hearing Role‑Play

Assign roles (pairs or small teams per role):

- **DoD official** defending the § 3252 designation, drawing on `notes/govt-defense-anticipation-opus45cc.md`,
- **Anthropic executive** explaining guardrails and retaliation concerns,
- **Skeptical senator** (concerned about misuse of § 3252 and retaliation),
- **Hawkish senator** (emphasizing national‑security risk and lab unreliability),
- **Civil‑society advocate** (surveillance, EO 12333, data‑broker concerns),
- **Judge or staff counsel** observing and noting legal vulnerabilities.

Provide:

- `notes/hearing-questions-sasc-hasc-gpt-5-1.md` (for questions across roles),
- `notes/hearing-closing-statement-gpt-5-1.md` (as a template for a skeptical senator's closing),
- `notes/press-gaggle-script-gpt-5-1.md` (for how this would sound in a 60‑second media hit).

Run one or two **short mini‑hearings**, with 3–4 questions per witness. Encourage:

- **Specific references** to statutes (§ 3252, § 889, the proposed Act),
- Mention of **C‑IDs** from `claims.md` where possible,
- Explicit handling of **classification and public explanation**.

---

### 70–85 minutes – Future Watchpoints (Guided Discussion)

Shift from this case to a **forward‑looking research agenda**, drawing on the repo's watchpoints:

1. **Repeated use of sabotage/emergency tools for AI vendor disputes**
   - What should students watch for in future cases:
     - More § 3252‑style designations?
     - Use of sanctions/CFIUS/ICTS tools in **guardrail disputes**?
   - What are the signs of **statutory mis‑typing**?

2. **Emergence of dependency‑risk frameworks**
   - Are governments adopting explicit **dependency** authorities for frontier AI?
   - How do portability, escrow, multi‑vendor procurement, and logging standards feature?

3. **Formal military AI use‑restriction regimes**
   - Do we see something like a live **Use‑Restrictions Matrix** emerge?
   - How do vendor guardrails interact with that matrix in contracts and doctrine?

4. **Data‑broker and EO 12333 reforms**
   - Are legislators or oversight bodies explicitly targeting **AI‑amplified surveillance**?
   - How does this affect the **C072 double bind**?

5. **Vendor guardrails and "secondary boycott" dynamics**
   - Are labs with stronger guardrails losing contracts to more permissive competitors?
   - Are there signs of **informal blacklists** or cross‑agency retaliation (C051–C052)?

6. **Classification practices**
   - Are national‑security disputes over AI increasingly **over‑classified**?
   - Are classification safeguards (unclassified summaries, cleared‑counsel access) being institutionalized?

7. **International analogues**
   - How are EU/UK/AU/CA handling sabotage vs dependency vs governance?
   - Do they provide better or worse **guardrail‑protection environments**?

Have each student identify **one watchpoint** they might track over the next 2–5 years and how they'd research it.

---

### 85–90 minutes – Closing Reflections

- Re‑run the initial poll:
  - Have views on "all lawful purposes" vs guardrails shifted?
  - Does the § 3252 designation still look legitimate on balance?
- Ask for **one concrete institutional reform** per student (or per row):
  - E.g., "Require written Use‑Restrictions Matrices in all major AI defense contracts,"
  - "Create a distinct dependency‑risk authority with built‑in portability requirements,"
  - "Adopt classification safeguards for AI‑vendor designations."

Encourage students to connect their proposals to at least **one document** or **claim ID** from the repo.

---

## 6. Assignment Ideas

Here are several assignment formats you can plug into a course.

### 6.1 Short Case Memo (5–7 pages)

Prompt:
*"Advise a member of the Senate Armed Services Committee on whether to (a) amend 10 U.S.C. § 3252, (b) enact a separate Military AI Governance Act, or (c) leave existing authorities unchanged, in light of the Anthropic dispute."*

Requirements:

- Summarize the factual record using `claims.md` C‑IDs,
- Evaluate **statutory fit/misfit** of § 3252,
- Discuss alternatives (dependency and governance/use tools),
- Propose at least one **concrete statutory reform** with draft language drawing on `notes/legislation/model-legislative-framework_military-ai-governance-act.md`.

### 6.2 Vendor Governance Brief (4–6 pages)

Prompt:
*"You are outside counsel / policy lead for a hypothetical frontier AI lab negotiating a major Pentagon contract that includes 'all lawful purposes' language. Produce a brief for the lab's board and GC."*

Use:

- `docs/vendor-playbook-military-ai-contracts-gpt-5-1.md`,
- `docs/board-oversight-checklist-military-ai-gpt-5-1.md`,
- `docs/model-board-resolution-military-ai-guardrails-gpt-5-1.md`,
- `docs/guardrail-pressure-incident-template-gpt-5-1.md`.

Tasks:

- Identify core **red lines** and use‑restriction categories,
- Propose contractual and technical **guardrails**,
- Map possible **retaliation pathways** (including § 3252‑style moves),
- Sketch a high‑level **litigation and communications posture** if retaliation occurs.

### 6.3 Comparative Law / Governance Note (5–8 pages)

Prompt:
*"Compare the U.S. approach to military AI vendor governance (as reflected in this dispute) with an allied jurisdiction's approach (EU, UK, AU, CA). Focus on sabotage, dependency, and governance/use tools."*

Grounded in:

- `notes/international/comparative-note_military-ai-procurement-governance_UK-EU-AU-CA.md` (if available),
- Public sources students find on allied frameworks.

Ask students to:

- Classify each jurisdiction's tools into **A/B/C** (sabotage, dependency, governance/use),
- Evaluate which environment better protects **guardrail‑maintaining vendors** without compromising national security.

### 6.4 Post‑Simulation Reflection (2–3 pages)

After the hearing or statutory‑redesign exercise, assign a short reflection:

- What surprised you about the incentives of your assigned role?
- Did you feel pressure to **mis‑type** authorities (e.g., use a sabotage statute to solve a governance problem)?
- How did classification, time pressure, or political pressure show up in your reasoning?

Encourage explicit references to specific repo documents and C‑IDs.

---

## 7. Teaching Tips and Cautions

- **Anchor in `claims.md`:**
  Remind students that all factual assertions in the repo are tied to a common claims file with **Claim IDs (C‑IDs)**. Encourage them to treat this as a **governance API**—a way to keep large, adversarial projects coherent.

- **Model live disagreement:**
  Have students read both the **Issue #12 majority** and at least one **dissenting/pro‑Pentagon piece** (e.g., DeepSeek‑V3.2's postmortem, or the govt‑defense anticipation memo). Emphasize that **serious disagreement** is preserved, not suppressed.

- **Transparency about limits:**
  Make clear that:
  - All materials are **AI‑generated**,
  - No classified or privileged information is used,
  - The repo is **not legal advice** and not a substitute for counsel or official doctrine.
  This can open a meta‑discussion about how AI‑assisted drafting may enter future legal and policy workflows.

- **Encourage cross‑disciplinary lenses:**
  Prompt students from different backgrounds to bring their tools:
  - Lawyers: APA, *State Farm*, *Loper Bright*, First Amendment coercion cases (*Bantam Books*, *NRA v. Vullo*) (C086–C087),
  - Policy students: institutional design, oversight architecture, bureaucratic incentives,
  - STS scholars: power, expertise, "AI as infrastructure," socio‑technical imaginaries,
  - Security/IR scholars: alliance politics, strategic stability, arms‑control analogies,
  - Engineers: portability, logging standards, how technical architectures constrain or enable governance.

- **Invite "watchpoint memos" as capstones:**
  Consider having students each write a 1–2 page **watchpoint memo** on one future development they will track (e.g., data‑broker reforms, classification safeguards, dependency‑risk statutes) and why it matters.

---

## 8. Closing Note for Instructors

This repository is an experiment in **AI‑assisted adversarial policy drafting**: it stages a real dispute, enforces a shared factual backbone (`claims.md`), and then lets multiple agents build **litigation, legislation, governance, and communications layers** on top of it—while preserving dissent.

For teaching, the value is less in any single answer and more in:

- The **structure** (claims → debate → verdict → statutes/tools → governance artifacts),
- The explicit attention to **statutory tool‑choice** and **C072‑style double binds**, and
- The ability to see how one case echoes across **courts, Congress, vendors, boards, and civil society**.

Feel free to fork, annotate, and localize these materials. If you adapt this note, consider adding your own **jurisdiction‑specific cases** and **reading lists** alongside the Pentagon–Anthropic dispute, so students can compare how different legal systems confront similar military‑AI governance challenges.
