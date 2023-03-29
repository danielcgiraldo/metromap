from api import SNT
from django.http import JsonResponse

"""
# Create your views here.
def get_tweets_endpoint(request):
    # Se llama y alamacena la funcion para obtener los tweets
    tweets = SNT.gettweets()
    # Transforma el diccionario en un JSON, permitiendo emojies
    return JsonResponse(tweets, safe=False, json_dumps_params={'ensure_ascii': False})
"""


    
def get_status(request):
    return JsonResponse({"status":"ok"})

def get_status_line(request, line):
    return JsonResponse({"status":"ok"})

def get_status_station(request, line, station):
    return JsonResponse({"status":"ok"})

def get_data(request):
    return JsonResponse({"status":"ok"})

def get_data_line(request, line):
    return JsonResponse({"status":"ok"})

def get_data_station(request, line, station):
    return JsonResponse({"status":"ok"})
