from functools import wraps
from django.http import HttpResponseRedirect
from functools import partial
import asyncio
import requests
import json
import jwt

def authentication_required(function):
  @wraps(function)
  async def authentication(request, *args, **kwargs):
    authenticated = await isAuthenticated(request)
    if (authenticated):
      return await function(request, *args, **kwargs)
    return HttpResponseRedirect("/")
  return authentication

async def isAuthenticated(request):
  token = request.COOKIES.get('token')
  if (token is None):
    return False
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, "http://localhost:8080/verification/isValid/",
      json = {"token": token}))
  text = response.text
  jsonText = json.loads(text)
  isValid = jsonText["isValid"]
  if (isValid == "true"):
    return True
  return False

def findUsername(request):
  token = request.COOKIES.get('token')
  if (token is None):
    return " "
  decoded = jwt.decode(token, options={"verify_signature": False})
  return decoded["username"]