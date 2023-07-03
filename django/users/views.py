from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from app_logic import user_validation

# Create your views here.
def navbar(request):
   return render(request, 'accts/signup.html', {'user': request.user})

def signup(request):
   page = "signup"
   if request.method == "POST":
      email = request.POST['email']
      username = request.POST['username']
      password = request.POST['password']
      result = user_validation(username)
      if result == "dupe_username":
         return render(request, 'accts/signup.html', {'page': page, 'dupe_username': True})
      else:
         user = get_user_model().objects.create_user(email, username, password)
      user.save(using="users")
      auth_login(request, user)
      return HttpResponseRedirect(reverse('gms:home'))
   else:
      return render(request, 'accts/signup.html', {'page': page})

def login(request):
   page = "login"
   if request.user.is_authenticated:
      return redirect(reverse('gms:home'))
   else:
      if request.method == 'POST':
         form = AuthenticationForm(request, data=request.POST)
         if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
               auth_login(request, user)
               return redirect('gms:home')
         else:
            form = AuthenticationForm()
            return render(request, 'accts/login.html', {'page': page, 'incorrect': True})
   return render(request, 'accts/login.html', {'page': page})

def logout(request):
   page = "logout"
   auth_logout(request)
   print("logged out")
   return render(request, 'accts/logout.html', {'page': page})

def password_change(request):
   page = "password_change"
   return render(request, 'accts/password_change.html', {'page': page})

def password_change_done(request):
   page = "password_change_done"
   return render(request, 'accts/password_change_done.html', {'page': page})

def password_reset(request):
   page = "password_reset"
   return render(request, 'accts/password_reset.html', {'page': page})

def password_reset_done(request):
   page = "password_reset_done"
   return render(request, 'accts/password_reset_done.html', {'page': page})

def password_reset_confirm(request):
   page = "password_reset_confirm"
   return render(request, 'accts/password_reset_confirm.html', {'page': page})

def password_reset_complete(request):
   page = "password_reset_complete"
   return render(request, 'accts/password_reset_complete.html', {'page': page})

def profile(request, username):
   page = "profile"
   title = username
   context = {
      'title': title,
      'page': page,
   }
   return render(request, 'accts/profile.html', context)