from django.urls import path, include
from django.conf.urls import handler404
from errors import errors
from app.settings import DEVELOPMENT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler404 = errors.handler404

urlpatterns = [
  path('', include('base.urls')),
  path('', include('whitelist.urls')),
  path('', include('maintenance.urls')),
  path('', include('home.urls')),
  path('', include('verification.urls')),
  path('', include('product.urls')),
  path('', include('settings.urls')),
  path('', include('ticket.urls')),
]

if DEVELOPMENT:
  urlpatterns += staticfiles_urlpatterns()