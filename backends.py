# home/backends.py
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # username here is actually email
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
