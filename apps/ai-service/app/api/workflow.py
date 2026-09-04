from typing import Optional, Dict, Any
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.schemas.state import TeamState
from app.graphs.team_graph import team_graph

router = APIRouter()


class StartWorkflowRequest(BaseModel):
    project_id: str
    user_idea: str
    preferred_tech: Optional[str] = None


class WorkflowResponse(BaseModel):
    project_id: str
    status: str
    current_agent: str
    scope: Optional[Dict[str, Any]] = None
    requirements: Optional[Dict[str, Any]] = None
    reviewer_feedback: Optional[str] = None


@router.post("/start", response_model=WorkflowResponse, status_code=status.HTTP_200_OK)
def start_workflow(request: StartWorkflowRequest):
    """
    Triggers execution of the multi-agent graph workflow for a project idea.
    """
    try:
        initial_state: TeamState = {
            "project_id": request.project_id,
            "user_idea": request.user_idea,
            "preferred_tech": request.preferred_tech,
            "scope": None,
            "requirements": None,
            "architecture": None,
            "reviewer_feedback": None,
            "approval_status": "PENDING",
            "current_agent": "START",
            "revision_count": 0,
            "messages": [{"role": "user", "content": request.user_idea}]
        }
        
        # Invoke LangGraph state machine
        final_state = team_graph.invoke(initial_state)
        
        return WorkflowResponse(
            project_id=request.project_id,
            status=final_state.get("approval_status", "COMPLETED"),
            current_agent=final_state.get("current_agent", "Tech Lead Reviewer"),
            scope=final_state.get("scope"),
            requirements=final_state.get("requirements"),
            reviewer_feedback=final_state.get("reviewer_feedback")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Workflow execution failed: {str(e)}"
        )


@router.get("/{project_id}/status")
def get_workflow_status(project_id: str):
    """
    Returns runtime status for an active project workflow.
    """
    return {
        "project_id": project_id,
        "status": "operational",
        "graph_nodes": ["project_manager", "business_analyst", "tech_lead_reviewer"]
    }
