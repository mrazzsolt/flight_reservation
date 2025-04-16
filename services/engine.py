from models.booking import Booking
from datetime import datetime

class BookingSystem:
    def __init__(self, airline):
        self._airline = airline
        self._bookings = []
        self._departures = []

    def load_bookings(self, bookings):
        self._bookings = bookings

    def load_departures(self, departures):
        self._departures = departures

    def get_all_bookings(self):
        return self._bookings

    def make_booking(self, flight_number, passenger_name, date):
        if not self._validate_date(date):
            return
        flight = self._airline.get_flight(flight_number)
        if not flight:
            print("\nNincs ilyen járat.")
            return
        if not self._departure_exists(flight_number, date):
            print("\nEzen a napon nincs ilyen járat. A 4. menüpontban tudod lekérdezni az indulásokat.")
            return
        if not self._seats_available(flight_number, date, flight.capacity):
            print("\nErre a napra már nincs több szabad hely ezen a járaton.")
            return
        booking = Booking(flight, passenger_name, date)
        self._bookings.append(booking)
        print(f"\n{booking}")

    def cancel_booking(self, passenger_name, flight_number):
        for booking in self._bookings:
            if booking.passenger_name == passenger_name and booking.flight.flight_number == flight_number:
                self._bookings.remove(booking)
                booking.cancel()
                print("\nFoglalás sikeresen lemondva.")
                return
        print("\nNem található ilyen foglalás.")

    def print_bookings(self):
        print()
        if not self._bookings:
            print("\nNincs aktív foglalás.")
        else:
            for booking in self._bookings:
                print(booking)

    def get_available_seats(self, flight_number, date):
        flight = self._airline.get_flight(flight_number)
        if not flight:
            return None
        bookings_on_date = [
            b for b in self._bookings if b.flight.flight_number == flight_number and b.date == date
        ]
        return flight.capacity - len(bookings_on_date)

    def check_availability(self):
        flights = self._airline.get_all_flights()
        flight_dict = {}
        print()
        for i, flight in enumerate(flights, start=1):
            if flight:
                print(f'{i}. {flight.flight_number}')
                flight_dict[i] = flight.flight_number
        selected_flight = self._get_menu_index(flight_dict)   
        dates = [d['departure_date'] for d in self._departures if d['flight_number'] == selected_flight]
        print()
        self._print_free_seats(selected_flight, dates)

    def _print_free_seats(self, selected_flight, dates):
        for date in dates:
            available = self.get_available_seats(selected_flight, date)
            if available is not None:
                print(f"A(z) {selected_flight} járaton jelenleg még {available} szabad hely van a {date} dátumra.")

    def _get_menu_index(self, flight_dict):
        while True:
            try:
                index = int(input("\nAdd meg a számot a járat elöl: "))
                selected_flight = flight_dict.get(index)
                if not selected_flight:
                    print("\nÉrvénytelen választás.") 
                else:
                    break
            except ValueError:
                print("\nKérlek egy számot adj meg.")
        return selected_flight

    def _validate_date(self, date):
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            if date_obj < datetime.now():
                print("\nA megadott dátum a múltban van.")
                return False
            return True
        except ValueError:
            print("\nHibás dátumformátum.")
            return False

    def _departure_exists(self, flight_number, date):
        return any(
            d['flight_number'] == flight_number and d['departure_date'] == date
            for d in self._departures
        )

    def _seats_available(self, flight_number, date, capacity):
        booked = sum(
            1 for b in self._bookings
            if b.flight.flight_number == flight_number and b.date == date
        )
        return booked < capacity