# data_access/booking_dal.py

from data_access.base_dal import BaseDataAccess
import model
import data_access
from datetime import date

class Booking_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self._guest_dal = data_access.Guest_DAL(db_path)
        self._room_dal = data_access.Room_DAL(db_path)

    def create_booking(self, guest_id: int, room_id: int, check_in_date, check_out_date, total_amount: float, booking_date) -> model.Booking:
        sql = """
            INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, total_amount, booking_date, is_cancelled)
            VALUES (?, ?, ?, ?, ?, ?, 0)
        """
        booking_id, _ = self.execute(sql, (guest_id, room_id, check_in_date, check_out_date, total_amount, booking_date))

        # Hole zugehörige Objekte
        guest = self._guest_dal.get_guest_by_id(guest_id)
        room = self._room_dal.get_room_by_id(room_id)

        return model.Booking(booking_id, check_in_date, check_out_date, booking_date, total_amount, room, guest, False)

    def get_booking_by_id(self, booking_id: int) -> model.Booking | None:
        sql = """
            SELECT 
                b.booking_id,
                b.check_in_date,
                b.check_out_date,
                b.booking_date,
                b.total_amount,
                b.is_cancelled,

                g.guest_id,
                g.first_name,
                g.last_name,
                g.email,
                g.phone_number,

                a.address_id,
                a.street,
                a.house_number,
                a.city,
                a.zip_code,
                a.country,

                r.room_id,
                r.room_number,
                r.price_per_night,

                h.hotel_id,
                h.name,
                h.stars,

                rt.room_type_id,
                rt.description,
                rt.max_guests,
                rt.room_type_name
            FROM Booking b
            JOIN Guest g ON b.guest_id = g.guest_id
            JOIN Address a ON g.address_id = a.address_id
            JOIN Room r ON b.room_id = r.room_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            JOIN Room_Type rt ON r.room_type_id = rt.room_type_id
            WHERE b.booking_id = ?
        """

        result = self.fetchone(sql, (booking_id,))
        if not result:
            return None

        (
            booking_id, check_in, check_out, booking_date, total_amount, is_cancelled,
            guest_id, first_name, last_name, email, phone_number,
            address_id, street, house_number, city, zip_code, country,
            room_id, room_number, price_per_night,
            hotel_id, hotel_name, hotel_stars,
            room_type_id, room_description, max_guests, room_type_name
        ) = result

        # Falls Strings → in echte date-Objekte umwandeln
        if isinstance(check_in, str):
            check_in = date.fromisoformat(check_in)
        if isinstance(check_out, str):
            check_out = date.fromisoformat(check_out)
        if isinstance(booking_date, str):
            booking_date = date.fromisoformat(booking_date)

        address = model.Address(address_id, street, house_number, city, zip_code, country)
        guest = model.Guests(guest_id, first_name, last_name, email, phone_number, address)
        hotel = model.Hotel(hotel_id, hotel_name, address, hotel_stars)
        room_type = model.RoomType(room_type_id, room_description, max_guests, room_type_name)
        room = model.Room(room_id, room_number, price_per_night, hotel, room_type)

        return model.Booking(
            booking_id,
            check_in,
            check_out,
            booking_date,
            total_amount,
            room,
            guest,
            bool(is_cancelled)
        )

    def get_bookings_by_guest(self, guest_id: int) -> list[model.Booking]:
        sql = """
            SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled
            FROM Booking
            WHERE guest_id = ?
        """
        results = self.fetchall(sql, (guest_id,))
        return [
            model.Booking(bid, gid, rid, date.fromisoformat(checkin), date.fromisoformat(checkout), bool(cancelled))
            for bid, gid, rid, checkin, checkout, cancelled in results
        ]

    def get_all_bookings(self) -> list[model.Booking]:
        sql = """
            SELECT 
                b.booking_id,
                b.check_in_date,
                b.check_out_date,
                b.booking_date,
                b.total_amount,
                b.is_cancelled,

                g.guest_id,
                g.first_name,
                g.last_name,
                g.email,
                g.phone_number,

                a.address_id,
                a.street,
                a.house_number,
                a.city,
                a.zip_code,
                a.country,

                r.room_id,
                r.room_number,
                r.price_per_night,

                h.hotel_id,
                h.name,
                h.stars,

                rt.room_type_id,
                rt.description,
                rt.max_guests,
                rt.room_type_name
            FROM Booking b
            JOIN Guest g ON b.guest_id = g.guest_id
            JOIN Address a ON g.address_id = a.address_id
            JOIN Room r ON b.room_id = r.room_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            JOIN Room_Type rt ON r.room_type_id = rt.room_type_id
            WHERE b.is_cancelled IN (0, 1)
            ORDER BY b.booking_id ASC
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

            # Konvertiere Strings in echte Datumsobjekte (falls nötig)
            if isinstance(booking_date, str):
                booking_date = date.fromisoformat(booking_date)
            if isinstance(check_in, str):
                check_in = date.fromisoformat(check_in)
            if isinstance(check_out, str):
                check_out = date.fromisoformat(check_out)

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
                bool(is_cancelled)
            )

            bookings.append(booking)

        return bookings


    def cancel_booking(self, booking_id: int) -> bool:
        sql = "UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0


    def update_check_in_date(self, booking_id: int, new_date: date) -> bool:
        sql = "UPDATE Booking SET check_in_date = ? WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (new_date, booking_id))
        return rowcount > 0

# Änderung des Check-out-Datums
    def update_check_out_date(self, booking_id: int, new_date: date) -> bool:
        sql = "UPDATE Booking SET check_out_date = ? WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (new_date, booking_id))
        return rowcount > 0

# Änderung des Betrags
    def update_total_amount(self, booking_id: int, new_amount: float) -> bool:
        sql = "UPDATE Booking SET total_amount = ? WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (new_amount, booking_id))
        return rowcount > 0

# Änderung der Zimmer-ID (Zimmerwechsel)
    def update_room(self, booking_id: int, new_room_id: int) -> bool:
        sql = "UPDATE Booking SET room_id = ? WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (new_room_id, booking_id))
        return rowcount > 0

# Änderung des Gastes (z. B. Umbuchung)
    def update_guest(self, booking_id: int, new_guest_id: int) -> bool:
        sql = "UPDATE Booking SET guest_id = ? WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (new_guest_id, booking_id))
        return rowcount > 0

