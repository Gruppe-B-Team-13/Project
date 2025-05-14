from data_access.base_dal import BaseDataAccess
from data_access.address_dal import Address_DAL
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
    
    def get_hotels_by_city(self, city: str) -> list[model.Hotel]:
        if not city or not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        
        sql = """
            SELECT Hotel.hotel_id,
                Hotel.name,
                Hotel.stars,
                Hotel.address_id
            FROM   Hotel
            JOIN   Address
            ON   Hotel.address_id = Address.address_id
            WHERE  Address.city = ?
        """
        params = tuple([city])
        result = self.fetchall(sql, (params))
        hotels: list[model.Hotel] = []
        
        for hotel_id, name, stars, address_id in result:
            address = self._address_dal.get_address_by_id(address_id)
            hotels.append(model.Hotel(hotel_id, name, address, stars)
            )
        
        return hotels

    def get_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:
        if not city or not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        if stars < 1 or stars > 5:
            raise ValueError("Anzahl Sterne muss zwischen 1 und 5 liegen.")
        
        sql = """
            SELECT Hotel.hotel_id,
                Hotel.name,
                Hotel.stars,
                Hotel.address_id
            FROM   Hotel
            JOIN   Address
            ON   Hotel.address_id = Address.address_id
            WHERE  Address.city = ? AND Hotel.stars >= ?
        """
        params = tuple([city, stars])
        result = self.fetchall(sql, (params))
        hotels: list[model.Hotel] = []
        
        for hotel_id, name, stars, address_id in result:
            address = self._address_dal.get_address_by_id(address_id)
            hotels.append(model.Hotel(hotel_id, name, address, stars)
            )
        
        return hotels