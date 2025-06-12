import model
import data_access

class FacilityManager:
    def __init__(self):
        self.__facilities_dal = data_access.Facilities_DAL()


    def get_all_facilities(self):
        return self.__facilities_dal.get_all_facilities()
    
    def get_facilities_by_room_id(self, room_id):
        return self.__facilities_dal.get_facilities_by_room_id(room_id)

    def create_facility(self, facility: model.Facility) -> model.Facility:
        return self.__facilities_dal.create_facility(facility)

    def update_facility(self, facility: model.Facility) -> model.Facility:
        return self.__facilities_dal.update_facility(facility)

    def delete_facility(self, facility_id: int) -> None:
        return self.__facilities_dal.delete_facility(facility)
