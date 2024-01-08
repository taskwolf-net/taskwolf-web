from django.urls import path, include
from . import ticket

urlpatterns = [
  path('tickets/', ticket.tickets),
  path('ticket/create/', ticket.createTicket),
  path('ticket/<str:id>/', ticket.ticket),
]