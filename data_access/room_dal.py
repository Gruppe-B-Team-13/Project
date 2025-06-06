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
            return model.Room(room_id, room_number, price_per_night, hotel, room_type)
        else:
            return None

## Check hotel id noch einfügen
    def get_rooms_filtered(self, city:str = None, min_stars:int = None, min_guests:int = None, check_in_date: str = None, check_out_date: str = None, hotel_id: int = None) -> list[model.Room]:

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

        sql = """
            SELECT Room.room_id, 
                Room.room_number,
                Room.price_per_night, 
                Room.hotel_id, 
                Room.room_type_id
            FROM Room
            JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
            JOIN Address ON Hotel.address_id = Address.address_id
            JOIN Room_Type ON Room.room_type_id = Room_Type.room_type_id
            WHERE 1 = 1
        """
        params = []

        if hotel_id is not None:
            sql += " AND Hotel.hotel_id = ?"
            params.append(hotel_id)

        if city is not None:
            sql += " AND Address.city = ?"
            params.append(city)

        if min_stars is not None:
            sql += " AND Hotel.stars >= ?"
            params.append(min_stars)

        if min_guests is not None:
            sql += " AND Room_Type.max_guests >= ?"
            params.append(min_guests)

        if check_in_date is not None and check_out_date is not None:
            sql += """
            AND NOT EXISTS (
                SELECT 1
                FROM Booking
                WHERE Booking.room_id = Room.room_id
                AND Booking.is_cancelled = 0
                AND Booking.check_in_date < ?
                AND Booking.check_out_date > ?
            )
            """
            params.extend([check_out_date, check_in_date])

        sql += " ORDER BY Room.price_per_night ASC"

        results = self.fetchall(sql, tuple(params))
        rooms: list[model.Room] = []

        for room_id, room_number, price_per_night, hotel_id, room_type_id in results:
            hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
            room_type = self._room_type_dal.get_room_type_by_id(room_type_id)
            rooms.append(model.Room(room_id, room_number, price_per_night, hotel, room_type))

        return rooms

    def create_room(self, hotel: model.Hotel, room_number: str, room_type: model.RoomType, price_per_night: float) -> model.Room:
        sql = """
            INSERT INTO Room (hotel_id, room_number, room_type_id, price_per_night)
            VALUES (?, ?, ?, ?)
        """
        room_id, _ = self.execute(sql, (hotel.hotel_id, room_number, room_type.room_type_id, price_per_night))
        return model.Room(room_id, room_number, price_per_night, hotel, room_type)


