from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def settings(request):
  return render(request, 'settings.html', {'title': 'Taskwolf - Profile - Settings',
    'css': ['css/base/home-header.css', 'css/profile/settings.css'], 'authenticated' :
      await isAuthenticated(request), 'username': findUsername(request)[0]})