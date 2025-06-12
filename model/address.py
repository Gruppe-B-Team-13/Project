class Address:

    def __init__(self, address_id, street, house_number, city, zip_code, country):
        self.__address_id = address_id
        self.street = street
        self.house_number = house_number
        self.city = city
        self.country = country
        self.zip_code = zip_code

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

    @street.setter
    def street(self, street):
        if not street.strip():
            raise ValueError("Die Strasse muss definiert werden.")
        self.__street = street

    @house_number.setter
    def house_number(self, house_number):
        if not house_number.strip():
            raise ValueError("Die Hausnummer muss definiert werden.")
        self.__house_number = house_number

    @city.setter
    def city(self, city):
        if not city.strip():
            raise ValueError("Die Stadt muss definiert werden.")
        self.__city = city

    @zip_code.setter
    def zip_code(self, zip_code):
        zip_str = str(zip_code).strip().upper()
        if not zip_str:
            raise ValueError("Die Postleitzahl darf nicht leer sein.")
        self.__zip_code = zip_str

    @country.setter
    def country(self, country):
        country = country.upper()
        self.__country = country

    def __str__(self):
        return f"{self.__street} {self.__house_number}, {self.__zip_code} {self.__city}, {self.__country}"

    def get_address_summary(self):
        return f"{self.__address_id} - Strasse: {self.__street} {self.__house_number}, {self.__zip_code} {self.__city}, {self.__country}"
