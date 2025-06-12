import model
import data_access

class BookingManager:
    def __init__(self):
        self.booking_dal = data_access.Booking_DAL()
        self.invoice_dal = data_access.Invoice_DAL()
        self.room_dal = data_access.Room_DAL()

    def get_all_bookings(self) -> list[model.Booking]:
        return self.booking_dal.get_all_bookings()

    def create_booking(self, check_in_date: str, check_out_date: str, booking_date: str, room_id: int, guest_id: int):
                       
        room = self.room_dal.get_room_by_id(room_id)
        if not room:
            raise ValueError("Zimmer nicht gefunden.")

        nights = self.calculate_nights(check_in_date, check_out_date)
        adjusted_price = self.apply_seasonal_price(room.price_per_night, check_in_date)
        total_amount = adjusted_price * nights

        return self.booking_dal.create_booking(
            guest_id=guest_id,
            room_id=room_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            total_amount=total_amount,
            booking_date=booking_date
        )

    def apply_seasonal_price(self, base_price: float, check_in_date: str) -> float:
        if check_in_date.month in [6, 7, 8]:  # Hochsaison
            return round(base_price * 1.2, 2)
        elif check_in_date.month in [1, 2, 11]:  # Nebensaison
            return round(base_price * 0.85, 2)
        return base_price


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

    def calculate_nights(self, check_in_date: str, check_out_date: str) -> int:
        if check_out_date <= check_in_date:
            raise ValueError("Check-Out-Datum muss nach dem Check-In-Datum liegen.")
        return (check_out_date - check_in_date).days