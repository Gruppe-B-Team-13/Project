from data_access.base_dal import BaseDataAccess
import data_access
import model
from datetime import date


class RoomTypeManager:
    def __init__(self, db_path: str = None):
        self.room_type_dal = data_access.RoomType_DAL(db_path)

    def get_filtered_room_types(self, city: str = None, min_stars: int = None, min_guests: int = None,
                                check_in_date: date = None, check_out_date: date = None) -> list[model.Room]:
        return self._room_type_dal.get_filtered_room_types(city, min_stars, min_guests, check_in_date, check_out_date)

    def get_all_room_types(self) -> list[model.RoomType]:
        return self.room_type_dal.get_all_room_types()

    def get_room_type_by_id(self, room_type_id: int) -> model.RoomType:
        return self.room_type_dal.get_room_type_by_id(room_type_id)