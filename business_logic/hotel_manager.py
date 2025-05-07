class HotelManager:
    def __init__(self):
        self.__hotels = []

    def add_hotel(self, hotel: Hotel):
        self.__hotels.append(hotel)


    def remove_hotel_by_id(self, hotel_id):
        self.__hotels = [h for h in slef.__hotels if h.Hotel__hotel_id != hotel_id]

    def find_by_name(self, name: str):
        return [h for h in self.__hotels if name.lower() in h.namelower()]

    def find_by_stars(self, min_stars: int):
        return[h for h in self.__hotels if h.stars >= min_stars]

    def get_all_hotels(self):
        return self.__hotels

    def print_all_hotels(self):
        for h in self.__hotels:
            print(h)