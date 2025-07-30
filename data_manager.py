import requests
from requests.auth import HTTPBasicAuth

url = "https://api.sheety.co/3940a86f6267132b315c846d8052c3e5/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = ""
        self.password = ""
        self.auth = HTTPBasicAuth(self.username,self.password)
        self.destination = {}

    def get_destination(self):
        reply = requests.get(url=url, auth=self.auth)
        self.destination = reply.json()["prices"]
        return self.destination

    def update_destination(self):
        for city in self.destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{url}/{city['id']}",
                json=new_data,
                auth=self.auth
            )
            print(response.text)