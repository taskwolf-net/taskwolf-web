from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def organizations(request):
  return render(request, 'organization/organizations.html', {'title': 'Taskwolf - Organizations',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organizations.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def organizationCreate(request):
  return render(request, 'organization/organization-create.html', {'title': 'Taskwolf - Create Organization',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-create.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def organization(request, id):
  return render(request, 'organization/organization.html', {'title': 'Taskwolf - Organization',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def organizationInvite(request, id):
  return render(request, 'organization/organization-invite.html', {'title': 'Taskwolf - Organization Invite',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-invite.css'],
      'username': findUsername(request)[0]})