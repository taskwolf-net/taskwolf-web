from functools import wraps
from functools import partial
import asyncio
import requests
import json
import jwt
import datetime
from home import home
from app.settings import BACKEND_ENDPOINT, COOKIE_DOMAIN, DEVELOPMENT
from django.utils import translation
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse

def authentication_required(function):
  @wraps(function)
  async def authentication(request, *args, **kwargs):
    authenticationResponse = await isAuthenticated(request)
    if (authenticationResponse["success"]):
      if ("data" in authenticationResponse):
        request.COOKIES["token"] = authenticationResponse["data"]["token"]
        request.COOKIES["refresh-token"] = authenticationResponse["data"]["refreshToken"]
      language = await applyLanguage(request)
      response = await function(request, *args, **kwargs)
      setCookie(response, "dulno-language", language, 30)
      setCookie(response, "dulno-home-language", language, 30)
      if ("data" in authenticationResponse):
        setCookie(response, "token", authenticationResponse["data"]["token"], 30)
        setCookie(response, "refresh-token", authenticationResponse["data"]["refreshToken"], 30)
      return response
    response = redirect("/")
    response.delete_cookie("token", domain=COOKIE_DOMAIN)
    response.delete_cookie("refresh-token", domain=COOKIE_DOMAIN)
    return response
  return authentication

async def isAuthenticated(request):
  token = request.COOKIES.get('token')
  if (token is None):
    return await refreshAuthentication(request)
  headers = {}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, BACKEND_ENDPOINT + "/v1/verification/isValid/",
      json = {"token": token}, headers = headers))
  if (response.status_code == 417):
    return await refreshAuthentication(request)
  text = response.text
  jsonText = json.loads(text)
  isValid = jsonText["isValid"]
  if (isValid == "true"):
    return {"success": True}
  return {"success": False}

async def refreshAuthentication(request):
  refreshToken = request.COOKIES.get('refresh-token')
  if (refreshToken is None):
    return {"success": False}
  headers = {}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, BACKEND_ENDPOINT + "/v1/verification/refresh/",
      json = {"refreshToken": refreshToken}, headers = headers))
  text = response.text
  jsonText = json.loads(text)
  success = jsonText["success"]
  if (success == "true"):
    request.dulnoToken = jsonText["productApiKey"]
    request.dulnoRefreshToken = jsonText["refreshToken"]
    return {"success": True, "data": {"token": jsonText["productApiKey"],
      "refreshToken": jsonText["refreshToken"]}}
  return {"success": False}

async def applyLanguage(request):
  token = request.COOKIES.get('token')
  if (token is None):
    return False
  headers = {"Authorization": "Bearer " + token}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.get, BACKEND_ENDPOINT + "/v1/settings/language/",
    headers = headers))
  text = response.text
  jsonText = json.loads(text)
  language = jsonText["language"]
  translation.activate(language)
  return language

def home_authentication_required(function):
  @wraps(function)
  async def authentication(request, *args, **kwargs):
    authenticationResponse = await isHomeAuthenticated(request)
    if (authenticationResponse["success"]):
      if ("data" in authenticationResponse):
        request.COOKIES["token"] = authenticationResponse["data"]["token"]
        request.COOKIES["refresh-token"] = authenticationResponse["data"]["refreshToken"]
      language = await applyHomeLanguage(request)
      response = await function(request, *args, **kwargs)
      setCookie(response, "dulno-language", language, 30)
      setCookie(response, "dulno-home-language", language, 30)
      if ("data" in authenticationResponse):
        setCookie(response, "token", authenticationResponse["data"]["token"], 30)
        setCookie(response, "refresh-token", authenticationResponse["data"]["refreshToken"], 30)
      return response
    response = redirect("/")
    response.delete_cookie("token", domain=COOKIE_DOMAIN)
    response.delete_cookie("refresh-token", domain=COOKIE_DOMAIN)
    return response
  return authentication

async def isHomeAuthenticated(request):
  token = request.COOKIES.get('home-token')
  if (token is None):
    return await isAuthenticated(request)
  headers = {}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, BACKEND_ENDPOINT + "/v1/verification/home/isValid/",
      json = {"token": token}, headers = headers))
  text = response.text
  jsonText = json.loads(text)
  isValid = jsonText["isValid"]
  if (isValid == "false"):
    return await isAuthenticated(request)
  return {"success": True}

async def applyHomeLanguage(request):
  token = request.COOKIES.get('token')
  if (token is None):
    headers = {"Home-Authorization": "Bearer " + request.COOKIES.get('home-token')}
  else:
    headers = {"Authorization": "Bearer " + token}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.get, BACKEND_ENDPOINT + "/v1/settings/language/",
    headers = headers))
  text = response.text
  jsonText = json.loads(text)
  language = jsonText["language"]
  translation.activate(language)
  return language

def applyWhitelistKey(request, headers):
  if (not settings.WHITELIST):
    return
  whitelistKey = request.COOKIES.get('dulno-whitelist-key')
  if (whitelistKey != None):
    headers["WHITELIST-KEY"] = whitelistKey

def setCookie(response, key, value, expirationDays):
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() +
    datetime.timedelta(days=expirationDays), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, expires=expires, domain=COOKIE_DOMAIN,
    secure=(DEVELOPMENT == False))