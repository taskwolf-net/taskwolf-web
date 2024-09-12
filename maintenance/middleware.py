from asgiref.sync import iscoroutinefunction, markcoroutinefunction
from django.conf import settings
from functools import partial
import asyncio
import requests
import json
from django.shortcuts import redirect
from django.utils import translation

class MaintenanceMiddleware(object):
  async_capable = True
  sync_capable = False

  def __init__(self, get_response):
    self.get_response = get_response
    if iscoroutinefunction(self.get_response):
      markcoroutinefunction(self)

  async def __call__(self, request):
    if (request.path == "/maintenance/" or request.path == "/whitelist/" or request.path == "/favicon.ico"):
      self.applyLanguage(request)
      return await self.get_response(request)
    running = await self.isRunning(request)
    if (running):
      self.applyLanguage(request)
      return redirect("/maintenance/")
    return await self.get_response(request)

  async def isRunning(self, request):
    response = await asyncio.get_event_loop().run_in_executor(None,
       partial(requests.get, "http://10.96.0.4/v1/maintenance/running/"))
    text = response.text
    jsonText = json.loads(text)
    maintenanceRunning = jsonText["found"]
    return maintenanceRunning

  def applyLanguage(self, request):
    language = request.COOKIES.get("taskwolf-home-language")
    if (language is None):
      translation.activate("en")
    translation.activate(language)