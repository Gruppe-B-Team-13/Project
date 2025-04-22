class Bookings:
    __next_id = 1
    def __init__(self, check_in_date, check_out_date, is_cancelled, booking_date, total_amount, room_id, guest, payment_id=None, currency_id=None):
        self.__booking_id = Bookings.__next_id
        Bookings.__next_id += 1
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = is_cancelled
        self.__booking_date = booking_date
        self.__total_amount = total_amount
        self.__room_id = room_id
        self.__guest = guest
        self.__payment_id = payment_id
        self.__currency_id = currency_id

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def check_in_date(self):
        return self.__check_in_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @property
    def booking_date(self):
        return self.__booking_date

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def room_id(self):
        return self.__room_id

    @property
    def guest(self):
        return self.__guest
    
    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def currency_id(self):
        return self.__currency_id

    def cancel_booking(self):
        self.__is_cancelled = True
    
    def get_booking_summary(self):
        storniert = "Ja" if self.__is_cancelled else "Nein"
        return f"Buchung {self.__booking_id}: {self.__guest.get_full_name()} - {self.__check_in_date} bis {self.__check_out_date} - Zimmer {self.__room_id} - Betrag: CHF {self.__total_amount} - Storniert: {storniert}"
    
    def apply_loyalty_points_from_guest(self):
        available_points = self.__guest.loyalty_points
        if available_points <= 0:
            print("Keine Treuepunkte verfügbar.")
            return
        
        applied_points = min(self.__total_amount, available_points)
        self.__total_amount -= applied_points
        self.__guest.deduct_points(applied_points)
        
        print(f"{applied_points} Punkte verwendet. Neuer Betrag: CHF {self.__total_amount:.2f}")
