from functools import wraps
from functools import partial
import asyncio
import requests
import json
import jwt
from home import home
from django.utils import translation
from django.conf import settings

def authentication_required(function):
  @wraps(function)
  async def authentication(request, *args, **kwargs):
    authenticated = await isAuthenticated(request)
    if (authenticated):
      await applyLanguage(request)
      return await function(request, *args, **kwargs)
    return await home.home(request)
  return authentication

async def isAuthenticated(request):
  token = request.COOKIES.get('token')
  if (token is None):
    return False
  headers = {}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, "http://10.96.0.4/v1/verification/isValid/",
      json = {"token": token}, headers = headers))
  text = response.text
  jsonText = json.loads(text)
  isValid = jsonText["isValid"]
  if (isValid == "true"):
    return True
  return False

async def applyLanguage(request):
  token = request.COOKIES.get('token')
  if (token is None):
    return False
  headers = {"Authorization": "Bearer " + token}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.get, "http://10.96.0.4/v1/settings/language/",
    headers = headers))
  text = response.text
  jsonText = json.loads(text)
  translation.activate(jsonText["language"])

def applyWhitelistKey(request, headers):
  if (not settings.WHITELIST):
    return
  whitelistKey = request.COOKIES.get('taskwolf-whitelist-key')
  if (whitelistKey != None):
    headers["WHITELIST-KEY"] = whitelistKey