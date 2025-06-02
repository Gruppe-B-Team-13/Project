import model
import data_access

class InvoiceManager:
    def __init__(self):
        self.invoice_dal = data_access.invoice_dal

    def create_invoice_from_booking(self, booking) -> int:
        """
        Erstellt eine Rechnung aus einer Buchung, falls das Check-out-Datum erreicht ist.
        Gibt die erzeugte invoice_id zurück.
        """
        if date.today() < booking.check_out_date:
            raise ValueError("Rechnung kann erst nach Check-out erstellt werden.")

        invoice = Invoice(
            invoice_id=None,
            booking=booking,                # ✅ jetzt korrekt: ganzes Objekt
            issue_date=date.today()
        )
        return self.invoice_dal.add_invoice(invoice)

    def get_invoice_by_id(self, invoice_id: int):
        return self.invoice_dal.get_invoice_by_id(invoice_id)

    def get_all_invoices(self):
        return self.invoice_dal.get_all_invoices()

    def get_invoices_by_guest(self, guest_id: int):
        return self.invoice_dal.get_invoices_by_guest(guest_id)

    def delete_invoice(self, invoice_id: int) -> bool:
        return self.invoice_dal.remove_invoice_by_id(invoice_id)
