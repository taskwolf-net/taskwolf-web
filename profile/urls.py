from django.urls import path, include
from . import profile

urlpatterns = [
  path('settings/', profile.settings)
]