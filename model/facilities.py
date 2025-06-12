class Facility:
    def __init__(self, facility_id, facility_name):
        self.facility_id = facility_id
        self.facility_name = facility_name

    @property
    def facility_id(self):
        return self.__facility_id

    @property
    def facility_name(self):
        return self.__facility_name

    @facility_id.setter
    def facility_id(self, value):
        self.__facility_id = value

    @facility_name.setter
    def facility_name(self, value):
        if not value.strip():
            raise ValueError("Der Name der Einrichtung darf nicht leer sein.")
        self.__facility_name = value.strip()

    def __str__(self):
        return f"{self.__facility_name}"


