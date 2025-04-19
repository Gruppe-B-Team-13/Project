class Rooms:
    def__init__(self, room_type, price_per_night, furnishing):
        self.__room_type = room_type
        self.__price_per_night = price_per_night
        self.__furnishing = []


    @property
    def room_type(self):
        return self.__room_type

    @property
    def price_per_night(self):
        return self.__price_per_night

    @property
    def furnishing(self):
        return self.__furnishing
