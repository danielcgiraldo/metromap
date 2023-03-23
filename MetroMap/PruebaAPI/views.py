from django.shortcuts import render
import requests
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.

import requests

def apiprueba(request):
    link = requests.get('https://randomuser.me/api/')
    data = link.json()
    #diccionario = dict(data)
    results = data['results']
    info = data["info"]
    plantillaExterna = open("C:\\Users\\jmpor\\OneDrive\\Documentos\\GitHub\\ppi_06\\MetroMap\\PruebaAPI\\plantillas\\apiprueba.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"results": results, "info": info})
    documeto = template.render(contexto)
    return HttpResponse(documeto)

def dicapi(request):
    link = requests.get('https://randomuser.me/api/')
    data = link.json()
    diccionario = dict(data)
    plantillaExterna = open("C:\\Users\\jmpor\\OneDrive\\Documentos\\GitHub\\ppi_06\\MetroMap\\PruebaAPI\\plantillas\\dicapi.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"diccionario": diccionario})
    documeto = template.render(contexto)
    return HttpResponse(documeto)