from django.shortcuts import render
from SNT import gettweets
from django.http import JsonResponse
import json
# Create your views here.

def get_tweets_endpoint(request):
    tweets = gettweets()
    return JsonResponse(tweets, safe=False)