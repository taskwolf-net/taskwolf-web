from django.urls import path, include
from . import home

urlpatterns = [
  path('', home.product),
  path('product/', home.product),
  path('solution/', home.solution),
  path('pricing/', home.pricing),
  path('imprint/', home.imprint),
  path('privacy-policy/', home.privacyPolicy),
]