# Phase 2: Database Schema & LangGraph Foundations

This phase implements the data layer and core multi-agent state engine for the **AI Software Development Team** platform. We will set up Prisma ORM in NestJS to manage PostgreSQL relational tables, define the Python `TeamState` state machine for LangGraph, and build the service endpoints to trigger and stream workflow runs.

## User Review Required

> [!IMPORTANT]
> - We will use **Prisma ORM** inside `apps/api` for typed PostgreSQL migrations and queries.
> - LangGraph will use a Redis or In-Memory checkpointer to persist state across human-in-the-loop approval interrupts.
> - The initial multi-agent graph will connect: `ProjectManagerNode -> BusinessAnalystNode -> TechLeadReviewerNode`.

---

## Proposed Changes

### Component 1: NestJS Database Layer & Prisma Setup (`apps/api`)

#### [NEW] [apps/api/prisma/schema.prisma](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/apps/api/prisma/schema.prisma)
Define relational database schemas:
*   `User`: Authentication and workspace ownership (`id`, `email`, `passwordHash`, `name`).
*   `Project`: Core project metadata (`id`, `userId`, `title`, `description`, `status`).
*   `AgentRun`: Execution logs (`id`, `projectId`, `agentRole`, `status`, `inputPrompt`, `outputPayload`, `executionTimeMs`).
*   `Artifact`: Generated outputs (`id`, `projectId`, `agentRunId`, `artifactType`, `content`, `versionNumber`).
*   `Approval`: Human-in-the-loop review state (`id`, `projectId`, `agentRunId`, `decision`, `userFeedback`).

#### [NEW] [apps/api/src/prisma/prisma.service.ts](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/apps/api/src/prisma/prisma.service.ts)
Global database access service extending `PrismaClient`.

---

### Component 2: Python LangGraph Engine & State (`apps/ai-service`)

#### [NEW] [apps/ai-service/app/schemas/state.py](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/apps/ai-service/app/schemas/state.py)
Define the `TeamState` TypedDict for graph node communication:
*   `project_id`: String UUID.
*   `user_idea`: Original input prompt from the user.
*   `scope`: PM Agent output (milestones, risks, scope).
*   `requirements`: BA Agent output (functional/non-functional specs).
*   `architecture`: Architect Agent output (tech stack, DB schema, API design).
*   `reviewer_feedback`: Reviewer Agent feedback string.
*   `approval_status`: PENDING / APPROVED / REJECTED.
*   `current_agent`: Currently active node.

#### [NEW] [apps/ai-service/app/graphs/team_graph.py](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/apps/ai-service/app/graphs/team_graph.py)
Define the LangGraph state machine:
*   Nodes: `project_manager_node`, `business_analyst_node`, `tech_lead_reviewer_node`.
*   Conditional Edges: Route back to planning nodes if the Tech Lead requests revisions.

#### [NEW] [apps/ai-service/app/api/workflow.py](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/apps/ai-service/app/api/workflow.py)
FastAPI router for workflow execution:
*   `POST /api/workflow/start`: Triggers graph execution.
*   `GET /api/workflow/{run_id}/state`: Fetches current graph checkpoint.

---

## Verification Plan

### Automated Checks
- Run Prisma schema validation: `npx prisma validate` inside `apps/api`.
- Test Python graph initialization and node transitions using `pytest`.
- Run NestJS build check: `npm run build` inside `apps/api`.

### Manual Verification
- Test triggering a workflow execution via FastAPI Swagger UI (`http://localhost:8000/docs`).
- Verify graph state persistence across node runs.
