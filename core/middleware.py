from django.http import HttpResponseBadRequest

class DomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if 'dominio1.com' in host:
            request.urlconf = 'app_dominio1.urls'
        elif 'dominio2.com' in host:
            request.urlconf = 'app_dominio2.urls'
        else:
            return HttpResponseBadRequest("Dominio no permitido")

        response = self.get_response(request)
        return response
