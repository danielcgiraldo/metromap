from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

# Create your views here.

# Creamos la vista 'tweets'
def map(request):
    # Check if public_key is in url
    template = loader.get_template('map.html')
    return HttpResponse(template.render())