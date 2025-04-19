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