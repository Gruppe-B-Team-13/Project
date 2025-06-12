from data_access.base_dal import BaseDataAccess
import model
import data_access
from datetime import date

class Invoice_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self._booking_dal = data_access.Booking_DAL(db_path)

    def get_invoice_filtered(
        self,
        invoice_id: int = None,
        booking_id: int = None
    ) -> list[model.Invoice]:
        sql = """
            SELECT invoice_id, booking_id, issue_date, total_amount
            FROM Invoice
            WHERE 1 = 1
        """
        params = []

        if invoice_id is not None:
            sql += " AND invoice_id = ?"
            params.append(invoice_id)

        if booking_id is not None:
            sql += " AND booking_id = ?"
            params.append(booking_id)

        results = self.fetchall(sql, tuple(params))
        invoices: list[model.Invoice] = []

        for inv_id, book_id, issue_date, total in results:
            booking = self._booking_dal.get_booking_by_id(book_id)
            invoice = model.Invoice(inv_id, booking, issue_date, total)
            invoices.append(invoice)

        return invoices
        
    def create_invoice(self, booking_id: int, issue_date: date, total_amount: float) -> model.Invoice:
        sql = """
            INSERT INTO Invoice (booking_id, issue_date, total_amount)
            VALUES (?, ?, ?)
        """
        invoice_id, _ = self.execute(sql, (booking_id, issue_date, total_amount))
        booking = self._booking_dal.get_booking_by_id(booking_id)
        return model.Invoice(invoice_id, booking, issue_date, total_amount)

    def cancel_invoice_by_booking_id(self, booking_id: int) -> bool:
        sql = "UPDATE Invoice SET total_amount = 0 WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0
