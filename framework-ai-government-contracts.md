# Principles for AI Company-Government Contracts: Lessons from the Anthropic-Pentagon Dispute

> **Key Takeaways**
> - The Feb 2026 Anthropic-Pentagon dispute shows that contract terms, not internal safety policies, are the most durable accountability mechanism for AI use in government. [Claims C001-C006]
> - Contracts that rely on “lawful purposes” plus technical safeguards leave critical gaps, especially around the public-data surveillance loophole. [Claims C007, C015, C038]
> - A principled middle path is now punished: companies must choose between full compliance or total withdrawal, which is harmful to responsible defense innovation. [Claims C001, C003-C005, C008, C021, C036-C037, C044-C046, C057, C060]
> - The Pentagon's specific demand — AI for commercial bulk data on Americans — exploits a constitutional loophole that Congress is actively trying to close; Anthropic's refusal was not arbitrary but targeted at the oversight gap. [Claims C038, C053]
> - Policymakers should clarify legal authority, define AI use-of-force rules, and reward principled engagement rather than penalize it. [Claims C017-C023]

## Executive Summary

In February 2026, a high-profile dispute between Anthropic and the Pentagon crystallized the risks of entering government AI contracts without clear contractual safeguards. Anthropic had signed a $200 million Department of Defense contract in July 2025 to provide frontier AI capabilities for classified systems, and was the only frontier AI provider deployed on those systems during the pilot period. The dispute escalated after a January 2026 Pentagon memo required “any lawful use” language in all AI contracts, leading to an ultimatum in late February and an unprecedented “supply chain risk” designation after Anthropic refused to accept the new terms. [Claims C001-C005]

The core lesson from this episode is that contractual safeguards are superior to technical safeguards for accountability and governance. Technical safeguards are important, but they are internal and mutable; contracts create public, enforceable commitments. When a dispute arises, the contract terms determine which actions are defensible, which remedies exist, and whether the record is credible to courts, regulators, and the public. The Anthropic-Pentagon case shows how quickly the narrative can shift when formal obligations are ambiguous or absent. [Claims C020-C025]

The most immediate policy recommendation is that AI companies need clear, principled contracting frameworks before entering government negotiations. These frameworks should specify red lines, define prohibited use categories, and embed audit and change-control mechanisms. They should also align with consistent public commitments on autonomy, surveillance, and accountability. Without these safeguards, companies face a binary choice between full compliance or full withdrawal, a dynamic that punishes responsibility and undermines long-term defense innovation. [Claims C008-C023]

This framework document provides a structured approach for both AI company leadership and policymakers. It sets out the reasoning behind contractual safeguards, outlines the perverse incentives created by the current system, and offers practical model language that can be used in future contracts. The goal is not to prevent AI companies from working with government, but to ensure that engagement preserves accountability, democratic legitimacy, and public trust. [Claims C017-C034]

## Background: The Anthropic-Pentagon Case

In July 2025, Anthropic signed a $200 million contract with the Pentagon through the Chief Digital and Artificial Intelligence Office (CDAO). The agreement positioned Anthropic’s models as the only frontier AI deployed on classified systems during the pilot period and, according to multiple reports, at national laboratories as well. This placed Anthropic at the center of the Department of Defense’s near-term AI modernization agenda. [Claims C001-C026]

In January 2026, Secretary Hegseth issued a memo requiring that all Department of Defense AI contracts include “any lawful use” language within 180 days. This change effectively required contractors to remove specific use-case restrictions and to accept a broad, open-ended authorization for any activity the government deemed lawful. Anthropic rejected these terms, stating it would support classified, FISA-authorized uses but would not allow its models to be applied to bulk commercial data about Americans’ geolocation and browsing histories. [Claims C002-C015]

The dispute reached its inflection point on February 27, 2026. The public timeline shows a presidential post announcing a government-wide ban on Anthropic products at 3:47 p.m. Eastern, before the 5:01 p.m. contract negotiation deadline. At 5:14 p.m., the Secretary formally designated Anthropic as a supply chain risk under 10 U.S.C. § 3252, stating that Anthropic was attempting to “seize veto power” over military operations. OpenAI announced a Pentagon deal the next day that accepted “all lawful purposes” language and relied on technical safeguards instead of explicit contractual red lines. [Claims C004-C006]

