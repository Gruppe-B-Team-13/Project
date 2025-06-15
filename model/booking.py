from datetime import date
import model

class Booking:
    def __init__(self, booking_id, check_in_date, check_out_date, booking_date, total_amount, room, guest, is_cancelled=False):
        self.booking_id = booking_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.is_cancelled = is_cancelled
        self.booking_date = booking_date
        self.total_amount = total_amount
        self.room = room
        self.guest = guest

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
    def room(self):
        return self.__room

    @property
    def guest(self):
        return self.__guest

    @booking_id.setter
    def booking_id(self, value):
        self.__booking_id = value

    @check_in_date.setter
    def check_in_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Das Check-in-Datum muss im Format - date(jahr, monat, tag) - sein.")
        if hasattr(self, "_Bookings__check_out_date") and self.__check_out_date is not None:
            if value >= self.__check_out_date:
                raise ValueError("Das Check-in-Datum muss vor dem Check-out-Datum liegen.")
        self.__check_in_date = value

    @check_out_date.setter
    def check_out_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Das Check-out-Datum muss im Format - date(jahr, monat, tag) - sein.")
        if hasattr(self, "_Bookings__check_in_date") and self.__check_in_date is not None:
            if value <= self.__check_in_date:
                raise ValueError("Das Check-out-Datum muss nach dem Check-in-Datum liegen.")
        self.__check_out_date = value

    @is_cancelled.setter
    def is_cancelled(self, value):
        self.__is_cancelled = value

    @booking_date.setter
    def booking_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Das Buchungsdatum muss im Format - date(jahr, monat, tag) - sein.")
        today = date.today()
        if value > today:
            raise ValueError("Das Buchungsdatum darf nicht in der Zukunft liegen.")
        if hasattr(self, "_Bookings__check_in_date") and self.__check_in_date is not None:
            if value > self.__check_in_date:
                raise ValueError("Das Buchungsdatum darf nicht nach dem Check-in-Datum liegen.")
        self.__booking_date = value

    @total_amount.setter
    def total_amount(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Der Betrag muss eine Zahl sein.")
        if value < 0:
            raise ValueError("Der Betrag darf nicht negativ sein.")
        self.__total_amount = float(value)

    @room.setter
    def room(self, value):
        if not isinstance(value, model.Room):
            raise TypeError("room muss ein Objekt der Klasse Room sein.")
        self.__room = value

    @guest.setter
    def guest(self, value):
        if not isinstance(value, model.Guests):
            raise TypeError("guest muss ein Objekt der Klasse Guest sein.")
        self.__guest = value

    def __str__(self):
        storniert = "Ja" if self.__is_cancelled else "Nein"
        return f"Buchung {self.__booking_id}: {self.__guest.get_full_name()} - {self.__check_in_date} bis {self.__check_out_date} - Zimmer {self.__room.get_room_number()} - Betrag: CHF {self.__total_amount} - Storniert: {storniert}"

    def get_booking_summary(self):
        storniert = "Ja" if self.__is_cancelled else "Nein"
        return (
            f"Buchung {self.__booking_id}\n"
            f"  Gast:     {self.__guest.get_full_name()}\n"
            f"  Zimmer:   {self.__room.get_room_number()}\n"
            f"  Zeitraum: {self.__check_in_date} bis {self.__check_out_date}\n"
            f"  Betrag:   CHF {self.__total_amount:.2f}\n"
            f"  Storniert: {storniert}"
        )


