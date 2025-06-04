from data_access.base_dal import BaseDataAccess
import model
import data_access

class Address_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def get_address_by_id(self, address_id: int) -> model.Address | None:
        sql = """
            SELECT address_id, street, house_number, zip_code, city, country FROM Address WHERE address_id = ?
            """
        params = tuple([address_id])
        result = self.fetchone(sql, params)
        if result:
            address_id, street, house_number, zip_code, city, country = result
            return model.Address(address_id, street, house_number, city, zip_code, country)
        else:
            return None
    
    def create_address(self, street: str, house_number: str, zip_code: str, city: str, country: str) -> model.Address:
        sql = """
            INSERT INTO Address (street, house_number, zip_code, city, country)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (street, house_number, zip_code, city, country)
        new_id, _ = self.execute(sql, params)

        return model.Address(new_id, street, house_number, city, zip_code, country)

    def find_address(self, street: str, house_number: str, zip_code: str, city: str, country: str) -> model.Address | None:
        sql = """
            SELECT address_id, street, house_number, city, zip_code, country
            FROM Address
            WHERE street = ? AND house_number = ? AND zip_code = ? AND city = ? AND country = ?
        """
        params = (street, house_number, zip_code, city, country)
        result = self.fetchone(sql, params)

        if result:
            address_id, street, house_number, city, zip_code, country = result
            return model.Address(address_id, street, house_number, city, zip_code, country)
        return None

