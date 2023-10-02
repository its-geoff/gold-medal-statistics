# expanded version of app_logic.py with extra print statements for testing

import http.client
import json
import os
from dotenv import load_dotenv
from datetime import datetime

# loads environment variables
load_dotenv()

# connects to api host
conn = http.client.HTTPSConnection("scoring-tables-api.p.rapidapi.com")

headers = {
   'X-RapidAPI-Key': os.environ.get("API-TOKEN"),
   'X-RapidAPI-Host': os.environ.get("API-HOST")
   }

# prompts the user for input and executes the binary search function
def main():
   start = datetime.now()
   gender = input("Enter a gender to find marks for: ")
   event = input("Enter an event to find marks for: ")
   time = float(input("Enter a time to search for: "))

   print(datetime.now() - start)

   bs_start = datetime.now()

   print("Points: " + str(binary_search(gender, event, time)))
   print(datetime.now() - bs_start)

# runs a binary search on the data set
# removes half the data each time depending on the target's relationship to the 
# middle value
def binary_search(gender, event, time):
   low = 1
   high = 1400
   mid = 0

   iterations = 0

   while low <= high:
      iterations += 1
      print(iterations)
      mid = (low + high) // 2
      print(low, mid, high)
      
      test = retrieve(gender, event, mid)
      while test == None:
         mid += 1
         test = retrieve(gender, event, mid)
      
      print(test, time)

      if test > time:
         low = mid + 1

      elif test < time:
         high = mid - 1
      else:
         return mid
   return mid - 1

# retrieves the desired time from the Scoring Tables API
def retrieve(gender, event, num):
   conn.request("GET", f"/marks/{gender}/{num}", headers=headers)

   res = conn.getresponse()
   data = res.read()

   response = json.loads(data)
   return response[event]

main()

"""
1
1 700 1400
11.67 11.5
700
2
700 1050 1400
10.47 11.5
3
700 874 1049
11.04 11.5
4
700 786 873
11.35 11.5
5
700 742 785
11.51 11.5
743
6
743 764 785
11.43 11.5
7
743 753 763
11.47 11.5
8
743 747 752
11.49 11.5
9
743 744 746
11.51 11.5
743
10
743 744 746
test  time
11.51 11.5
new low
743
11
743 744 746
11.51 11.5
743
"""