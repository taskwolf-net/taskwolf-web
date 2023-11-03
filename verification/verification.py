from django.shortcuts import render
from django.http import HttpResponse

def login(request):
  return render(request, 'login.html', {'title': 'Taskwolf - Login',
    'css': ['css/home-header.css', 'css/login.css']})

def register(request):
  return render(request, 'register.html', {'title': 'Taskwolf - Register',
    'css': ['css/home-header.css', 'css/register.css']})

def forgotPassword(request):
  return render(request, 'forgot-password.html', {'title': 'Taskwolf - Forgot Password',
    'css': ['css/home-header.css', 'css/forgot-password.css']})