from django.http import HttpResponseBadRequest
from dotenv import load_dotenv
import os

class DomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if os.getenv("EMBED_HOST") in host:
            request.urlconf = 'embed.urls'
        elif os.getenv("API_HOST") in host:
            request.urlconf = 'api.urls'
        else:
            return HttpResponseBadRequest("Dominio no permitido")

        response = self.get_response(request)
        return response
