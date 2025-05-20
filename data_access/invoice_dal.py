# data_access/invoice_dal.py

from data_access.base_dal import BaseDataAccess
from model.invoice import Invoice
from datetime import date
from data_access.booking_dal import Booking_DAL

class Invoice_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.booking_dal = Booking_DAL(db_path)

    def add_invoice(self, invoice: Invoice) -> int:
        sql = """
            INSERT INTO Invoice (booking_id, invoice_date)
            VALUES (?, ?)
        """
        params = (
            invoice.booking.booking_id,
            invoice.issue_date.isoformat()
        )
        lastrowid, _ = self.execute(sql, params)
        return lastrowid

    def get_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        sql = """
            SELECT invoice_id, booking_id, invoice_date
            FROM Invoice
            WHERE invoice_id = ?
        """
        result = self.fetchone(sql, (invoice_id,))
        if result:
            invoice_id, booking_id, invoice_date = result
            booking = self.booking_dal.get_booking_by_id(booking_id)
            return Invoice(invoice_id, booking, date.fromisoformat(invoice_date))
        return None

    def get_all_invoices(self) -> list[Invoice]:
        sql = "SELECT invoice_id, booking_id, invoice_date FROM Invoice"
        results = self.fetchall(sql)
        invoices = []
        for invoice_id, booking_id, invoice_date in results:
            booking = self.booking_dal.get_booking_by_id(booking_id)
            invoices.append(Invoice(invoice_id, booking, date.fromisoformat(invoice_date)))
        return invoices

    def get_invoices_by_guest(self, guest_id: int) -> list[Invoice]:
        sql = """
            SELECT invoice_id, booking_id, invoice_date
            FROM Invoice
            JOIN Booking ON Invoice.booking_id = Booking.booking_id
            WHERE Booking.guest_id = ?
        """
        results = self.fetchall(sql, (guest_id,))
        invoices = []
        for invoice_id, booking_id, invoice_date in results:
            booking = self.booking_dal.get_booking_by_id(booking_id)
            invoices.append(Invoice(invoice_id, booking, date.fromisoformat(invoice_date)))
        return invoices

    def remove_invoice_by_id(self, invoice_id: int) -> bool:
        sql = "DELETE FROM Invoice WHERE invoice_id = ?"
        _, rowcount = self.execute(sql, (invoice_id,))
        return rowcount > 0
