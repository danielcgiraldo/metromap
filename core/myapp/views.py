from SNT import gettweets
from django.http import JsonResponse
# Create your views here.

def get_tweets_endpoint(request):
    tweets = gettweets()
    return JsonResponse(tweets, safe=False, json_dumps_params={'ensure_ascii': False})

