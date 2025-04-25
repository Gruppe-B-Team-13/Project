from data_access.base_dal import DatabaseConnection
from model.guest import Guests
from data_access.address_dal import Address_DAL

class Guest_DAL:
    def __init__(self):
        self.connection = DatabaseConnection().connect()
        self.address_dal = Address_DAL()

    def get_all_guests(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT first_name, last_name, email, phone_number, address_id, loyalty_points FROM Guest")
        rows = cursor.fetchall()

        guests = []
        for row in rows:
            address = self.address_dal.get_address_by_id(row[4])
            guest = Guests(
                first_name=row[0],
                last_name=row[1],
                email=row[2],
                phone_number=row[3],
                address=address,
                loyalty_points=row[5]
            )
            guests.append(guest)
        return guests

if __name__ == "__main__":
    dal = Guest_DAL()
    for guest in dal.get_all_guests():
        print(guest.get_guest_summary())
