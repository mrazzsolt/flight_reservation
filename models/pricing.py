from abc import ABC, abstractmethod

class Pricing(ABC):
    @abstractmethod
    def calculate_price(self, flight):
        pass


class DomesticPricing(Pricing):
    def calculate_price(self, flight):
        if flight.distance_km:
            return flight.distance_km * 350
        return 15000


class InternationalPricing(Pricing):
    def calculate_price(self, flight):
        if flight.distance_km:
            return flight.distance_km * 100
        return 45000
