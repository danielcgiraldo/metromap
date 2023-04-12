from django.http import JsonResponse

def secret_authentication(fn, request, credits, params = []):
    """
    Checks whether a valid secret-key is received and, 
    if so, verifies whether the user has enough credits 
    to perform the requested action. If the user has 
    enough credits, the function subtracts the credits 
    consumed by the request from the user's credit balance.

    Parameters:
        fn (f)
            Function to execute after authentication
        secret (str)
            The secret-key received in request
        credits (double)
            The number of credits consumed by the specific 
            request

    Returns:
        Returns an error if the user does not have enough 
        credits or if the secret-key is incorrect. Otherwise, 
        it calls fn
    """
    # Get secret-key from headers
    secret = request.META.get("HTTP_SECRET_KEY")
    if (secret == None):
       return JsonResponse({'status':'error', 'error':'invalid_client_credentials', 'description':'secret_key not received',}, status=403)
    return fn(params)