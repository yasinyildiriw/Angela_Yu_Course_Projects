import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : ""
}
news_parameters = {
    "q" : STOCK_NAME,
    "sortBy" : "popularity",
    "apiKey" : ""
}

response = requests.get(url=f"{STOCK_ENDPOINT}",params=stock_parameters)
response.raise_for_status()
data = response.json()
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]

yesterday_s_closing_price = yesterday_data["4. close"]
yesterday_s_closing_price = float(yesterday_s_closing_price)

the_day_before_yesterday_s = data_list[1]["4. close"]
the_day_before_yesterday_s = float(the_day_before_yesterday_s)

difference = yesterday_s_closing_price-the_day_before_yesterday_s
percent = difference/the_day_before_yesterday_s
percent_abs = abs(percent)

articles = []



client = Client(account_sid, auth_token)
if percent_abs*100 > 5:
    report = requests.get(url=f"{NEWS_ENDPOINT}",params=news_parameters)
    report.raise_for_status()
    veri = report.json()["articles"]
    articles = veri[:3]
    mesaj = [f"Headline : {article['title']}.\Brief : {article['description']}" for article in articles]
    if percent > 0:
        yukselis = "🔺"

        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {int(yukselis)}{percent_abs}%\n{mesaj}",
            from_="whatsapp:",
            to="whatsapp:",
        )
        print(message.status)
    else:
        dusus = "🔻"

        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {int(dusus)}{percent_abs}%\n{mesaj}",
            from_="whatsapp:",
            to="whatsapp:",
        )
        print(message.status)