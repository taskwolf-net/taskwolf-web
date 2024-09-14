from django.shortcuts import render
from django.http import HttpResponse

def whitelist(request):
  return render(request, 'whitelist.html', {'title': 'Dulno - Whitelist',
    'css': ['css/whitelist/whitelist.css']})