import model
import data_access

class FacilityManager:
    def __init__(self):
        self.__facilities_dal = data_access.Facilities_DAL()


    def add_facility(self, facility: model.Facility):
        self.__facilities.append(facility)

    def remove_facility_by_id(self, facility_id):
        self.__facilities = [f for f in self.__facilities if f.facility_id != facility_id]
    
    def get_all_facilities(self):
        return self.__facilities

    def find_by_name(self, name: str):
        return [f for f in self.__facilities if name.lower() in f.facility_name.lower()]

    def get_facility_by_id(self, facility_id: int):
        for f in self.__facilities:
            if f.facility_id == facility_id:
                return f
        return None
