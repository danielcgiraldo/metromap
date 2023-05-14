from api.models import User
from django.http import JsonResponse
import secrets

class UserCredentials:
    def __init__(self, email, allowed_domains = None):
        self.email = email
        self.allowed_domains = allowed_domains
    
    def set(self):
        """
        If the email has existing credentials associated with it, update those credentials.
        Otherwise, create new credentials for the given email.

        Parameters:
            email

        Returns:
            New credentials
        """
        # Search for a user with the given email
        user = User.objects.filter(email=self.email).first()

        # Check if the user was found
        if not user:
            # Generate new secret and public keys and update them
            secret, public = secrets.token_hex(10), secrets.token_hex(10)
            user = User(email= self.email, status = "1", credits = 70,
                        secret_key =  secret, public_key = public,
                        allowed_domains = "{}")
            user.save()
            # Return the new credentials
            return JsonResponse({'status': 'ok', 
                    'data': {'email': self.email, 'secret_key': secret, 'public_key': public}})
        
        # If user was not found, return error
        else:
            return JsonResponse({'status': 'error', 'error': 'not_found', 'description': 'email '}, status=404)
        
    def get(self):
        """
        If the email has existing credentials associated with it, return those credentials.

        Parameters:
            email

        Returns:
            Credentials
        """
        # Search for a user with the given email
        user = User.objects.filter(email=self.email).first()

        # Check if the user was found
        if user:
            # Return the user's credentials
            return JsonResponse({'status': 'ok', 
                    'data': {'email': self.email, 'secret_key': user.secret_key, 'public_key': user.public_key}})
        # If user was not found, return error
        else:
            return JsonResponse({'status': 'error', 'error': 'not_found', 'description': 'email not found'}, status=404)
        

    def update(self):
        if self.allowed_domains != None:
            # Search for a user with the given email
            user = User.objects.filter(email=self.email).first()
            user.update(allowed_domains=self.allowed_domains)
            return JsonResponse({'status': 'ok', 
                    'message': {'domains changed successfully'}})
        else:
            return JsonResponse({'status': 'error', 'error': 'not_found', 'description': 'email not found'}, status=404)
