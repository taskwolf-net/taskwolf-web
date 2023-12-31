from django.urls import path, include
from django.conf.urls import handler404
from errors import errors

handler404 = errors.handler404

urlpatterns = [
  path('', include('base.urls')),
  path('', include('home.urls')),
  path('', include('verification.urls')),
  path('', include('product.urls')),
  path('', include('settings.urls')),
]