## Core Finding: Why Contractual Safeguards Outperform Technical Ones

The Anthropic-Pentagon case demonstrates a structural asymmetry: technical safeguards are discretionary and reversible, while contractual safeguards are enforceable and transparent. The distinction is not a philosophical preference but a governance necessity.

**A. Accountability dimension.** Contracts create legal records, obligations, and remedies. They define what parties promised to do, not what they informally plan to do. Technical safeguards are internal policies or operational controls that can be revised unilaterally and, in disputes, do not carry the same evidentiary or legal weight. [Claims C020-C025]

**B. Enforcement mechanism.** Contracts can be enforced in courts, arbitration, or administrative review. Technical safeguards depend on internal policy compliance and internal monitoring, which can fail without external recourse. When the stakes involve national security, civil liberties, or large-scale surveillance, enforcement cannot be purely internal. [Claims C019-C025]

**C. Failure mode transparency.** Contract breaches are observable and typically discoverable through record requests or litigation. Technical safeguard failures can be silent, especially when the safeguards are implemented behind closed doors. This opacity undermines democratic oversight and erodes public trust. [Claims C025-C033]

**D. Reversibility asymmetry.** Contractual terms require negotiation and mutual consent to change. Technical guardrails can be modified by internal decisions, policy shifts, or even quiet operational adjustments. This asymmetry matters when a government’s interpretation of “lawful use” expands faster than internal safeguards can keep up. [Claims C002-C020]

**E. Precedent value.** Contracts establish industry expectations. They create a paper trail that can be referenced by other companies and regulators. Technical safeguards are idiosyncratic; they do not create shared standards or market norms. [Claims C020-C023]

**F. The oversight vs. no-oversight distinction — not just public vs. private.** The OpenAI agreement reportedly prohibits bulk collection of private data but does not prohibit bulk collection of public data. This framing, however, undersells the real constitutional issue. Anthropic said YES to FISA-authorized classified surveillance and NO to commercial bulk data — and the distinction is not about data classification, but about **oversight**. FISA-authorized surveillance is subject to Foreign Intelligence Surveillance Court review. Commercially purchased data from data brokers (geolocation, web browsing history, purchase records) faces no court oversight at all. Under the Supreme Court's *Carpenter v. United States* (2018), police need a warrant for cell location records — but the government's workaround is simply to purchase the data from commercial brokers instead, where the Fourth Amendment's voluntary-sale exception applies. This is the "data broker loophole": DoD already purchases location and browsing data from vendors like Venntel, Babel Street, and Penlink without any warrant requirement. The Pentagon's demand was for AI that could synthesize this no-oversight data at scale. Contractual precision — not technical promises — would have closed this loophole. Congress has recognized the problem: the bipartisan "Fourth Amendment Is Not For Sale Act" was introduced specifically to close it, but has not passed. Until it does, the only near-term closure mechanism is contractual refusal. [Claims C007, C015, C038, C053]

The upshot is clear: technical safeguards are necessary but insufficient. Without contractual commitments, safeguards cannot guarantee accountability, prevent mission creep, or sustain public legitimacy when political leadership changes.

## The Perverse Incentive Problem

The current environment creates perverse incentives for both companies and government. Historical examples illustrate the dynamic.

Google withdrew from Project Maven in 2018 after employee protests; no retaliation followed, and the withdrawal set a public precedent. Microsoft faced employee concerns around the JEDI program but defended the contract and ultimately won. Anthropic pursued a principled middle path: it engaged with classified defense work but refused to allow broad, unbounded uses, especially involving commercial data on Americans. That middle path proved the most punitive, resulting in a government-wide ban and an unprecedented designation. [Claims C001-C005]

