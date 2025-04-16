from services.bookingio import BookingSystemIO
from services.engine import BookingSystem
from models.airline import Airline

def main():
    airline = Airline("BPAirline")
    io = BookingSystemIO(airline)
    flights = io.load_flights('data/flights.csv')
    engine = BookingSystem(flights)
    bookings = io.load_bookings('data/bookings.csv')
    departures = io.load_departures('data/departures.csv')
    engine.load_bookings(bookings)
    engine.load_departures(departures)

    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy vásárlás")
        print("2. Korábbi foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Elérhető járatok és időpontjaik")
        print("5. Kilépés")
        choice = input("\nÍrd be a kívánt művelet számát a továbblépéshez: ")
        if choice == "1":
            passenger_name = input("Add meg az utas teljes nevét: ")
            flight_number = input("Add meg a járatszámot: ")
            date = input("Add meg az utazás dátumát (ÉÉÉÉ-HH-NN): ")
            engine.make_booking(flight_number, passenger_name, date)
            io.save_bookings('data/bookings.csv', engine.get_all_bookings())
        elif choice == "2":
            passenger_name = input("Add meg az utas teljes nevét: ")
            flight_number = input("Add meg a járatszámot: ")
            engine.cancel_booking(passenger_name, flight_number)
            io.save_bookings('data/bookings.csv', engine.get_all_bookings())
        elif choice == "3":
            engine.print_bookings()
        elif choice == "4":
            engine.check_availability()
        elif choice == "5":
            print("Kilépés...")
            break
        else:
            print("Nincs ilyen menüpont.")

if __name__ == "__main__":
    main()
