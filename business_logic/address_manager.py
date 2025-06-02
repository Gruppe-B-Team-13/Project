import model
import data_access

class AddressManager:

    def __init__(self):
        self.__address_dal = data_access.Address_DAL()

