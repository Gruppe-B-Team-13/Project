class RoomType:
    def __init__(self, room_type_id, room_type_name, description, max_guests):
        self.__room_type_id = room_type_id
        self.__room_type_name = room_type_name
        self.__description = description
        self.__max_guests = max_guests

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

    def __str__(self):
        return f"{self.__room_type_name} – {self.__description} (max. {self.__max_guests} Gäste)"
