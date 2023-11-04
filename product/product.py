from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def dashboard(request):
  return render(request, 'dashboard.html', {'title': 'Taskwolf - Dashboard',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/dashboard.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def workflows(request):
  return render(request, 'workflows.html', {'title': 'Taskwolf - Workflows',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/workflows.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def tables(request):
  return render(request, 'tables.html', {'title': 'Taskwolf - Tables',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/tables.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def organizations(request):
  return render(request, 'organizations.html', {'title': 'Taskwolf - Organizations',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/organizations.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def organizationCreate(request):
  return render(request, 'organization-create.html', {'title': 'Taskwolf - Create Organization',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/organization-create.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def organization(request, id):
  return render(request, 'organization.html', {'title': 'Taskwolf - Organization',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/organization.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def organizationInvite(request, id):
  return render(request, 'organization-invite.html', {'title': 'Taskwolf - Organization Invite',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/organization-invite.css'],
      'username': findUsername(request)[0]})