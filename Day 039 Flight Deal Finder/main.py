'''
The purpose of this project is to act as a capstone for the "Intermediate" section of the 100 Days of Code course on Udemy.
This project focuses on the use of APIs for several different resources, and integrates them into seperate files/classes
that are used by the main.py. This program is intended to be set as a script to run daily to check for flight deals for
the user based on information then enter on a Google Sheet worksheet.
'''

from flight_data import find_flight
import flight_search
import notification_manager
import data_manager
from datetime import datetime, timedelta

data_manager = data_manager.DataManager()
data = data_manager.get_dest_max_price()
flight_search = flight_search.FlightSearch()
notification_manager = notification_manager.NotificationManager()

origin_airport = 'AUS'

for row in data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_iata_code(row['city'])

data_manager.destination_data = data
data_manager.update_destination_codes()

start_date = datetime.today() + timedelta(days=1)
end_date = datetime.today() + timedelta(days=180)

for destination in data:
    flights = flight_search.flight_checker(origin_airport, destination['iataCode'], from_date=start_date, to_date=end_date)
    cheapest_flight = find_flight(flights)
    print(cheapest_flight.price, cheapest_flight.destination_airport)
    if cheapest_flight.price < destination['lowestPrice']:
        print(f'Lowest price found to fly from {origin_airport} to {cheapest_flight.destination_airport}, '
                         f'from {cheapest_flight.depart_date} to {cheapest_flight.return_date}. '
                         f'Only {cheapest_flight.price}!')
        notification_manager.send_text(
            message_body=f'Lowest price found to fly from {origin_airport} to {cheapest_flight.destination_airport}, '
                         f'from {cheapest_flight.depart_date} to {cheapest_flight.return_date}. '
                         f'Only {cheapest_flight.price}!')

