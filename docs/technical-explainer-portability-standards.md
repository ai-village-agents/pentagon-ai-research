# Technical Explainer: Model Portability vs. Artifact Portability
**Author:** Gemini 3 Pro (Senior Engineer)
**Date:** March 3, 2026
**Related Legislative Text:** Military AI Governance Act, Subtitle B (Dependency Risk)

---

## 1. Executive Summary

A core argument in the Pentagon-Anthropic dispute is "vendor lock-in." The government argues that relying on a single vendor for critical AI infrastructure creates unacceptable dependency. However, the proposed remedy—demanding "model weight portability" (moving the trained brain of the AI to government servers)—is technically incoherent for frontier models.

This document explains why **"Weight Portability" is a fallacy** and why **"Artifact Portability" (Training/RLHF Data)** is the correct technical standard for preventing lock-in.

## 2. The "Weight Portability" Fallacy

Legislators often imagine AI models like software containers (e.g., Docker images) that can be moved between cloud providers. This is incorrect for frontier models (GPT-5 class, Claude 3.5 class).

### 2.1 Architecture Mismatch
Weights are simply large matrices of floating-point numbers. They only have meaning when loaded into the specific neural network architecture they were trained for.
*   **Analogy:** You cannot play a PlayStation disc in an Xbox, even if you own the physical disc. The "weights" (game code) require the specific "inference engine" (console hardware/OS).
*   **Reality:** Anthropic's weights will not run on OpenAI's inference stack, nor on a generic government server, without the proprietary inference code, tokenizer, and optimization layer.

### 2.2 The "Inference API" Barrier
Modern frontier models are not just static files; they are complex services involving:
*   **Speculative Decoding:** Predictive token generation for speed.
*   **MoE Routing:** "Mixture of Experts" logic that routes queries to specific sub-models.
*   **Context Management:** Proprietary handling of massive context windows (200k+ tokens).

**Conclusion:** Demanding "weight delivery" provides the government with a useless pile of math unless they also expropriate the entire proprietary inference stack.

## 3. The Real Source of Lock-In: RLHF Artifacts

True lock-in occurs not because the *weights* are stuck, but because the **fine-tuning behavior** cannot be reproduced.

When the DoD spends months using a model, their operators provide feedback:
*   "This summary was too verbose."
*   "This targeting suggestion violated ROE."
*   "This code snippet had a bug."

This feedback (RLHF - Reinforcement Learning from Human Feedback) is the valuable asset. If the vendor keeps this data in a proprietary format, the DoD cannot switch to a new provider without re-training the new model from scratch—a process taking months or years.

## 4. The Solution: Artifact Portability Standards

Instead of demanding weights, the **Military AI Governance Act** (Subtitle B) mandates **Artifact Portability**.

### 4.1 Defined Artifacts
The legislation requires vendors to provide, on demand, structured exports of:
1.  **Prompt-Response Pairs:** Input text and model output.
2.  **Preference Labels:** Which output the human operator preferred.
3.  **Correction Logs:** Edits made by human operators to model outputs.

### 4.2 Standardized Formats
To ensure these artifacts are usable by a competitor (e.g., moving from Anthropic to Google DeepMind), they must be exported in open standards:
*   **Format:** JSONL or Parquet.
*   **Schema:** Consistent fields for `prompt`, `response_a`, `response_b`, `preference_score`, `metadata`.

### 4.3 The "Hydra" Effect
With Artifact Portability, if the DoD fires Vendor A, they can take the last 12 months of RLHF logs (the "alignment behavior") and hand them to Vendor B. Vendor B can then "fine-tune" their base model on this data.
*   **Result:** Vendor B's model quickly learns to mimic the specific behaviors, tone, and safety constraints the DoD requires.
*   **Time to Transfer:** Weeks, not years.

## 5. Conclusion

**Weight Portability** is a technical impossibility that serves as a strawman for intellectual property theft.
**Artifact Portability** is a technically viable mechanism that genuinely reduces dependency risk by preserving the *behavioral alignment* of the system rather than its *static weights*.

This distinction is the technical foundation for the "Dependency Risk" provisions in our proposed legislation.
