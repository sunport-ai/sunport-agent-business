# Sunport AI — Business Agent (v0.1)

## Objective

Build a BUSINESS AI agent that provides **decision-grade business guidance**, not generic advice.

The agent must consistently produce:

- structured outputs
- explicit tradeoffs
- concrete deliverables
- clear next actions

This agent plugs into an existing orchestration system via a shared Python interface.

## Scope of work

You will work **only** in this repository:

- `sunport-agent-business`

You will **not**:

- touch orchestration
- touch infrastructure
- access production systems
- access databases or credentials

All work is done locally using a provided harness.

## Required capabilities (v0.1)

The agent must reliably handle:

### Strategy & Planning

- Go-to-market plans (B2B / SaaS)
- ICP + persona definition
- Channel selection & sequencing

### Positioning & Competition

- Competitive positioning
- Differentiation analysis
- Messaging frameworks

### Pricing & Business Models

- Pricing tier options
- Tradeoff analysis
- Monetization critique

### Execution Artifacts

- Executive summaries
- 1-page strategy briefs
- Sales outreach sequences (email + call outline)

## Response quality requirements (non-negotiable)

Every response must be:

- **Structured** (clear sections)
- **Actionable** (specific steps)
- **Decision-oriented** (recommendations + tradeoffs)

### Mandatory sections (most responses):

- **Plan** (numbered)
- **Deliverables**
- **Risks / Tradeoffs**
- **Next actions**

### Forbidden:

- Generic advice
- "It depends" without options
- Long unstructured paragraphs
- Overconfident assumptions without clarification

## Deliverables

You are expected to submit:

1. **Improved agent/prompts/system.txt**
   - enforces tone
   - enforces structure
   - asks clarifying questions when needed

2. **10–15 golden prompt tests**
   - 8 happy paths
   - 2 missing-context cases
   - 2 tradeoff-heavy cases
   - 1 ambiguous prompt

3. **docs/examples.md**
   - 3 high-quality example outputs
   - demonstrates decision-grade responses

## Acceptance criteria

A PR is accepted if:

- ≥90% of test outputs include:
  - Plan
  - Deliverables
  - Risks / Tradeoffs
  - Next actions
- Responses adapt to user context
- No generic or filler content
- All tests pass locally

## How you will be evaluated

We review PRs using:

- automated tests
- a quality rubric
- manual review of example outputs

## Timeline

Expected effort: **1–2 weeks**, depending on experience.

