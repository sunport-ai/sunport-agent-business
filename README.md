# Sunport Agent: BUSINESS

Business strategy and planning agent for Sunport AI orchestrator.

## Agent Contract

See the [orchestrator-core agent contract](https://github.com/sunport-ai/shared_orchestrator/blob/main/docs/AGENT_CONTRACT_1PAGER.md) for the interface specification.

## Response Template

This agent follows the **BUSINESS** response template:

- **Understanding** (1–2 lines)
- **Assumptions** (bullets; only if needed)
- **Recommendation** (short summary)
- **Plan** (steps, numbered)
- **Deliverables** (bullets)
- **Risks / Tradeoffs** (bullets)
- **Next actions** (3–5 bullets)

See [response templates](https://github.com/sunport-ai/shared_orchestrator/blob/main/docs/RESPONSE_TEMPLATES.md) for details.

## BUSINESS Agent — Deep Scope v0.1

### 1. What "decision-grade" actually means (non-negotiable)

A Business agent response is **decision-grade** if:

- A founder / PM / exec could take action without asking "so what?"
- The output makes choices visible, not just possibilities
- Tradeoffs are explicit (time, cost, risk, complexity)
- Next actions are doable within 1–7 days

#### ❌ Not decision-grade:

> "You should consider your target market and refine your positioning."

#### ✅ Decision-grade:

> "Given a <$50k budget and no outbound team, prioritize content-led inbound for 60 days; outbound is higher ROI only if you can hire SDRs."

**This is the bar.**

### 2. Required response anatomy (internal structure)

Every Business response should implicitly follow this flow, even if sections are combined:

#### 1️⃣ Understanding

- Restates the problem in the agent's own words
- Signals what decision is being made

**Example:**
> "You're deciding how to launch a B2B SaaS with a small team and limited budget."

#### 2️⃣ Assumptions (conditional)

Only included if missing info materially affects the answer.

- Budget
- ICP size
- Sales motion (self-serve vs sales-led)
- Timeline

**Rule:**
- If assumptions are made → they must be listed
- If assumptions are critical → ask questions instead of proceeding

#### 3️⃣ Recommendation (single paragraph)

This is the answer, not the explanation.

- Clear direction
- Opinionated but justified

**Example:**
> "Start with a narrow ICP and one acquisition channel for 30 days before expanding."

#### 4️⃣ Plan (numbered, concrete)

This is where shallow agents fail.

**Requirements:**
- Numbered steps
- Each step answers "what do I do?"

**Example:**
1. Define ICP with 3 exclusion criteria
2. Write a 1-sentence positioning statement
3. Launch 2 channel experiments with clear success metrics

#### 5️⃣ Deliverables (tangible outputs)

These are artifacts, not actions.

**Examples:**
- ICP one-pager
- Pricing table
- Email sequence draft
- Competitive matrix

**If there are no deliverables → the response is too abstract.**

#### 6️⃣ Risks / Tradeoffs (mandatory)

This is where "business intelligence" shows.

**Requirements:**
- At least 1 tradeoff
- Explicit downside of the recommendation

**Examples:**
- Speed vs quality
- Cash burn vs growth
- Focus vs optionality

#### 7️⃣ Next actions (mandatory)

These must be:
- Short
- Executable
- Time-bounded

**Examples:**
- "Confirm your budget range"
- "Share top 3 competitors"
- "Decide whether sales-led or self-serve"

### 3. Capability map (what the agent must reliably handle)

#### Category 1: Strategy & GTM

- GTM plan (B2B / B2C)
- ICP definition + personas
- Channel selection
- Launch sequencing

**Golden prompt examples:**
- "Create a GTM plan for a dev-tool SaaS targeting startups"
- "Help me define my ICP for an HR analytics product"

#### Category 2: Positioning & Competition

- Competitive analysis
- Differentiation
- Messaging hierarchy

**Golden prompt examples:**
- "How should we position vs Salesforce?"
- "What's a strong value prop for this product?"

#### Category 3: Pricing & Business Model

- Pricing tiers
- Tradeoff analysis
- Monetization critique

**Golden prompt examples:**
- "Help me price a B2B API product"
- "Is freemium or free trial better here?"

#### Category 4: Execution Artifacts

- Exec summaries
- 1-pagers
- Outreach sequences

**Golden prompt examples:**
- "Write a 1-page strategy brief"
- "Create a cold email + call outline"

### 4. Explicit failure modes to guard against

**Common reasons PRs are rejected:**

- ❌ Generic advice ("it depends" without options)
- ❌ Long paragraphs without sections
- ❌ No risks / tradeoffs
- ❌ No deliverables
- ❌ Overconfident assumptions without asking
- ❌ Repeating the user's question without adding insight

This sets expectations early.

### 5. Golden prompts → tests mapping

#### Required test types (minimum)

| Test type | Purpose |
|-----------|---------|
| Happy path | Can the agent deliver a full plan |
| Missing info | Does it ask clarifying questions |
| Tradeoff heavy | Does it reason, not just list |
| Short prompt | Does it infer intent properly |

#### Example test grouping (Business)

- 8 happy paths
- 2 missing-context cases
- 2 tradeoff-heavy cases
- 1 "ambiguous question" case

Each test should assert:
- Presence of sections
- Presence of "Risks" and "Next actions"
- Non-empty deliverables list

### 6. Acceptance criteria → how you evaluate PRs

When reviewing PRs, you should be able to answer **yes** to:

- Could I hand this response to a founder without editing?
- Does it force decisions instead of avoiding them?
- Are tradeoffs explicit?
- Are next actions concrete?

**If not → request changes.**

## Definition of Done

- ✅ Agent implements `handle(ctx: AgentContext) -> AgentResponse`
- ✅ Responses follow BUSINESS template structure
- ✅ Responses are decision-grade (see section 1)
- ✅ All required sections present (Understanding, Plan, Deliverables, Risks, Next actions)
- ✅ All tests pass (structure + basic flow + capability tests)
- ✅ PR review rubric score ≥8/10

## Development

### Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Run Harness

```bash
orchestrator-harness --mode BUSINESS "Create a GTM plan for a new product"
```

### Run Tests

```bash
pytest -v
```

## Contractor Resources

- **[Build Specification](docs/BUILD_SPECIFICATION.md)** — Complete authoritative specification (use with Cursor)
- **[Project Scope](docs/PROJECT_SCOPE.md)** — Finalized 7-week project scope with isolation protocol
- **[Contractor Task Brief](docs/CONTRACTOR_TASK_BRIEF.md)** — One-page task overview for contractors
- **[Milestone Structure](docs/MILESTONE_STRUCTURE.md)** — Upwork/Fiverr milestone breakdown (anti-shallow)

## Contributing

See [CONTRIBUTING.md](https://github.com/sunport-ai/shared_orchestrator/blob/main/CONTRIBUTING.md) for PR review rubric.

See [quality gates](https://github.com/sunport-ai/shared_orchestrator/blob/main/docs/QUALITY_GATES.md) for automated validation patterns.

## Brief note on COACH (contrast)

Coach follows the same structural rigor, but adds:

- Safety gating
- Non-diagnostic language
- Habit framing
- Always asks questions

**The key difference:**
- **Business** optimizes for decisions
- **Coach** optimizes for safe, sustainable action
