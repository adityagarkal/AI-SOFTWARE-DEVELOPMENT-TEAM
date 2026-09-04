from langgraph.graph import StateGraph, START, END
from app.schemas.state import TeamState
from app.graphs.nodes import (
    project_manager_node,
    business_analyst_node,
    tech_lead_reviewer_node
)


def should_continue_or_revise(state: TeamState) -> str:
    """
    Conditional routing function evaluating Tech Lead feedback.
    """
    approval_status = state.get("approval_status", "PENDING")
    revision_count = state.get("revision_count", 0)
    
    if approval_status == "REVISION_REQUESTED" and revision_count < 3:
        print("[Graph Router] Routing back to Project Manager for revision.")
        return "project_manager"
    
    print("[Graph Router] Workflow execution completed successfully.")
    return END


def create_team_graph():
    """
    Constructs and compiles the multi-agent StateGraph.
    """
    workflow = StateGraph(TeamState)
    
    # Add agent nodes
    workflow.add_node("project_manager", project_manager_node)
    workflow.add_node("business_analyst", business_analyst_node)
    workflow.add_node("tech_lead_reviewer", tech_lead_reviewer_node)
    
    # Define linear graph edges
    workflow.add_edge(START, "project_manager")
    workflow.add_edge("project_manager", "business_analyst")
    workflow.add_edge("business_analyst", "tech_lead_reviewer")
    
    # Add conditional router edge from Tech Lead Reviewer
    workflow.add_conditional_edges(
        "tech_lead_reviewer",
        should_continue_or_revise,
        {
            "project_manager": "project_manager",
            END: END
        }
    )
    
    return workflow.compile()


# Export compiled graph instance
team_graph = create_team_graph()
