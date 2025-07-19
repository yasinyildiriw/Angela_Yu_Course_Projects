import os
import requests
from twilio.rest import Client

api_key = ""
MY_LAT = 36.642694
MY_LON = 29.142773

account_sid = ""
auth_token = ""

city_coor = {
    "lat" : MY_LAT,
    "lon" : MY_LON,
    "appid" : api_key,
    "cnt" : 4,
}
will_rain = False

response =requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast",params=city_coor)
response.raise_for_status()
data = response.json()
# i=0
# while i<4:
#     weather = data["list"][i]["weather"][0]["id"]
#     i += 1
#     if weather < 700:
#         print("bring an umbrella")
for hour_data in data["list"]:
    condition = hour_data["weather"][0]["id"]
    if condition < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
    .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="",#if you want to use by sms delete whatsapp:
        to = "",
    )
    print(message.status)