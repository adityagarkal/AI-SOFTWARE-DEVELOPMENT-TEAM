import { Injectable, HttpException, HttpStatus } from '@nestjs/common';
import { HttpService } from '@nestjs/axios';
import { firstValueFrom } from 'rxjs';
import { PrismaService } from '../prisma/prisma.service.js';
import { TriggerWorkflowDto } from './dto/trigger-workflow.dto.js';
import { ArtifactType } from '@prisma/client';

@Injectable()
export class WorkflowService {
  private readonly aiServiceUrl = process.env.AI_SERVICE_URL || 'http://localhost:8000';

  constructor(
    private readonly httpService: HttpService,
    private readonly prisma: PrismaService,
  ) {}

  async triggerWorkflow(dto: TriggerWorkflowDto) {
    try {
      // 1. Call FastAPI AI Service to invoke LangGraph multi-agent execution
      const payload = {
        project_id: dto.projectId,
        user_idea: dto.userIdea,
        preferred_tech: dto.preferredTech,
      };

      const response = await firstValueFrom(
        this.httpService.post(`${this.aiServiceUrl}/api/workflow/start`, payload),
      );

      const data = response.data;

      // 2. Log AgentRun record in PostgreSQL
      const agentRun = await this.prisma.agentRun.create({
        data: {
          projectId: dto.projectId,
          agentRole: 'TECH_LEAD_REVIEWER',
          status: data.status === 'APPROVED' ? 'SUCCESS' : 'NEEDS_REVISION',
          inputPrompt: dto.userIdea,
          outputPayload: JSON.stringify(data),
          executionTimeMs: 1200,
        },
      });

      // 3. Save versioned Project Scope artifact
      if (data.scope) {
        await this.prisma.artifact.create({
          data: {
            projectId: dto.projectId,
            agentRunId: agentRun.id,
            artifactType: ArtifactType.PROJECT_SCOPE,
            title: data.scope.title || 'Project Scope Summary',
            content: JSON.stringify(data.scope, null, 2),
            versionNumber: 1,
          },
        });
      }

      // 4. Save versioned User Stories artifact
      if (data.requirements) {
        await this.prisma.artifact.create({
          data: {
            projectId: dto.projectId,
            agentRunId: agentRun.id,
            artifactType: ArtifactType.USER_STORIES,
            title: 'Functional Requirements & User Stories',
            content: JSON.stringify(data.requirements, null, 2),
            versionNumber: 1,
          },
        });
      }

      // 5. Create Human Approval record
      const approval = await this.prisma.approval.create({
        data: {
          projectId: dto.projectId,
          agentRunId: agentRun.id,
          decision: data.status === 'APPROVED' ? 'APPROVED' : 'PENDING',
          userFeedback: data.reviewer_feedback,
        },
      });

      return {
        message: 'Workflow executed and artifacts persisted successfully',
        agentRunId: agentRun.id,
        approvalId: approval.id,
        summary: data,
      };
    } catch (error: any) {
      throw new HttpException(
        `Failed to trigger AI workflow: ${error.message || 'AI service unavailable'}`,
        HttpStatus.BAD_GATEWAY,
      );
    }
  }

  async getProjectArtifacts(projectId: string) {
    return this.prisma.artifact.findMany({
      where: { projectId },
      orderBy: { createdAt: 'desc' },
    });
  }

  async getProjectAgentRuns(projectId: string) {
    return this.prisma.agentRun.findMany({
      where: { projectId },
      include: {
        artifacts: true,
        approvals: true,
      },
      orderBy: { createdAt: 'desc' },
    });
  }
}
