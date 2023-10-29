from functools import wraps
from django.http import HttpResponseRedirect

def authentication_required(function):
  @wraps(function)
  def authentication(request, *args, **kwargs):
    print("Authentication")
    return function(request, *args, **kwargs)
  return authentication