from django.shortcuts import render
from django.http import HttpResponse

def handler404(request, *args, **argv):
  print("Error")
  return render(request, 'errors/404.html', status=404)