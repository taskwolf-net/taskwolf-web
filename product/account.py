from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def accountApps(request):
  return render(request, 'account/account-apps.html', {'title': gettext('product.account.apps.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/account/account-apps.css']})

@authentication_required
async def accountAdd(request):
  return render(request, 'account/account-add.html', {'title': gettext('product.account.add.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/account/account-add.css']})

@authentication_required
async def accounts(request):
  return render(request, 'account/accounts.html', {'title': gettext('product.accounts.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/account/accounts.css']})