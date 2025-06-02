from data_access.base_dal import BaseDataAccess
import data_access
import model
from datetime import date


class RoomTypeManager:
    def __init__(self, db_path: str = None):
        self._room_type_dal = data_access.RoomType_DAL(db_path)

    def get_filtered_room_types(self, city: str = None, min_stars: int = None, min_guests: int = None,
                                check_in_date: date = None, check_out_date: date = None) -> list[model.Room]:
        return self._room_type_dal.get_filtered_room_types(city, min_stars, min_guests, check_in_date, check_out_date)

    def print_filtered_room_types(self, city: str = None, min_stars: int = None, min_guests: int = None,
                                  check_in_date: date = None, check_out_date: date = None):
        rooms = self.get_filtered_room_types(city, min_stars, min_guests, check_in_date, check_out_date)

        if not rooms:
            print("Keine passenden Zimmer gefunden.")
            return

        num_nights = (check_out_date - check_in_date).days if check_in_date and check_out_date else None

        for room in rooms:
            print(f"Hotel: {room.hotel.name} ({room.hotel.stars} Sterne)")
            print(f"Adresse: {room.hotel.address.street} {room.hotel.address.house_number}, "
                  f"{room.hotel.address.zip_code} {room.hotel.address.city}, {room.hotel.address.country}")
            print(f"Zimmertyp: {room.room_type.room_type_name}")
            print(f"Max. Gäste: {room.room_type.max_guests}")
            print(f"Beschreibung: {room.room_type.description}")
            print(f"Preis pro Nacht: {room.price_per_night:.2f} CHF")
            if num_nights:
                total_price = room.price_per_night * num_nights
                print(f"Gesamtpreis ({num_nights} Nächte): {total_price:.2f} CHF")
            print("-" * 60)
