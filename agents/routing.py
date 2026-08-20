from langgraph.graph import END

from agents.State import AgentState


def should_continue(state: AgentState):
    lastmessage = state["messages"][-1]

    if lastmessage.tool_calls:  # type: ignore
        return "tasktool"

    return "end"  # if no toolcall is there
