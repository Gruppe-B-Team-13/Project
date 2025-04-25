from data_access.base_dal import DatabaseConnection
from data_access.hotel_dal import Hotel_DAL
from data_access.room_type_dal import RoomType_DAL
from model.room import Room
from data_access.facilities_dal import Facility_DAL


class Room_DAL:
    def __init__(self):
        self.connection = DatabaseConnection().connect()
        self.hotel_dal = Hotel_DAL()
        self.room_type_dal = RoomType_DAL()
        self.facility_dal = Facility_DAL()

    def get_all_rooms(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT room_id, room_number, price_per_night, hotel_id, room_type_id FROM Room")
        rows = cursor.fetchall()

        rooms = []
        for row in rows:
            hotel = self.hotel_dal.get_hotel_by_id(row[3])
            room_type = self.room_type_dal.get_room_type_by_id(row[4])
            facilities = self.get_facilities_for_room(row[0])

            room = Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                hotel=hotel,
                room_type=room_type,
                facilities=facilities
            )

            rooms.append(room)
        return rooms

    def get_facilities_for_room(self, room_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT facility_id FROM Room_Facilities WHERE room_id = ?", (room_id,))
        rows = cursor.fetchall()
        return [self.facility_dal.get_facility_by_id(row[0]) for row in rows]


if __name__ == "__main__":
    dal = Room_DAL()
    for room in dal.get_all_rooms():
        print(room)
