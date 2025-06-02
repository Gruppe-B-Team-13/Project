from data_access.base_dal import BaseDataAccess
import model

class Review_DAL:
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.hotel_dal = Hotel_DAL()
