from data_access.base_dal import DatabaseConnection
from model.room_type import RoomType

class RoomType_DAL:
    def __init__(self):
        self.connection = DatabaseConnection().connect()

    def get_room_type_by_id(self, room_type_id):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT room_type_id, room_type_name, description, max_guests 
            FROM Room_type 
            WHERE room_type_id = ?
        """, (room_type_id,))
        row = cursor.fetchone()
        if row:
            return RoomType(
                room_type_id=row[0],
                room_type_name=row[1],
                description=row[2],
                max_guests=row[3]
            )
        return None

    def get_all_room_types(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT room_type_id, room_type_name, description, max_guests FROM Room_type")
        rows = cursor.fetchall()
        return [
            RoomType(room_type_id=r[0], room_type_name=r[1], description=r[2], max_guests=r[3])
            for r in rows
        ]
