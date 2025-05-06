class RoomManager:
    def __init__(self):
        self.__rooms = []

    def add_room(self, room: Rooms):
        self.__rooms.append(room)

    def remove_room_by_id(self, room_id):
        self.__rooms = [r for r in self.__rooms if r.room_id != room_id]

    def find_by_id(self, room_id: int):
        for r in self.__rooms:
            if r.room_id == room_id:
                return r

        return None

    def find_by_room_number(self, room_number: int):
        return [r for r in self.__rooms if r.room_number == number]

    def find_by_hotel_name(self, hotel_name: str):
        return [r for r in self.__rooms if hotel_name.lower() in r.hotel.name.lower()]


    def find_by_room_type(self, room_type_name: str):
        return [r for r in self.__rooms if room_type_name.lower() in r.room_type.room_type_name.lower()]


    def find_by_price_range(self, min_price: float, max_price: float):
        return [r for r in self.__rooms if r.price_per_night <= r.price_per_night <= max_price]

    def get_all_rooms(self):
        return self.__rooms


    def print_all_rooms(self):
        for r in self.__rooms:
            print(r)