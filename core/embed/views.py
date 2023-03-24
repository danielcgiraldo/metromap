from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def tweets(request):
    url = "https://api.metromap.online/v1/tweets"
    response = requests.get(url)
    api = response.json()
    tweet_info = []
    for tweet in api['data']:
        tweet_dict = {}
        tweet_dict['url'] = tweet['url']
        tweet_dict['content'] = tweet['content']
        tweet_info.append(tweet_dict)
    context = {"tweet_info": tweet_info, "api_url": url}
    return render(request, 'tweets.html', context)