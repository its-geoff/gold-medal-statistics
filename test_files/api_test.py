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

# testing response speed
start = datetime.now()
for i in range(1, 11):
   conn.request("GET", f"/marks/men/{i}", headers=headers)

   res = conn.getresponse()
   data = res.read()

   response = json.loads(data)

   print(response["100m"])
print(datetime.now() - start)