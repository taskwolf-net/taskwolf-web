from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def workflows(request):
  return render(request, 'workflow/workflows.html', {'title': 'Taskwolf - Workflows',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflows.css']})

@authentication_required
async def workflow(request, id):
  return render(request, 'workflow/workflow.html', {'title': 'Taskwolf - Workflow',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow.css']})

@authentication_required
async def workflowCreate(request):
  return render(request, 'workflow/workflow.html', {'title': 'Taskwolf - Workflow - Create',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow.css']})

@authentication_required
async def workflowTrigger(request):
  return render(request, 'workflow/workflow-component.html', {'title': 'Taskwolf - Trigger',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-component.css'],
    'type': 'trigger', 'typename': "Trigger"})

@authentication_required
async def workflowAction(request):
  return render(request, 'workflow/workflow-component.html', {'title': 'Taskwolf - Action',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-component.css'],
    'type': 'action', 'typename': "Action"})

@authentication_required
async def workflowCondition(request):
  return render(request, 'workflow/workflow-condition.html', {'title': 'Taskwolf - Condition',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-condition.css']})

@authentication_required
async def workflowTimeline(request):
  return render(request, 'workflow/workflow-timeline.html', {'title': 'Taskwolf - Timeline',
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-timeline.css']})