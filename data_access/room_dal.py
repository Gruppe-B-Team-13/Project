from data_access.base_dal import BaseDataAccess
from data_access.hotel_dal import Hotel_DAL
from data_access.room_type_dal import RoomType_DAL
from data_access.address_dal import Address_DAL
from model.room import Room
from model.hotel import Hotel
from model.facilities import Facility

def get_all_rooms_with_facilities(self) -> list[Room]:
    sql = """
        SELECT
            r.room_id,
            r.room_number,
            r.price_per_night,
            r.hotel_id,
            r.room_type_id,
            f.facility_id,
            f.facility_name
        FROM Room r
        LEFT JOIN Room_Facility rf ON r.room_id = rf.room_id
        LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
    """

    results = self.fetchall(sql)
    rooms_dict = {}

    for row in results:
        (
            room_id,
            room_number,
            price_per_night,
            hotel_id,
            room_type_id,
            facility_id,
            facility_name,
        ) = row

        if room_id not in rooms_dict:
            hotel = self._hotel_dal.get_hotel_by_id(hotel_id)
            room_type = self.room_type_dal.get_room_type_by_id(room_type_id)
            rooms_dict[room_id] = Room(
                room_id, room_number, price_per_night, hotel, room_type, facilities=[]
            )

        if facility_id and facility_name:
            rooms_dict[room_id].facilities.append(
                Facility(facility_id, facility_name)
            )

    return list(rooms_dict.values())


