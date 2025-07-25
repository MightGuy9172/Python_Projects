import  requests
from datetime import datetime
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

#Yours key and authentication
API_KEY=os.environ['APP_KEY']
APP_ID=os.environ['APP_ID']
SHEET_KEY=os.environ['SHEET']
USERNAME=os.environ['MY_USER']
PASS=os.environ['PASS']

exercises_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint=f"https://api.sheety.co/{SHEET_KEY}/workoutTracking/workouts"

weight=52
height=174.6
age=22

headers={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters={
    "query":input("Tell me which exercises you did? : "),
    "weight_kg":weight,
    "height_cm":height,
    "age":age,
}

exercise_response=requests.post(url=exercises_endpoint,json=parameters,headers=headers)
exercise_data=exercise_response.json()


today=datetime.now()
for exercise in exercise_data["exercises"]:
    exercise_data={
        "workout":{
            "date":today.strftime("%d/%m/%Y"),
            "time":today.strftime("%H:%M:%S"),
            "exercise":exercise["name"],
            "duration":int(exercise["duration_min"]),
            "calories":int(exercise["nf_calories"]),
        }
    }

    response=sheet_response=requests.post(url=sheet_endpoint,json=exercise_data,auth=HTTPBasicAuth(USERNAME,PASS))
