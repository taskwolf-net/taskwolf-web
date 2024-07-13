from django.urls import path, include
from . import verification

urlpatterns = [
  path('login/', verification.login),
  path('register/', verification.register),
  path('register/confirm/<str:user>/<str:token>/', verification.registerConfirm),
  path('login-register/', verification.loginRegister),
  path('payment/', verification.payment),
  path('payment/complete/', verification.paymentComplete),
  path('password/reset/request/', verification.passwordResetRequest),
  path('password/reset/complete/<str:user>/<str:token>/', verification.passwordResetComplete),
]