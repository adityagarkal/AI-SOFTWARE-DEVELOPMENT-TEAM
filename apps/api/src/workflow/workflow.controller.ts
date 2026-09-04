import { Controller, Post, Get, Body, Param } from '@nestjs/common';
import { WorkflowService } from './workflow.service.js';
import { TriggerWorkflowDto } from './dto/trigger-workflow.dto.js';

@Controller('workflow')
export class WorkflowController {
  constructor(private readonly workflowService: WorkflowService) {}

  @Post('trigger')
  async triggerWorkflow(@Body() dto: TriggerWorkflowDto) {
    return this.workflowService.triggerWorkflow(dto);
  }

  @Get('project/:projectId/artifacts')
  async getArtifacts(@Param('projectId') projectId: string) {
    return this.workflowService.getProjectArtifacts(projectId);
  }

  @Get('project/:projectId/runs')
  async getAgentRuns(@Param('projectId') projectId: string) {
    return this.workflowService.getProjectAgentRuns(projectId);
  }
}
