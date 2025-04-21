class Address:
    def __init__(self, address_id, street, house_number, city, zip_code, country):
        self.__address_id = address_id 
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

    def get_address(self):
        return f"{self.__street} {self.__house_number}, {self.__zip_code} {self.__city}, {self.__country}"
