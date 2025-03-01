def domain(request):
  domain = request.get_host()
  base_url = f"{request.scheme}://{domain}"
  return {
    'domain': domain,
    'base_url': base_url
  }