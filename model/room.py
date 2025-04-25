class Room:
    def __init__(self, room_id, room_number, price_per_night, hotel, room_type, facilities = None):
        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__hotel = hotel
        self.__room_type = room_type
        self.__facilities = facilities if facilities is not None else []

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
    def facilities(self):
        return self.__facilities

    def change_price(self, new_price: float):
        self.__price_per_night = new_price

    def __str__(self):
        facilities_str = ", ".join(str(f) for f in self.__facilities) if self.__facilities else "Keine Ausstattung"
        return (
            f"Zimmer {self.__room_number} – Typ: {self.__room_type.room_type_name}, "
            f"Preis: {self.__price_per_night:.2f} CHF, Hotel: {self.__hotel.name}, "
            f"Ausstattung: [{facilities_str}]"
        )

