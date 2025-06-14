#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
import time
from flight_data import find_cheapest_flight

data_manager=DataManager()
sheet_data=data_manager.get_data()

search=FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "DEL"

# ==================== Retrieve your customer emails ====================

customer_data = data_manager.get_customer_emails()
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]
# print(f"Your email list includes {customer_email_list}")

if sheet_data[0]['iataCode']=="":
    for row in sheet_data:
        row["iataCode"]=search.get_iata(row["city"])

    data_manager.sheet=sheet_data
    data_manager.put_data()

# ==================== Search for Flights and Send Notifications ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination}")
    flights = search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")

        # ==================== Send Notifications and Emails  ====================

        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            if cheapest_flight.stops == 0:
                message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct " \
                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            else:
                message = f"Low price alert! Only GBP {cheapest_flight.price} to fly " \
                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                          f"with {cheapest_flight.stops} stop(s) " \
                          f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

            print(f"Check your email. Lower price flight found to {destination['city']}!")
            notification_manager.send_whatsapp(message_body=message)
            notification_manager.send_emails(email_list=customer_email_list, email_body=message)