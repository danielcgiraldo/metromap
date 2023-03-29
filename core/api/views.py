from api import SNT
from django.http import JsonResponse

# Create your views here.
def get_tweets_endpoint(request):
    # Se llama y alamacena la funcion para obtener los tweets
    tweets = SNT.gettweets()
    # Transforma el diccionario en un JSON, permitiendo emojies
    return JsonResponse(tweets, safe=False, json_dumps_params={'ensure_ascii': False})

    