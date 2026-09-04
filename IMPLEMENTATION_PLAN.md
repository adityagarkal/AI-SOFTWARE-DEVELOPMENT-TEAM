# Phase 1: Scaffolding and Environment Configuration

This phase establishes the foundational structure of the **AI Software Development Team** platform. We will set up a clean monorepo folder layout, configure local database services using Docker Compose, and initialize the front-end, backend-API, and AI service frameworks.

## User Review Required

> [!IMPORTANT]
> - We will run the front-end, backend, and AI service as separate services within a single repository (monorepo structure) using independent dependencies to prevent version conflicts.
> - We will use Docker Compose for managing local state databases (PostgreSQL, Redis, ChromaDB). Please ensure you have **Docker Desktop** installed and running on your Windows host machine.

---

## Proposed Changes

### Monorepo Structure

We will create the following layout:
* `apps/web/` - Next.js front-end
* `apps/api/` - NestJS backend gateway
* `apps/ai-service/` - FastAPI + LangGraph AI service
* Root configurations for version control and workspace management.

#### [NEW] [docker-compose.yml](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/docker-compose.yml)
Create a Docker Compose configuration mapping the standard service ports:
- PostgreSQL (Port `5432`)
- Redis (Port `6379`)
- ChromaDB (Port `8000` or hosted locally within FastAPI)

#### [NEW] [.gitignore](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/.gitignore)
Create a root gitignore file to exclude `node_modules`, `.env` files, build targets, Python virtual environments (`.venv`), and local docker database volume directories.

---

### Component 1: Front-end (Next.js)

#### [NEW] [apps/web/](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/apps/web)
Scaffold a modern Next.js project using `create-next-app` with:
- TypeScript, Tailwind CSS, ESLint, App Router, and a `src/` directory.

---

### Component 2: Backend (NestJS)

#### [NEW] [apps/api/](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/apps/api)
Scaffold a NestJS backend application using `@nestjs/cli` configured for:
- TypeScript and npm package manager.

---

### Component 3: AI Service (FastAPI)

#### [NEW] [apps/ai-service/](file:///d:/BE%20Major%20Project/AI-SOFTWARE-DEVELOPMENT-TEAM/apps/ai-service)
Initialize a Python FastAPI project with:
- A virtual environment (`.venv`).
- `requirements.txt` containing `fastapi`, `uvicorn`, `langgraph`, and Google Gemini dependencies.
- A basic `main.py` health endpoint.

---

## Verification Plan

### Automated Checks
- Verify node projects build successfully:
  - `npm run build` inside `apps/web`
  - `npm run build` inside `apps/api`
- Run linting check for frontend/backend.
- Validate FastAPI starts successfully using `uvicorn`.

### Manual Verification
- Test Docker Compose starts all database containers (`docker compose up -d`).
- Run a basic HTTP check on the FastAPI service endpoint: `http://localhost:8000/docs`.
- Test database connection configurations.
