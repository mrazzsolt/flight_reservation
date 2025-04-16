class Booking:
    def __init__(self, flight, passenger_name, date):
        self._flight = flight
        self._passenger_name = passenger_name
        self._date = date

    @property
    def flight(self):
        return self._flight

    @property
    def passenger_name(self):
        return self._passenger_name

    @property
    def date(self):
        return self._date

    def cancel(self):
        self._flight.cancel_seat()

    def __str__(self):
        return f"{self._passenger_name} sikeresen foglalt egy jegyet a(z) {self._flight.flight_number} számú járatra ({self._date}) - Ár: {self._flight.price} Ft"
