from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from app_logic import username_validation, email_validation, password_validation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from marks.models import Mark, Athlete
from .models import User
import datetime

# Create your views here.
def navbar(request):
   return render(request, 'accts/signup.html', {'user': request.user})

def signup(request):
   page = "signup"
   if request.method == "POST":
      email = request.POST['email']
      username = request.POST['username']
      password = request.POST['password']
      confirm = request.POST['confirm']
      username_result = username_validation(username)
      if username_result:
         return render(request, 'accts/signup.html', {'page': page, 'dupe_username': True})
      email_result = email_validation(email)
      if email_result:
         return render(request, 'accts/signup.html', {'page': page, 'dupe_email': True})
      password_result = password_validation(password, confirm)
      if password_result:
         return render(request, 'accts/signup.html', {'page': page, 'diff_pass': True})
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
      return HttpResponseRedirect(reverse('accts:profile', kwargs = {'username': request.user}))
   else:
      if request.method == 'POST':
         form = AuthenticationForm(request, data=request.POST)
         if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
               auth_login(request, user)
               return HttpResponseRedirect(reverse('gms:home'))
         else:
            form = AuthenticationForm()
            return render(request, 'accts/login.html', {'page': page, 'incorrect': True})
   return render(request, 'accts/login.html', {'page': page})

@login_required
def logout(request):
   page = "logout"   
   auth_logout(request)
   return render(request, 'accts/logout.html', {'page': page})

@login_required
def password_change(request):
   page = "password change"
   user = get_user_model().objects.get(username = request.user.username)
   if request.method == "POST":
      new_password = request.POST['new_password']
      confirm = request.POST['confirm_new']
      if password_validation(new_password, confirm):
         return render(request, 'accts/password_change.html', {'page': page, 'diff_pass': True})
      else:
         HttpResponseRedirect(reverse('accts:password_change_done'))
   return render(request, 'accts/password_change.html', {'page': page})
   

@login_required
def password_change_done(request):
   page = "password change done"
   return render(request, 'accts/password_change_done.html', {'page': page})

# def password_reset(request):
#    page = "login"
#    return render(request, 'accts/password_reset.html', {'page': page})

# def password_reset_done(request):
#    page = "login"
#    return render(request, 'accts/password_reset_done.html', {'page': page})

# def password_reset_confirm(request):
#    page = "login"
#    return render(request, 'accts/password_reset_confirm.html', {'page': page})

# def password_reset_complete(request):
#    page = "login"
#    return render(request, 'accts/password_reset_complete.html', {'page': page})

def profile(request, username):
   page = "profile"
   title = username
   num_marks = Mark.objects.using("marks").filter(user = username).count()
   num_athletes = Athlete.objects.using("marks").filter(user = username).count()
   last_login = User.objects.using("users").get(username = username).last_login
   eighthours = datetime.timedelta(hours=8)
   date = last_login - eighthours
   output_date = date.strftime('%m-%d-%Y')
   context = {
      'title': title,
      'num_marks': num_marks,
      'num_athletes': num_athletes,
      'last_login': output_date,
      'page': page,
   }
   return render(request, 'accts/profile.html', context)