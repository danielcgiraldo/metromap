from django.http import HttpResponse, JsonResponse
from django.template import loader
import requests
import os

# Create your views here.

def get_now_str():
    import datetime
    import pytz 

    # get the current UTC date and time
    now_utc = datetime.datetime.now(pytz.utc)   

    # format the date and time as a string in the desired format
    now_str = now_utc.strftime('%Y-%m-%d %H:%M:%S %Z')  
    
    return now_str


def map(request):
    # Check if public_key is in url
    key = request.GET.get('public-key', '')
    if(key == ""):
        template = loader.get_template('error.html')
        return HttpResponse(template.render({'now_str': get_now_str(), 'error' : '401', 'case': '001'}))
    else:
<<<<<<< Updated upstream
        template = loader.get_template('map.html')
        return HttpResponse(template.render())
    
=======
        # Check if public_key is valid
        user = User.objects.filter(public_key=key).first()
        if (user == None):
            return HttpResponse(template.render({'now_str': get_now_str(), 'error': '401', 'case': '002'}))
        else:
            if user.credits < 1:
                return HttpResponse(template.render({'now_str': get_now_str(), 'error': '403', 'case': '001'}))
            else:
                user.credits = user.credits - 1
                user.save()
                template = loader.get_template('map.html')
                return HttpResponse(template.render({"paid": user.paid}))

>>>>>>> Stashed changes

def check_incoming(request):
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
    url = request.GET.get('uri', '')

    payload = {}
    headers = {
      'secret-key': os.getenv("SECRET-KEY")
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return JsonResponse(response.json(), status=response.status_code)