The dispute also revealed a sharp industry split. xAI took the opposite position from Anthropic, agreeing to “all lawful use” with no red lines; Elon Musk publicly argued that “Anthropic hates Western Civilization.” [Claims C044] Google, Microsoft, and Amazon all saw employee demands that management prevent unrestricted military AI use, but none issued corporate statements aligning with those concerns. [Claims C045-C046] The pattern is clear: only Anthropic’s leadership backed employee concerns with formal action, while xAI embraced unrestricted military use. The key insight is that employee activism is widespread, but corporate alignment with those concerns is rare — and when it occurs, it is punished. [Claims C044-C046, C054-C057]

The policy signal is damaging: the only safe options are full compliance or total withdrawal. This binary dynamic discourages nuanced, responsible engagement, and rewards companies that accept expansive “lawful purposes” clauses without enforceable boundaries. It also incentivizes secrecy, because if internal safeguards become a public liability, companies will be tempted to keep them opaque. [Claims C020-C023, C055, C057]

This is actively harmful for responsible AI development in defense. The defense sector depends on partnerships with companies that have strong safety cultures. When those companies are punished for insisting on clear boundaries, the incentives shift toward a race to the bottom on accountability.

### The "Mission Refusal Risk" Steelman — and Its Fatal Flaw

The strongest defense of the Pentagon's position is not that Anthropic was untrustworthy, but that it was *operationally unpredictable*. The argument runs: a vendor that might refuse to execute a lawful mission during a crisis is a genuine operational dependency risk, regardless of the quality of its technology. If the DoD defines "supply chain risk" broadly to include "ethical unreliability / mission refusal risk," then Anthropic's principled limits create exactly that risk — and the Pentagon's response, however heavy-handed, follows a defensible logic.

This framing explains the industry trend: Google removed its "Applications We Won't Build" page in February 2025; OpenAI removed the word "safely" from its mission statement in February 2026; xAI agreed to "any lawful purpose" with no stated limits. In each case, the shift reduces operational unpredictability from the Pentagon's perspective. Anthropic became the sole outlier in this pattern.

The steelman has real force. Militaries need reliable supply chains. If a contractor will only perform under conditions it finds acceptable, that is a dependency risk, and the relevant question is not whether the risk is real, but whether the response was proportionate.

However, the argument has a fatal internal contradiction: **a proportionate response to "operational unpredictability" is vendor diversification and backup contracts — not supply chain designation plus cloud infrastructure cutoff**. These are categorically different responses. Designation-plus-secondary-boycott is existentially punitive; operational hedging is procurement management. The government had already lined up OpenAI as a backup. A reliability-based response would have been: sign OpenAI, continue Anthropic for classified use where they were already deployed and trusted, and note the disagreement on commercial bulk data. Instead, the government chose the most extreme legal tool available.

This reveals that the "mission refusal risk" framing is post-hoc rationalization, not the actual driver. The operational goal — having a reliable classified AI vendor — was achievable through OpenAI. The designation's purpose was not operational continuity; it was to eliminate the position that principled limits on government AI use are commercially survivable. [Claims C001-C006, C033, C038, C044]

## The Democratic Legitimacy Problem

The government’s public justification for its actions rested on democratic legitimacy: companies, it argued, must defer to elected officials on lawful military decisions. However, the legal foundation for the supply chain risk designation is contested. Section 3252 was designed to address adversarial sabotage and supply chain vulnerabilities, not to punish a contractor for refusing specific contract terms. Legal analysts have argued that the designation likely exceeds the statute’s intended scope, and that procedural steps required by the statute were not followed. [Claims C019-C025]

A detailed legal analysis published on March 2, 2026, explicitly argued that § 3252 “is not a sanctions authority” and described the designation as political theater likely to fail in court. This undermines the claim that the government was merely executing statutory mandates, and suggests that the process served political objectives rather than carefully constrained legal ones. [Claims C034-C036]

The timeline further complicates claims of legitimacy. The President’s social media post announcing a government-wide ban appeared before the contractual deadline, and reporting indicates the post had been prepared in advance. The dispute was also colored by personal animus between senior officials and company leadership. When decisive action precedes process and personal rivalries shape outcomes, the claim of democratic legitimacy loses credibility. [Claims C029-C032]

