import csv
from models.booking import Booking
from models.flight import DomesticFlight, InternationalFlight

class BookingSystemIO:
    def __init__(self,airline):
        self.airline = airline

    def load_flights(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['type'] == 'DomesticFlight':
                    flight = DomesticFlight(row['flight_number'], row['destination'], int(row['capacity']), int(row['distance_km']))
                elif row['type'] == 'InternationalFlight':
                    flight = InternationalFlight(row['flight_number'], row['destination'], int(row['capacity']), int(row['distance_km']))
                else:
                    continue
                self.airline.add_flight(flight)
        return self.airline

    def load_bookings(self, filename):
        bookings = []
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    flight = self.airline.get_flight(row['flight_number'])
                    if flight:
                        booking = Booking(flight, row['passenger_name'], row['date'])
                        bookings.append(booking)
        except FileNotFoundError:
            print("Nincs előző foglalási fájl. Új fájl lesz létrehozva.")
        return bookings

    def save_bookings(self, filename, bookings):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['passenger_name', 'flight_number', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for b in bookings:
                writer.writerow({
                    'passenger_name': b.passenger_name,
                    'flight_number': b.flight.flight_number,
                    'date': b.date
                })


    def load_departures(self, filename):
        departures = []
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    departures.append({
                        'flight_number': row['flight_number'],
                        'departure_date': row['departure_date']
                    })
        except FileNotFoundError:
            print(f"A fájl nem található: {filename}")
        except KeyError:
            print("Hibás oszlopnevek a fájlban.")
        return departures
