import model
import data_access
from datetime import date 

class GuestManager:
    def __init__(self):
        self.guest_dal = data_access.Guest_DAL()
        self.booking_dal = data_access.Booking_DAL()

    def find_guest_by_name(self, first_name: str, last_name: str) -> model.Guests | None:
        return self.guest_dal.find_guest(first_name, last_name)

    def create_guest(self, first_name: str, last_name: str, email: str, phone_number: str, address_id: int) -> model.Guests:
        guest = self.find_guest_by_name(first_name, last_name)
        if guest:
            return guest
        return self.guest_dal.create_guest(first_name, last_name, email, phone_number, address_id)

    def get_guest_by_id(self, guest_id: int) -> model.Guests | None:
        return self.guest_dal.get_guest_by_id(guest_id)

    def change_guest_first_name(self, guest_id: int, new_first_name: str) -> bool:
        return self.guest_dal.update_first_name(guest_id, new_first_name)

    def change_guest_last_name(self, guest_id: int, new_last_name: str) -> bool:
        return self.guest_dal.update_last_name(guest_id, new_last_name)


    def change_guest_address_id(self, guest_id: int, new_address_id: int) -> bool:
        return self.guest_dal.update_address_id(guest_id, new_address_id)


    def change_guest_email(self, guest_id: int, new_email: str) -> bool:
        return self.guest_dal.update_email(guest_id, new_email)



    def change_guest_phone_number(self, guest_id: int, new_phone_number: str) -> bool:
        return self.guest_dal.update_phone_number(guest_id, new_phone_number)
        


