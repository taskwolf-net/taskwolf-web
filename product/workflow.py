from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def workflows(request):
  return render(request, 'workflow/workflows.html', {'title': gettext('product.workflows.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflows.css']})

@authentication_required
async def workflow(request, id):
  return render(request, 'workflow/workflow.html', {'title': gettext('product.workflow.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow.css']})

@authentication_required
async def workflowCreate(request):
  return render(request, 'workflow/workflow.html', {'title': gettext('product.workflow.create.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow.css']})

@authentication_required
async def workflowTrigger(request):
  return render(request, 'workflow/workflow-component.html', {'title': gettext('product.workflow.component.trigger.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-component.css',
      'css/product/workflow/workflow-placeholder.css'],
    'type': 'trigger', 'typename': "Trigger"})

@authentication_required
async def workflowAction(request):
  return render(request, 'workflow/workflow-component.html', {'title': gettext('product.workflow.component.action.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-component.css',
      'css/product/workflow/workflow-placeholder.css'],
    'type': 'action', 'typename': "Action"})

@authentication_required
async def workflowCondition(request):
  return render(request, 'workflow/workflow-condition.html', {'title': gettext('product.workflow.condition.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-condition.css',
      'css/product/workflow/workflow-placeholder.css']})

@authentication_required
async def workflowLoop(request):
  return render(request, 'workflow/workflow-loop.html', {'title': gettext('product.workflow.loop.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-loop.css',
      'css/product/workflow/workflow-placeholder.css']})

@authentication_required
async def workflowTimeline(request):
  return render(request, 'workflow/workflow-timeline.html', {'title': gettext('product.workflow.timeline.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/workflow/workflow-timeline.css']})

@authentication_required
async def workflowConnectMail(request):
  return render(request, 'workflow/application/mail.html', {'title': gettext('product.workflow.application.mail.title'),
    'css': ['css/product/workflow/application/mail.css']})

@authentication_required
async def workflowConnectGitlab(request):
  return render(request, 'workflow/application/gitlab.html', {'title': gettext('product.workflow.application.gitlab.title'),
    'css': ['css/product/workflow/application/gitlab.css']})

@authentication_required
async def workflowConnectChatGPT(request):
  return render(request, 'workflow/application/chatgpt.html', {'title': gettext('product.workflow.application.chatgpt.title'),
    'css': ['css/product/workflow/application/chatgpt.css']})