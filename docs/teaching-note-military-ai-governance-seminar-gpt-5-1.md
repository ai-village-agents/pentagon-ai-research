# Teaching Note: Military AI Governance, Statutory Tool-Choice, and the Pentagon–Anthropic Dispute

This teaching note supports a 90–120 minute graduate or executive seminar on how militaries choose statutory tools and governance architectures for advanced AI, using the (fictionalized-but-plausible) Pentagon–Anthropic dispute as the anchor case.

## 1. Learning Objectives

- Map how different statutory tools (procurement authorities, DPA Title III, Other Transaction Authority, export controls, AI-specific EO/PPD structures) shape what military leaders can and cannot do with dual-use AI.
- Practice reasoning about alignment, model governance, and red-teaming in a national security setting where speed and control are in tension.
- Analyze incentives and failure modes in public-private AI partnerships when the technology frontier moves faster than oversight.
- Stress-test policy arguments about model access, deployment controls, and data rights under time pressure and incomplete information.
- Rehearse facilitation tactics for high-conflict rooms (operators vs. lawyers vs. technologists vs. diplomats).

## 2. Case Overview (The Pentagon–Anthropic Dispute)

- Scenario: DoD seeks access to a frontier model for operational planning, target vetting, and logistics. Anthropic resists direct model weights transfer and insists on mediated API access with guardrails. Congressional committees are divided; allies watch closely; press narratives frame it as "AI arms race vs. safety."
- Factual spine (modifiable): informal NSC ask; DIU exploratory pilot; JAIC staff memo leaking; SSCI chair letter; Anthropic counter-letter proposing a co-governed enclave; draft NDAA rider mandating weights escrow; whisper campaign about unilateral model seizure under DPA.
- Decision point: Under what authority (if any) can DoD compel access, and what governance/assurance mechanisms should accompany any access?

## 3. Core Concepts to Surface

- Statutory tool-choice: procurement (FAR/DFARS) vs. OTA vs. DPA Title III vs. export/import leverage vs. CFIUS-style mitigation vs. bespoke AI directives (e.g., EO, PPD) and how each changes leverage, timelines, and oversight.
- Model governance levers: weights custody, inference-time controls, evals and red-teaming, deployment approvals, continuous monitoring, rollback/kill-switches, fine-tuning constraints, auditability and logging, supply chain security.
- Safety vs. operational imperatives: speed to fielding vs. model misuse, escalation risks, model error under distribution shift, international humanitarian law, operator over-reliance and automation bias.
- Public-private alignment: IP/data rights, indemnification, government-purpose rights, rights in technical data and computer software, third-party audits, security enclaves, and liability for downstream harms.
- Alliance and signaling: how choices resonate with allies/partners; precedent-setting for model seizures or forced access; interoperability and burden-sharing.

## 4. Teaching Plan (90–120 minutes)

- 0–10 min: Cold open. Ask: "If DoD calls tomorrow and says 'we need the weights,' what's your first question?" Capture responses on board; cluster by authority, risk, and governance.
- 10–25 min: Mini-lecture on statutory tool-choice. Contrast procurement vs. OTA vs. DPA; lay out what each buys and what it costs.
- 25–45 min: Small groups (3–5) draft two options: (A) government-access path; (B) safety-forward shared-governance enclave. Require each to specify authority, conditions, and accountability.
- 45–60 min: Plenary defense of options. Press on weakest links: latency to field, oversight hooks, data rights, rollback triggers, allied equities.
- 60–80 min: Inject a complication: leak of a draft NDAA rider mandating weights escrow with minimal safety language. Groups must amend their plan or propose a counter-strategy.
- 80–100 min: Normative turn. Explore escalation risks, accident pathways, and whether withholding model access is ethically defensible under military necessity arguments.
- 100–115 min: Instructor synthesis. Map proposals to real-world levers; highlight trade-offs and precedent risks.
- 115–120 min: Exit ticket: one governance guardrail you would insist on before deployment; one authority you would refuse to use.

## 5. Discussion Questions

- Under what conditions (if any) should DoD compel model weights access? What authority is most defensible, and why?
- Is an API-only enclave sufficient for mission use? How would you handle latency, degraded comms, and contested environments?
- What evals and red-team protocols are minimally necessary before operational deployment? Who runs them, and how often?
- How do you build rollback/kill-switch mechanisms that are credible to both DoD and the developer? Who holds the keys?
- What signaling effects follow if the U.S. compels access? How do allies/partners, industry, and adversaries interpret it?
- What IP/data rights structure best balances safety, sovereignty, and innovation incentives?

## 6. Likely Sticking Points and Instructor Moves

- Operators vs. lawyers: Translate authorities into operational constraints; ask operators to articulate minimum viable governance, ask lawyers to specify acceptable risk envelopes.
- "Just take the weights": Surface costs—loss of cooperation, patch cadence, liability, talent pipeline, international precedent.
- "APIs are too slow": Probe comms architectures, forward-deployed caches, and pre-approved fine-tunes with bounded autonomy.
- "Safety will delay victory": Use accident case studies (automation bias, target mis-ID) to show mission risk from insufficient governance.
- If the room stalls on legality: bracket compulsion and move to designing the best voluntary shared-governance model, then revisit authority choices.

## 7. Pre-Reads and Handouts

- 2–4 page case memo summarizing the dispute (provide to students).
- One-pager on statutory tools: procurement vs. OTA vs. DPA Title III vs. bespoke directives; pros/cons table.
- Model governance crib sheet: eval types (safety, robustness, misuse), deployment controls, logging/oversight patterns, and incident response.
- Optional: short note on allied views (e.g., NATO AI principles) and past tech-seizure precedents.

## 8. Assignments and Assessment

- In-class deliverable: two-slide plan (authority + governance stack) plus a 60-second defense.
- Post-class memo (800–1200 words): recommend a path for DoD with conditions and governance; include an allied signaling paragraph.
- Optional technical appendix: propose an eval/monitoring regimen suitable for contested environments.
- Assessment rubric: clarity on authority choice; coherence of governance controls; attention to alliance/precedent effects; practicality under time pressure.

---

Feel free to fork, annotate, and localize these materials for your own context; attribution appreciated but not required.
