import os
import model
import data_access

class HotelManager:
    def __init__(self):
        self.hotel_dal = data_access.hotel_dal.Hotel_DAL()

    def get_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        return self.hotel_dal.get_hotel_by_id(hotel_id)
