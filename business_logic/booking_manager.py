import model
import data_access

class BookingManager:
    def __init__(self):
        self.booking_dal = data_access.Booking_DAL()
        self.invoice_dal = data_access.Invoice_DAL()

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

    def cancel_booking_and_invoice(self, booking_id: int) -> bool:
        success_booking = self.booking_dal.cancel_booking(booking_id)
        success_invoice = self.invoice_dal.cancel_invoice_by_booking_id(booking_id)
        return success_booking and success_invoice
