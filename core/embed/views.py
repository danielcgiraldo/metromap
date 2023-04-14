from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

# Create your views here.

def map(request):
    # Check if public_key is in url
    key = request.GET.get('public-key', '')
    if(key == ""):
        return JsonResponse({"status":"error", "error": "invalid_client_credentials", "description": "public-key not received"}, status=403)
    # Render map in /templates/map.html
    template = loader.get_template('map.html')
    return HttpResponse(template.render())
