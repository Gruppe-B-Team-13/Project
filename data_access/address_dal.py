from data_access.base_dal import DatabaseConnection
from model.address import Address

class Address_DAL:
    def __init__(self):
        self.connection = DatabaseConnection().connect()

    def get_all_addresses(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT address_id, street, house_number, zip_code, city, country FROM Address")
        rows = cursor.fetchall()

        addresses = []
        for row in rows:
            address = Address(
                address_id=row[0],
                street=row[1],
                house_number=row[2],
                city=row[3],
                zip_code=row[4],
                country=row[5]
            )
            addresses.append(address)
        return addresses

if __name__ == "__main__":
    dal = Address_DAL()
    for address in dal.get_all_addresses():
        print(address)
