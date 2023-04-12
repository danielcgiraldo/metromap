from django.http import JsonResponse

def get_status(request):
    # checks if secret key credentials are in the header
    sk = request.META.get("HTTP_SECRET_KEY")
    if (sk == None):
       return JsonResponse({'status':'error', 'error':'invalid_client_credentials', 'description':'secret_key not received',}, status=403)
    return JsonResponse({'status':'error', 'error':'under_maintenance','message':'Map in under maintenace'})