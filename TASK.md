# Task Checklist — Phase 1: Scaffolding & Environment Configuration

- [x] **Step 1: Monorepo Folder Layout & Root Configuration** <!-- id: step-1 -->
  - [x] Create folder structure: `apps/web`, `apps/api`, `apps/ai-service` <!-- id: 1.1 -->
  - [x] Create root `.gitignore` file <!-- id: 1.2 -->
- [x] **Step 2: Docker Infrastructure Setup** <!-- id: step-2 -->
  - [x] Create `docker-compose.yml` (PostgreSQL, Redis, ChromaDB) <!-- id: 2.1 -->
  - [x] Test local container configuration <!-- id: 2.2 -->
- [ ] **Step 3: Next.js Front-end Setup (`apps/web`)** <!-- id: step-3 -->
  - [ ] Run non-interactive `create-next-app` in `apps/web` <!-- id: 3.1 -->
  - [ ] Verify `npm run build` succeeds <!-- id: 3.2 -->
- [ ] **Step 4: NestJS Backend Setup (`apps/api`)** <!-- id: step-4 -->
  - [ ] Run non-interactive `@nestjs/cli new` in `apps/api` <!-- id: 4.1 -->
  - [ ] Verify `npm run build` succeeds <!-- id: 4.2 -->
- [ ] **Step 5: FastAPI AI Service Setup (`apps/ai-service`)** <!-- id: step-5 -->
  - [ ] Initialize Python structure, `requirements.txt`, and `main.py` <!-- id: 5.1 -->
  - [ ] Verify FastAPI health endpoint runs cleanly <!-- id: 5.2 -->
