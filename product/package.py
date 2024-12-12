from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def packageGeneral(request):
  return render(request, 'package/package-general.html', {'title': gettext('product.package.general.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/package/package-tab.css', 'css/product/package/package-general.css']})

@authentication_required
async def packageLimitation(request):
  return render(request, 'package/package-limitation.html', {'title': gettext('product.package.limitation.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/package/package-tab.css', 'css/product/package/package-limitation.css']})

@authentication_required
async def packagePayment(request):
  return render(request, 'package/package-payment.html', {'title': gettext('product.package.payment.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/package/package-tab.css', 'css/product/package/package-payment.css']})

@authentication_required
async def packageUpgrade(request):
  return render(request, 'package/package-upgrade.html', {'title': gettext('product.package.upgrade.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/package/package-tab.css', 'css/product/package/package-upgrade.css']})

@authentication_required
async def packageTermination(request):
  return render(request, 'package/package-termination.html', {'title': gettext('product.package.termination.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/package/package-tab.css', 'css/product/package/package-termination.css']})