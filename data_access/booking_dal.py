# data_access/booking_dal.py

from data_access.base_dal import BaseDataAccess
import model
from datetime import date

class Booking_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def add_booking(self, booking: model.Booking) -> int:
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

    def get_booking_by_id(self, booking_id: int) -> model.Booking | None:
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

    def get_bookings_by_guest(self, guest_id: int) -> list[model.Booking]:
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

    def get_all_bookings(self) -> list[model.Booking]:
        sql = """
            SELECT 
                Booking.booking_id,
                Booking.check_in_date,
                Booking.check_out_date,
                Booking.booking_date,
                Booking.total_amount,
                Booking.is_cancelled,

                Guest.guest_id,
                Guest.first_name,
                Guest.last_name,
                Guest.email,
                Guest.phone_number,

                Address.address_id,
                Address.street,
                Address.house_number,
                Address.city,
                Address.zip_code,
                Address.country,

                Room.room_id,
                Room.room_number,
                Room.price_per_night,

                Hotel.hotel_id,
                Hotel.name,
                Hotel.stars,

                Room_Type.room_type_id,
                Room_Type.description,
                Room_Type.max_guests,
                Room_Type.room_type_name
            FROM Booking
            JOIN Guest ON Booking.guest_id = Guest.guest_id
            JOIN Address ON Guest.address_id = Address.address_id
            JOIN Room ON Booking.room_id = Room.room_id
            JOIN Hotel ON Room.hotel_id = Hotel.hotel_id
            JOIN Room_Type ON Room.room_type_id = Room_Type.room_type_id
            WHERE Booking.is_cancelled IN (0, 1)
        """
        results = self.fetchall(sql)
        bookings = []

        for row in results:
            (
                booking_id, check_in, check_out, booking_date, total_amount, is_cancelled,
                guest_id, first_name, last_name, email, phone_number,
                address_id, street, house_number, city, zip_code, country,
                room_id, room_number, price_per_night,
                hotel_id, hotel_name, hotel_stars,
                room_type_id, room_description, max_guests, room_type_name
            ) = row

            booking_date = date.fromisoformat(booking_date)  # <- FIX

            address = model.Address(address_id, street, house_number, city, zip_code, country)
            guest = model.Guests(guest_id, first_name, last_name, email, phone_number, address)
            hotel = model.Hotel(hotel_id, hotel_name, address, hotel_stars)
            room_type = model.RoomType(room_type_id, room_description, max_guests, room_type_name)
            room = model.Room(room_id, room_number, price_per_night, hotel, room_type)

            booking = model.Booking(
                booking_id,
                check_in,
                check_out,
                booking_date,
                total_amount,
                room,
                guest,
                is_cancelled
            )
            bookings.append(booking)


        return bookings




    def cancel_booking(self, booking_id: int) -> bool:
        sql = "UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0

    def delete_booking(self, booking_id: int) -> bool:
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0
