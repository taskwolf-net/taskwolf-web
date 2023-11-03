from django.urls import path, include
from . import verification

urlpatterns = [
  path('login/', verification.login),
  path('register/', verification.register),
  path('forgot-password/', verification.forgotPassword),
]