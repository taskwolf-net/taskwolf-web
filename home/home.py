from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import isAuthenticated, findUsername

async def home(request):
  return render(request, 'home.html', {'title': 'Taskwolf - Home',
    'css': ['css/base/home-header.css', 'css/home/home.css'], 'authenticated':
      await isAuthenticated(request), 'username': findUsername(request)[0]})

async def product(request):
  return render(request, 'product.html', {'title': 'Taskwolf - Product',
    'css': ['css/base/home-header.css', 'css/home/product.css'], 'authenticated':
      await isAuthenticated(request), 'username': findUsername(request)[0]})

async def features(request):
  return render(request, 'features.html', {'title': 'Taskwolf - Features',
    'css': ['css/base/home-header.css', 'css/home/features.css'], 'authenticated':
      await isAuthenticated(request), 'username': findUsername(request)[0]})

async def aboutUs(request):
  return render(request, 'about-us.html', {'title': 'Taskwolf - About us',
    'css': ['css/base/home-header.css', 'css/home/about-us.css'], 'authenticated':
      await isAuthenticated(request), 'username': findUsername(request)[0]})