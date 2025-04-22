class Address:
    __next_id = 1 

    def __init__(self, street, house_number, city, zip_code, country):
        self.__address_id = Address.__next_id
        Address.__next_id += 1 
        self.__street = street
        self.__house_number = house_number
        self.__city = city
        self.__zip_code = zip_code
        self.__country = country

    @property
    def address_id(self):
        return self.__address_id

    @property
    def street(self):
        return self.__street

    @property
    def house_number(self):
        return self.__house_number

    @property
    def city(self):
        return self.__city

    @property
    def zip_code(self):
        return self.__zip_code

    @property
    def country(self):
        return self.__country

    def get_address_summary(self):
        return f"{self.__address_id} - Strasse: {self.__street} {self.__house_number}, {self.__zip_code} {self.__city}, {self.__country}"
