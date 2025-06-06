import model
import data_access

class BookingManager:
    def __init__(self):
        self.booking_dal = data_access.Booking_DAL()

    def get_all_bookings(self) -> list[model.Booking]:
        return self.booking_dal.get_all_bookings()

    def create_booking(self, guest_id: int, room_id: int, check_in_date, check_out_date, total_amount: float, booking_date) -> model.Booking:
        return self.booking_dal.create_booking(guest_id, room_id, check_in_date, check_out_date, total_amount, booking_date)


    def remove_booking(self, booking: model.Booking):
        self.__bookings = [b for b in self.__bookings if b.booking_id != booking_id]


    def get_active_bookings(self):
        return [b for b in self.__bookings if not b.is_cancelled]

    def get_cancelled_bookings(self):
        return [b for b in self.__bookings if b.is_cancelled]

    def get_bookings_by_guest(self, guest_id: int):
        return [b for b in self.__bookings if b.guest_id == guest_id]

    def find_bookings_by_room(self, room_id: int):
        return [b for b in self.__bookings if b.room_id == room_id]

    def cancel_booking(self, booking_id: int):
        for booking in self.__bookings:
                if booking.booking_id == booking_id:
                    booking.is_cancelled = True
                    return True
        return False