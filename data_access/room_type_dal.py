from data_access.base_dal import BaseDataAccess
from model.room_type import RoomType

class RoomType_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def get_room_type_by_id(self, room_type_id: int) -> RoomType | None:
        if room_type_id is None:
            raise ValueError("room_type_id darf nicht None sein.")

        sql = """
            SELECT Room_Type.room_type_id, Room_Type.description, Room_Type.max_guests, Room_Type.room_type_name
            FROM   Room_Type
            WHERE  Room_Type.room_type_id = ?
        """
        params = tuple([room_type_id])
        result = self.fetchone(sql, params)
        if result:
            room_type_id, description, max_guests, room_type_name = result
            return RoomType(room_type_id, description, max_guests, room_type_name)
        else:
            return None
