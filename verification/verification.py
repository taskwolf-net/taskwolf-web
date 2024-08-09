from django.shortcuts import render
from django.http import HttpResponse
from home.home import home_page
from django.utils.translation import gettext

@home_page
async def login(request):
  redirect = request.GET.get('redirect', '')
  return render(request, 'login.html', {'title': gettext("home.login.title"),
    'css': ['css/base/home-header.css', 'css/base/2fa.css', 'css/verification/login.css'],
    'redirect': redirect})

@home_page
async def register(request):
  redirect = request.GET.get('redirect', '')
  return render(request, 'register.html', {'title': gettext("home.registration.title"),
    'css': ['css/base/home-header.css', 'css/verification/register.css'],
    'script': ['https://www.google.com/recaptcha/api.js?render=6LdpvhAqAAAAAFbSWycUwLBbDnS4TaSvjJOofiOg'],
    'redirect': redirect})

@home_page
async def registerConfirm(request, user, token):
  return render(request, 'register-confirm.html', {'title': gettext("home.registration.confirm.title"),
    'css': ['css/base/home-header.css', 'css/verification/register-confirm.css'],
    'user': user, 'token': token})

@home_page
async def loginRegister(request):
  redirect = request.GET.get('redirect', '')
  return render(request, 'login-register.html', {'title': gettext("home.login.register.title"),
    'css': ['css/base/verification-header.css', 'css/verification/login-register.css'],
    'redirect': redirect})

@home_page
async def payment(request):
  return render(request, 'payment.html', {'title': gettext("home.payment.title"),
    'css': ['css/base/verification-header.css', 'css/verification/payment.css']})

@home_page
async def paymentComplete(request):
  return render(request, 'payment-complete.html', {'title': gettext("home.payment.complete.title"),
    'css': ['css/base/verification-header.css', 'css/verification/payment-complete.css']})

@home_page
async def offer(request, id):
  return render(request, 'offer.html', {'title': gettext("home.offer.title"),
    'css': ['css/base/verification-header.css', 'css/verification/offer.css'],
    'offer': id})

@home_page
async def passwordResetRequest(request):
  return render(request, 'password-reset-request.html', {'title': gettext("home.password.reset.request.title"),
    'css': ['css/base/home-header.css', 'css/verification/password-reset-request.css']})

@home_page
async def passwordResetComplete(request, user, token):
  return render(request, 'password-reset-complete.html', {'title': gettext("home.password.reset.complete.title"),
    'css': ['css/base/home-header.css', 'css/verification/password-reset-complete.css'],
    'user': user, 'token': token})