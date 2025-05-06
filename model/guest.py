class Guests:

    def __init__(self, guest_id, first_name, last_name, email, phone_number, address, loyalty_points=0, booking_history=None):
        self.guest_id = guest_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.loyalty_points = loyalty_points

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

    @guest_id.setter
    def guest_id(self, value):
        self.__guest_id = value

    @first_name.setter
    def first_name(self, value):
        if not value.strip():
            raise ValueError("Der Vorname darf nicht leer sein.")
        self.__first_name = value.strip()

    @last_name.setter
    def last_name(self, value):
        if not value.strip():
            raise ValueError("Der Nachname darf nicht leer sein.")
        self.__last_name = value.strip()

    @email.setter
    def email(self, value):
        if "@" not in value or not value.strip():
            raise ValueError("Bitte eine gültige E-Mail-Adresse angeben.")
        self.__email = value.strip()

    @phone_number.setter
    def phone_number(self, value):
        if not value.strip():
            raise ValueError("Die Telefonnummer darf nicht leer sein.")
        self.__phone_number = value.strip()

    @address.setter
    def address(self, value):
        if not isinstance(value, Address):
            raise TypeError("Die Adresse muss ein Objekt der Klasse Address sein.")
        self.__address = value

    @loyalty_points.setter
    def loyalty_points(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Treuepunkte müssen eine positive ganze Zahl oder 0 sein.")
        self.__loyalty_points = value

    def __str__(self):
        return f"{self.__guest_id} - Name: {self.__first_name} {self.__last_name} - Email: {self.__email} - Telefonnummer: {self.__phone_number} - Adresse: {self.__address} - Treuepunkte: {self.__loyalty_points}"

    def get_guest_summary(self):
        return (
            f"Gast {self.__guest_id}\n"
            f"  Name:        {self.get_full_name()}\n"
            f"  E-Mail:      {self.__email}\n"
            f"  Telefon:     {self.__phone_number}\n"
            f"  Adresse:     {self.__address}\n"
            f"  Treuepunkte: {self.__loyalty_points}"
        )

   def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def deduct_points(self, points):
        if points > self.__loyalty_points:
            print("Nicht genügend Treuepunkte vorhanden.")
            return
        self.__loyalty_points -= points

    def add_points(self, points):
        if not isinstance(points, int) or points < 0:
            raise ValueError("Es können nur positive ganze Zahlen als Punkte hinzugefügt werden.")
        self.__loyalty_points += points


