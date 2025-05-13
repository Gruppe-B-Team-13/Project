import model
from data_access.base_dal import BaseDataAccess
from data_access.address_dal import Address_DAL

class Hotel_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def get_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        sql = """
            SELECT hotel_id, name FROM Hotel WHERE hotel_id = ?
            """
        params = tuple([hotel_id])
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name = result
            return model.Hotel(hotel_id, name)
        else:
            return None

    def read_all_hotels(self) -> list[model.Hotel]:
        sql = """
        SELECT hotel_id, Name, stars, address_id FROM hotel
        """
        results = self.fetchall(sql)
        
        hotels = []
        for hotel_id, name, stars, address_id in results:
            hotel.append(model.Hotel(hotel_id=hotel_id, name=name))

        return hotels