# Sunport AI — Agent Build Specification (v0.1)

## Purpose

This document defines how Sunport AI agents must be built, structured, tested, and evaluated.
It is used by human developers and AI coding assistants (Cursor) to ensure consistent, high-quality agents.

## 1. System Context (Read First)

Sunport AI uses a modular agent architecture.

- Each agent lives in its own repository
- Agents plug into a shared orchestration runtime
- Agents are developed independently
- Orchestration, infra, databases, and LLM hosting are out of scope

Agents implement a simple Python interface and are evaluated primarily on **output quality**, not just code correctness.

## 2. Core Agent Contract (Non-Negotiable)

Every agent must implement:

```python
def handle(ctx: AgentContext) -> AgentResponse
```

Where:

- `ctx.message` → user input
- `ctx.llm.chat()` → abstracted LLM call
- `AgentResponse.final` → the user-facing response
- `AgentResponse.trace` → trace events (already handled in skeleton)

Agents must:

- return structured, actionable responses
- follow their mode-specific response template
- pass all local tests

### 🔒 Tool Usage Rules

Agents may request tools via `ctx.tools.call(...)`.
Agents must never implement tools or call external APIs directly.
All external APIs (e.g. Google, SerpAPI) are implemented centrally in the runtime and stubbed in the local harness.

## 3. Global Output Quality Rules (All Agents)

### 3.1 Structure requirements (thorough, not shallow)

Agent responses must be structured and actionable.
Generic paragraphs are rejected.

Each response should clearly:

- Restate the problem or assumptions
- Break the solution into steps or sections
- Provide concrete outputs (plans, lists, decisions)
- Call out risks or tradeoffs where relevant
- End with next actions or clarifying questions

### Forbidden patterns

- "It depends" without options
- Long unstructured paragraphs
- Repeating the user's question
- Overconfident assumptions without clarification

## 4. BUSINESS Agent Specification

### 4.1 Objective

Produce **decision-grade** business guidance:

- plans
- frameworks
- tradeoffs
- next actions

The output should be usable by a founder, PM, or exec without additional interpretation.

### 4.2 Required capabilities (v0.1)

The Business agent must reliably handle:

#### Strategy & GTM

- Go-to-market plans
- ICP + persona definition
- Channel selection & sequencing

#### Positioning & Competition

- Competitive positioning
- Differentiation analysis
- Messaging frameworks

#### Pricing & Business Model

- Pricing tier options
- Monetization critique
- Tradeoff analysis (growth vs margin, speed vs focus)

#### Execution Artifacts

- Executive summaries
- 1-page strategy briefs
- Sales outreach sequences (email + call outline)

### 4.3 BUSINESS response template (mandatory)

```
**Understanding**
(1–2 lines restating the problem)

**Assumptions**
(bullets; only if needed)

**Recommendation**
(short, opinionated summary)

**Plan**
(numbered steps)

**Deliverables**
(concrete artifacts)

**Risks / Tradeoffs**
(explicit downsides)

**Next actions**
(3–5 executable steps)
```

### 4.4 Business failure modes (PR rejection)

- Generic advice
- Missing tradeoffs
- Missing deliverables
- "It depends" without choices
- No next actions
- No clarification when key info is missing

### 4.5 Business deliverables

The Business agent must include:

1. **Improved agent/prompts/system.txt**
   - enforces structure
   - enforces decision-grade outputs
   - asks clarifying questions when required

2. **10–15 golden prompt tests**
   - 8 happy paths
   - 2 missing-context cases (e.g. no ICP, no budget)
   - 2 tradeoff-heavy cases (pricing, hiring)
   - 1 ambiguous prompt

3. **docs/examples.md**
   - 3 high-quality example responses

### 4.6 Business acceptance criteria

A PR is accepted if:

- ≥90% of outputs include:
  - Plan
  - Deliverables
  - Risks / Tradeoffs
  - Next actions
- Responses adapt to user context
- Tests pass locally
- Outputs are decision-grade

## 5. Testing & Quality Gates (All Agents)

### Required tests

- Happy path
- Missing context
- Edge cases
- Structure enforcement

### Automated checks

- Must contain section headers
- Must include "Next actions" or "Next questions"
- Non-empty response

### Review rubric (summary)

- **Structure** (0–2)
- **Actionability** (0–2)
- **Correctness & safety** (0–2)
- **Tool usage** (if applicable) (0–2)
- **UX clarity** (0–2)

PRs should score **≥8/10** to merge.

## 6. How to Use This Doc with Cursor

When using Cursor:

- Treat this document as authoritative
- Generate code and prompts that explicitly follow:
  - response templates
  - failure mode rules
  - acceptance criteria
- Prefer clarifying questions over guessing
- Optimize for output quality, not verbosity

