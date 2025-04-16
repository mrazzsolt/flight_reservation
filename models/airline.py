class Airline:
    def __init__(self, airline_name):
        self._airline_name = airline_name
        self._flights = []

    @property
    def name(self):
        return self._airline_name

    def add_flight(self, flight):
        self._flights.append(flight)

    def get_flight(self, flight_number):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                return flight
        return None

    def get_all_flights(self):
        return self._flights
