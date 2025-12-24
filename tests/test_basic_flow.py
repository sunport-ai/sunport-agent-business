from orchestrator_core.harness.runner import run_agent_once
from agent.agent import Agent


def test_agent_returns_non_empty_response():
    agent = Agent()
    resp = run_agent_once(agent, mode=agent.mode, user_message="Test message")
    assert resp.final.strip()
    assert resp.mode == "BUSINESS"


