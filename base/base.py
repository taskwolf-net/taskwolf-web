from django.shortcuts import render
from django.http import HttpResponse

def close(request):
  return render(request, 'close/close.html')