import http.client
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from marks.models import Mark, Athlete
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

# loads environment variables
load_dotenv()

# connects to api host
conn = http.client.HTTPSConnection("scoring-tables-api.p.rapidapi.com")

headers = {
   'X-RapidAPI-Key': os.environ.get("API-TOKEN"),
   'X-RapidAPI-Host': os.environ.get("API-HOST")
   }

# prompts the user for input and executes the binary search function
# test function - used only for testing
def main():
   start = datetime.now()
   gender = input("Enter a gender to find marks for: ")
   event = input("Enter an event to find marks for: ")
   mark = float(input("Enter a mark to search for: "))

   print("Points: " + str(jt_binary_search(gender, event, mark)))

# runs a binary search on the data set - high to low marks (sprints/distance)
# removes half the data each time depending on the target's relationship to the 
# middle value
def sd_binary_search(gender, event, mark):
   low = 1
   high = 1400
   mid = 0

   while low <= high:
      mid = (low + high) // 2
      
      test = retrieve(gender, event, mid)
      while test == None:
         mid += 1
         test = retrieve(gender, event, mid)
      

      if test > mark:
         low = mid + 1
      elif test < mark:
         high = mid - 1
      else:
         return mid
   return mid - 1

# runs a binary search on the data set - low to high marks (jumps/throws)
# removes half the data each time depending on the target's relationship to the 
# middle value
def jt_binary_search(gender, event, mark):
   low = 1
   high = 1400
   mid = 0

   while low <= high:
      mid = (low + high) // 2
      
      test = retrieve(gender, event, mid)
      while test == None:
         mid += 1
         test = retrieve(gender, event, mid)
      

      if test < mark:
         low = mid + 1
      elif test > mark:
         high = mid - 1
      else:
         return mid
   return mid - 1

# retrieves the desired mark from the Scoring Tables API
def retrieve(gender, event, num):
   conn.request("GET", f"/marks/{gender}/{num}", headers=headers)

   res = conn.getresponse()
   data = res.read()

   response = json.loads(data)
   return response[event]

# validates the gender input for the API
def gender_validation(input):
   if input.lower() == "men" or input.lower() == "women":
      return input.lower()
   else:
      if input.lower() == "m" or input.lower() == "male":
         return "men"
      elif input.lower() == "w" or input.lower() == "f" or input.lower() == "female":
         return "women"
      else:
         return None

# allows different abbreviations to work for event input
def choose_event(event):
   if event == "100" or event == "100m":
      event_out = "100m"
   elif event == "200" or event == "200m":
      event_out = "200m"
   elif event == "400" or event == "400m":
      event_out = "400m"
   elif event == "800" or event == "800m":
      event_out = "800m"
   elif event == "1600" or event == "1600m":
      event_out = "1600m"
   elif event == "3200" or event == "3200m":
      event_out = "3200m"
   elif event == "100h" or event == "100mh":
      event_out = "100mH"
   elif event == "110h" or event == "110mh":
      event_out = "110mH"
   elif event == "4x1" or event == "4x100" or event == "4x100m":
      event_out = "4x100m"
   elif event == "4x4" or event == "4x400" or event == "4x400m":
      event_out = "4x400m"
   if event == "hj" or event == "high" or event == "high jump":
      event_out = "HJ"
   elif event == "pv" or event == "pole" or event == "vault" or event == "pole vault":
      event_out = "PV"
   elif event == "lj" or event == "long" or event == "long jump":
      event_out = "LJ"
   elif event == "tj" or event == "triple" or event == "triple jump":
      event_out = "TJ"
   elif event == "sp" or event == "shot" or event == "shot put":
      event_out = "SP"
   elif event == "dt" or event == "discus" or event == "discus throw":
      event_out = "DT"
   return event_out

# checks if an athlete's page exists
def check_for_athlete(name, gender, team, user):
   # filters by name first to shorten number of loop iterations
   for athlete in Athlete.objects.filter(name = name, user = user):
      if athlete.gender.lower() == gender.lower() and athlete.team.lower() == team.lower():
         return True
      else:
         return False

# checks entered marks to set an athlete's grade
def set_grade(user, athlete):
   for count in Mark.objects.using("marks").filter(user = user, name = athlete.name):
      max_grade = 0
      if count.grade > max_grade:
         max_grade = count.grade
   athlete.grade = max_grade
   athlete.save(using="marks")

