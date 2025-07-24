import requests
from datetime import datetime

AGE = 21
GENDER = "male"
WEIGHT = 79
HEIGHT = 178

APP_ID = ""
X_API_KEY = ""

USERNAME = ""
PASSWORD = ""
TOKEN = ""

endpoint = "https://trackapi.nutritionix.com"
sheet_endpoint = "https://api.sheety.co"

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
