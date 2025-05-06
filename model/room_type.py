class RoomType:
    def __init__(self, room_type_id, room_type_name, description, max_guests):
        self.room_type_id = room_type_id
        self.room_type_name = room_type_name
        self.description = description
        self.max_guests = max_guests

    @property
    def room_type_id(self):
        return self.__room_type_id

    @property
    def room_type_name(self):
        return self.__room_type_name

    @property
    def description(self):
        return self.__description

    @property
    def max_guests(self):
        return self.__max_guests

    @room_type_id.setter
    def room_type_id(self, value):
        self.__room_type_id = value

    @room_type_name.setter
    def room_type_name(self, value):
        if not value.strip():
            raise ValueError("Der Name des Zimmertyps darf nicht leer sein.")
        self.__room_type_name = value.strip()

    @description.setter
    def description(self, value):
        self.__description = value.strip() if isinstance(value, str) else ""

    @max_guests.setter
    def max_guests(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Die maximale Gästeanzahl muss mindestens 1 sein.")
        self.__max_guests = value

    def __str__(self):
        return f"{self.__room_type_name} – {self.__description} (max. {self.__max_guests} Gäste)"
