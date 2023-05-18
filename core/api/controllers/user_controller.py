from api.models import User
from django.http import JsonResponse
import secrets


class UserCredentials:
    def __init__(self, userID, allowed_domains=None):
        self.userID = userID
        self.allowed_domains = allowed_domains

    def set(self):
        """
        If the userID has existing credentials associated with it, update those credentials.
        Otherwise, create new credentials for the given userID.

        Parameters:
            userID

        Returns:
            New credentials
        """
        # Search for a user with the given userID
        user = User.objects.filter(id=self.userID).first()

        # Check if the user was found
        if not user:
            # Generate new secret and public keys and update them
            secret, public = secrets.token_hex(10), secrets.token_hex(10)
            user = User(id=self.userID, status="1", credits=70,
                        secret_key=secret, public_key=public,
                        paid=False, allowed_domains="[]")
            user.save()
            # Return the new credentials
            return JsonResponse({'status': 'ok',
                                 'data': {'userID': self.userID, 'secret_key': secret, 'public_key': public, 'allowed_domains': {}}})

        # If user was not found, return error
        else:
            return JsonResponse({'status': 'error', 'error': 'not_found', 'description': 'userID '}, status=404)

    def get(self):
        """
        If the userID has existing credentials associated with it, return those credentials.

        Parameters:
            userID

        Returns:
            Credentials
        """
        # Search for a user with the given userID
        user = User.objects.filter(id=self.userID).first()

        # Check if the user was found
        if user:
            # Return the user's credentials
            return JsonResponse({'status': 'ok',
                                 'data': {'userID': self.userID, 'secret_key': user.secret_key, 'public_key': user.public_key, 'allowed_domains': user.allowed_domains, 'credits': user.credits}})
        # If user was not found, return error
        else:
            return JsonResponse({'status': 'error', 'error': 'not_found', 'description': 'userID not found'}, status=404)

    def update(self):
        if self.allowed_domains is not None:
            # Search for a user with the given userID
            user = User.objects.filter(id=self.userID).first()
            
            if user:
                user.allowed_domains = self.allowed_domains
                user.save()
                
                return JsonResponse({'status': 'ok', 'message': 'Domains changed successfully'})
            else:
                return JsonResponse({'status': 'error', 'error': 'not_found', 'description': 'User not found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'error': 'bad_request', 'description': 'allowed_domains not provided'}, status=400)

