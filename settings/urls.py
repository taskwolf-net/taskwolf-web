from django.urls import path, include
from . import settings

urlpatterns = [
  path('settings/', profile.settings)
]