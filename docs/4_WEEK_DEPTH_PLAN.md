# Business Agent — 4-Week Depth Plan (v0.1 → v0.2)

The goal over 4 weeks is to move the Business agent from:

**"Good structured advice"** → **"Context-aware, scenario-driven, decision-assisting system"**

## Week 1 — Foundation & Quality Lock-In

### Focus

Make the agent consistently decision-grade.

### Work items

- Refine `system.txt` to strictly enforce:
  - structure
  - tradeoffs
  - next actions
- Implement the core golden prompts (10–15)
- Ensure clarifying-question behavior when context is missing
- Pass all structure tests

### Output

- Reliable baseline quality
- No shallow responses

### 📌 Gate to pass week 1

- ≥90% outputs pass rubric
- No missing sections
- No hallucinated assumptions

---

## Week 2 — Scenario Awareness & Business Context Modeling

### Focus

Teach the agent to adapt its recommendations based on business context, not just the question.

### Add a "Business Context Lens"

The agent should infer or ask about:

- Company stage (idea / early / growth)
- Business model (B2B / B2C / marketplace)
- Sales motion (self-serve / sales-led)
- Budget & team constraints

### New capabilities

- Same question → different answers based on context
- Explicitly call out why a recommendation changes

### Example

**Prompt:** "How should I do GTM?"

Agent must differentiate:

- solo founder vs funded startup
- B2B vs B2C
- enterprise vs SMB

### New deliverables

- `docs/context_dimensions.md` — how the agent reasons about stage, budget, ICP
- 5–7 new golden prompts testing context shifts

### 📌 Gate to pass week 2

- Outputs visibly change with context
- Agent asks smart clarifying questions when context is missing
- No "one-size-fits-all" answers

---

## Week 3 — Tradeoff Reasoning & Option Comparison

### Focus

Turn the agent into a decision assistant, not just a planner.

### New requirement: Explicit options

For major decisions, the agent must present:

- Option A
- Option B
- Sometimes Option C

With:

- pros
- cons
- when to choose each

### Scenarios to cover

- Pricing models
- Hiring vs outsourcing
- Build vs buy
- Sales-led vs product-led
- Speed vs quality

### Response upgrade

Add a **"Options & Comparison"** section when appropriate.

### New tests

- Tradeoff-heavy prompts (5–7)
- Ambiguous "what should I do?" prompts
- "Challenge my plan" prompts

### 📌 Gate to pass week 3

- At least one tradeoff section in most strategy answers
- Clear recommendations, not neutrality
- Agent explains why an option is preferred

---

## Week 4 — Memory, Continuity & Strategic Follow-Ups

### Focus

Make the agent feel like it remembers and builds, not resets every turn.

Even if memory is fake/stubbed, the logic must exist.

### New behaviors

- Reference prior assumptions (via `ctx.memory` / `retrieve()`)
- Avoid repeating earlier questions
- Build on previous plans instead of restarting

### Examples

**User:** "We decided on outbound last week — now what?"

**Agent:**
- References previous GTM choice
- Moves to next logical step
- Adjusts plan instead of restarting

### Deliverables

- 5–8 multi-turn golden scenarios
- Memory-aware reasoning (even if stubbed)
- Improved follow-up question quality

### 📌 Gate to pass week 4

- Agent shows continuity
- No repetitive advice
- Strong follow-up sequencing

---

## Stretch Goals (Optional, Still Valuable)

If they're strong and finish early:

### A) Lightweight evaluation hooks

Add internal "self-check" step:

- "Did I include tradeoffs?"
- "Did I include next actions?"

### B) Business artifact generation

Turn plans into:

- tables
- bullet matrices
- simple frameworks

### C) Red-team prompts

- "Convince me not to do this"
- "What's the biggest mistake founders make here?"

---

## How to Scope This Cleanly in Contracts

### Suggested milestones (aligned to weeks)

- **Milestone 1 (Week 1):** Core quality + structure
- **Milestone 2 (Week 2):** Context-aware reasoning
- **Milestone 3 (Week 3):** Tradeoff & option modeling
- **Milestone 4 (Week 4):** Continuity & memory-aware behavior

Each milestone requires:

- passing tests
- reviewed example outputs
- rubric score ≥ threshold