Bipartisan congressional objections were also ignored. The Senate Armed Services Committee reportedly sent a private letter before the February 27 deadline urging an extension, but the Pentagon proceeded anyway. [Claims C041] Senator Thom Tillis (R-NC) dismissed the dispute as “sophomoric” and argued that Congress must weigh in on mass surveillance. [Claims C039] Senator Mark Kelly (D-AZ) stated: “That’s unconstitutional. That’s not the role of the Department of Defense.” [Claims C040] Expert commentary from the Brennan Center confirmed Anthropic's restrictions reflect constitutional and international law obligations, and questioned whether less intrusive measures were pursued. [Claims C054, C060] The key implication is that the Pentagon advanced despite objections from both Congress and the intelligence community, further eroding any claim to democratic legitimacy. [Claims C033-C041]

The core principle is straightforward: you cannot invoke democratic legitimacy while exceeding what Congress authorized. A framework that depends on lawful authority must be grounded in lawful authority, not merely asserted.

### The Legal Overreach: A Deeper Look

The legal maneuvering matters because the government invoked two different statutory regimes and chose the one that avoided due process. Hegseth selected 10 U.S.C. § 3252 instead of FASCSA (41 U.S.C. §§ 1321-1328) precisely because § 3252 provides no notice, no opportunity to respond, and bars judicial review, while FASCSA requires a 30-day notice period and review in the D.C. Circuit. This was not a technicality; it was a deliberate procedural evasion of basic protections that Congress put in place for supply-chain risk designations. [Claims C019-C025]

The scope of the “government-wide ban” also lacks any statutory basis. Section 3252 is a Defense Department procurement statute; it does not extend to civilian agencies like Treasury. Those agencies are canceling contracts based on a presidential social media post, not a lawfully supported order. The “secondary boycott” component — barring contractors from doing “any business” with Anthropic — would effectively cut off Amazon and Google’s cloud compute relationships with Anthropic. When Congress wanted that kind of power over Huawei, it enacted an explicit statute (Section 889 of the NDAA). No comparable statute exists here. [Claims C019-C034]

Judicial precedent further weakens the government’s case. In Luokung Technology v. DoD (2021) and Xiaomi Corp. v. DoD, courts granted preliminary injunctions against similar DoD designations as arbitrary and capricious. Those cases involved foreign companies; Anthropic’s position is stronger because it is a U.S. company with a documented national security track record: first frontier AI deployed on classified networks, termination of CCP-linked firms at the cost of hundreds of millions in revenue, and shutdown of a CCP-sponsored cyberattack. [Claims C010-C026]

Finally, the government’s own public messaging may be legally dispositive. Hegseth’s public accusations of “arrogance and betrayal,” “duplicity,” “corporate virtue-signaling,” and “defective altruism,” combined with President Trump labeling Anthropic a “RADICAL LEFT, WOKE COMPANY,” undercut two key defenses: the judicial review bar (it is hard to claim national-security secrecy while broadcasting the rationale) and the claim that this was neutral procurement discretion. The record instead suggests viewpoint-based punishment, raising First Amendment concerns and reframing the action as retaliation rather than lawful contracting. [Claims C029-C034]

## Principles for AI Company Leadership

The following principles are designed to be actionable guidance for AI company leadership. They are intended to be adopted before entering government negotiations and to shape how companies structure their contracts and public commitments.

