from functools import wraps
from functools import partial
import asyncio
import requests
import json
import jwt
import datetime
from home import home
from django.utils import translation
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse

def authentication_required(function):
  @wraps(function)
  async def authentication(request, *args, **kwargs):
    response = await function(request, *args, **kwargs)
    authenticated = await isAuthenticated(request, response)
    if (authenticated):
      await applyLanguage(request)
      return response
    response = redirect("/")
    response.delete_cookie("token", domain=".taskwolf.net")
    response.delete_cookie("refresh-token", domain=".taskwolf.net")
    return response
  return authentication

async def isAuthenticated(request, response):
  token = request.COOKIES.get('token')
  if (token is None):
    return False
  headers = {}
  applyWhitelistKey(request, headers)
  requestResponse = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, "https://api.taskwolf.net/v1/verification/isValid/",
      json = {"token": token}, headers = headers))
  if (requestResponse.status_code == 417):
    return await refreshAuthentication(request, response)
  text = requestResponse.text
  jsonText = json.loads(text)
  isValid = jsonText["isValid"]
  if (isValid == "true"):
    return True
  return False

async def refreshAuthentication(request, response):
  refreshToken = request.COOKIES.get('refresh-token')
  if (refreshToken is None):
    return False
  headers = {}
  applyWhitelistKey(request, headers)
  requestResponse = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, "https://api.taskwolf.net/v1/verification/refresh/",
      json = {"refreshToken": refreshToken}, headers = headers))
  text = requestResponse.text
  jsonText = json.loads(text)
  success = jsonText["success"]
  if (success == "true"):
    setCookie(response, "token", jsonText["productApiKey"], 10 / (60 * 24))
    setCookie(response, "refresh-token", jsonText["refreshToken"], 1)
    request.COOKIES["token"] = jsonText["productApiKey"]
    request.COOKIES["refresh-token"] = jsonText["refreshToken"]
    return True
  return False

async def applyLanguage(request):
  token = request.COOKIES.get('token')
  if (token is None):
    return False
  headers = {"Authorization": "Bearer " + token}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.get, "https://api.taskwolf.net/v1/settings/language/",
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

def setCookie(response, key, value, expirationDays):
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() +
    datetime.timedelta(days=expirationDays), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, expires=expires, domain=".taskwolf.net",
    secure=True)