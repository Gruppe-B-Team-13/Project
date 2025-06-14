import os
import model
import data_access
from datetime import date


class HotelManager:
    def __init__(self):
        self.hotel_dal = data_access.Hotel_DAL()

    def get_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:

        if hotel_id is None:
            raise ValueError("hotel_id darf nicht None sein.")
            
        return self.hotel_dal.get_hotel_by_id(hotel_id)

    def get_filtered_hotels(self, city: str = None, min_stars: int = None, min_guests: int = None, room_id: int = None, check_in_date: date = None, check_out_date: date = None) -> list[model.Hotel]:
                            
        if min_stars is not None and min_stars < 1:
            raise ValueError("Mindestanzahl an Sternen muss mindestens 1 sein.")
        if min_guests is not None and min_guests < 1:
            raise ValueError("Mindestanzahl an Gästen muss mindestens 1 sein.")
        if city and not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        if (check_in_date and not check_out_date) or (check_out_date and not check_in_date):
            raise ValueError("Sowohl check_in_date als auch check_out_date müssen gesetzt sein.")

        return self.hotel_dal.get_hotels_filtered(city, min_stars, min_guests,room_id, check_in_date, check_out_date)

    def remove_hotel_by_id(self, hotel_id: int):

        if hotel_id is None:
            raise ValueError("hotel_id darf nicht None sein.")
            
        self.hotel_dal.remove_hotel_by_id(hotel_id)
        
    def update_hotel_by_id(self, hotel_id: int, name: str = None, stars: int = None, address_id: int = None):
        if hotel_id is None:
            raise ValueError("hotel_id darf nicht None sein.")
        return self.hotel_dal.update_hotel_by_id(hotel_id, name, stars, address_id)
        
    def create_hotel(self, name: str, stars: int, address_id: int) -> model.Hotel:
        existing = self.hotel_dal.find_hotel_by_name(name)
        if existing:
            return existing
        return self.hotel_dal.create_hotel(name, stars, address_id)

    def find_hotel_by_name(self, name: str) -> model.Hotel | None:
        return self.hotel_dal.find_hotel_by_name(name)
