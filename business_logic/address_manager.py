import model
import data_access

class AddressManager:

    def __init__(self):
        self.address_dal = data_access.Address_DAL()

    def find_address(self, street: str, house_number: str, zip_code: str, city: str, country: str) -> model.Address | None:
        return self.address_dal.find_address(street, house_number, zip_code, city, country)

    def create_address(self, street: str, house_number: str, zip_code: str, city: str, country: str) -> model.Address:
        # Erst prüfen, ob Adresse bereits existiert
        existing = self.find_address(street, house_number, zip_code, city, country)
        if existing:
            return existing
        # Adresse erstellen
        return self.address_dal.create_address(street, house_number, zip_code, city, country)