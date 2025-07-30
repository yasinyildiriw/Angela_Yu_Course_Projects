import requests
from requests.auth import HTTPBasicAuth

class DataManager:

    def __init__(self):

        self._user = ""
        self._password = ""
        self.prices_endpoint = "https://api.sheety.co/3940a86f6267132b315c846d8052c3e5/flightDeals/prices"
        self.users_endpoint = "https://api.sheety.co/3940a86f6267132b315c846d8052c3e5/flightDeals/responses"
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination(self):
        reply = requests.get(url=self.prices_endpoint, auth=self.auth)
        self.destination = reply.json()["prices"]
        return self.destination

    def update_destination(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

