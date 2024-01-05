from django.urls import path, include
from . import ticket

urlpatterns = [
  path('tickets/', ticket.tickets),
  path('ticket/', ticket.ticket),
]