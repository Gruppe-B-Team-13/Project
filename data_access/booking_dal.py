# data_access/booking_dal.py

from data_access.base_dal import BaseDataAccess
from model.booking import Booking
from datetime import date

class Booking_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def add_booking(self, booking: Booking) -> int:
        sql = """
            INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date.isoformat(),
            booking.check_out_date.isoformat(),
            int(booking.is_cancelled)
        )
        lastrowid, _ = self.execute(sql, params)
        return lastrowid

    def get_booking_by_id(self, booking_id: int) -> Booking | None:
        sql = """
            SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled
            FROM Booking
            WHERE booking_id = ?
        """
        result = self.fetchone(sql, (booking_id,))
        if result:
            booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled = result
            return Booking(
                booking_id,
                guest_id,
                room_id,
                date.fromisoformat(check_in_date),
                date.fromisoformat(check_out_date),
                bool(is_cancelled)
            )
        return None

    def get_bookings_by_guest(self, guest_id: int) -> list[Booking]:
        sql = """
            SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled
            FROM Booking
            WHERE guest_id = ?
        """
        results = self.fetchall(sql, (guest_id,))
        return [
            Booking(bid, gid, rid, date.fromisoformat(checkin), date.fromisoformat(checkout), bool(cancelled))
            for bid, gid, rid, checkin, checkout, cancelled in results
        ]

    def get_all_bookings(self) -> list[Booking]:
        sql = "SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled FROM Booking"
        results = self.fetchall(sql)
        return [
            Booking(bid, gid, rid, date.fromisoformat(checkin), date.fromisoformat(checkout), bool(cancelled))
            for bid, gid, rid, checkin, checkout, cancelled in results
        ]

    def cancel_booking(self, booking_id: int) -> bool:
        sql = "UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0

    def delete_booking(self, booking_id: int) -> bool:
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0
