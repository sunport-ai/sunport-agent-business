from __future__ import annotations

import sys
from orchestrator_core.harness.runner import run_agent_once
from agent.agent import Agent


def main() -> int:
    msg = " ".join(sys.argv[1:]).strip() if len(sys.argv) > 1 else "Hello"
    agent = Agent()
    resp = run_agent_once(agent, mode=agent.mode, user_message=msg)
    print(resp.final)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
