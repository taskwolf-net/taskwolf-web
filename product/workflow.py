from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated, findUsername

@authentication_required
async def workflows(request):
  return render(request, 'workflow/workflows.html', {'title': 'Taskwolf - Workflows',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflows.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def workflow(request, id):
  return render(request, 'workflow/workflow.html', {'title': 'Taskwolf - Workflow',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def workflowCreate(request):
  return render(request, 'workflow/workflow.html', {'title': 'Taskwolf - Workflow - Create',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow.css'],
      'username': findUsername(request)[0]})

@authentication_required
async def workflowTrigger(request, id):
  return render(request, 'workflow/workflow-component.html', {'title': 'Taskwolf - Trigger',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-component.css'],
      'username': findUsername(request)[0], 'type': 'trigger', 'typename': "Trigger"})

@authentication_required
async def workflowTriggerCreate(request):
  return render(request, 'workflow/workflow-component.html', {'title': 'Taskwolf - Trigger - Create',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-component.css'],
      'username': findUsername(request)[0], 'type': 'trigger', 'typename': "Trigger"})

@authentication_required
async def workflowAction(request, id):
  return render(request, 'workflow/workflow-component.html', {'title': 'Taskwolf - Action',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-component.css'],
      'username': findUsername(request)[0], 'type': 'action', 'typename': "Action"})

@authentication_required
async def workflowActionCreate(request):
  return render(request, 'workflow/workflow-component.html', {'title': 'Taskwolf - Action - Create',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-component.css'],
      'username': findUsername(request)[0], 'type': 'action', 'typename': "Action"})