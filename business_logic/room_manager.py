class RoomManager:
    def __init__(self, room_dal):
        self.room_dal = room_dal

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
