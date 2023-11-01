from django.urls import path, include
from . import product

urlpatterns = [
  path('dashboard/', product.dashboard)
]