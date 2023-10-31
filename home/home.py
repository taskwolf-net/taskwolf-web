from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

async def home(request):
  return render(request, 'home.html', {'title': 'Taskwolf - Home',
    'css': ['css/home.css'], "authenticated": await isAuthenticated(request),
      "username": findUsername(request)[0]})

@authentication_required
async def product(request):
  return render(request, 'product.html', {'title': 'Taskwolf - Product',
    'css': ['css/product.css'], "authenticated": await isAuthenticated(request),
      "username": findUsername(request)[0]})

async def features(request):
  return render(request, 'features.html', {'title': 'Taskwolf - Features',
    'css': ['css/features.css'], "authenticated": await isAuthenticated(request),
      "username": findUsername(request)[0]})

async def aboutUs(request):
  return render(request, 'about-us.html', {'title': 'Taskwolf - About us',
    'css': ['css/about-us.css'], "authenticated": await isAuthenticated(request),
      "username": findUsername(request)[0]})