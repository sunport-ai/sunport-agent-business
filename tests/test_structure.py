from orchestrator_core.harness.runner import run_agent_once
from agent.agent import Agent


def _has_any_heading(text: str) -> bool:
    # simple heuristic: bold headings or markdown headings
    lower = text.lower()
    return ("**plan**" in lower) or ("# " in text) or ("## " in text)


def test_agent_output_is_structured():
    agent = Agent()
    prompt = "Create a helpful response with clear sections and next steps."
    resp = run_agent_once(agent, mode=agent.mode, user_message=prompt)
    assert resp.final.strip()
    assert _has_any_heading(resp.final), "Expected headings/sections (structured output)"
    assert "next" in resp.final.lower(), "Expected a Next actions / Next questions section"
