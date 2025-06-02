from data_access.base_dal import BaseDataAccess
import model
import data_access



class Room_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self._hotel_dal = data_access.Hotel_DAL(db_path)
        self._room_type_dal = data_access.RoomType_DAL(db_path)
        self._address_dal = data_access.Address_DAL(db_path)

    def get_room_by_id(self, room_id: int) -> model.Room | None:
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
            room_type = self._room_type_dal.get_room_type_by_id(room_type_id)
            return Room(room_id, room_number, price_per_night, hotel, room_type)
        else:
            return None

    def get_rooms_by_city_and_capacity(self, city: str, capacity: int) -> list[model.Room]:
        if not city or not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        if capacity < 1:
            raise ValueError("Kapazität kann nicht null sein.")
     
        sql = """
            SELECT Room.room_id,Room.hotel_id,Room.room_number,Room.room_type_id,Room.price_per_night
            FROM   Room

            JOIN   Hotel
            ON   Room.hotel_id = Hotel.hotel_id

            JOIN   Address
            ON   Hotel.address_id = Address.address_id

            JOIN Room_Type
            ON Room.room_type_id = Room_Type.room_type_id

            WHERE  Address.city = ? AND Room_Type.max_guests >= ?
            ORDER BY Room.Hotel_id
        """

        params = tuple([city, capacity])
        result = self.fetchall(sql, (params))
        rooms: list[Room] = []     

        for room_id, hotel_id, room_number, room_type_id, price_per_night in result:
            hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
            room_type = self._room_type_dal.get_room_type_by_id(room_type_id)
            rooms.append(Room(room_id, room_number, price_per_night, hotel, room_type))
        return rooms

    def get_all_rooms_with_facilities(self) -> list[model.Room]:

        sql = """
            SELECT
                Room.room_id, Room.room_number, Room.price_per_night, Room.hotel_id, Room.room_type_id,
                Facility.facility_id, Facility.facility_name
            FROM Room

            LEFT JOIN Room_Type ON Room_Type.room_type_id = Room.room_type_id

            LEFT JOIN Room_Facility ON Room.room_id = Room_Facility.room_id


            LEFT JOIN Facilities ON Room_Facility.facility_id = Facility.facility_id
        """
        results = self.fetchall(sql)
        rooms_dict = {}

        for row in results:
            (
                room_id,
                room_number,
                price_per_night,
                hotel_id,
                room_type_id,
                facility_id,
                facility_name,
            ) = row

            if room_id not in rooms_dict:
                hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
                room_type = self._room_type_dal.get_room_type_by_id(room_type_id)
                rooms_dict[room_id] = Room(
                    room_id, room_number, price_per_night, hotel, room_type, facilities=[]
                    )

            if facility_id and facility_name:


                rooms_dict[room_id].facilities.append(
                Facility(facility_id, facility_name))
            return list(rooms_dict.values())


    def get_rooms_by_min_guests_and_min_stars(self, min_guests: int, min_stars: int) -> list[model.Room]:
        if min_guests < 1:
            raise ValueError("Die Mindestanzahl an Gästen muss mindestens 1 sein.")
        if min_stars < 1:
            raise ValueError("Die Mindestanzahl an Sternen muss mindestens 1 sein.")

        sql = """
            SELECT Room.room_id,
                Room.room_number,
                Room.price_per_night,
                Room.hotel_id,
                Room.room_type_id
            FROM Room 

            JOIN Room_Type 
            ON Room.room_type_id = Room_Type.room_type_id

            JOIN Hotel 
            ON Room.hotel_id = Hotel.hotel_id

            WHERE Room_Type.max_guests >= ? AND Hotel.stars >= ?

            ORDER BY Hotel.stars DESC, Room.price_per_night ASC;
        """

        params = tuple([min_guests, min_stars])
        results = self.fetchall(sql, (params))
        rooms: list[Room] = []

        for room_id, room_number, price_per_night, hotel_id, room_type_id in results:
            hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
            room_type = self._room_type_dal.get_room_type_by_id(room_type_id)
            rooms.append(Room(room_id, room_number, price_per_night, hotel, room_type))

        return rooms

    def get_rooms_filtered(self, city:str = None, min_stars:int = None, min_guests:int = None) -> list[model.Room]:

        if min_stars is not None and min_stars < 1:
            raise ValueError("Mindestanzahl an Sternen muss mindestens 1 sein.")
        if min_guests is not None and min_guests < 1:
            raise ValueError("Mindestanzahl an Kunden muss mindestens 1 sein.")
        if city and not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")

        sql = """
            SELECT Room.room_id, 
                Room.room_number,
                Room.price_per_night, 
                Room.hotel_id, 
                Room.room_type_id
            FROM Room 

            JOIN Hotel  
            ON Room.hotel_id = Hotel.hotel_id

            JOIN Address 
            ON Hotel.address_id = Address.address_id

            JOIN Room_Type
            ON Room.room_type_id = Room_Type.room_type_id
            
            WHERE 1 = 1
        """
        params = []

        if city:
            sql += " AND Address.city = ?"
            params.append(city)

        if min_stars is not None:
            sql += " AND Hotel.stars >= ?"
            params.append(min_stars)

        if min_guests is not None:
            sql += " AND Room_Type.max_guests >= ?"
            params.append(min_guests)

        sql += " ORDER BY Room.price_per_night ASC, Hotel.stars DESC"

        results = self.fetchall(sql, (params))
        rooms: list[model.Room] = []

        for room_id, room_number, price_per_night, hotel_id, room_type_id in results:
            hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
            room_type = self._room_type_dal.get_room_type_by_id(room_type_id)
            rooms.append(model.Room(room_id, room_number, price_per_night, hotel, room_type))

        return rooms
