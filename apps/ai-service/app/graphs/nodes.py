from typing import Dict, Any
from app.schemas.state import TeamState


def project_manager_node(state: TeamState) -> Dict[str, Any]:
    """
    Project Manager Agent Node:
    Analyzes the user idea and defines project scope, milestones, and initial task breakdown.
    """
    user_idea = state.get("user_idea", "")
    print(f"[PM Agent] Processing project idea: {user_idea}")
    
    mock_scope = {
        "title": "Project Scope Summary",
        "description": f"Scope breakdown for: {user_idea}",
        "milestones": [
            "M1: Infrastructure Setup",
            "M2: Core API & Database",
            "M3: Front-end Interface",
            "M4: Quality Assurance & Docs"
        ],
        "estimated_weeks": 4,
        "risks": ["Third-party API rate limits", "Database scaling"]
    }
    
    return {
        "scope": mock_scope,
        "current_agent": "Project Manager",
        "messages": [{"role": "assistant", "content": "Project Manager has defined project scope and milestones."}]
    }


def business_analyst_node(state: TeamState) -> Dict[str, Any]:
    """
    Business Analyst Agent Node:
    Transforms project scope into functional requirements, non-functional requirements, and user stories.
    """
    scope = state.get("scope", {})
    print(f"[BA Agent] Generating requirements based on scope: {scope.get('title')}")
    
    mock_requirements = {
        "functional_requirements": [
            "FR-1: User Registration & JWT Authentication",
            "FR-2: Project Creation Dashboard",
            "FR-3: Real-time Workflow Execution Monitor"
        ],
        "non_functional_requirements": [
            "NFR-1: Sub-second API latency for REST calls",
            "NFR-2: 99.9% uptime database availability"
        ],
        "user_stories": [
            "As a user, I want to enter a project idea so that AI agents generate engineering artifacts."
        ]
    }
    
    return {
        "requirements": mock_requirements,
        "current_agent": "Business Analyst",
        "messages": [{"role": "assistant", "content": "Business Analyst has generated functional requirements and user stories."}]
    }


def tech_lead_reviewer_node(state: TeamState) -> Dict[str, Any]:
    """
    Tech Lead / Reviewer Agent Node:
    Evaluates generated artifacts for quality, consistency, and completeness.
    """
    scope = state.get("scope")
    requirements = state.get("requirements")
    revision_count = state.get("revision_count", 0)
    
    print(f"[Reviewer Agent] Evaluating outputs (Revision #{revision_count})")
    
    if scope and requirements:
        approval_status = "APPROVED"
        feedback = "Tech Lead verified scope and requirements. All checks passed."
    else:
        approval_status = "REVISION_REQUESTED"
        feedback = "Missing required planning artifacts. Regeneration required."
        revision_count += 1
        
    return {
        "approval_status": approval_status,
        "reviewer_feedback": feedback,
        "revision_count": revision_count,
        "current_agent": "Tech Lead Reviewer",
        "messages": [{"role": "assistant", "content": f"Tech Lead Reviewer evaluation: {approval_status}"}]
    }
