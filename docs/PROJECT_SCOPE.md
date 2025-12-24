# Project Scope: Sunport AI — Business Agent (Logic Engine)

**Role:** AI Engineer / Backend Developer (Python/LLM focus)  
**Duration:** ~6-8 Weeks  
**Repository:** `sunport-agent-business` (Standalone Repo)

## 🔒 Isolation Protocol (Read First)

To maintain security and focus, this project is scoped as a standalone reasoning module.

**No Access Required:** You do not need access to the core production database, user graph, or payment systems.

**Mocking:** All external context (user data, company stage) will be provided via mock objects in the test suite.

**Deliverable:** You are building the "brain" and the prompt architecture. The integration into the main platform will be handled internally.

## 🎯 Objective

Build a **"Decision-Grade" Business Assistant**. The agent must go beyond generic advice to provide structured, tradeoff-aware, and persona-specific recommendations.

## 📅 Phase 1: Foundation (Weeks 1-4)

### Week 1: Structure & Reliability

**Goal:** Eliminate "fluff." Enforce strict JSON/Markdown structures.

**Tasks:**

- Refine `system.txt` to ban generic summaries.
- Implement Golden Prompts (8 happy paths, 2 edge cases).
- Test Gate: 90% of outputs must have explicit headers: "Plan," "Risks," "Next Actions."

### Week 2: Context Awareness

**Goal:** The answer changes based on who the user is (Mock Contexts).

**Tasks:**

- Implement logic to detect context: Stage (Idea vs. Scale), Model (B2B vs. B2C).
- Test Gate: A prompt about "Pricing Strategy" must yield totally different answers for a "Bootstrapped B2C App" vs. a "Series B SaaS."

### Week 3: Trade-off Modeling

**Goal:** The agent must explain why it chose a path and what was sacrificed.

**Tasks:**

- Force "Options & Comparison" sections for binary choices (e.g., Build vs. Buy).
- Test Gate: No "it depends" answers without providing distinct selectable options with pros/cons.

### Week 4: Continuity (Memory)

**Goal:** Multi-turn logic.

**Tasks:**

- Implement `retrieve()` patterns to reference previous turns (e.g., "As we discussed regarding your budget...").
- Test Gate: Agent does not repeat questions asked in Turn 1 during Turn 3.

## 📅 Phase 2: Advanced Reasoning (Weeks 5-7)

### Week 5: Persona-Aware Framing

**Goal:** Adapt tone and focus based on the stakeholder (Founder vs. PM vs. VC).

**Tasks:**

- Add `decision_maker` parameter.
- **Founder Mode:** Focus on speed, risk, and runway.
- **PM Mode:** Focus on scope, sequencing, and dependencies.
- Test Gate: Same prompt generated for two different personas passes stylistic diff review.

### Week 6: Adversarial Thinking (Red Teaming)

**Goal:** The agent must critique its own plan.

**Tasks:**

- Implement a "Pre-Mortem" step: "What kills this plan?"
- Create "Convince me not to do this" prompt variations.
- Test Gate: Agent successfully identifies at least 2 valid failure modes for every GTM strategy proposed.

### Week 7: Validation Logic

**Goal:** Move from strategy to execution/proof.

**Tasks:**

- Add "Validation Plan" subsection (Metrics, KPIs, Time-to-signal).
- Test Gate: Recommendations must include "How to validate this in 7 days."

## ✅ Final Definition of Done

- **Standalone Repo:** A clean, pip-installable package.
- **Test Suite:** pytest suite with >50 "Golden Prompt" scenarios passing.
- **Documentation:** clear README.md on how to inject context variables.
- **No Hallucinations:** Strict adherence to provided context; agent admits when it doesn't know.

## Non-Goals

- ❌ No UI or frontend work
- ❌ No production database access
- ❌ No real API integrations
- ❌ No autonomous agent orchestration
- ❌ No memory persistence beyond provided interfaces



