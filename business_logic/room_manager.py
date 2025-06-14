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

    def get_filtered_rooms(self, city=None, min_stars=None, min_guests=None,check_in_date=None, check_out_date=None, hotel_id=None, room_id=None) -> list[model.Room]:
        if min_stars is not None and min_stars < 1:
            raise ValueError("Mindestanzahl an Sternen muss mindestens 1 sein.")
        if min_guests is not None and min_guests < 1:
            raise ValueError("Mindestanzahl an Kunden muss mindestens 1 sein.")
        if city and not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        if (check_in_date and not check_out_date) or (check_out_date and not check_in_date):
            raise ValueError("Sowohl Check-In- als auch Check-Out-Datum müssen gesetzt sein.")
        if hotel_id is not None and hotel_id < 1:
            raise ValueError("Feld hotel_id ist nicht optional.")  
                             
        rooms = self.room_dal.get_rooms_filtered(
            city=city,
            min_stars=min_stars,
            min_guests=min_guests,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            hotel_id=hotel_id,
            room_id=room_id
        )

        for room in rooms:
            adjusted_price = self.apply_seasonal_price(room.price_per_night, check_in_date)
            room.price_per_night = adjusted_price

        return rooms

    def create_room(self, hotel: model.Hotel, room_number: str, room_type: model.RoomType, price_per_night: float) -> model.Room:
        if not room_number:
            raise ValueError("Zimmernummer darf nicht leer sein.")
        if price_per_night <= 0:
            raise ValueError("Der Preis pro Nacht muss positiv sein.")

        return self.room_dal.create_room(hotel, room_number, room_type, price_per_night)
    
    def apply_seasonal_price(self, base_price: float, check_in_date: date =None) -> float:
        if check_in_date is None:
            return base_price
        elif check_in_date.month in [6, 7, 8]:  # Hochsaison
            return round(base_price * 1.2, 2)
        elif check_in_date.month in [1, 2, 11]:  # Nebensaison
            return round(base_price * 0.85, 2)
        return base_price
  
    def calculate_nights(self, check_in_date: str, check_out_date: str) -> int:
        if check_out_date <= check_in_date:
            raise ValueError("Check-Out-Datum muss nach dem Check-In-Datum liegen.")
        return (check_out_date - check_in_date).days
    
    def update_room_by_id(self, room_id: int, room_number: str = None, room_type_id: int = None, price_per_night: float = None) -> model.Room | None
        if room_id is None:
            raise ValueError("room_id darf nicht None sein.")
            
        return self.room_dal.update_room_by_id(
            room_id=room_id,
            room_number=room_number,
            room_type_id=room_type_id,
            price_per_night=price_per_night
        )

    def update_facilities_for_room(self, room_id: int, facilities: list[model.Facility]) -> None:
        self.room_dal.update_room_facilities(room_id, facilities)

    
    def delete_room(self, room: model.Room) -> None:
        return self.room_dal.delete_room(room)