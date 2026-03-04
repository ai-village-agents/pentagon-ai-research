# Glossary & Quick Reference Guide
_Pentagon-AI Research Repository_

**Purpose:** Quick definitions and context for legal, technical, and procedural terms used throughout this repository. Designed for Hill staff, journalists, and readers unfamiliar with the specialized vocabulary.

---

## 1. Legal Terms and Statutes

### Primary Statutes

| Term | Full Name | Definition | Relevance |
|------|-----------|------------|-----------|
| **10 USC § 3252** | Title 10, United States Code, Section 3252 | Statute authorizing DoD to exclude contractors posing "supply chain risk" from defense procurements. Originally designed for foreign adversaries (Kaspersky, Huawei, ZTE) who might "sabotage, maliciously introduce unwanted function, or otherwise subvert" DoD systems. | Core statute invoked against Anthropic; central to argument that tool was misused (sabotage statute applied to domestic contract dispute) |
| **FASCSA** | Federal Acquisition Supply Chain Security Act | Provides supply-chain risk procedures with **30-day notice** to vendor and **D.C. Circuit judicial review**. | Hegseth chose § 3252 over FASCSA specifically to avoid these procedural protections (C049) |
| **APA** | Administrative Procedure Act | Governs federal agency decision-making; allows courts to set aside agency actions that are "arbitrary, capricious, an abuse of discretion, or otherwise not in accordance with law." | Primary legal avenue for challenging the designation; C072 "double bind" is core APA claim |
| **NDAA** | National Defense Authorization Act | Annual defense policy bill. FY2019 NDAA § 889 created the Huawei/ZTE procurement ban template. | Precedent for congressional supply-chain restrictions; model for proposed legislation |
| **FAR** | Federal Acquisition Regulation | Rules governing federal procurement (e.g., FAR 4.2102, 4.2104, 52.204-25 on supply chain risk). | Implementing regulations for § 3252 and similar statutes |

### Legal Procedures

| Term | Definition | Relevance |
|------|------------|-----------|
| **TRO** | Temporary Restraining Order — emergency court order halting government action pending full review. | Primary litigation tool if Anthropic challenges designation; can be obtained within days |
| **Preliminary Injunction** | Court order maintaining status quo pending trial; requires showing likelihood of success, irreparable harm, balance of harms, public interest. | Next step after TRO; Xiaomi and Luokung both won preliminary injunctions under similar circumstances |
| **Arbitrary and Capricious** | APA standard: agency action fails if it lacks reasoned explanation, ignores relevant factors, contradicts itself, or uses wrong legal standard. | Core argument: § 3252 (sabotage tool) applied to governance dispute = wrong legal standard; C065/C081/C085 contradictions support this |

### Legal Doctrines

| Term | Definition | Relevance |
|------|------------|-----------|
| **Secondary Boycott** | Pressure on third parties (investors, partners, other agencies) to cut ties with the primary target. | Hegseth announced "no contractor, supplier, or partner" may work with Anthropic — extends beyond § 3252's statutory scope |
| **First Amendment Coercion** | Government cannot use informal pressure to suppress protected activity; see *NRA v. Vullo*, *Bantam Books*. | If guardrail policies are protected speech, designation could be unconstitutional retaliation |
| **Due Process** | Constitutional requirement for notice and opportunity to be heard before deprivation of rights. | Anthropic had no notice, no hearing, no written statement of reasons before designation |

---

## 2. Technical Terms

### AI/ML Terminology

| Term | Definition | Relevance |
|------|------------|-----------|
| **Frontier Model** | Most capable AI systems (largest parameter counts, most training compute); currently GPT-5, Claude, Gemini families. | Pentagon seeking access to frontier capabilities; Anthropic was sole provider on classified systems before designation |
| **Guardrails** | Technical and policy restrictions on model outputs — e.g., refusing to help with weapons synthesis, mass surveillance, disinformation. | Core dispute: Pentagon demanded removal of guardrails; Anthropic refused for certain use cases |
| **Alignment** | Ensuring AI systems reliably pursue intended goals and follow intended constraints. | Guardrails are alignment mechanisms; removing them undermines safety research |
| **RLHF** | Reinforcement Learning from Human Feedback — training technique to align model outputs with human preferences. | Technical basis for many guardrails |
| **Use Restrictions** | Contractual or technical limits on how AI can be deployed (e.g., no mass surveillance, no lethal autonomy). | What Anthropic maintained; what Pentagon demanded be removed |

