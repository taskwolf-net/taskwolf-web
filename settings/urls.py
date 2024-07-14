from django.urls import path, include
from . import settings

urlpatterns = [
  path('settings/', settings.profileSettings),
  path('settings/profile/', settings.profileSettings),
  path('settings/account/', settings.accountSettings),
  path('email/change/complete/<str:user>/<str:token>/', settings.changeEmailComplete),
  path('settings/language/', settings.languageSettings),
  path('settings/theme/', settings.themeSettings),
  path('settings/notifications/', settings.notificationsSettings),
  path('settings/2fa/', settings.twoFactorAuthenticationSettings),
]