import model
import data_access

class FacilityManager:
    def __init__(self):
        self._facilities_dal = data_access.Facilities_DAL()


    def get_all_facilities(self):
        return self._facilities_dal.get_all_facilities()
    
    def get_facilities_by_room_id(self, room_id):
        return self._facilities_dal.get_facilities_by_room_id(room_id)

    def create_facility(self, facility: model.Facility) -> model.Facility:
        return self._facilities_dal.create_facility(facility)

    def update_facility(self, facility: model.Facility) -> model.Facility:
        return self._facilities_dal.update_facility(facility)

    def delete_facility(self, facility_id: int) -> None:
        return self._facilities_dal.delete_facility(facility)

    def get_facility_by_id(self, facility_id: int) -> model.Facility | None:
        return self._facilities_dal.get_facility_by_id(facility_id)
