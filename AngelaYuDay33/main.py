import requests
from datetime import datetime
import smtplib

EMAIL = ""
PASSWORD = ""

MY_LAT = 36.627046
MY_LONG = 29.125875
parameters = {
    "lat":MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]
    iss_latitude = float(data["latitude"])
    iss_longitude = float(data["longitude"])
    if MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
def is_it_night():
    respond = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    respond.raise_for_status()
    veri = respond.json()
    sunrise_hour = int(veri["results"]["sunrise"].split("T")[1].split(":")[0]) + 3 # Cause Türkiye inside GMT+3
    sunset_hour = int(veri["results"]["sunset"].split("T")[1].split(":")[0]) + 3 # Cause Türkiye inside GMT+3
    print(f"Sunrise Hour : {sunrise_hour}\nSunset Hour : {sunset_hour}")

    now = datetime.now()
    if now.hour > sunset_hour or now.hour < sunrise_hour:
        return True
while True:
    if iss_close() and is_it_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )