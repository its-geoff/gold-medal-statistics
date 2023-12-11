from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Mark, Athlete
from app_logic import sd_binary_search, jt_binary_search, gender_validation, \
   choose_event, check_for_athlete, set_grade, update_personal_record
from conversions import min_to_sec

# used for edit function
overlay = False

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
   for counter in Mark.objects.using("marks").filter(user = user):
      mark = Mark.objects.using("marks").get(user = user, id = counter.id)
      if mark.points == 0:
         mark.delete(using = "marks")
   if Athlete.objects.using("marks").filter(user = user).count() > 0:
      for counter in Athlete.objects.using("marks").filter(user = user):
         athlete = Athlete.objects.using("marks").get(user = user, name = counter.name)
         if Mark.objects.using("marks").filter(user = user, name = counter.name).count() == 0:
            athlete.delete(using = "marks")
         else:
            set_grade(user, athlete)
   leaderboard = Mark.objects.using("marks").filter(user = user).order_by('-points')
   context = {
      'leaderboard': leaderboard,
      'page': page,
   }
   
   return render(request, 'gms/scores.html', context)

# saves correct point value and entry
@login_required
def new_entry(request):
   user = request.user.username
   # request.POST - pulls data from new_entry template using id to use in python code
   name = request.POST['name']
   # gender validation
   gender = gender_validation(request.POST['gender'])
   if gender == "none":
      leaderboard = Mark.objects.using("marks").filter(user = user).order_by('-points')
      return render(request, 'gms/scores.html', {
         'page': "scores",
         'leaderboard': leaderboard,
         'gender_error_message': "Please enter a valid gender.",
      })
   grade = int(request.POST['grade'])
   if grade < 9 or grade > 12:
      leaderboard = Mark.objects.using("marks").filter(user = user).order_by('-points')
      return render(request, 'gms/scores.html', {
         'page': "scores",
         'leaderboard': leaderboard,
         'grade_error_message': "Please enter a grade from 9-12.",
      })
   team = request.POST['team']
   # event validation
   event_in = request.POST['event'].lower()
   event = choose_event(event_in)
   if event == "none":
      leaderboard = Mark.objects.using("marks").filter(user = user).order_by('-points')
      return render(request, 'gms/scores.html', {
         'page': "scores",
         'leaderboard': leaderboard,
         'event_error_message': "Please enter a valid event.",
      })
   # mark validation
   mark_in = request.POST['mark']
   try:
      if mark_in.find(":") != -1:
         mark = min_to_sec(mark_in)
      else:
         mark = float(mark_in)
   except ValueError:
      leaderboard = Mark.objects.using("marks").filter(user = user).order_by('-points')
      return render(request, 'gms/scores.html', {
         'page': "scores",
         'leaderboard': leaderboard,
         'mark_error_message': "Please enter a valid mark.",
      })
   if check_for_athlete(name, gender, team, user):
      athlete = Athlete.objects.using("marks").get(user = user, name = name)
   else:
      athlete = Athlete.create(name, gender, grade, team, user)
      athlete.save(using="marks")
   entry = Mark.create(name, gender, grade, team, event, mark, user)
   entry.save(using="marks")
   leaderboard = Mark.objects.using("marks").filter(user = user).order_by('-points')
   # points calculation and validation
   try:
      if event == "HJ" or event == "PV" or event == "LJ" or event == "TJ" \
      or event == "SP" or event == "DT":
         entry.points = jt_binary_search(entry.gender, entry.event, entry.mark)
      else:
         entry.points = sd_binary_search(entry.gender, entry.event, entry.mark)
   except (KeyError, Mark.DoesNotExist):
      render(request, 'gms/new_entry.html', {
            'leaderboard': leaderboard,
            'points_error_message': "Unable to retrieve the requested mark.",
        })
   # if successful, save athlete and entry
   else:
      update_personal_record(athlete, entry)
      athlete.save(using="marks")
      entry.save(using="marks")
   return HttpResponseRedirect(reverse('gms:scores'))

# allows the user to edit a mark with the given index
@login_required
def edit(request, index):
   global overlay
   overlay = not overlay

   if overlay:
      # confirm edit
      print("overlay")
   else:
      # configure overlay
      print("no overlay")
   
   return HttpResponseRedirect(reverse('gms:scores'))

# allows the user to delete a mark with the given index
@login_required
def delete(request, index):
   entry = Mark.objects.using("marks").filter(user = request.user.username).order_by('-points')[index]
   entry.delete(using="marks")

   return HttpResponseRedirect(reverse('gms:scores'))

@login_required
def stats(request):
   page = "stats"
   user = request.user.username
   men_list = Athlete.objects.using("marks").filter(user = user, gender = "men").order_by('name')
   context = {
      'men_list': men_list,
      'page': page,
   }

   return render(request, 'gms/stats.html', context)

@login_required
def men(request):
   page = "men"
   user = request.user.username
   men_list = Athlete.objects.using("marks").filter(user = user, gender = "men").order_by('name')
   context = {
      'men_list': men_list,
      'page': page,
   }

   return render(request, 'gms/men.html', context)

@login_required
def women(request):
   page = "women"
   user = request.user.username
   women_list = Athlete.objects.using("marks").filter(user = user, gender = "women").order_by('name')
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
   men_list = Athlete.objects.using("marks").filter(user = user, gender = "men").order_by('name')
   athlete = Athlete.objects.using("marks").get(user = user, name = name)

   if athlete.grade == 9:
      grade = "Freshman"
   elif athlete.grade == 10:
      grade = "Sophomore"
   elif athlete.grade == 11:
      grade = "Junior"
   elif athlete.grade == 12:
      grade = "Senior"
      
   context = {
      'men_list': men_list,
      'athlete': athlete,
      'grade': grade,
      'title': title,
      'page': page,
   }

   return render(request, 'gms/men_profile.html', context)

@login_required
def women_profile(request, name):
   page = "women"
   title = name
   user = request.user.username
   women_list = Athlete.objects.using("marks").filter(user = user, gender = "women").order_by('name')
   athlete = Athlete.objects.using("marks").get(user = user, name = name)

   if athlete.grade == 9:
      grade = "Freshman"
   elif athlete.grade == 10:
      grade = "Sophomore"
   elif athlete.grade == 11:
      grade = "Junior"
   elif athlete.grade == 12:
      grade = "Senior"

   context = {
      'women_list': women_list,
      'athlete': athlete,
      'grade': grade,
      'title': title,
      'page': page,
   }

   return render(request, 'gms/women_profile.html', context)