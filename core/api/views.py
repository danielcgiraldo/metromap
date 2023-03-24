from api import SNT
from django.http import JsonResponse

# Create your views here.

def get_tweets_endpoint(request):
    tweets = SNT.gettweets()
    return JsonResponse(tweets, safe=False, json_dumps_params={'ensure_ascii': False})

    