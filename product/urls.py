from django.urls import path, include
from . import product, workflow, organization, account, template

urlpatterns = [
  path('dashboard/', product.dashboard),
  path('workflows/', workflow.workflows),
  path('workflow/trigger/', workflow.workflowTrigger),
  path('workflow/action/', workflow.workflowAction),
  path('workflow/condition/', workflow.workflowCondition),
  path('workflow/timeline/', workflow.workflowTimeline),
  path('workflow/<str:id>/', workflow.workflow),
  path('workflow/', workflow.workflowCreate),
  path('templates/', template.templates),
  path('organizations/', organization.organizations),
  path('organization/add/', organization.organizationCreate),
  path('organization/<str:id>/', organization.organization),
  path('organization/<str:id>/invite/', organization.organizationInvite),
  path('account/apps/', account.accountApps),
  path('accounts/', account.accounts),
]