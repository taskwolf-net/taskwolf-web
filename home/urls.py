from django.urls import path, include
from . import home

urlpatterns = [
  path('home/', home.home)
]