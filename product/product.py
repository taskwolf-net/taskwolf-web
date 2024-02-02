from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def dashboard(request):
  return render(request, 'dashboard/dashboard.html', {'title': gettext('product.dashboard.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/dashboard/dashboard.css']})

@authentication_required
async def help(request):
  return render(request, 'help/help.html', {'title': gettext('product.help.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/help/help.css']})