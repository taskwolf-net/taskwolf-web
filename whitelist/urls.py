from django.urls import path, include
from . import whitelist

urlpatterns = [
  path('whitelist/', whitelist.whitelist),
]