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

def forgotPassword(request):
  return render(request, 'forgot-password.html', {'title': 'Taskwolf - Forgot Password',
    'css': ['css/base/home-header.css', 'css/verification/forgot-password.css']})