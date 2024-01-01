from django.urls import path, include
from . import settings

urlpatterns = [
  path('settings/profile/', settings.profileSettings),
  path('settings/account/', settings.accountSettings),
  path('settings/notifications/', settings.notificationsSettings),
  path('settings/billing/', settings.billingSettings),
]