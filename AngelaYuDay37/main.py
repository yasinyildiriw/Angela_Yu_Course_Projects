import requests
from datetime import datetime

today = datetime.now()

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
#
# response = requests.post(url=pixela_endpoint,json=user_parameters)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Running Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

quantity = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many kilometers did you run today? "),
}

response = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}",json=quantity,headers=headers)
print(response.text)

# response = requests.put(url=f"{graph_endpoint}/{GRAPH_ID}/{today.strftime("%Y%m%d")}",json=quantity,headers=headers)
# print(response.text)

# response = requests.delete(url=f"{graph_endpoint}/{GRAPH_ID}/{today.strftime("%Y%m%d")}", headers=headers)
# print(response.text)
