from data_access.base_dal import BaseDataAccess
from data_access.address_dal import Address_DAL
from datetime import date
import model

class Hotel_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self._address_dal = Address_DAL(db_path)   
    
    def get_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        if hotel_id is None:
            raise ValueError("hotel_id darf nicht None sein.")

        sql = """
            SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Hotel.address_id
            FROM   Hotel
            WHERE  hotel_id = ?
        """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars, address_id = result
            address = self._address_dal.get_address_by_id(address_id)
            return model.Hotel(hotel_id, name, address, stars)
        else:
            return None
    
    def get_hotels_filtered(self, city: str = None, min_stars: int = None, min_guests: int = None, room_id: int = None,
                            check_in_date: date = None, check_out_date: date = None) -> list[model.Hotel]:

        if min_stars is not None and min_stars < 1:
            raise ValueError("Mindestanzahl an Sternen muss mindestens 1 sein.")
        if min_guests is not None and min_guests < 1:
            raise ValueError("Mindestanzahl an Gästen muss mindestens 1 sein.")
        if city and not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        if (check_in_date and not check_out_date) or (check_out_date and not check_in_date):
            raise ValueError("Sowohl check_in_date als auch check_out_date müssen gesetzt sein.")

        sql = """
            SELECT Hotel.hotel_id,
                            Hotel.name,
                            Hotel.stars,
                            Hotel.address_id
            FROM Hotel
            JOIN Address ON Hotel.address_id = Address.address_id
            JOIN Room ON Room.hotel_id = Hotel.hotel_id
            JOIN Room_Type ON Room.room_type_id = Room_Type.room_type_id
            LEFT JOIN Booking ON Booking.room_id = Room.room_id AND Booking.is_cancelled = 0

            Where 1 = 1
        """

        params = []
        
        if check_in_date and check_out_date:
            sql += """
            AND (
                Booking.room_id IS NULL OR
                NOT (
                    ? < Booking.check_out_date AND
                    ? > Booking.check_in_date
                )
            )
            """
            params.extend([check_in_date, check_out_date])

        if city is not None:
            sql += " AND Address.city = ?"
            params.append(city)

        if min_stars is not None:
            sql += " AND Hotel.stars >= ?"
            params.append(min_stars)

        if room_id is not None:
            sql += " AND Room.room_id = ?"
            params.append(room_id)
            
        if min_guests is not None:
            sql += " AND Room_Type.max_guests >= ?"
            params.append(min_guests)

        sql += """
            GROUP BY Hotel.hotel_id
            ORDER BY Hotel.stars DESC, Hotel.name ASC
            """

        results = self.fetchall(sql, tuple(params))
        hotels: list[model.Hotel] = []

        for hotel_id, name, stars, address_id in results:
            address = self._address_dal.get_address_by_id(address_id)
            hotels.append(model.Hotel(hotel_id, name, address, stars))

        return hotels

    def get_all_hotels(self) -> list[model.Hotel]:
        sql = """
            SELECT hotel_id, name, stars, address_id
            FROM Hotel
            ORDER BY stars DESC, name ASC
        """
        results = self.fetchall(sql)
        hotels = []
        for hotel_id, name, stars, address_id in results:
            address = self._address_dal.get_address_by_id(address_id)
            hotels.append(model.Hotel(hotel_id, name, address, stars))
        return hotels

    def remove_hotel_by_id(self, hotel_id: int) -> bool:
        if hotel_id is None:
            raise ValueError("hotel_id darf nicht None sein.")

        sql = """
            DELETE 
            FROM Hotel 
            WHERE hotel_id = ?
        """
        params = tuple([hotel_id])
        rowcount, _ = self.execute(sql, params)
        return rowcount > 0

    def update_hotel_by_id(self, hotel_id: int, name: str = None, stars: int = None, address_id: int = None) -> model.Hotel | None:
        if hotel_id is None:
            raise ValueError("hotel_id darf nicht None sein.")

        updates = []
        params = []

        if name is not None:
            updates.append("name = ?")
            params.append(name)
        if stars is not None:
            if stars < 1 or stars > 5:
                raise ValueError("Sterne müssen zwischen 1 und 5 liegen.")
            updates.append("stars = ?")
            params.append(stars)
        if address_id is not None:
            updates.append("address_id = ?")
            params.append(address_id)

        if not updates:
            raise ValueError("Mindestens ein Feld muss aktualisiert werden.")

        sql = f"""
            UPDATE Hotel
            SET {', '.join(updates)}
            WHERE hotel_id = ?
        """
        params.append(hotel_id)

        _, rowcount = self.execute(sql, tuple(params))

        if rowcount > 0:
            return self.get_hotel_by_id(hotel_id)
        else:
            return None

    def find_hotel_by_name(self, name: str) -> model.Hotel | None:
        sql = """
            SELECT hotel_id, stars, address_id
            FROM Hotel
            WHERE name = ?
        """
        result = self.fetchone(sql, (name,))
        if not result:
            return None
        hotel_id, stars, address_id = result
        address = self._address_dal.get_address_by_id(address_id)
        return model.Hotel(hotel_id, name, address, stars)

    def create_hotel(self, name: str, stars: int, address_id: int) -> model.Hotel:
        sql = """
            INSERT INTO Hotel (name, stars, address_id)
            VALUES (?, ?, ?)
        """
        hotel_id, _ = self.execute(sql, (name, stars, address_id))
        address = self._address_dal.get_address_by_id(address_id)
        return model.Hotel(hotel_id, name, address, stars)
