from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def profileSettings(request):
  return render(request, 'settings-profile.html', {'title': 'Taskwolf - Profile Settings',
    'css': ['css/base/neutral-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-profile.css']})

@authentication_required
async def accountSettings(request):
  return render(request, 'settings-account.html', {'title': 'Taskwolf - Account Settings',
    'css': ['css/base/neutral-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-account.css']})

def changeEmailComplete(request, user, token):
  return render(request, 'email-change-complete.html', {'title': 'Taskwolf - Change Email Complete',
    'css': ['css/base/home-header.css', 'css/settings/email-change-complete.css'],
    'user': user, 'token': token})

@authentication_required
async def languageSettings(request):
  return render(request, 'settings-language.html', {'title': 'Taskwolf - Language Settings',
    'css': ['css/base/neutral-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-language.css']})

@authentication_required
async def notificationsSettings(request):
  return render(request, 'settings-notifications.html', {'title': 'Taskwolf - Account Settings',
    'css': ['css/base/neutral-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-notifications.css']})

@authentication_required
async def billingSettings(request):
  return render(request, 'settings-billing.html', {'title': 'Taskwolf - Billing Settings',
    'css': ['css/base/neutral-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-billing.css']})