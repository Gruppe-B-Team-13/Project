Class Guests:
    def __init__(self, first_name, last_name, email, phone_number, address, guest-id, loyalty_points, booking_history):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__guest-id = []
        self.__loyalty_points = loyalty_points

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def address(self):
        return self.__address

    @property
    def guest-id(self):
        return self.__guest-id