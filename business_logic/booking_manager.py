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






    #Methoden zur Buchungsbearbeitung via GuestManager

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
        return self.booking_dal.update_check_in_date(booking_id, new_date)

    def update_booking_check_out(self, booking_id: int, new_date: date) -> bool:
        return self.booking_dal.update_check_out_date(booking_id, new_date)

    def update_booking_room(self, booking_id: int, new_room_id: int) -> bool:
        return self.booking_dal.update_room_id(booking_id, new_room_id)

    def update_booking_total_amount(self, booking_id: int, new_amount: float) -> bool:
        return self.booking_dal.update_total_amount(booking_id, new_amount)

    def update_booking_cancelled(self, booking_id: int, cancelled: bool) -> bool:
        return self.booking_dal.update_is_cancelled(booking_id, cancelled)

    def get_booking_by_id(self, booking_id: int) -> model.Booking | None:
        return self.booking_dal.get_booking_by_id(booking_id)

# Alle Buchungen dieses Gastes
    def get_bookings_for_guest(self, guest_id):
        return self.booking_dal.get_bookings_by_guest(guest_id)


# Neue Buchung erstellen (aus Sicht des Gastes)
    def add_booking_for_guest(self, booking):
        if booking.guest is None or booking.guest.guest_id is None:
            raise ValueError("Gast-ID darf nicht leer sein.")
        return self.booking_dal.create_booking(
            booking.guest.guest_id,
            booking.room.room_id,
            booking.check_in_date,
            booking.check_out_date,
            booking.total_amount,
            booking.booking_date
        )


# Check-in-Datum aktualisieren (aus Sicht des Gastes)
    def update_check_in_date_for_guest(self, booking_id, guest_id, new_date):
        booking = self.booking_dal.get_booking_by_id(booking_id)
        if booking and booking.guest.guest_id == guest_id:
            return self.booking_dal.update_check_in_date(booking_id, new_date)
        else:
            raise PermissionError("Zugriff verweigert.")


# Check-out-Datum aktualisieren (aus Sicht des Gastes)
    def update_check_out_date_for_guest(self, booking_id, guest_id, new_date):
        booking = self.booking_dal.get_booking_by_id(booking_id)
        if booking and booking.guest.guest_id == guest_id:
            return self.booking_dal.update_check_out_date(booking_id, new_date)
        else:
            raise PermissionError("Zugriff verweigert.")


# Zimmer ändern (aus Sicht des Gastes)
    def update_room_for_guest(self, booking_id, guest_id, new_room_id):
        booking = self.booking_dal.get_booking_by_id(booking_id)
        if booking and booking.guest.guest_id == guest_id:
            return self.booking_dal.update_room(booking_id, new_room_id)
        else:
            raise PermissionError("Zugriff verweigert.")


# Betrag ändern (aus Sicht des Gastes)
    def update_total_amount_for_guest(self, booking_id, guest_id, new_total_amount):
        booking = self.booking_dal.get_booking_by_id(booking_id)
        if booking and booking.guest.guest_id == guest_id:
            return self.booking_dal.update_total_amount(booking_id, new_total_amount)
        else:
            raise PermissionError("Zugriff verweigert.")


# Buchung stornieren (aus Sicht des Gastes)
    def cancel_booking_for_guest(self, booking_id, guest_id):
        booking = self.booking_dal.get_booking_by_id(booking_id)
        if booking and booking.guest.guest_id == guest_id:
            return self.booking_dal.remove_booking(booking_id)
        else:
            raise PermissionError("Zugriff verweigert.")