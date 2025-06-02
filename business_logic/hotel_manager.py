import os
import model
import data_access
from datetime import date


class HotelManager:
    def __init__(self):
        self.hotel_dal = data_access.Hotel_DAL()

    def get_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        return self.hotel_dal.get_hotel_by_id(hotel_id)

    def get_filtered_hotels(self, city: str = None, min_stars: int = None, min_guests: int = None,
                            check_in_date: date = None, check_out_date: date = None) -> list[model.Hotel]:
        return self.hotel_dal.get_hotels_filtered(city, min_stars, min_guests, check_in_date, check_out_date)

    def print_filtered_hotels(self, city: str = None, min_stars: int = None, min_guests: int = None,
                               check_in_date: date = None, check_out_date: date = None):
        hotels = self.get_filtered_hotels(city, min_stars, min_guests, check_in_date, check_out_date)
        if not hotels:
            print("Keine Hotels gefunden.")
            return
        for hotel in hotels:
            print(f"{hotel.name} ({hotel.stars} Sterne) - {hotel.address.city}")