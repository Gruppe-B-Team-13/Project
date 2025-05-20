#invoice_dal.py

from data_access.base_dal import BaseDataAccess
from model.invoice import Invoice # Sicherstellen, dass diese Klasse wirklich existiert
import datetime

class Invoice_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        
    def add_invoice(self, invoice: Invoice) -> int:
        sql = """
            INSERT INTO Invoice (booking_id, guest_id, invoice_date, total_amount, is_paid)
            VALUES (?, ?, ?, ?, ?)
        """


        params = (

            invoice_booking_id,
            invoice_guest_id,
            invoice_invoice_date.isoformat(), # ISO-Format fpr SQLite
            invoice_total_amount,
            int(invoice_is_paid), # Boolean, 1 = True, 0 = False

        )

        return self.execute(sql, params)

    def get_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        sql = """
            SELECT booking_id, guest_id, invoice_date, total_amount, is_paid
            FROM Invoice
            WHERE invoice_id = ?
        """

        result = self.fetchone(sql, (invoice_id,))
        if result:
            invoice_id, booking_id, guest_id, invoice_date, total_amount, is_paid = results
            return Invoice(invoice_id, booking_id, guest_id, datetime.date.fromisoformat(invoice_date), total_amount, bool(is_paid))
        return None

    def get_invoices_by_guest(self, guest_id: int) -> list[Invoice]:
        sql = """
            SELECT invoice_id, booking_id, guest_id, invoice_date, total_amount, is_paid
            FROM Invoice
            WHERE guest_id = ?
        """
        results = self.fetchall(sql, (guest_id,))
        return [
            Invoice(invoice_id, booking_id, guest_id, datetime.date.fromisoformat(invoice_date), total_amount, bool(is_paid))
            for invoice_id, booking_id, guest_id, invoice_date, total_amount, is_paid in results
        ]

    def get_all_invoices(self) -> list[Invoice]:
        sql = "SELECT invoice_id, booking_id, guest_id, invoice_date, total_amount, is_paid FROM Invoice"
        results = self.fetchall(sql)
        return [
            Invoice(invoice_id, booking_id, guest_id, datetime.date.fromisoformat(invoice_date), total_amount, bool(is_paid))
            for invoice_id, booking_id, guest_id, invoice_date, total_amount, is_paid in results
        ]

    def remove_invoice_by_id(self, invoice_id: int) -> bool:
        sql = "DELETE FROM Invoice WHERE invoice_id = ?"
        return self.execute(sql, (invoice_id,))