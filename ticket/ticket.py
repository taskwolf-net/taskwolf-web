from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def tickets(request):
  return render(request, 'tickets.html', {'title': 'Taskwolf - Tickets',
    'css': ['css/base/neutral-header.css', 'css/ticket/tickets.css']})

@authentication_required
async def createTicket(request):
  return render(request, 'ticket-create.html', {'title': 'Taskwolf - Create Ticket',
    'css': ['css/base/neutral-header.css', 'css/ticket/ticket-create.css']})

@authentication_required
async def ticket(request, id):
  return render(request, 'ticket.html', {'title': 'Taskwolf - Ticket',
    'css': ['css/base/neutral-header.css', 'css/ticket/ticket.css'], 'ticket': id})