from django.urls import path, include
from . import maintenance

urlpatterns = [
  path('maintenance/', maintenance.maintenance),
]