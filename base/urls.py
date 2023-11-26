from django.urls import path, include
from . import base

urlpatterns = [
  path('close/', base.close)
]