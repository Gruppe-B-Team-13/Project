import model
import data_access

class GuestManager:
    def __init__(self):
        self.guest_dal = data_access.Guest_DAL()

    def find_guest_by_name(self, first_name: str, last_name: str) -> model.Guests | None:
        return self.guest_dal.find_guest(first_name, last_name)

    def create_guest(self, first_name: str, last_name: str, email: str, phone_number: str, address_id: int) -> model.Guests:
        return self.guest_dal.create_guest(first_name, last_name, email, phone_number, address_id)

    def get_guest_by_id(self, guest_id: int) -> model.Guests | None:
            return self._guest_dal.get_guest_by_id(guest_id)

    def add_loyalty_points_to_guest(self, guest_id: int, points: int):
        guest = self.find_by_id(guest_id)
        if guest:
            guest.add_points (points)
            return True
        return False

    def deduct_loyalty_points_from(self, guest_id: int, points: int):
        guest = self.find_by_id(guest_id)
        if guest:
            guest.deduct_points(points)
            return True
        return False


    def find_by_email(self, email: str):
        return [g for g in self._guests if g.email.lower() == email.lower()]

    def find_by_name(self, name: str):
        return [g for g in self._guests if g.name.lower() == name.lower()]

    def print_all_summaries(self):
        for g in self._guests:
            print(g.get_guest_summary())