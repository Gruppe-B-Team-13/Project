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
        self.__original_total_amount = total_amount
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
    def original_total_amount(self):
        return self.__original_total_amount

    @property
    def available_points(self):
        return self.__guest.loyalty_points

    @property
    def applied_points(self):
        return min(self.__total_amount, self.available_points)

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
        if self.applied_points <= 0:
            print("Keine Treuepunkte verfügbar.")
            return

        used_points = self.applied_points
        self.__guest.deduct_points(used_points)
        self.__total_amount -= used_points
        print(f"{used_points} Punkte verwendet. Neuer Betrag: CHF {self.__total_amount:.2f}")



    def add_loyalty_points_to_guest(self):
        if self.original_total_amount < 100:
            print("Keine Treuepunkte hinzugefügt, da der Mindestbetrag 100 CHF beträgt.")
            return
        points = int(self.original_total_amount // 10)  
        self.__guest.add_points(points)
        print(f"{points} Punkte hinzugefügt. Neuer Punktestand: {self.__guest.loyalty_points}")
