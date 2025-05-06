from datetime import date

class Review:
    def __init__(self, review_id, review_stars, review_comment, review_date, hotel):
        self.review_id = review_id
        self.review_stars = review_stars
        self.review_comment = review_comment
        self.review_date = review_date
        self.hotel = hotel

    @property
    def review_id(self):
        return self.__review_id

    @property
    def review_stars(self):
        return self.__review_stars

    @property
    def review_comment(self):
        return self.__review_comment

    @property
    def review_date(self):
        return self.__review_date

    @property
    def hotel(self):
        return self.__hotel

    @review_id.setter
    def review_id(self, value):
        self.__review_id = value

    @review_stars.setter
    def review_stars(self, value):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Die Bewertung muss eine ganze Zahl zwischen 1 und 5 sein.")
        self.__review_stars = value

    @review_comment.setter
    def review_comment(self, value):
        if not isinstance(value, str):
            raise TypeError("Der Kommentar muss ein String sein.")
        self.__review_comment = value.strip()

    @review_date.setter
    def review_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Das Bewertungsdatum muss vom Typ datetime.date sein.")
        self.__review_date = value

    @hotel.setter
    def hotel(self, value):
        if not isinstance(value, Hotel):
            raise TypeError("Das Hotel muss ein Objekt der Klasse Hotel sein.")
        self.__hotel = value

    def __str__(self):
        return (
            f"{self.__review_id}, {self.__review_stars} Sterne – "
            f"{self.__review_comment} - {self.__review_date} - "
            f"Hotel: {self.__hotel.name}"
        )
