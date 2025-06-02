from data_access.base_dal import BaseDataAccess
from model.address import Address

class Address_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def get_address_by_id(self, address_id: int) -> Address | None:
        sql = """
            SELECT address_id, street, house_number, zip_code, city, country FROM Address WHERE address_id = ?
            """
        params = tuple([address_id])
        result = self.fetchone(sql, params)
        if result:
            address_id, street, house_number, zip_code, city, country = result
            return Address(address_id, street, house_number, city, zip_code, country)
        else:
            return None