from data_access.base_dal import BaseDataAccess
from data_access.hotel_dal import Hotel_DAL
from data_access.room_type_dal import RoomType_DAL
from data_access.address_dal import Address_DAL
from model.room import Room
from model.hotel import Hotel


class Room_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self._hotel_dal = Hotel_DAL(db_path)
        self.room_type_dal = RoomType_DAL(db_path)
        self._address_dal    = Address_DAL(db_path)

    def get_room_by_id(self, room_id: int) -> Room | None:
        if room_id is None:
            raise ValueError("room_id darf nicht None sein.")

        sql = """
            SELECT Room.room_id, Room.hotel_id, Room.room_number, Room.room_type_id, Room.price_per_night
            FROM   Room
            WHERE  Room.room_id = ?
        """
        params = tuple([room_id])
        result = self.fetchone(sql, params)
        if result:
            room_id, hotel_id, room_number, room_type_id, price_per_night = result
            hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
            room_type = self.room_type_dal.get_room_type_by_id(room_type_id)
            return model.Room(room_id, room_number, price_per_night, hotel, room_type)
        else:
            return None


    def get_rooms_by_city_and_capacity(self, city: str, capacity: int) -> list[Room]:
        if not city or not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        if capacity < 1:
            raise ValueError("Kapazität kann nicht null sein.")
        
        sql = """
            SELECT Room.room_id,
                Room.hotel_id,
                Room.room_number,
                Room.room_type_id,
                Room.price_per_night
            FROM   Room
            JOIN   Hotel
            ON   Room.hotel_id = Hotel.hotel_id
            JOIN   Address
            ON   Hotel.address_id = Address.address_id
            JOIN Room_Type
            ON Room.room_type_id = Room_Type.room_type_id
            WHERE  Address.city = ? AND Room_Type.max_guests >= ?
        """
        params = tuple([city, capacity])
        result = self.fetchall(sql, (params))
        rooms: list[model.Rooms] = []
        
        for room_id, hotel_id, room_number, room_type_id, price_per_night in result:
            room_type = self.room_type_dal.get_room_type_by_id(room_type_id)
            hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
            rooms.append(Room(room_id, room_number, price_per_night, hotel, room_type)
            )

        return rooms