# updates an athlete's PR if it's better than the previous one
def update_personal_record(athlete, mark):
   if int(athlete.grade) != int(mark.grade):
      athlete.grade = max(int(athlete.grade), int(mark.grade))
   athlete.save(using="marks")
   if mark.event == "100m":
      if mark.points > athlete.one_points:
         athlete.one_mark = mark.mark
         athlete.one_points = mark.points
   elif mark.event == "200m":
      if mark.points > athlete.two_points:
         athlete.two_mark = mark.mark
         athlete.two_points = mark.points
   elif mark.event == "400m":
      if mark.points > athlete.four_points:
         athlete.four_mark = mark.mark
         athlete.four_points = mark.points
   elif mark.event == "100mh":
      if mark.points > athlete.one_h_points:
         athlete.one_h_mark = mark.mark
         athlete.one_h_points = mark.points
   elif mark.event == "110mh":
      if mark.points > athlete.one_h_points:
         athlete.one_h_mark = mark.mark
         athlete.one_h_points = mark.points
   elif mark.event == "400mh":
      if mark.points > athlete.four_h_points:
         athlete.four_h_mark = mark.mark
         athlete.four_h_points = mark.points
   elif mark.event == "4x100m":
      if mark.points > athlete.one_r_points:
         athlete.one_r_mark = mark.mark
         athlete.one_r_points = mark.points
   elif mark.event == "4x400m":
      if mark.points > athlete.four_r_points:
         athlete.four_r_mark = mark.mark
         athlete.four_r_points = mark.points
   elif mark.event == "800m":
      if mark.points > athlete.eight_points:
         athlete.eight_mark = mark.mark
         athlete.eight_points = mark.points
   elif mark.event == "1600m":
      if mark.points > athlete.sixteen_points:
         athlete.sixteen_mark = mark.mark
         athlete.sixteen_points = mark.points
   elif mark.event == "3200m":
      if mark.points > athlete.thirtytwo_points:
         athlete.thirtytwo_mark = mark.mark
         athlete.thirtytwo_points = mark.points    
   elif mark.event == "HJ":
      if mark.points > athlete.hj_points:
         athlete.hj_mark = mark.mark
         athlete.hj_points = mark.points    
   elif mark.event == "PV":
      if mark.points > athlete.pv_points:
         athlete.pv_mark = mark.mark
         athlete.pv_points = mark.points    
   elif mark.event == "LJ":
      if mark.points > athlete.lj_points:
         athlete.lj_mark = mark.mark
         athlete.lj_points = mark.points    
   elif mark.event == "TJ":
      if mark.points > athlete.tj_points:
         athlete.tj_mark = mark.mark
         athlete.tj_points = mark.points
   elif mark.event == "SP":
      if mark.points > athlete.sp_points:
         athlete.sp_mark = mark.mark
         athlete.sp_points = mark.points
   elif mark.event == "DT":
      if mark.points > athlete.dt_points:
         athlete.dt_mark = mark.mark
         athlete.dt_points = mark.points      
   athlete.save(using="marks")

# applies changes made to the mark given by the index
def apply_edit(request, index):
   user = request.user.username
   entry = Mark.objects.using("marks").filter(user = user).order_by('-points')[index]

   old_name = entry.name
   name = request.POST['name']
   old_gender = entry.gender
   gender = gender_validation(request.POST['gender'])
   old_team = entry.team
   team = request.POST['team']
   old_event = entry.event
   event = request.POST['event'].lower()
   old_mark = entry.mark
   mark = float(request.POST['mark'])

   athlete = Athlete.objects.using("marks").get(user = user, name = name)
   
   # compares old values to edited values to identify changes
   if old_name != name:
      entry.name = name
   elif old_gender != gender:
      entry.gender = gender
   elif old_team != team:
      entry.team = team
   elif old_event != event:
      entry.event = event
      if event == "HJ" or event == "PV" or event == "LJ" or event == "TJ" \
      or event == "SP" or event == "DT":
         entry.points = jt_binary_search(entry.gender, entry.event, entry.mark)
      else:
         entry.points = sd_binary_search(entry.gender, entry.event, entry.mark)
      update_personal_record(athlete, entry)
   elif old_mark != mark:
      entry.mark = mark
      if event == "HJ" or event == "PV" or event == "LJ" or event == "TJ" \
      or event == "SP" or event == "DT":
         entry.points = jt_binary_search(entry.gender, entry.event, entry.mark)
      else:
         entry.points = sd_binary_search(entry.gender, entry.event, entry.mark)
      update_personal_record(athlete, entry)

   entry.save(using="marks")

# validates username
def username_validation(username):
   try:
      if get_user_model().objects.using("users").get(username = username) != get_user_model().DoesNotExist:
         return True
   except ObjectDoesNotExist:
      return False

# validates email
def email_validation(email):
   try:
      if get_user_model().objects.using("users").get(email = email) != get_user_model().DoesNotExist:
         return True
   except ObjectDoesNotExist:
      return False
   
# validates password
def password_validation(password, confirm):
   if password and confirm and password != confirm:
      return True
   else:
      return False