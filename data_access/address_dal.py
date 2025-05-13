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
                SELECT hotel_id, name, stars, address_id
                FROM   Hotel
                WHERE  hotel_id = ?
            """
            row = self.fetchone(sql, (hotel_id,))
            if row is None:
                return None

            hotel_id, name, stars, address_id = row
            address = self._address_dal.get_address_by_id(address_id)

            if address is None:
                raise ValueError("Fehler: Keine Adresse gefunden.")
            return model.Hotel(
                hotel_id=hotel_id,
                name=name,
                address=address,
                stars=stars
            )