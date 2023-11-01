from django.urls import path, include
from . import home

urlpatterns = [
  path('', home.home),
  path('product/', home.product),
  path('features/', home.features),
  path('about-us/', home.aboutUs)
]