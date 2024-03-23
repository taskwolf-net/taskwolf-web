from django.urls import path, include
from . import product, workflow, process, database, organization, account, template

urlpatterns = [
  path('dashboard/', product.dashboard),
  path('workflows/', workflow.workflows),
  path('workflow/trigger/', workflow.workflowTrigger),
  path('workflow/action/', workflow.workflowAction),
  path('workflow/condition/', workflow.workflowCondition),
  path('workflow/timeline/', workflow.workflowTimeline),
  path('workflow/<str:id>/', workflow.workflow),
  path('workflow/', workflow.workflowCreate),
  path('processes/', process.processes),
  path('process/', process.process),
  path('process/<str:id>/', process.processSelected),
  path('databases/', database.databases),
  path('database/create/', database.databaseCreate),
  path('database/<str:id>/', database.database),
  path('templates/', template.templates),
  path('organizations/', organization.organizations),
  path('organization/add/', organization.organizationCreate),
  path('organization/<str:id>/', organization.organization),
  path('organization/join/<str:organization>/<str:token>/', organization.organizationJoin),
  path('account/apps/', account.accountApps),
  path('accounts/', account.accounts),
  path('help/', product.help),
]