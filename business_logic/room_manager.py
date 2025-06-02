import os
import model
import data_access

class RoomManager:
    def __init__(self):
        self.room_dal = data_access.Room_DAL()

    def get_all_rooms_with_facilities(self) -> list[str]:
        rooms = self.room_dal.get_all_rooms_with_facilities()
        result = []

        for room in rooms:
            facilities_str = (
                ", ".join(str(f) for f in room.facilities)
                if room.facilities
                else "Keine Ausstattung"
            )
            room_info = (
                f"Zimmer {room.room_number} – Typ: {room.room_type.room_type_name}, "
                f"max. Gäste: {room.room_type.max_guests}, "
                f"Preis: {room.price_per_night:.2f} CHF\n"
                f"  Ausstattung: {facilities_str}"
            )
            result.append(room_info)

        return result

    def get_filtered_rooms(self, city: str = None, min_stars: int = None, min_guests: int = None) -> list[model.Room]:
        return self.room_dal.get_rooms_filtered(city, min_stars, min_guests)

    def print_filtered_rooms(self, city: str = None, min_stars: int = None, min_guests: int = None):
        rooms = self.get_filtered_rooms(city, min_stars, min_guests)
        if not rooms:
            print("Keine Zimmer gefunden.")
            return
        for room in rooms:
            print(room.get_room_summary())