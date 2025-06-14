import model
import data_access

class GuestManager:
    def __init__(self):
        self.guest_dal = data_access.Guest_DAL()
        self.booking_dal = data_access.Booking_DAL()

    def find_guest_by_name(self, first_name: str, last_name: str) -> model.Guests | None:
        return self.guest_dal.find_guest(first_name, last_name)

    def create_guest(self, first_name: str, last_name: str, email: str, phone_number: str, address_id: int) -> model.Guests:
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

    def get_all_bookings(self) -> list[model.Booking]:
        return self.booking_dal.get_all_bookings()

    def update_booking_check_in(self, booking_id: int, new_date: date) -> bool:
        return data_access.Booking_DAL().update_check_in_date(booking_id, new_date)

    def update_booking_check_out(self, booking_id: int, new_date: date) -> bool:
        return data_access.Booking_DAL().update_check_out_date(booking_id, new_date)

    def update_booking_room(self, booking_id: int, new_room_id: int) -> bool:
        return data_access.Booking_DAL().update_room_id(booking_id, new_room_id)

    def update_booking_total_amount(self, booking_id: int, new_amount: float) -> bool:
        return data_access.Booking_DAL().update_total_amount(booking_id, new_amount)

    def update_booking_cancelled(self, booking_id: int, cancelled: bool) -> bool:
        return data_access.Booking_DAL().update_is_cancelled(booking_id, cancelled)



