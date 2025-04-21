Class Bookings:
    def __init__(self, booking_date, booking_time):
        self.__booking_date = booking_date
        self.__booking_time = booking_time
        self.__booking_id = []
        self.__booking_status = []
        self.__guest_id = []
        self.__room_id = []
        self.__service_id = []
        self.__payment_id = []
        self.__currency_id = []
        self.__total_price = []
        self.__guest_name = []

    @property
    def booking_date(self):
        return self.__booking_date

    @property
    def booking_time(self):
        return self.__booking_time