from django.urls import path, include
from . import product, workflow, organization, account, template

urlpatterns = [
  path('dashboard/', product.dashboard),
  path('workflows/', workflow.workflows),
  path('workflow/trigger/<str:id>/', workflow.workflowTrigger),
  path('workflow/trigger/', workflow.workflowTriggerCreate),
  path('workflow/action/<str:id>/', workflow.workflowAction),
  path('workflow/action/', workflow.workflowActionCreate),
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