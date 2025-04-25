from data_access.base_dal import DatabaseConnection
from model.hotel import Hotel

class Hotel_DAL:
    def __init__(self):
        self.connection = DatabaseConnection().connect()

    def get_all_hotels(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Hotel")
        rows = cursor.fetchall()
        return [Hotel(*row) for row in rows]

if __name__ == "__main__":
    dal = Hotel_DAL()
    for hotel in dal.get_all_hotels():
        print(hotel)
