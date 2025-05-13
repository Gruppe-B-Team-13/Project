from .address import Address

class Hotel:
    def __init__(self, hotel_id: int, name, address, stars):
        self.hotel_id = hotel_id
        self.name = name
        self.address = address
        self.stars = stars
        self.__rooms = []

    @property
    def hotel_id(self):
        return self.__hotel_id

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def stars(self):
        return self.__stars

    @property
    def rooms(self):
        return self.__rooms

    @hotel_id.setter
    def hotel_id(self, value):
        self.__hotel_id = value

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Der Hotelname darf nicht leer sein.")
        self.__name = value.strip()

    @address.setter
    def address(self, value):
        if not isinstance(value, Address):
            raise TypeError("Die Adresse muss ein Objekt der Klasse Address sein.")
        self.__address = value

    @stars.setter
    def stars(self, value):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Die Bewertung (Sterne) muss eine Zahl zwischen 1 und 5 sein.")
        self.__stars = value

    def add_room(self, room):
        if not isinstance(room, Room):
            raise TypeError("Es kann nur ein Objekt der Klasse Room hinzugefügt werden.")
        self.__rooms.append(room)

    def __str__(self):
        return (
            f"Hotel {self.__hotel_id}: {self.__name} "
            f"({self.__stars} Sterne) – {self.__address}, "
            f"{len(self.__rooms)} Zimmer"
        )

    def __repr__(self):
        return (
            f"Hotel {self.__hotel_id}: {self.__name} "
            f"({self.__stars} Sterne) – {self.__address}, "
            f"{len(self.__rooms)} Zimmer"
        )

    def get_hotel_summary(self) -> str:
        address_str = str(self.address)
        return (
            f"Hotel {self.hotel_id}: {self.name} "
            f"({self.stars} Sterne)\n"
            f"Adresse: {address_str}\n"
            f"Anzahl Zimmer: {len(self.rooms)}"
        )