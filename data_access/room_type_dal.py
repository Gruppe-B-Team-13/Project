from data_access.base_dal import BaseDataAccess
import data_access
import model
from datetime import date

class RoomType_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self._hotel_dal = data_access.Hotel_DAL(db_path)

    def get_room_type_by_id(self, room_type_id: int) -> model.RoomType | None:

        sql = """
            SELECT Room_Type.room_type_id, Room_Type.description, Room_Type.max_guests, Room_Type.room_type_name
            FROM   Room_Type
            WHERE  Room_Type.room_type_id = ?
        """
        params = tuple([room_type_id])
        result = self.fetchone(sql, params)
        if result:
            room_type_id, description, max_guests, room_type_name = result
            return model.RoomType(room_type_id, description, max_guests, room_type_name)
        else:
            return None
    def get_all_room_types(self) -> list[model.RoomType]:

        sql = """
            SELECT room_type_id, description, max_guests, room_type_name
            FROM Room_Type
        """
        results = self.fetchall(sql)
        return [model.RoomType(room_type_id, description, max_guests, room_type_name)
                for room_type_id, description, max_guests, room_type_name in results]

    def get_filtered_room_types(self, city: str = None, min_stars: int = None, min_guests: int = None,check_in_date: date = None, check_out_date: date = None, room_type_id: int = None) -> list[model.Room]:
                                 
        sql = """
            SELECT Room.room_id, Room.hotel_id, Room.room_number, Room.room_type_id, Room.price_per_night
            FROM Room
            JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
            JOIN Address ON Hotel.address_id = Address.address_id
            JOIN Room_Type ON Room.room_type_id = Room_Type.room_type_id
            LEFT JOIN Booking ON Booking.room_id = Room.room_id AND Booking.is_cancelled = 0
            WHERE 1 = 1
        """

        params = []

        if check_in_date and check_out_date:
            sql += """
                AND (
                    Booking.booking_id IS NULL OR
                    NOT (? < Booking.check_out_date AND ? > Booking.check_in_date)
                )
            """
            params.extend([check_in_date, check_out_date])

        if city:
            sql += " AND Address.city = ?"
            params.append(city)

        if min_stars is not None:
            sql += " AND Hotel.stars >= ?"
            params.append(min_stars)

        if min_guests is not None:
            sql += " AND Room_Type.max_guests >= ?"
            params.append(min_guests)

        if room_type_id is not None:
            sql += " AND Room_Type.room_type_id = ?"
            params.append(room_type_id)
            
        sql += " ORDER BY Hotel.hotel_id, Room.room_type_id, Room.price_per_night ASC"

        results = self.fetchall(sql, tuple(params))

        seen = set()
        filtered_rooms = []

        for room_id, hotel_id, room_number, room_type_id, price_per_night in results:
            key = (hotel_id, room_type_id)
            if key not in seen:
                seen.add(key)
                hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
                room_type = self.get_room_type_by_id(room_type_id)
                filtered_rooms.append(model.Room(room_id, room_number, price_per_night, hotel, room_type))

        return filtered_rooms

    def create_room_type(self, description: str, max_guests: int, room_type_name: str) -> model.RoomType:

        sql = """
            INSERT INTO Room_Type
            (description, max_guests, room_type_name)
            VALUES
            (?, ?, ?)
        """
        params = tuple([description, max_guests, room_type_name])
        room_type_id, _ = self.execute(sql, params)
        return model.RoomType(None, description, max_guests, room_type_name)

    def update_room_type_by_id(self, room_type_id: int, description: str = None, max_guests: int = None, room_type_name: str = None) -> model.RoomType | None:

        updates = []
        params = []

        if description is not None:
            updates.append("description = ?")
            params.append(description)
        if max_guests is not None:
            if max_guests < 1:
                raise ValueError("max_guests muss mindestens 1 sein.")
            updates.append("max_guests = ?")
            params.append(max_guests)
        if room_type_name is not None:
            updates.append("room_type_name = ?")
            params.append(room_type_name)

        if not updates:
            raise ValueError("Mindestens ein Feld muss aktualisiert werden.")

        sql = f"""
            UPDATE Room_Type
            SET {', '.join(updates)}
            WHERE room_type_id = ?
        """
        params.append(room_type_id)

        _, rowcount = self.execute(sql, tuple(params))

        if rowcount > 0:
            return self.get_room_type_by_id(room_type_id)
        else:
            return None

        
    def delete_room_type(self, room_type_id: int) -> None:
        
        sql = """
            DELETE FROM Room_Type
            WHERE room_type_id = ?
        """
        params = tuple([room_type_id])
        self.execute(sql, params)