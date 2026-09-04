# Task Checklist — Phase 2: Database Schema & LangGraph Foundations

- [x] **Step 1: NestJS Prisma ORM Setup & Database Schema Design (`apps/api`)** <!-- id: step-2-1 -->
  - [x] Install Prisma dependencies (`prisma`, `@prisma/client`) in `apps/api` <!-- id: 2.1.1 -->
  - [x] Create `apps/api/prisma/schema.prisma` with models (`User`, `Project`, `AgentRun`, `Artifact`, `Approval`) <!-- id: 2.1.2 -->
  - [x] Create `apps/api/src/prisma/prisma.service.ts` database access module <!-- id: 2.1.3 -->
  - [x] Verify Prisma schema validation and NestJS build <!-- id: 2.1.4 -->

- [x] **Step 2: Python LangGraph `TeamState` & Graph Foundations (`apps/ai-service`)** <!-- id: step-2-2 -->
  - [x] Create `apps/ai-service/app/schemas/state.py` defining `TeamState` TypedDict <!-- id: 2.2.1 -->
  - [x] Create `apps/ai-service/app/graphs/nodes.py` for agent node functions <!-- id: 2.2.2 -->
  - [x] Create `apps/ai-service/app/graphs/team_graph.py` assembling the LangGraph state graph <!-- id: 2.2.3 -->

- [ ] **Step 3: FastAPI Workflow Execution Endpoints (`apps/ai-service`)** <!-- id: step-2-3 -->
  - [ ] Create `apps/ai-service/app/api/workflow.py` with `POST /api/workflow/start` endpoint <!-- id: 2.3.1 -->
  - [ ] Mount workflow router in `apps/ai-service/main.py` <!-- id: 2.3.2 -->
  - [ ] Test workflow execution via FastAPI Swagger UI <!-- id: 2.3.3 -->

- [ ] **Step 4: NestJS Workflow Controller & Integration (`apps/api`)** <!-- id: step-2-4 -->
  - [ ] Create `apps/api/src/workflow/workflow.controller.ts` bridge to FastAPI <!-- id: 2.4.1 -->
  - [ ] Verify end-to-end integration and NestJS build <!-- id: 2.4.2 -->
