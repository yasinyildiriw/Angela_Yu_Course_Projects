import smtplib
import datetime as dt
from random import choice

my_email = ""
password = ""

now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt") as file:
        lines = file.readlines()
    mesaj = choice(lines)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                    to_addrs="",
                    msg=f"Subject:Motivation\n\n{mesaj}")