class Room:
    def __init__(self, room_id, room_number, price_per_night, hotel, room_type, facilities=None):
        self.room_id = room_id
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.hotel = hotel
        self.room_type = room_type
        self.facilities = facilities if facilities is not None else []

        hotel.add_room(self)

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

    @room_id.setter
    def room_id(self, value):
        self.__room_id = value

    @room_number.setter
    def room_number(self, value):
        if not value.strip():
            raise ValueError("Die Zimmernummer darf nicht leer sein.")
        self.__room_number = value.strip()

    @price_per_night.setter
    def price_per_night(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Der Preis pro Nacht muss eine positive Zahl sein.")
        self.__price_per_night = float(value)

    @hotel.setter
    def hotel(self, value):
        if not isinstance(value, Hotel):
            raise TypeError("Das Hotel muss ein Objekt der Klasse Hotel sein.")
        self.__hotel = value

    @room_type.setter
    def room_type(self, value):
        if not isinstance(value, RoomType):
            raise TypeError("Der Zimmertyp muss ein Objekt der Klasse RoomType sein.")
        self.__room_type = value

    @facilities.setter
    def facilities(self, value):
        if value is None:
            self.__facilities = []
        elif isinstance(value, list) and all(isinstance(f, Facility) for f in value):
            self.__facilities = value
        else:
            raise TypeError("facilities muss entweder None oder eine Liste von Facility-Objekten sein.")

    def change_price(self, new_price: float):
        self.price_per_night = new_price

    def __str__(self):
        facilities_str = ", ".join(str(f) for f in self.__facilities) if self.__facilities else "Keine Ausstattung"
        return (
            f"Zimmer {self.__room_number} – Typ: {self.__room_type.room_type_name}, "
            f"Preis: {self.__price_per_night:.2f} CHF, Hotel: {self.__hotel.name}, "
            f"Ausstattung: [{facilities_str}]"
        )
