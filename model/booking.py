class Bookings:
    def __init__(self, booking_id, check_in_date, check_out_date, is_cancelled, booking_date, total_amount, room_id, guest_id=None, guest_name=None, payment_id=None, currency_id=None):
        self.__booking_id = booking_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = is_cancelled
        self.__booking_date = booking_date
        self.__total_amount = total_amount
        self.__room_id = room_id
        self.__guest_id = guest_id
        self.__guest_name = guest_name
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
    def guest_id(self):
        return self.__guest_id
    
    @property
    def guest_name(self):
        return self.__guest_name

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
        return f"Buchung {self.__booking_id}: {self.__guest_name} - {self.__check_in_date} bis {self.__check_out_date} - Zimmer {self.__room_id} - Betrag: CHF {self.__total_amount} - Storniert: {storniert}"
