from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Mark, Athlete
from app_logic import sd_binary_search, jt_binary_search, gender_validation, check_for_athlete, update_personal_record

# Create your views here.
def home(request):
   page = "home"
   return render(request, 'gms/home.html', {'page': page})

def about(request):
   page = "about"
   return render(request, 'gms/about.html', {'page': page})

@login_required
def scores(request):
   page = "scores"
   user = request.user.username
   leaderboard = Mark.objects.using("marks").filter(user = user).order_by('-points')
   context = {
      'leaderboard': leaderboard,
      'page': page,
   }
   
   return render(request, 'gms/scores.html', context)

# saves correct point value
# try to run every time a new entry is made?
@login_required
def new_entry(request):
   # pulls data from new_entry template using id to use in python code
   name = request.POST['name']
   gender = gender_validation(request.POST['gender'])
   team = request.POST['team']
   event = request.POST['event'].lower()
   user = request.user.username
   # allows different abbreviations to work
   if event == "hj" or event == "high" or event == "high jump":
      event = "HJ"
   elif event == "pv" or event == "pole" or event == "vault" or event == "pole vault":
      event = "PV"
   elif event == "lj" or event == "long" or event == "long jump":
      event = "LJ"
   elif event == "tj" or event == "triple" or event == "triple jump":
      event = "TJ"
   elif event == "sp" or event == "shot" or event == "shot put":
      event = "SP"
   elif event == "dt" or event == "discus" or event == "discus throw":
      event = "DT"
   mark = float(request.POST['mark'])
   if check_for_athlete(name, gender, team):
      athlete = Athlete.objects.using("marks").get(user = user, name = name)
   else:
      athlete = Athlete.create(name, gender, team, user)
      athlete.save(using="marks")
   entry = Mark.create(name, gender, team, event, mark, user)
   entry.save(using="marks")
   leaderboard = Mark.objects.using("marks").filter(user = user).order_by('-points')
   try:
      if event == "HJ" or event == "PV" or event == "LJ" or event == "TJ" \
      or event == "SP" or event == "DT":
         entry.points = jt_binary_search(entry.gender, entry.event, entry.mark)
      else:
         entry.points = sd_binary_search(entry.gender, entry.event, entry.mark)
   except (KeyError, Mark.DoesNotExist):
      render(request, 'gms/new_entry.html', {
            'leaderboard': leaderboard,
            'error_message': "Unable to retrieve the requested mark.",
        })
   else:
      update_personal_record(athlete, entry)
      athlete.save(using="marks")
      entry.save(using="marks")
   return HttpResponseRedirect(reverse('gms:scores'))

@login_required
def delete(request, index):
   entry = Mark.objects.using("marks").filter(user = request.user.username).order_by('-points')[index]
   entry.delete(using="marks")

   return HttpResponseRedirect(reverse('gms:scores'))

@login_required
def stats(request):
   page = "stats"
   user = request.user.username
   men_list = Athlete.objects.using("marks").filter(user = user, gender = "men")
   women_list = Athlete.objects.using("marks").filter(user = user, gender = "women")
   context = {
      'men_list': men_list,
      'women_list': women_list,
      'page': page,
   }

   return render(request, 'gms/stats.html', context)

@login_required
def men(request):
   page = "men"
   user = request.user.username
   men_list = Athlete.objects.using("marks").filter(user = user, gender = "men")
   context = {
      'men_list': men_list,
      'page': page,
   }

   return render(request, 'gms/men.html', context)

@login_required
def women(request):
   page = "women"
   user = request.user.username
   women_list = Athlete.objects.using("marks").filter(user = user, gender = "women")
   context = {
      'women_list': women_list,
      'page': page,
   }

   return render(request, 'gms/women.html', context)

@login_required
def men_profile(request, name):
   page = "men"
   title = name
   user = request.user.username
   men_list = Athlete.objects.using("marks").filter(user = user, gender = "men")
   athlete = Athlete.objects.using("marks").get(user = user, name = name)
   context = {
      'men_list': men_list,
      'athlete': athlete,
      'title': title,
      'page': page,
   }

   return render(request, 'gms/men_profile.html', context)

@login_required
def women_profile(request, name):
   page = "women"
   title = name
   user = request.user.username
   women_list = Athlete.objects.using("marks").filter(user = user, gender = "women")
   athlete = Athlete.objects.using("marks").get(user = user, name = name)
   context = {
      'women_list': women_list,
      'athlete': athlete,
      'title': title,
      'page': page,
   }

   return render(request, 'gms/women_profile.html', context)