from data_access.base_dal import BaseDataAccess
import model

class Invoice_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

