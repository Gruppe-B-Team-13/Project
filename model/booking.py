Class Bookings:
    def __init__(self, booking_id: int,check_in_date, check_out_date,is_cancelled:bool,total_amount:float, guest, room):
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.is_cancelled = is_cancelled
        self.total_amout = total_amount
        self.guest = guest #Link zum "Guest"-Objekt(Hier wird das Objekt der Klasse "Guest" erwartet)
        self.room = room  #Link zum "Room"-Objekt(Hier wird das Objekt der Klasse "Room" erwartet)

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def check_in_date(self):
        return self.check_in_date

    @property
    def check_out_date(self):
        return self.check_out_date

    @property
    def is_cancelled(self):
        return self.is_cancelled

    @property
    def total_amount(self):
        return self.total_amount

    @total_amount.setter
    def total_amount(self, value:float):
        if value < 0:
            raise ValueError("Gesamtkosten können nicht negativ sein.")
        self.total_amount = value

Class Facilities:
    def __init__(self, facilities_name, facilities_description):
        self.__facilities_name = facilities_name
        self.__facilities_description = facilities_description


    @property
    def facilities_name(self):
        return self.__facilities_name

    @property
    def facilities_description(self):
        return self.__facilities_description
    
    def apply_loyalty_points_from_guest(self):
        if self.applied_points <= 0:
            print("Keine Treuepunkte verfügbar.")
            return

        used_points = self.applied_points
        self.__guest.deduct_points(used_points)
        self.__total_amount -= used_points
        print(f"{used_points} Punkte verwendet. Neuer Betrag: CHF {self.__total_amount:.2f}")



    def add_loyalty_points_to_guest(self):
        if self.original_total_amount < 100:
            print("Keine Treuepunkte hinzugefügt, da der Mindestbetrag 100 CHF beträgt.")
            return
        points = int(self.original_total_amount // 10)  
        self.__guest.add_points(points)
        print(f"{points} Punkte hinzugefügt. Neuer Punktestand: {self.__guest.loyalty_points}")
