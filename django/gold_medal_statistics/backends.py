from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

class CustomBackend(BaseBackend):
   """
   Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

   Use the login name and a hash of the password.
   """

   def authenticate(self, request, username=None, password=None):
      try:
         user = get_user_model().objects.using("users").get(username = username)
         print("username found")
         if user.check_password(password) is True:
            return user
      except get_user_model().DoesNotExist:
         return None


   def get_user(self, user_id):
      try:
         return get_user_model().objects.using("users").get(pk=user_id)
      except get_user_model().DoesNotExist:
         return None