from functools import wraps
from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import isAuthenticated
from product.product import dashboard
from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import gettext

def home_page(function):
  @wraps(function)
  async def home_page(request, *args, **kwargs):
    applyLanguage(request)
    return await function(request, *args, **kwargs)
  return home_page

def applyLanguage(request):
  language = request.COOKIES.get("taskwolf-home-language")
  if (language is None):
    translation.activate("en")
  translation.activate(language)

@home_page
async def home(request):
  authenticated = await isAuthenticated(request)
  if (authenticated):
    return redirect("/dashboard/")
  return render(request, 'home.html', {'title': gettext("home.home.title"),
    'css': ['css/base/home-header.css', 'css/home/home.css']})

@home_page
async def product(request):
  return render(request, 'product.html', {'title': gettext("home.product.title"),
    'css': ['css/base/home-header.css', 'css/home/product.css']})

@home_page
async def pricing(request):
  return render(request, 'pricing.html', {'title': gettext("home.pricing.title"),
    'css': ['css/base/home-header.css', 'css/home/pricing.css']})