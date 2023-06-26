from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Mark, Athlete
from app_logic import binary_search, gender_validation, check_for_athlete, update_personal_record

# Create your views here.
def home(request):
   page = "home"
   template = loader.get_template('gms/home.html')
   return render(request, 'gms/home.html', {'page': page})

def about(request):
   page = "about"
   template = loader.get_template('gms/about.html')
   return render(request, 'gms/about.html', {'page': page})

def scores(request):
   page = "scores"
   leaderboard = Mark.objects.order_by('-points')
   template = loader.get_template('gms/scores.html')
   context = {
      'leaderboard': leaderboard,
   }
   
   return render(request, 'gms/scores.html', {'leaderboard': leaderboard, 'page': page})

# saves correct point value
# try to run every time a new entry is made?
def new_entry(request):
   # pulls data from new_entry template using id to use in python code
   name = request.POST['name']
   gender = gender_validation(request.POST['gender'])
   team = request.POST['team']
   event = request.POST['event'].lower()
   mark = float(request.POST['mark'])
   if check_for_athlete(name, gender, team):
      athlete = Athlete.objects.get(name = name)
   else:
      athlete = Athlete.create(name, gender, team)
      athlete.save()
   entry = Mark.create(name, gender, team, event, mark)
   entry.save()
   leaderboard = Mark.objects.order_by('-points')
   try:
      entry.points = binary_search(entry.gender, entry.event, entry.mark)
   except (KeyError, Mark.DoesNotExist):
      render(request, 'gms/new_entry.html', {
            'leaderboard': leaderboard,
            'error_message': "Unable to retrieve the requested mark.",
        })
   else:
      athlete.save()
      entry.save()
   return HttpResponseRedirect(reverse('gms:scores'))

def stats(request):
   page = "stats"
   men_list = Athlete.objects.filter(gender = "men")
   women_list = Athlete.objects.filter(gender = "women")
   template = loader.get_template('gms/stats.html')
   context = {
      'men_list': men_list,
      'women_list': women_list,
   }

   return render(request, 'gms/stats.html', {'men_list': men_list, 'women_list':
                 women_list, 'page': page})

def men(request):
   page = "men"
   men_list = Athlete.objects.filter(gender = "men")
   template = loader.get_template('gms/men.html')
   context = {
      'men_list': men_list,
   }

   return render(request, 'gms/men.html', {'men_list': men_list, 'page': page})

def women(request):
   page = "women"
   women_list = Athlete.objects.filter(gender = "women")
   template = loader.get_template('gms/women.html')
   context = {
      'women_list': women_list,
   }

   return render(request, 'gms/women.html', {'women_list': women_list, 'page': page})

def men_profile(request, name):
   page = "men"
   title = name
   men_list = Athlete.objects.filter(gender = "men")
   athlete = Athlete.objects.get(name = name)
   template = loader.get_template('gms/men_profile.html')
   context = {
      'men_list': men_list,
      'athlete': athlete,
      'title': title,
   }

   return render(request, 'gms/men_profile.html', {'men_list': men_list, 'athlete': athlete, 
                 'title': title, 'page': page})

def women_profile(request, name):
   page = "women"
   title = name
   women_list = Athlete.objects.filter(gender = "women")
   athlete = Athlete.objects.get(name = name)
   template = loader.get_template('gms/women_profile.html')
   context = {
      'women_list': women_list,
      'athlete': athlete,
      'title': title,
   }

   return render(request, 'gms/women_profile.html', {'women_list': women_list, 
                 'athlete': athlete, 'title': title, 'page': page})