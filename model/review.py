class Review:
    def __init__(self, review_id, review_stars, review_comment, review_date, hotel):
        self.__review_id = review_id
        self.__review_stars = review_stars
        self.__review_comment = review_comment
        self.__review_date = review_date
        self.__hotel = hotel


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

    def __str__(self):
            return f"{self.__review_id}, {self.__review_stars} Sterne – {self.__review_comment} - {self.__review_date}"



