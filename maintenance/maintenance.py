from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext

def maintenance(request):
  return render(request, 'maintenance.html', {'title': gettext("maintenance.title"),
    'css': ['css/base/verification-header.css', 'css/base/home-language.css',
      'css/base/home-footer.css', 'css/maintenance/maintenance.css']})