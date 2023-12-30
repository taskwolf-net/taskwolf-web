from django.shortcuts import render
from django.http import HttpResponse

def login(request):
  return render(request, 'login.html', {'title': 'Taskwolf - Login',
    'css': ['css/base/home-header.css', 'css/verification/login.css']})

def register(request):
  return render(request, 'register.html', {'title': 'Taskwolf - Register',
    'css': ['css/base/home-header.css', 'css/verification/register.css']})

def registerEmail(request):
  return render(request, 'register-email.html', {'title': 'Taskwolf - Register Email',
    'css': ['css/base/home-header.css', 'css/verification/register-email.css']})

def registerConfirm(request, user, token):
  return render(request, 'register-confirm.html', {'title': 'Taskwolf - Registration Confirm',
    'css': ['css/base/home-header.css', 'css/verification/register-confirm.css'],
    'user': user, 'token': token})

def passwordResetRequest(request):
  return render(request, 'password-reset-request.html', {'title': 'Taskwolf - Password Reset',
    'css': ['css/base/home-header.css', 'css/verification/password-reset-request.css']})

def passwordResetComplete(request, user, token):
  return render(request, 'password-reset-complete.html', {'title': 'Taskwolf - Password Reset',
    'css': ['css/base/home-header.css', 'css/verification/password-reset-complete.css'],
    'user': user, 'token': token})