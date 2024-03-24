from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def processes(request):
  return render(request, 'process/processes.html', {'title': gettext('product.process.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/process/processes.css']})

@authentication_required
async def process(request):
  return render(request, 'process/process.html', {'title': gettext('product.process.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/process/process.css']})

@authentication_required
async def processSelected(request, id):
  return render(request, 'process/process.html', {'title': gettext('product.process.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/process/process.css']})