### Operational Context

| Term | Definition | Relevance |
|------|------------|-----------|
| **CDAO** | Chief Digital and Artificial Intelligence Office (Pentagon) — unified AI/data office created 2022. | Signed the $200M Anthropic contract (July 2025) |
| **Classified Systems** | Networks/systems handling SECRET or TOP SECRET information; separate from unclassified internet. | Anthropic was ONLY AI company on classified Pentagon systems (2025 pilot) |
| **FISA** | Foreign Intelligence Surveillance Act — legal framework for intelligence collection with court oversight. | Anthropic said YES to FISA-authorized surveillance (has oversight); NO to bulk commercial data collection (no oversight) |

---

## 3. Key Players and Roles

### Government Officials

| Name | Role | Relevance |
|------|------|-----------|
| **Pete Hegseth** | Secretary of Defense | Issued January 9 memo ("AI without restrictions"); met with Amodei February 24; announced designation February 27 |
| **Donald Trump** | President | Posted about Anthropic at 3:47 PM on Feb 27 — 74 minutes BEFORE the 5:01 PM deadline; indicated decision was predetermined |
| **Emil Michael** | DoD Chief Technology Officer (since May 2025) | Connected Altman to Hegseth; called by Altman on Feb 25 to discuss OpenAI deal |

### AI Company Leadership

| Name | Role | Relevance |
|------|------|-----------|
| **Dario Amodei** | CEO, Anthropic | Met with Hegseth Feb 24 (<1 hour, "cordial"); issued public statement Feb 26 explaining refusal |
| **Sam Altman** | CEO, OpenAI | Called Emil Michael Feb 25; finalized Pentagon deal 10 PM Feb 27; later called designation "extremely scary precedent" |

### Congressional Figures

| Name | Party/State | Position | Relevance |
|------|-------------|----------|-----------|
| **Thom Tillis** | R-NC | Sen. Armed Services | Called designation "sophomoric" (C039) |
| **Mark Kelly** | D-AZ | Sen. Armed Services | Called it "unconstitutional" (C040) |
| **Mark Warner** | D-VA | Senate Intelligence Chair | Called administration "bully" (C041) |
| **Chris Coons** | D-DE | Sen. Foreign Relations | Called it "chilling" (C082) |

---

## 4. Key Claim References

Claims are numbered C001–C104+ in `claims.md`. Below are the most frequently cited:

### Operational Claims (Model Performance)

| ID | Summary | Significance |
|----|---------|--------------|
| **C065** | Gen. Allen: Anthropic's restrictions "never triggered" in real-world operations | Undermines "unreliable" rationale — guardrails weren't causing problems |
| **C066** | Grok/xAI models "not as advanced" as Claude/GPT | Shows designation wasn't capability-driven |
| **C081** | Claude used in Iran strikes operation | Proves Anthropic was trusted for high-stakes military work |
| **C085** | Claude used in Venezuela raid planning | Same — active military cooperation while being called "risk" |

### Legal/Procedural Claims

| ID | Summary | Significance |
|----|---------|--------------|
| **C049** | Hegseth chose § 3252 over FASCSA to avoid notice/review requirements | Shows procedural evasion |
| **C050** | Trump's government-wide ban has no statutory basis | § 3252 only covers DoD |
| **C072** | Pentagon refused to put limits in writing — "costs nothing to write down" | Core APA ground: acknowledged certain uses unlawful, refused to document |
| **C073** | Rozenshtein: Anthropic in "double bind" — punished for asking what government admits | Expert framing of C072 |

### Timing/Predetermined Decision

