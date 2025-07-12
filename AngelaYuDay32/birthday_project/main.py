##################### Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib

EMAIL = ""
PASSWORD = ""
# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
now = dt.datetime.now()
month = now.month
day = now.day
today = (month,day)
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
file_path = f"letter_{random.randint(1,3)}.txt"
data = pandas.read_csv("birthdays.csv")
dictionary = {(data_row["month"], data_row["day"]) : data_row for (index,data_row) in data.iterrows()}
if today in dictionary:
    birthday_person = dictionary[today]
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:HAPPY BIRTHDAY\n\n{content}"
        )
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



