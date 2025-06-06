import os
import model
import data_access
from datetime import date

class RoomManager:
    def __init__(self):
        self.room_dal = data_access.Room_DAL()

    def get_all_rooms_with_facilities(self) -> list[str]:
        rooms = self.room_dal.get_all_rooms_with_facilities()
        result = []

        for room in rooms:
            result.append(room)
        return result

    def get_filtered_rooms(self, city: str = None, min_stars: int = None, min_guests: int = None, check_in_date: str = None, check_out_date: str = None, hotel_id: int = None) -> list[model.Room]:
        return self.room_dal.get_rooms_filtered(city, min_stars, min_guests, check_in_date, check_out_date, hotel_id)

    def create_room(self, hotel: model.Hotel, room_number: str, room_type: model.RoomType, price_per_night: float) -> model.Room:
        if not room_number:
            raise ValueError("Zimmernummer darf nicht leer sein.")
        if price_per_night <= 0:
            raise ValueError("Der Preis pro Nacht muss positiv sein.")

        return self.room_dal.create_room(hotel, room_number, room_type, price_per_night)
  
