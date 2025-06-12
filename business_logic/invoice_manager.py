from datetime import date
import model
import data_access

class InvoiceManager:
    def __init__(self, db_path: str = None):
        self.invoice_dal = data_access.Invoice_DAL(db_path)

    def create_invoice(self, booking: model.Booking, issue_date: date, total_amount: float) -> model.Invoice:
        if not isinstance(booking, model.Booking):
            raise TypeError("booking muss ein Objekt der Klasse Booking sein.")
        if not isinstance(issue_date, date):
            raise TypeError("issue_date muss ein Datum sein.")
        if not isinstance(total_amount, (int, float)):
            raise TypeError("total_amount muss eine Zahl sein.")
        if total_amount <= 0:
            raise ValueError("Der Rechnungsbetrag muss größer als 0 sein.")

        return self.invoice_dal.create_invoice(booking.booking_id, issue_date, total_amount)

    def get_filtered_invoices(self, invoice_id: int = None, booking_id: int = None) -> list[model.Invoice]:
        return self.invoice_dal.get_invoice_filtered(invoice_id=invoice_id, booking_id=booking_id)

