from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.
from .forms import UserCreationForm

class CustomUserAdmin(UserAdmin):
   add_form = UserCreationForm

   list_display = ('username', 'email', 'is_active', 'last_login')
   list_filter = ('username', 'email', 'last_login')
   fieldsets = (
      (None, {'fields': ('username', 'email', 'password')}),
      ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
      ('Important Dates', {'fields': ('last_login',)}),
   )

   add_fieldsets = (
      (None, {'fields': ('username', 'email', 'password1', 'password2')},
      ),
   )

   search_fields = ('username', 'email')
   ordering = ('username', 'email')
   filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(get_user_model(), CustomUserAdmin)