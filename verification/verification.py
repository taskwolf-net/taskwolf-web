from django.shortcuts import render
from django.http import HttpResponse
from home.home import home_page

@home_page
async def login(request):
  return render(request, 'login.html', {'title': 'Taskwolf - Login',
    'css': ['css/base/home-header.css', 'css/verification/login.css']})

@home_page
async def register(request):
  return render(request, 'register.html', {'title': 'Taskwolf - Register',
    'css': ['css/base/home-header.css', 'css/verification/register.css']})

@home_page
async def registerEmail(request):
  return render(request, 'register-email.html', {'title': 'Taskwolf - Register Email',
    'css': ['css/base/home-header.css', 'css/verification/register-email.css']})

@home_page
async def registerConfirm(request, user, token):
  return render(request, 'register-confirm.html', {'title': 'Taskwolf - Registration Confirm',
    'css': ['css/base/home-header.css', 'css/verification/register-confirm.css'],
    'user': user, 'token': token})

@home_page
async def passwordResetRequest(request):
  return render(request, 'password-reset-request.html', {'title': 'Taskwolf - Password Reset',
    'css': ['css/base/home-header.css', 'css/verification/password-reset-request.css']})

@home_page
async def passwordResetComplete(request, user, token):
  return render(request, 'password-reset-complete.html', {'title': 'Taskwolf - Password Reset',
    'css': ['css/base/home-header.css', 'css/verification/password-reset-complete.css'],
    'user': user, 'token': token})