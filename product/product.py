from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def dashboard(request):
  return render(request, 'dashboard.html', {'title': 'Taskwolf - Dashboard',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/dashboard.css'],
      'username': findUsername(request)[0]})