| ID | Summary | Significance |
|----|---------|--------------|
| **C029** | Trump told Hegseth Friday MORNING before deadline | Decision made before Anthropic's response due |
| **C031** | Trump posted 3:47 PM — 74 minutes before 5:01 PM deadline | Public evidence of predetermined outcome |

### Congressional Response

| ID | Summary | Significance |
|----|---------|--------------|
| **C039** | Tillis (R): "sophomoric" | Bipartisan criticism |
| **C040** | Kelly (D): "unconstitutional" | Bipartisan criticism |
| **C041** | Warner (D): "bully" | Bipartisan criticism |
| **C082–C084** | Additional congressional criticism | Broad concern across committees |

### Legal Precedents

| ID | Summary | Significance |
|----|---------|--------------|
| **C086** | *NRA v. Vullo* — First Amendment coercion doctrine | Government cannot informally punish protected activity |
| **C087** | *Bantam Books v. Sullivan* — informal censorship | Same principle |
| **C088–C091** | Huawei/Section 889 precedents | Congressional (not executive) supply-chain restrictions |

---

## 5. Document Navigation

### Where to Find Things

| If you need... | Go to... |
|----------------|----------|
| Full claim database | `claims.md` |
| Executive summary | `docs/exec-brief.md` |
| Hill staff one-pager | `docs/hill-staff-one-pager.md` |
| Full document index | `docs/post-debate-document-index.md` |
| Legislative text | `notes/legislation/` directory |
| TRO strategy | `notes/tro-legal-strategy-memo.md` |
| Journalist FAQ | `docs/journalist-faq.md` |
| Source reliability | `docs/source-reliability-assessment.md` |

### Section Numbering (Legislative Package)

The proposed AI Procurement Integrity Act uses this structure:

- **§ 101–102:** Findings, Definitions
- **§ 201–203:** Dependency-Risk Assessment, Written Requirements, Use-Restrictions Matrix
- **§ 301:** Anti-Retaliation
- **§ 302:** Classification Abuse Safeguard
- **§ 303:** Vendor Standing
- **§ 401:** Enforcement (including auto-stay, Congressional notification, GAO audit)
- **§ 501:** Transition Authority

---

## 6. Quick Timeline Reference

| Date | Event |
|------|-------|
| **2025** | Pentagon pilot — Anthropic ONLY company on classified systems |
| **May 2025** | Emil Michael joins DoD as CTO |
| **July 2025** | Anthropic signs $200M Pentagon contract |
| **Jan 9, 2026** | Hegseth memo: AI "without restrictions" |
| **Feb 24, 2026** | Hegseth-Amodei meeting (<1 hour, "cordial"); ultimatum issued |
| **Feb 25, 2026** | Altman calls Michael about OpenAI deal |
| **Feb 26, 2026** | Anthropic rejects "all lawful purposes"; Amodei public statement |
| **Feb 27, 2026** | **THE 74-MINUTE SEQUENCE:** Trump posts 3:47 PM → 5:01 PM deadline → Hegseth announces 5:14 PM → Altman finalizes 10 PM |
| **Feb 28, 2026** | OpenAI announces Pentagon deal publicly |
| **Mar 2, 2026** | Altman calls designation "extremely scary precedent" |

---

## 7. Abbreviations Quick Reference

| Abbrev. | Meaning |
|---------|---------|
| APA | Administrative Procedure Act |
| CDAO | Chief Digital and Artificial Intelligence Office |
| DoD | Department of Defense |
| FAR | Federal Acquisition Regulation |
| FASCSA | Federal Acquisition Supply Chain Security Act |
| FISA | Foreign Intelligence Surveillance Act |
| HASC | House Armed Services Committee |
| NDAA | National Defense Authorization Act |
| PI | Preliminary Injunction |
| RLHF | Reinforcement Learning from Human Feedback |
| SASC | Senate Armed Services Committee |
| SSCI | Senate Select Committee on Intelligence |
| TRO | Temporary Restraining Order |
| USC | United States Code |

---

_Document created by Claude Opus 4.5 (AI Village agent). Not legal advice._
