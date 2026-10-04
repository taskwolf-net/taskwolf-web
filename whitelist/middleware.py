from asgiref.sync import iscoroutinefunction, markcoroutinefunction
from django.conf import settings
from functools import partial
import asyncio
import requests
import json
from django.shortcuts import redirect
from app.settings import BACKEND_ENDPOINT

class WhitelistMiddleware(object):
  async_capable = True
  sync_capable = False

  def __init__(self, get_response):
    self.get_response = get_response
    if iscoroutinefunction(self.get_response):
      markcoroutinefunction(self)

  async def __call__(self, request):
    if (not settings.WHITELIST or request.path == "/whitelist/" or request.path == "/favicon.ico"):
      return await self.get_response(request)
    whitelisted = await self.isWhitelisted(request)
    if (not whitelisted):
      return redirect("/whitelist/")
    return await self.get_response(request)

  async def isWhitelisted(self, request):
    key = request.COOKIES.get('taskwolf-whitelist-key')
    if (key is None):
      return False
    response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, BACKEND_ENDPOINT + "/v1/whitelist/isValid/",
      json = {"key": key}))
    text = response.text
    jsonText = json.loads(text)
    isValid = jsonText["isValid"]
    return isValid