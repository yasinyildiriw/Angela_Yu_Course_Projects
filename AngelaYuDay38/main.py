import requests
from datetime import datetime

AGE = 21
GENDER = "male"
WEIGHT = 79
HEIGHT = 178

APP_ID = "471c58e4"
X_API_KEY = "4098abe874ec34f92b1deb0d175976c9"

USERNAME = "yasin"
PASSWORD = "pqzjanljfnlasnfjsnj12"
TOKEN = "eWFzaW46cHF6amFubGpmbmxhc25manNuajEy"

endpoint = "https://trackapi.nutritionix.com"
sheet_endpoint = "https://api.sheety.co/3940a86f6267132b315c846d8052c3e5/myWorkouts/workouts"

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

exercise = input("Which exercises you did? : ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : X_API_KEY
}

parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
istek = requests.post(url=f"{endpoint}/v2/natural/exercise", json=parameters, headers=headers)
gelen = istek.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
print(gelen)
for exercise in gelen["exercises"]:
    sheet_input = {
        "workout" : {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # sheet_response = requests.post(url=sheet_endpoint, json=sheet_input) # no authentication
    # sheet_response = requests.post(url=sheet_endpoint,json=sheet_input,auth=(f"{USERNAME}",f"{PASSWORD}")) # basic authentication
    sheet_response = requests.post(url=sheet_endpoint,json=sheet_input,headers=bearer_headers) # bearer token authentication