from __future__ import annotations

from orchestrator_core.contracts import AgentContext, AgentResponse
from orchestrator_core.contracts.models import Message


class Agent:
    """Sunport AI agent for mode: BUSINESS."""
    mode = "BUSINESS"

    def handle(self, ctx: AgentContext) -> AgentResponse:
        # Trace start
        ctx.add_event("agent.start", mode=self.mode)

        system = (ctx.read_file("agent/prompts/system.txt")
                  if hasattr(ctx, "read_file") else None)
        if not system:
            # Fallback if ctx doesn't have read_file()
            with open("agent/prompts/system.txt", "r", encoding="utf-8") as f:
                system = f.read()

        style = ""
        try:
            with open("agent/prompts/style.txt", "r", encoding="utf-8") as f:
                style = f.read()
        except Exception:
            style = ""

        # Basic pattern: LLM-only in v0.1.0 (tools can be added as needed)
        messages = [
            Message(role="system", content=system + "\n\n" + style),
            Message(role="user", content=ctx.message),
        ]

        ctx.add_event("llm.call", mode=self.mode)
        reply = ctx.llm.chat([m.model_dump() for m in messages])
        ctx.add_event("llm.result", mode=self.mode, chars=len(reply or ""))

        # Trace end
        ctx.add_event("agent.end", mode=self.mode)

        return AgentResponse(mode=self.mode, final=reply or "", trace=ctx.trace)
