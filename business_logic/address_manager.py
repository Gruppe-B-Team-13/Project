from models.address import Address #Import der Klasse, da in einem eigenen Modul gespeichert

Class address.manager

    def __init__(self):
        self.__address = address

    def add_address(self, address: Address):
        self._addresses.append(address)

    def get_alladdresses(self):
        return self._addresses


    def find_by_city(self, city:str):
        return[addr for addr in self._addresses if addr.city.lower() == city.lower()]


    def find_by_country(self, country:str):
        return[addr for addr in self._addresses if addr.country.lower() == country.lower()]

    def remove_address(self, address: Address):
        try:
            self._addresses.remove(address)
            return True
        except ValueError:
            return False