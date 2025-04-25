from data_access.base_dal import DatabaseConnection
from model.hotel import Hotel
from data_access.address_dal import Address_DAL

class Hotel_DAL:
    def __init__(self):
        self.connection = DatabaseConnection().connect()
        self.address_dal = Address_DAL()

    def get_all_hotels(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT hotel_id, name, address_id, stars FROM Hotel")
        rows = cursor.fetchall()

        hotels = []
        for row in rows:
            address = self.address_dal.get_address_by_id(row[2])
            hotel = Hotel(
                hotel_id=row[0],
                name=row[1],
                address=address,
                stars=row[3]
            )
            hotels.append(hotel)
        return hotels

    def get_hotel_by_id(self, hotel_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT hotel_id, name, address_id, stars FROM Hotel WHERE hotel_id = ?", (hotel_id,))
        row = cursor.fetchone()
        if row:
            address = self.address_dal.get_address_by_id(row[2])
            return Hotel(
                hotel_id=row[0],
                name=row[1],
                address=address,
                stars=row[3]
            )
        return None

if __name__ == "__main__":
    dal = Hotel_DAL()
    for hotel in dal.get_all_hotels():
        print(hotel)
