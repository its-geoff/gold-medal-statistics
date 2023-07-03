from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db import models

class UserManager(BaseUserManager):
   def create_user(self, email, username, password=None, **extra_fields):
      if not email:
         raise ValueError('The Email field must be set.')
      email = self.normalize_email(email)
      if not username:
         raise ValueError('The Username field must be set.')
      username = get_user_model().normalize_username(username)
      user = self.model(email=email, username=username, **extra_fields)
      user.set_password(password)
      user.save(using="users")
      return user

   def create_superuser(self, email, username, password=None, **extra_fields):
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(max_length = 80, unique=True)
   username = models.CharField(max_length = 30, unique=True)
   team = models.CharField(max_length = 50, default="admin")
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   is_superuser = models.BooleanField(default=False)

   objects = UserManager()

   def get_username_text(self):
      return self.username
   
   def get_username_text_upper(self):
      return self.username.upper()

   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = ['email']