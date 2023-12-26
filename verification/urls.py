from django.urls import path, include
from . import verification

urlpatterns = [
  path('login/', verification.login),
  path('register/', verification.register),
  path('register/email/', verification.registerEmail),
  path('register/confirm/<str:user>/<str:token>/', verification.registerConfirm),
  path('forgot-password/', verification.forgotPassword),
]