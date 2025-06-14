from data_access.base_dal import BaseDataAccess
import data_access
import model
from datetime import date


class RoomTypeManager:
    def __init__(self, db_path: str = None):
        self.room_type_dal = data_access.RoomType_DAL(db_path)

    def get_all_room_types(self) -> list[model.RoomType]:
        return self.room_type_dal.get_all_room_types()


    def get_filtered_room_types(self, city: str = None, min_stars: int = None, min_guests: int = None,check_in_date: date = None, check_out_date: date = None, room_type_id: int = None) -> list[model.Room]:
                             
        if check_in_date and check_out_date and check_in_date >= check_out_date:
            raise ValueError("Check-in-Datum muss vor dem Check-out-Datum liegen.")

        return self.room_type_dal.get_filtered_room_types(city, min_stars, min_guests, check_in_date, check_out_date, room_type_id)

    def get_room_type_by_id(self, room_type_id: int) -> model.RoomType:
        if room_type_id is None:
            raise ValueError("room_type_id darf nicht None sein.")
            
        return self.room_type_dal.get_room_type_by_id(room_type_id)

    def create_room_type(self, room_type: model.RoomType) -> model.RoomType:
        return self.room_type_dal.create_room_type(room_type)

    def update_room_type_by_id(self, room_type_id: int, description: str = None, max_guests: int = None, room_type_name: str = None) -> model.RoomType | None:

        if room_type_id is None:
            raise ValueError("room_type_id darf nicht None sein.")
            
        return self.room_type_dal.update_room_type_by_id(room_type_id, description, max_guests, room_type_name)

    def delete_room_type(self, room_type_id: int) -> None:
        self.room_type_dal.delete_room_type(room_type_id)