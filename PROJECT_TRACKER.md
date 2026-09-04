# 📊 AI Software Development Team — Project Progress Tracker

Welcome to your **Project Development Control Center**! Use this interactive dashboard to track your progress, manage deadlines, and update task statuses as we build your final-year major project over the next 4–5 months.

---

## 📈 Overall Project Progress

```mermaid
gantt
    title Development Completion by Phase
    dateFormat X
    axisFormat %d
    
    section Completed
    Phase 1: Setup & Scaffolding   : active, 0, 15
    section Pending
    Phase 2: DB & Graph Core      : 15, 30
    Phase 3: Analytical Agents     : 30, 50
    Phase 4: Execution Agents      : 50, 70
    Phase 5: RAG Integration      : 70, 85
    Phase 6: Human-in-the-Loop     : 85, 95
    Phase 7: Evaluation & Thesis   : 95, 100
```

### Key Metrics
*   **Overall Progress:** `[█░░░░░░░░░] 10%`
*   **Total Tasks:** 60
*   **Completed Tasks:** 6
*   **Pending Tasks:** 54
*   **Current Milestone:** **M1 - Environment Setup & Service Scaffolding** (Target: End of Week 3)
*   **Next Milestone:** **M2 - Core LangGraph Flow & Database Persistence** (Target: End of Week 6)

---

## 🎯 Today's Focus & Upcoming Deadlines

### 📅 Today's Tasks
- [ ] Approve Phase 1 Implementation Plan.
- [ ] Initialize workspace directory structure and `.gitignore`.
- [ ] Create `docker-compose.yml` for Postgres, Redis, and ChromaDB.

### ⚠️ Critical Deadlines
*   **Milestone 1 (Infra Setup):** September 25, 2026 (In 21 Days)
*   **Milestone 2 (Sequential MVP):** October 16, 2026
*   **Milestone 3 (Full 9-Agent Loop):** November 6, 2026
*   **Milestone 4 (RAG & HITL):** December 25, 2026
*   **Milestone 5 (Final Deploy & Viva):** January 22, 2027

---

## 🗓️ Phase-by-Phase Task Checklist

### Phase 1: Setup & Scaffolding (Weeks 1–3)
**Target: September 25, 2026 | Progress: [████░░░░░░] 40%**

- [x] Define Project Architecture & Roadmap.
- [x] Verify Node.js, npm, and Python environmental dependencies.
- [ ] Create monorepo directory layout (`apps/web`, `apps/api`, `apps/ai-service`).
- [ ] Set up root `.gitignore` and global configurations.
- [ ] Setup `docker-compose.yml` (Postgres, Redis, ChromaDB).
- [ ] Initialize Next.js front-end in `apps/web`.
- [ ] Initialize NestJS backend in `apps/api`.
- [ ] Initialize FastAPI Python structure in `apps/ai-service`.
- [ ] Test container startup and database connections.
- [ ] Test service-to-service communication.

---

### Phase 2: Database Schema & LangGraph Foundations (Weeks 4–6)
**Target: October 16, 2026 | Progress: [░░░░░░░░░░] 0%**

- [ ] Design PostgreSQL database models (Prisma/TypeORM schemas).
- [ ] Implement tables for `Projects`, `AgentRuns`, `Artifacts`, and `Approvals`.
- [ ] Define Python `TeamState` schema for LangGraph.
- [ ] Build first basic sequential Graph (`PM -> BA -> Reviewer`).
- [ ] Integrate Redis checkpointer for workflow state saving.
- [ ] Develop REST API endpoints to trigger LangGraph runs from NestJS.
- [ ] Set up WebSocket server in NestJS for real-time console log streaming.

---

### Phase 3: Analytical Planning Agents (Weeks 7–9)
**Target: November 6, 2026 | Progress: [░░░░░░░░░░] 0%**

- [ ] **Project Manager Agent (PMA)**
  - [ ] Implement system prompt & output schema.
  - [ ] Generate scope, milestones, risks, and task list.
- [ ] **Business Analyst Agent (BAA)**
  - [ ] Transform scope into user stories and functional specifications.
- [ ] **System Architect Agent**
  - [ ] Generate DB designs, technology recommendations, and API contracts.
- [ ] **Documentation Agent**
  - [ ] Create dynamic `README.md` and basic setup instructions.
- [ ] Test agent coordination and validation layers.

---

### Phase 4: Execution, QA & Reviewer Agents (Weeks 10–12)
**Target: November 27, 2026 | Progress: [░░░░░░░░░░] 0%**

- [ ] **UI/UX Agent**
  - [ ] Generate wireframe specifications and screen flow plans.
- [ ] **Developer Planning Agent**
  - [ ] Create detailed file architectures and code skeleton structures.
- [ ] **QA Agent**
  - [ ] Generate unit test suites, integration test templates, and review schemas.
- [ ] **Reviewer / Tech Lead Agent**
  - [ ] Run automated quality gate evaluations.
  - [ ] Implement LangGraph revision loop back to analytical nodes on feedback reject.

---

### Phase 5: RAG Knowledge Base Ingestion (Weeks 13–14)
**Target: December 11, 2026 | Progress: [░░░░░░░░░░] 0%**

- [ ] Create PDF & text parser endpoints in NestJS.
- [ ] Set up ChromaDB collections schema.
- [ ] Write vector embedding creation helper using Gemini Embeddings API.
- [ ] Write semantic search querying layer in Python.
- [ ] Integrate ChromaDB retrieval tool into LangGraph nodes.

---

### Phase 6: Human-in-the-Loop & Version Control (Weeks 15–16)
**Target: December 25, 2026 | Progress: [░░░░░░░░░░] 0%**

- [ ] Implement LangGraph `interrupts` at key review nodes.
- [ ] Build front-end forms for Approve / Regenerate / Reject actions.
- [ ] Build front-end version history comparison screen using code diffs.
- [ ] Implement GitHub OAuth & Octokit PR creation.

---

### Phase 7: Evaluation, Deploy & Thesis (Weeks 17–20)
**Target: January 22, 2027 | Progress: [░░░░░░░░░░] 0%**

- [ ] Deploy Next.js to Vercel, NestJS/FastAPI to Render/Railway.
- [ ] Setup production database instance (e.g., Neon Postgres).
- [ ] Build testing scripts to evaluate response times, token cost, and success rate.
- [ ] Complete major project thesis documentation.
- [ ] Prepare Viva voice answers and demo video recording.

---

## 💡 Productivity Features & How to Track

### 🧩 Weekly Goals Tracker
Keep your momentum high by picking 2-3 core tasks every Monday. Write them in the **Weekly Goals** section here to stay hyper-focused.
*   **This Week's Goal (Week 1):** Scaffolding the workspace folders, root config files, and docker-compose database files.

### ⏱️ Time Estimation Guide
When taking on a task:
1. Estimate it in hours (e.g., *2 hours to set up Prisma*).
2. If it takes longer than 2x your estimate, break it down into smaller sub-tasks.
3. Record actual durations in your weekly progress report to build accurate estimation skills.

### 🔔 Deadline Reminder Guide
*   **Weekly Check-in:** Set a calendar reminder every Friday at 5:00 PM to update the `PROJECT_TRACKER.md` progress percentages.
*   **Milestone Alerts:** Set reminders 3 days before any major Milestone target to run an end-to-end audit.
