class FlightData:

    def __init__(self, price, origin_airport, destination_airport, depart_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.depart_date = depart_date
        self.return_date = return_date

def find_flight(data):
    flight_comp = data['data'][0]
    lowest_price = float(flight_comp['price']['grandTotal'])
    origin = flight_comp['itineraries'][0]['segments'][0]['departure']['iataCode']
    destination = flight_comp['itineraries'][0]['segments'][0]['arrival']['iataCode']
    depart_date = flight_comp['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
    return_date = flight_comp['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
    cheapest_flight = FlightData(lowest_price, origin, destination, depart_date, return_date)

    for flight in data['data']:
        price = float(flight['price']['grandTotal'])
        if price < lowest_price:
            lowest_price = price
            origin = flight['itineraries'][0]['segments'][0]['departure']['iataCode']
            destination = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
            depart_date = flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            return_date = flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, depart_date, return_date)

    return cheapest_flight
