from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# Creamos la vista 'tweets'
def map(request):
    # Check if public_key is in url
    key = request.GET.get('public-key', '')
    if(key == ""):
        return JsonResponse({"status":"error", "error": "invalid_client_credentials", "description": "public-key not received"}, status=403)
    return JsonResponse({"status":"error", "error": "under_maintenance", "message": "Map is under maintenance"})
    