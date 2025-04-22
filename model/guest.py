class Guests:
    __next_id = 1  

    def __init__(self,first_name, last_name, email, phone_number, address, loyalty_points=0, booking_history=None):
        self.__guest_id = Guests.__next_id
        Guests.__next_id += 1  
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__loyalty_points = loyalty_points
        self.__booking_history = booking_history if booking_history is not None else []
        
    @property
    def guest_id(self):
        return self.__guest_id
        
    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

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
    def loyalty_points(self):
        return self.__loyalty_points

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def deduct_points(self, points):
        if points > self.__loyalty_points:
            print("Nicht genügend Treuepunkte vorhanden.")
            return
        self.__loyalty_points -= points

    def add_points(self, points):
        self.__loyalty_points += points

    def get_guest_summary(self):
        return f"{self.__guest_id} - Name: {self.__first_name} {self.__last_name} - Email: {self.__email} - Telefonnummer: {self.__phone_number} - Adresse: {self.__address} - Treuepunkte: {self.__loyalty_points}"