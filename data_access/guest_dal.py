from data_access.base_dal import BaseDataAccess
import model
import data_access

class Guest_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.address_dal = data_access.Address_DAL(db_path)

    def find_guest(self, first_name: str, last_name: str) -> model.Guests | None:
        sql = """
            SELECT guest_id, first_name, last_name, email, phone_number, address_id
            FROM Guest
            WHERE first_name = ? AND last_name = ?
        """
        result = self.fetchone(sql, (first_name, last_name))
        if result:
            guest_id, first_name, last_name, email, phone_number, address_id = result
            address = self.address_dal.get_address_by_id(address_id)
            return model.Guests(guest_id, first_name, last_name, email, phone_number, address)
        return None

    def create_guest(self, first_name: str, last_name: str, email: str, phone_number: str, address_id: int) -> model.Guests:
        sql = """
            INSERT INTO Guest (first_name, last_name, email, phone_number, address_id)
            VALUES (?, ?, ?, ?, ?)
        """
        guest_id, _ = self.execute(sql, (first_name, last_name, email, phone_number, address_id))
        address = self.address_dal.get_address_by_id(address_id)
        return model.Guests(guest_id, first_name, last_name, email, phone_number, address)

    def get_guest_by_id(self, guest_id: int) -> model.Guests | None:
        sql = """
            SELECT Guest.guest_id, Guest.first_name, Guest.last_name,
                Guest.email, Guest.phone_number,
                Address.address_id, Address.street, Address.house_number,
                Address.city, Address.zip_code, Address.country
            FROM Guest
            JOIN Address ON Guest.address_id = Address.address_id
            WHERE Guest.guest_id = ?
        """
        result = self.fetchone(sql, (guest_id,))
        
        if result:
            (guest_id, first_name, last_name, email, phone_number,
            address_id, street, house_number, city, zip_code, country) = result
            
            address = model.Address(address_id, street, house_number, city, zip_code, country)
            return model.Guests(guest_id, first_name, last_name, email, phone_number, address)
        else:
            return None


def update_phone_number(self, guest_id: int, new_phone_number: str) -> bool:
    sql = "UPDATE Guest SET phone_number = ? WHERE guest_id = ?"
    _, rowcount = self.execute(sql, (new_phone_number, guest_id))
    return rowcount > 0
