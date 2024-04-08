from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def webhooks(request):
  return render(request, 'webhook/webhooks.html', {'title': gettext('product.webhooks.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/webhook/webhooks.css']})

@authentication_required
async def addWebhook(request):
  return render(request, 'webhook/webhook-add.html', {'title': gettext('product.webhook.add.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/webhook/webhook-add.css']})

@authentication_required
async def webhook(request, id):
  return render(request, 'webhook/webhook.html', {'title': gettext('product.webhook.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/webhook/webhook.css'],
    'webhook': id})