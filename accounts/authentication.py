from django.contrib.auth.backends import BaseBackend
from .models import User

class UserPhoneBackend(BaseBackend):
    def authenticate(self, request,backend=None, username=None, password=None):
        try:
            if username.isdigit():
                user = User.objects.get(phoneNumber=username)
            else:
                user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
