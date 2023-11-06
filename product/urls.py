from django.urls import path, include
from . import product, workflow, organization

urlpatterns = [
  path('dashboard/', product.dashboard),
  path('workflows/', workflow.workflows),
  path('tables/', product.tables),
  path('organizations/', organization.organizations),
  path('organization/add/', organization.organizationCreate),
  path('organization/<str:id>/', organization.organization),
  path('organization/<str:id>/invite/', organization.organizationInvite),
]