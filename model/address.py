class Address:
    def __init__(self, street, house_number, city, zip_code, country):
        self.__street = street
        self.__house_number = house_number
        self.__city = city
        self.__zip_code = zip_code
        self.__country = country

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

    def __str__(self):
        return f"{self.__street} {self.__house_number}, {self.__zip_code} {self.__city}, {self.__country}"
