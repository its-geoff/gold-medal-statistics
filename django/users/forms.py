from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

# Create your forms here.
class UserCreationForm(forms.ModelForm):
   password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

   class Meta:
      model = get_user_model()
      fields = ['email', 'username']

   def clean_password(self):
      password1 = self.cleaned_data.get('password1')
      password2 = self.cleaned_data.get('password2')
      if password1 and password2 and password1 != password2:
         raise forms.ValidationError("passwords do not match")
      return password2

   def save(self, commit=True):
      user = super(UserCreationForm, self).save(commit=False)
      user.set_password(self.cleaned_data['password1'])

      if commit:
         user.save(using="users")
      return user



class UserLoginForm(forms.Form):
   query = forms.CharField(label='Username or Email')
   password = forms.CharField(label='Password',widget=forms.PasswordInput)

   def clean(self, *args, **kwargs):
      query = self.cleaned_data.get('query')
      password = self.cleaned_data.get('password')

      user_qs_final = get_user_model().objects.filter(
               Q(username__iexact=query) |
               Q(email__iexact=query).distinct() 

         )
      if not user_qs_final.exists() and user_qs_final.count() != 1:
         raise forms.ValidationError('Invalid credentials = user does not exist')

      user_obj = user_qs_final.first()
      if not user_obj.check_password(password):
         raise forms.ValidationError(' password is not correct')

      self.cleaned_data["user_obj"] = user_obj
      return super(UserLoginForm, self).clean(*args, **kwargs)