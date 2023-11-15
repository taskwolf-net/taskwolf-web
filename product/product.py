from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def dashboard(request):
  return render(request, 'dashboard/dashboard.html', {'title': 'Taskwolf - Dashboard',
    'css': ['css/base/product-header.css', 'css/product-sidebar.css', 'css/product/dashboard/dashboard.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def tables(request):
  return render(request, 'tables/tables.html', {'title': 'Taskwolf - Tables',
    'css': ['css/base/product-header.css', 'css/product-sidebar.css', 'css/product/tables/tables.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def templates(request):
  return render(request, 'template/templates.html', {'title': 'Taskwolf - Templates',
    'css': ['css/base/product-header.css', 'css/product-sidebar.css', 'css/product/template/templates.css'],
      'username': findUsername(request)[0]})