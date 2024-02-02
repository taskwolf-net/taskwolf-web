from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def tickets(request):
  return render(request, 'tickets.html', {'title': gettext('tickets.page.title'),
    'css': ['css/base/neutral-header.css', 'css/ticket/tickets.css']})

@authentication_required
async def createTicket(request):
  return render(request, 'ticket-create.html', {'title': gettext('ticket.create.page.title'),
    'css': ['css/base/neutral-header.css', 'css/ticket/ticket-create.css']})

@authentication_required
async def ticket(request, id):
  return render(request, 'ticket.html', {'title': gettext('ticket.page.title'),
    'css': ['css/base/neutral-header.css', 'css/ticket/ticket.css'], 'ticket': id})