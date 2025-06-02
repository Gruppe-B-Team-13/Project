from data_access.base_dal import BaseDataAccess
import model

class Guest_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.address_dal = Address_DAL()

