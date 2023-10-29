from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required

@authentication_required
def home(request):
  return render(request, 'home.html', {'title': 'Taskwolf - Home',
    'css': ['css/home.css']})