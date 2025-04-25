class Hotel:
    def __init__(self, hotel_id, name, address, stars):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__address = address
        self.__stars = stars
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

    def __str__(self):
        return f"{self.__hotel_id}, {self.__name}, {self.__address}, {self.__stars}, {self.__rooms}"