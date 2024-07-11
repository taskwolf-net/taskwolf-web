from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def organization(request):
  return render(request, 'organization/organization.html', {'title': gettext('product.organization.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization.css']})

@authentication_required
async def organizationJoin(request, organization, token):
  return render(request, 'organization/organization-join.html', {'title': gettext('product.organization.join.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-join.css'],
    'organization': organization, 'token': token})