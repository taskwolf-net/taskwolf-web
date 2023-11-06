from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def workflows(request):
  return render(request, 'workflow/workflows.html', {'title': 'Taskwolf - Workflows',
    'css': ['css/product-header.css', 'css/product-sidebar.css', 'css/workflow/workflows.css'],
      'username': findUsername(request)[0]})