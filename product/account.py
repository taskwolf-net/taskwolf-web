from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def accountApps(request):
  return render(request, 'account/account-apps.html', {'title': 'Taskwolf - Apps',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/account/account-apps.css']})

@authentication_required
async def accounts(request):
  return render(request, 'account/accounts.html', {'title': 'Taskwolf - Accounts',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/account/accounts.css']})