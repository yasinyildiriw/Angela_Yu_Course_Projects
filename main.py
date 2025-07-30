import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import notification_manager


flight_search = FlightSearch()
data_manager = DataManager()

sheet_data = data_manager.get_destination()

FROM_CITY_IATA = "IST"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = FlightSearch.get_destination_code(row["city"])
        time.sleep(2)

print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(FROM_CITY_IATA,destination["iataCode"],from_time=tomorrow,to_time=six_month_from_today)
    cheapest_flight = FlightData.find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")

        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")