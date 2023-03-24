from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HolaMundo(request):
    return HttpResponse("Hola Embed")