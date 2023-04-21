from django.http import JsonResponse
from api.controllers.incident_controller import Incident
from api.controllers.data_controller import Data

"""
# Create your views here.
def get_tweets_endpoint(request):
    # Se llama y alamacena la funcion para obtener los tweets
    tweets = SNT.gettweets()
    # Transforma el diccionario en un JSON, permitiendo emojies
    return JsonResponse(tweets, safe=False, json_dumps_params={'ensure_ascii': False})
"""


def get_status(params):
    """
    if len(params) == 0, then request is /status
    elif len(params) == 1, request is /status/:line
    finally elif len(params) == 2 request is /status/:line/:station
    """
    return JsonResponse({'status':'error', 'error':'under_maintenance','message':'Map in under maintenace'})

def get_status_line(request, line):
    # checks if secret key credentials are in the header
    sk = request.META.get("HTTP_SECRET_KEY")
    if (sk == None):
       return JsonResponse({'status':'error', 'error':'invalid_client_credentials', 'description':'secret_key not received',}, status=403)
    return JsonResponse({'status':'error', 'error':'under_maintenance','message':'Map in under maintenace'})

def get_status_station(request, line, station):
    # checks if secret key credentials are in the header
    sk = request.META.get("HTTP_SECRET_KEY")
    if (sk == None):
       return JsonResponse({'status':'error', 'error':'invalid_client_credentials', 'description':'secret_key not received',}, status=403)
    return JsonResponse({'status':'error', 'error':'under_maintenance','message':'Map in under maintenace'})

def get_data(line, station):
    incident = Data(line, station)
    return JsonResponse({'status':'ok', 'data':incident.get_data()})

def get_incident(line, station):
    incident = Incident(line, station)
    return JsonResponse({'status':'ok', 'data':incident.get_data()})
    