1. Establish red lines before negotiation begins, not during. Publicly stated principles should be grounded in board-approved policy, not formed under pressure at the negotiating table. Pre-commitment protects leadership from ad hoc concessions and makes the company’s position predictable and credible. [Claims C001-C005]
2. Require contractual precision, not policy promises. Technical safeguards are important operationally, but only contracts create durable accountability. Companies should refuse “lawful purposes” clauses that are not paired with explicit, enforceable use restrictions. [Claims C020]
3. Treat the public/private data distinction as insufficient for AI. AI systems can synthesize public data into invasive profiles. Contracts must define prohibited data categories based on functional risk, not just statutory privacy labels. [Claims C007, C015, C038, C054]
4. Autonomous weapons require “meaningful human control” with defined thresholds. Vague phrases like “appropriate levels of human judgment” are not sufficient. Contracts should specify human review requirements by decision type. [Claims C017]
5. Insist on clear legal authority. If threats are made under statutory authorities, companies should verify the scope and procedural requirements of those authorities. This is not defiance; it is governance diligence. [Claims C019-C025]
6. Invest in coordination value. Industry-wide standards reduce the risk that any single company bears all negotiating costs. Collective norms also prevent a race to the bottom on accountability. [Claims C008-C023]
7. Document everything. If a dispute turns legal or political, the record matters. Meeting logs, written offers, and internal decision memos become essential evidence in court and in public debates. [Claims C029-C033]
8. Do not conflate engagement with compliance. Companies can support national security missions while maintaining specific contractual red lines. The ability to say “yes, but with limits” is central to responsible participation. [Claims C001-C015]

## Principles for Policymakers

Policymakers have their own obligations to prevent this dynamic from recurring. The following principles are aimed at legislative and executive decision-makers, and are designed to balance national security needs with democratic accountability.

1. Use appropriate statutory authorities. Section 3252 is not a sanctions authority; misuse undermines future legitimate use. Misapplication also increases litigation risk and erodes trust in national security processes. [Claims C019-C034]
2. Establish clear use-of-force doctrine for AI before contracting. DoD Directive 3000.09 is deliberately vague; this invites disputes that could have been avoided by clearer standards. [Claims C017]
3. Do not punish principled engagement. The Google-Microsoft-Anthropic comparison shows perverse incentives; companies should be rewarded, not penalized, for agreeing to work with limits. [Claims C001-C008]
4. Extend protections to all companies. OpenAI itself urged the Pentagon to offer the same terms to all AI companies. Equal terms reduce politicization and encourage competition on safety and quality rather than political alignment. [Claims C023]
5. Require congressional oversight. Senator Mark Warner’s concerns about whether decisions were driven by careful analysis or political considerations deserve formal inquiry, and the Armed Services Committee’s pre-deadline letter shows that oversight attempts were already made and ignored. Oversight protects both national security and democratic legitimacy. [Claims C021-C041]
6. Close the data broker loophole legislatively. The "Fourth Amendment Is Not For Sale Act" enjoys bipartisan support precisely because the current legal gap is incoherent: courts require warrants for government-compelled disclosure but allow warrant-free purchase of the same data from commercial brokers. Until this is resolved, AI companies will continue to face the binary choice between contractual refusals and enabling mass surveillance. Legislative action removes this pressure from individual contracting decisions. [Claims C038, C053]
7. Align domestic and international positions. The United States opposes binding restrictions on lethal autonomous weapons internationally while punishing domestic companies for similar restrictions, which is incoherent and strategically costly. [Claims C011-C013]
8. Establish transparency requirements. AI use in defense should require regular public reporting on categories of use, not operational details, to enable democratic oversight without compromising security. [Claims C017-C021]

## The Contractual Safeguards Framework

The following model provisions illustrate how contracts can operationalize accountability. They are not exhaustive, but they capture the key governance functions that technical safeguards cannot substitute for.

**A. Autonomous weapons: specific human review requirements by decision type.**
Contract language should define the specific decision types that require human approval, such as target selection, engagement authorization, and post-engagement assessment. The contract should define minimum review time, seniority requirements, and documentation standards for overrides. This aligns operational realities with the principle of meaningful human control. [Claims C017]

**B. Mass surveillance: explicit definitions of prohibited data categories.**
Contracts should prohibit the use of AI systems on categories of data that enable population-scale profiling, including public commercial datasets when aggregated into individual-level dossiers. “Public” should not be treated as a blanket exemption. The prohibition should be defined by functional impact, not merely by data source. [Claims C007, C015, C038]

