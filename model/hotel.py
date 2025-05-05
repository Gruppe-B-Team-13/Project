class Hotel:
    def __init__(self, hotel_id, name, address, stars):
        self.__hotel_id = hotel_id
        self.name = name
        self.address = address
        self.stars = stars
        self.__rooms = []

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def stars(self):
        return self.__stars

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Der Name muss definiert werden.")
        else:
            self.__name = name

    @address.setter
    def address(self, address):
        if address.strip() == "":
            raise ValueError("Die Adresse muss definiert werden.")
        else:
            self.__address = address

    @stars.setter
    def stars(self, stars):
        if stars < 1 or stars > 5:
            raise ValueError("Die Bewertung muss zwischen 1 und 5 liegen.")
        else:
            self.__stars = stars

    def __str__(self):
        return f"{self.__hotel_id}, {self.__name}, {self.__address}, {self.__stars}, {self.__rooms}"