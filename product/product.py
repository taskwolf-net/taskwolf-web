from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def dashboard(request):
  return render(request, 'dashboard/dashboard.html', {'title': 'Taskwolf - Dashboard',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/dashboard/dashboard.css']})

@authentication_required
async def templates(request):
  return render(request, 'template/templates.html', {'title': 'Taskwolf - Templates',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/template/templates.css']})