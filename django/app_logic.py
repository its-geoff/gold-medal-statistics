import http.client
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from marks.models import Athlete

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

   print("Points: " + str(binary_search(gender, event, mark)))

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
      print(test, mark)
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
      print(test, mark)
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
      if input.lower() == "m":
         return "men"
      elif input.lower() == "w":
         return "women"
      else:
         return None
   
# checks if an athlete's page exists
def check_for_athlete(name, gender, team):
   # filters by name first to shorten number of loop iterations
   for athlete in Athlete.objects.filter(name = name):
      if athlete.gender.lower() == gender.lower() and athlete.team.lower() == team.lower():
         return True
      else:
         return False

# updates an athlete's PR if it's better than the previous one
def update_personal_record(athlete, mark):
   if check_for_athlete(athlete.name, athlete.gender, athlete.team):
      chosen_athlete = athlete
   else:
      chosen_athlete = Athlete.create(athlete.name, athlete.gender, athlete.team)
   chosen_athlete.save()
   if mark.event == "100m":
      if mark.points > chosen_athlete.one_points:
         chosen_athlete.one_mark = mark.mark
         chosen_athlete.one_points = mark.points
   elif mark.event == "200m":
      if mark.points > chosen_athlete.two_points:
         chosen_athlete.two_mark = mark.mark
         chosen_athlete.two_points = mark.points
   elif mark.event == "400m":
      if mark.points > chosen_athlete.four_points:
         chosen_athlete.four_mark = mark.mark
         chosen_athlete.four_points = mark.points
   elif mark.event == "100mh":
      if mark.points > chosen_athlete.one_h_points:
         chosen_athlete.one_h_mark = mark.mark
         chosen_athlete.one_h_points = mark.points
   elif mark.event == "110mh":
      if mark.points > chosen_athlete.one_h_points:
         chosen_athlete.one_h_mark = mark.mark
         chosen_athlete.one_h_points = mark.points
   elif mark.event == "400mh":
      if mark.points > chosen_athlete.four_h_points:
         chosen_athlete.four_h_mark = mark.mark
         chosen_athlete.four_h_points = mark.points
   elif mark.event == "4x100m":
      if mark.points > chosen_athlete.one_r_points:
         chosen_athlete.one_r_mark = mark.mark
         chosen_athlete.one_r_points = mark.points
   elif mark.event == "4x400m":
      if mark.points > chosen_athlete.four_r_points:
         chosen_athlete.four_r_mark = mark.mark
         chosen_athlete.four_r_points = mark.points
   elif mark.event == "800m":
      if mark.points > chosen_athlete.eight_points:
         chosen_athlete.eight_mark = mark.mark
         chosen_athlete.eight_points = mark.points
   elif mark.event == "1600m":
      if mark.points > chosen_athlete.sixteen_points:
         chosen_athlete.sixteen_mark = mark.mark
         chosen_athlete.sixteen_points = mark.points
   elif mark.event == "3200m":
      if mark.points > chosen_athlete.thirtytwo_points:
         chosen_athlete.thirtytwo_mark = mark.mark
         chosen_athlete.thirtytwo_points = mark.points    
   elif mark.event == "HJ":
      if mark.points > chosen_athlete.hj_points:
         chosen_athlete.hj_mark = mark.mark
         chosen_athlete.hj_points = mark.points    
   elif mark.event == "PV":
      if mark.points > chosen_athlete.pv_points:
         chosen_athlete.pv_mark = mark.mark
         chosen_athlete.pv_points = mark.points    
   elif mark.event == "LJ":
      if mark.points > chosen_athlete.lj_points:
         chosen_athlete.lj_mark = mark.mark
         chosen_athlete.lj_points = mark.points    
   elif mark.event == "TJ":
      if mark.points > chosen_athlete.tj_points:
         chosen_athlete.tj_mark = mark.mark
         chosen_athlete.tj_points = mark.points    
   chosen_athlete.save()
   return chosen_athlete