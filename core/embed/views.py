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

def check_incoming(request, fn, line = None, station = None):
    """
    Check if the request is made from map, and not someone else.

    Parameters:
        request (django.http.request.HttpRequest): The request object.
        fn (function): The function to be executed if the request is valid.
        line (str): The line of the station.
        station (str): The station.

    Returns:
        If the request is valid, the function returns the result of fn.
    """

    # TODO: Check public key in request
    
    # Get referer
    referer = request.META.get('HTTP_REFERER', '')

    # Check if referer is valid
    if referer and not referer.startswith(request.scheme + '://' + request.get_host()):
        return JsonResponse({"status":"error", "error": "invalid_referer", "description": "referer is not metromap.online"}, status=403)
    if line:
        return fn(line, station)
    else:
        return fn()

def get_data(line, station):
    pass

def get_update():
    pass

def get_incidents(line, station):
    pass