import { Module } from '@nestjs/common';
import { AppController } from './app.controller.js';
import { AppService } from './app.service.js';

import { PrismaModule } from './prisma/prisma.module.js';
import { WorkflowModule } from './workflow/workflow.module.js';

@Module({
  imports: [PrismaModule, WorkflowModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
