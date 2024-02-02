from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def organizations(request):
  return render(request, 'organization/organizations.html', {'title': gettext('product.organizations.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organizations.css']})

@authentication_required
async def organizationCreate(request):
  return render(request, 'organization/organization-create.html', {'title': gettext('product.organization.create.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-create.css']})

@authentication_required
async def organization(request, id):
  return render(request, 'organization/organization.html', {'title': gettext('product.organization.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization.css']})

@authentication_required
async def organizationJoin(request, organization, token):
  return render(request, 'organization/organization-join.html', {'title': gettext('product.organization.join.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-join.css'],
    'organization': organization, 'token': token})