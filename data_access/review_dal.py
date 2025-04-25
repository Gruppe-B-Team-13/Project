from data_access.base_dal import DatabaseConnection
from model.review import Review
from data_access.hotel_dal import Hotel_DAL
from model.hotel import Hotel

class Review_DAL:
    def __init__(self):
        self.connection = DatabaseConnection().connect()
        self.hotel_dal = Hotel_DAL()  # Erzeugt Zugriff auf Hotels

    def get_all_reviews(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT review_id, review_stars, review_comment, review_date, hotel_id FROM Review")
        rows = cursor.fetchall()

        reviews = []
        for row in rows:
            hotel_id = row[4]
            hotel = self.hotel_dal.get_hotel_by_id(hotel_id)  # Hotel-Objekt laden
            review = Review(
                review_id=row[0],
                review_stars=row[1],
                review_comment=row[2],
                review_date=row[3],
                hotel=hotel
            )
            reviews.append(review)
        return reviews

if __name__ == "__main__":
    dal = Review_DAL()
    for review in dal.get_all_reviews():
        print(review)
