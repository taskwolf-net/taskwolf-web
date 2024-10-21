from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from home.home import home_page
from django.utils.translation import gettext

@authentication_required
async def organizationMember(request):
  return render(request, 'organization/organization-member.html', {'title': gettext('product.organization.member.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-member.css']})

@authentication_required
async def organizationTeam(request):
  return render(request, 'organization/organization-team.html', {'title': gettext('product.organization.team.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-team.css']})

@authentication_required
async def organizationPackage(request):
  return render(request, 'organization/organization-package.html', {'title': gettext('product.organization.package.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-package.css']})

@authentication_required
async def organizationLimitation(request):
  return render(request, 'organization/organization-limitation.html', {'title': gettext('product.organization.limitation.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-limitation.css']})

@authentication_required
async def organizationPayment(request):
  return render(request, 'organization/organization-payment.html', {'title': gettext('product.organization.payment.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-payment.css']})

@authentication_required
async def organizationUpgrade(request):
  return render(request, 'organization/organization-upgrade.html', {'title': gettext('product.organization.upgrade.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-upgrade.css']})

@authentication_required
async def organizationTermination(request):
  return render(request, 'organization/organization-termination.html', {'title': gettext('product.organization.termination.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/organization/organization-termination.css']})

@home_page
async def organizationJoin(request, organization, token):
  return render(request, 'organization/organization-join.html', {'title': gettext('product.organization.join.title'),
    'css': ['css/base/verification-header.css', 'css/base/home-language.css', 'css/product/organization/organization-join.css'],
    'organization': organization, 'token': token})