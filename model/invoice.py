from datetime import date

class Invoice:
    def __init__(self, invoice_id, booking, issue_date):
        self.invoice_id = invoice_id
        self.booking = booking
        self.issue_date = issue_date
        self.total_amount = booking.total_amount

    @property
    def invoice_id(self):
        return self.__invoice_id

    @property
    def booking(self):
        return self.__booking

    @property
    def booking_id(self):
        return self.__booking.booking_id

    @property
    def issue_date(self):
        return self.__issue_date

    @property
    def total_amount(self):
        return self.__total_amount

    @invoice_id.setter
    def invoice_id(self, value):
        self.__invoice_id = value

    @booking.setter
    def booking(self, value):
        if not isinstance(value, Bookings):
            raise TypeError("booking muss ein Objekt der Klasse Bookings sein.")
        self.__booking = value

    @issue_date.setter
    def issue_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Das Rechnungsdatum muss im Format - date(jahr, monat, tag) - sein.")
        self.__issue_date = value

    def __str__(self):
        return (
            f"Rechnung {self.__invoice_id} – Buchung {self.booking_id} – "
            f"Datum: {self.__issue_date} – Betrag: CHF {self.total_amount:.2f}"
        )
