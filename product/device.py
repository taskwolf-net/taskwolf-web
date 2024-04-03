from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def devices(request):
  return render(request, 'device/devices.html', {'title': gettext('product.devices.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/device/devices.css']})