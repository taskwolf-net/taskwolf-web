from django.urls import path, include
from . import product

urlpatterns = [
  path('dashboard/', product.dashboard),
  path('workflows/', product.workflows),
  path('tables/', product.tables),
  path('organizations/', product.organizations),
  path('organization/create/', product.organizationCreate),
  path('organization/<str:id>/', product.organization),
  path('organization/<str:id>/invite/', product.organizationInvite),
]