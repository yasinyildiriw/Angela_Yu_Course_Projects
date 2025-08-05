from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
MAIL = os.getenv("MAIL")
PASSWORD = os.getenv("PASSWORD")

url = "https://www.amazon.com/dp/B09MCVP94B/ref=sspa_dk_detail_1?sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw"
headers = {
    "Accept-Language": "en-US,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=headers)
data = response.text

soup = BeautifulSoup(data,"html.parser")
price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")
price_str = price_whole.text + price_fraction.text
price = float(price_str)

product = soup.find(name="span", class_="a-size-large product-title-word-break").text

message = f"Subject:Amazon Price Alert! \n\n Your {product} is {price}$ now. Don't miss this chance {url}"
if price < 100:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MAIL, password=PASSWORD)
    connection.sendmail(
        from_addr = MAIL,
        to_addrs = MAIL,
        msg = message.encode("utf-8")
    )
