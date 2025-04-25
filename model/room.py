class Room:
    def __init__(self, room_id, room_number, price_per_night, hotel, room_type):
        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__hotel = hotel  # Hotel-Objekt
        self.__room_type = room_type  # RoomType-Objekt

    @property
    def room_id(self):
        return self.__room_id

    @property
    def room_number(self):
        return self.__room_number

    @property
    def price_per_night(self):
        return self.__price_per_night

    @property
    def hotel(self):
        return self.__hotel

    @property
    def room_type(self):
        return self.__room_type

    @property
    def furnishing(self):
        return self.__furnishing

    def change_price(self, new_price: float):
        self.__price_per_night = new_price

    def __str__(self):
        return (f"Zimmer {self.__room_number} – Typ: {self.__room_type.room_type_name}, "
                f"Preis: {self.__price_per_night:.2f} CHF, Hotel: {self.__hotel.name}")
