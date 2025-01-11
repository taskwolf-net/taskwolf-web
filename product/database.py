from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def databases(request):
  return render(request, 'database/databases.html', {'title': gettext('product.databases.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/database/databases.css']})

@authentication_required
async def database(request, id):
  return render(request, 'database/database.html', {'title': gettext('product.database.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/database/database.css']})

@authentication_required
async def databaseCreate(request):
  return render(request, 'database/database-create.html', {'title': gettext('product.database.create.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/database/database-create.css']})

@authentication_required
async def databaseImport(request):
  return render(request, 'database/database-import.html', {'title': gettext('product.database.import.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/database/database-import.css']})