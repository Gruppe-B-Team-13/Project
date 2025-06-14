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



    def update_street(self, address_id: int, new_street: str) -> bool:
        sql = "UPDATE Address SET street = ? WHERE address_id = ?"
        _, rowcount = self.execute(sql, (new_street, address_id))
        return rowcount > 0

    def update_house_number(self, address_id: int, new_house_number: str) -> bool:
        sql = "UPDATE Address SET house_number = ? WHERE address_id = ?"
        _, rowcount = self.execute(sql, (new_house_number, address_id))
        return rowcount > 0

    def update_zip_code(self, address_id: int, new_zip_code: str) -> bool:
        sql = "UPDATE Address SET zip_code = ? WHERE address_id = ?"
        _, rowcount = self.execute(sql, (new_zip_code, address_id))
        return rowcount > 0

    def update_city(self, address_id: int, new_city: str) -> bool:
        sql = "UPDATE Address SET city = ? WHERE address_id = ?"
        _, rowcount = self.execute(sql, (new_city, address_id))
        return rowcount > 0

    def update_country(self, address_id: int, new_country: str) -> bool:
        sql = "UPDATE Address SET country = ? WHERE address_id = ?"
        _, rowcount = self.execute(sql, (new_country, address_id))
        return rowcount > 0

