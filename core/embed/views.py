from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

# Creamos la vista 'tweets'
def tweets(request):
     # Establecemos la URL de la API de Twitter
    url = "https://api.metromap.online/v1/tweets"

     # Realizamos una solicitud GET a la API
    response = requests.get(url)

    # Convertimos la respuesta a formato JSON
    api = response.json()

    # Creamos una lista vacía para almacenar la información de los tweets
    tweet_info = []

    # Iteramos a través de los tweets en el objeto JSON y crear un diccionario de tweet 
    # para cada uno, por último los añadimos a la lista tweet_info
    for tweet in api['data']:
        tweet_dict = {}
        tweet_dict['url'] = tweet['url']
        tweet_dict['content'] = tweet['content']
        tweet_info.append(tweet_dict)

    # Creamos un diccionario de contexto con la información de los tweets y la URL de la API
    context = {"tweet_info": tweet_info, "api_url": url}

    # Renderizamos la plantilla 'tweets.html' con el contexto proporcionado
    return render(request, 'tweets.html', context)