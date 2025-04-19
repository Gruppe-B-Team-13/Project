Class Review:
    def __init__(self, review_text, review_rating):
        self.__review_text = review_text
        self.__review_rating = review_rating


    @property
    def review_text(self):
        return self.__review_text

    @property
    def review_rating(self):
        return self.__review_rating
