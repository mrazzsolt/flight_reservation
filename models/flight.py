from abc import ABC, abstractmethod
from models.pricing import Pricing
from models.pricing import DomesticPricing, InternationalPricing

class Flight(ABC):
    def __init__(self, flight_number, destination, capacity, pricing: Pricing,distance_km):
        self._flight_number = flight_number
        self._destination = destination
        self._capacity = capacity
        self._available_seats = capacity
        self._pricing = pricing
        self._distance_km = distance_km


    @property
    def available_seats(self):
        return self._available_seats

    @available_seats.setter
    def available_seats(self, value):
        if value < 0:
            raise ValueError("Available seats cannot be negative.")
        if value > self._capacity:
            raise ValueError("Available seats cannot exceed capacity.")
        self._available_seats = value

    @property
    def distance_km(self):
        return self._distance_km
    
    @property
    def flight_number(self):
        return self._flight_number

    @property
    def destination(self):
        return self._destination

    @property
    def capacity(self):
        return self._capacity

    @property
    def price(self):
        return self._pricing.calculate_price(self)

    def is_available(self):
        return self.available_seats > 0

    def reserve_seat(self):
        if self.is_available():
            self.available_seats = self.available_seats - 1
            return True
        return False

    def cancel_seat(self):
        if self.available_seats < self._capacity:
            self.available_seats = self.available_seats + 1

    @abstractmethod
    def info(self):
        pass

class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, capacity, distance_km):
        super().__init__(flight_number, destination, capacity, DomesticPricing(), distance_km)

    def info(self):
        return f"Belföldi járat: {self.flight_number} -> {self.destination}, Ár: {self.price} Ft, Szabad helyek: {self.available_seats}/{self.capacity}"


class InternationalFlight(Flight):
    def __init__(self, flight_number, destination, capacity, distance_km):
        super().__init__(flight_number, destination, capacity, InternationalPricing(), distance_km)

    def info(self):
        return f"Nemzetközi járat: {self.flight_number} -> {self.destination}, Ár: {self.price} Ft, Szabad helyek: {self.available_seats}/{self.capacity}"