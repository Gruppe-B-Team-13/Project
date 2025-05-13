# address_dal.py
from data_access.base_dal import BaseDataAccess
from model.address import Address

class Address_DAL(BaseDataAccess):
    def get_all_addresses(self) -> list[Address]:
        sql = "SELECT address_id, street, house_number, zip_code, city, country FROM Address"
        rows = self.fetchall(sql)
        return [
            Address(
                address_id=row[0],
                street=row[1],
                house_number=row[2],
                zip_code=row[3],
                city=row[4],
                country=row[5]
            ) for row in rows
        ]

    def get_address_by_id(self, address_id: int) -> model.Address | None:
        sql = """
            SELECT address_id, street, house_number, zip_code, city, country FROM Address WHERE address_id = ?
            """
        params = tuple([address_id])
        result = self.fetchone(sql, params)
        if result:
            address_id, street, house_number, zip_code, city, country = result
            return model.Address(address_id, street, house_number, zip_code, city, country)
        else:
            return None