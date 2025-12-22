    # sunport-agent-business

    Agent mode: **BUSINESS**

    This repository contains a single Sunport AI agent module for the **BUSINESS** domain.
    It is developed and tested locally using the shared harness from `sunport-orchestrator-core`.

    ## Quickstart

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -U pip
    pip install -e ".[dev]"
    ```

    Run the agent locally (FakeLLM + fake tools + in-memory memory):

    ```bash
    python -m agent.cli "Hello"
    ```

    Run tests:

    ```bash
    pytest
    ```

    ## Output quality requirements

    Agent responses must be **structured and actionable** (not generic paragraphs).

    Each response should:
    - Restate the problem / assumptions
    - Break the solution into steps/sections
    - Provide concrete outputs (plans, lists, decisions)
    - Call out risks or tradeoffs where relevant
    - End with next actions or clarifying questions

    ## Response template for BUSINESS

    **Understanding**
(1–2 lines)

**Assumptions**
(bullets; only if needed)

**Recommendation**
(short summary)

**Plan**
(numbered steps)

**Deliverables**
(bullets)

**Risks / Tradeoffs**
(bullets)

**Next actions**
(3–5 bullets)


    ## Shared contract

    See the shared contract in `sunport-orchestrator-core/docs/AGENT_CONTRACT_1PAGER.md`.