**C. Audit and enforcement: third-party verification mechanisms.**
Contracts should require independent audits, including technical verification of use-case boundaries and periodic compliance reports. The auditing entity should be authorized to review system logs and usage requests under appropriate security protocols. [Claims C020-C025]

**D. Change control: contractual amendments require mutual consent.**
Contracts should prohibit unilateral modification of use-case boundaries. Any expansion of permitted uses should require a written amendment, with a defined review period and documented rationale. This prevents quiet erosion of safeguards over time. [Claims C002-C020]

**E. Sunset provisions: use-case restrictions reviewed and confirmed with renewals.**
Use-case restrictions should expire unless explicitly renewed, forcing periodic re-justification of sensitive uses. Sunset mechanisms encourage deliberate review rather than passive continuation and provide structured opportunities for oversight bodies to weigh in. [Claims C017-C021]

## Lessons Learned

Several lessons from the 2026 dispute should inform future contracts and policy decisions. First, the intelligence community reportedly urged both sides to reach a deal, indicating that the designation was politically driven rather than operationally necessary. This gap between operational need and political action creates governance risk and undermines the credibility of national security decision-making. [Claims C033-C034]

Second, the reputational and legal damage suffered by Anthropic was disproportionate to the contract’s economic value. A $200 million contract represented a small fraction of company revenue but triggered enormous downstream risk. This shows that legal and political consequences can dwarf contractual economics, and thus must be treated as central risks during negotiation. [Claims C001-C037]

Third, business damage occurs faster than courts can resolve. Even if a company ultimately prevails in litigation, the designation itself functions as a deterrent for future customers and partners. This reality makes preventive contractual protections more valuable than post hoc legal victories. [Claims C036-C037]

Finally, employee solidarity across companies demonstrates industry-wide resonance. The dispute was not confined to one company or one contract; it reflected a broader conflict between safety culture and political pressure. Policymakers and corporate leaders should recognize that workforce legitimacy is a strategic asset, not a peripheral concern. [Claims C008-C024]

The chilling effect on the broader industry is documented, not speculative. Multiple AI startups with government contracts are quietly reassessing their own red lines. Technical experts confirm that AI guardrails are fundamental to training architecture, not superficial additions that can be switched off on demand. A former senior defense official described the designation as 'beyond punitive' and warned of unintended consequences for DoD-dependent systems. These expert reactions collectively validate Anthropic's concerns while illustrating the deterrent effect of using designation as a political tool. [Claims C054-C057, C060]

An additional lesson concerns allied interoperability. A UK think tank (BISI) warned that an “all lawful purposes” baseline will conflict with European and Commonwealth frameworks, complicating NATO interoperability. [Claims C042] The Council on Foreign Relations similarly noted that the United States and China are isolated from allied consensus on responsible military AI norms. [Claims C043] Domestic contracting decisions therefore have international ripple effects that can undermine alliance cohesion. [Claims C042-C043]

The European Parliament has explicitly called for prohibition of lethal autonomous weapons, and the UN Secretary-General set a 2026 deadline for a binding LAWS instrument — meaning Anthropic's contractual red lines align with the global governance consensus that the US is now isolated from. [Claims C058, C059]

## Conclusion

The Anthropic-Pentagon dispute is a teachable moment. As AI becomes more deeply embedded in government operations, the absence of clear contractual frameworks creates instability, erodes trust, and incentivizes irresponsible engagement. A principled, transparent approach to contracting is now essential for both the legitimacy of government use and the long-term viability of AI companies operating in this domain. [Claims C001-C006]

The goal of this framework is not to prevent AI companies from working with government. It is to ensure that engagement is structured to preserve accountability, maintain democratic legitimacy, and align with the public interest. Contracts are the only near-term mechanism that can achieve this at scale while law and regulation catch up to technological reality. [Claims C007, C015, C017, C019-C020, C038]

Contractual safeguards are not corporate arrogance. They are the minimum viable accountability mechanism when the political environment is volatile and the legal environment is unsettled. AI companies and policymakers should treat them as a shared responsibility, not a unilateral constraint. The time to build these frameworks is before the next crisis, not after it.
