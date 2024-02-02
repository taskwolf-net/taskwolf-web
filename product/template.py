from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def templates(request):
  return render(request, 'template/templates.html', {'title': gettext('product.templates.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/template/templates.css']})