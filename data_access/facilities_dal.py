from data_access.base_dal import BaseDataAccess
import model

class Facilities_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def get_all_facilities(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT facility_id, facility_name FROM Facilities")
        rows = cursor.fetchall()

        facilities = []
        for row in rows:
            facility = Facilities(
                facility_id=row[0],
                facility_name=row[1]
            )
            facilities.append(facility)
        return facilities

    def get_facility_by_id(self, facility_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT facility_id, facility_name FROM Facilities WHERE facility_id = ?", (facility_id,))
        row = cursor.fetchone()
        if row:
            return Facility(
                facility_id=row[0],
                facility_name=row[1]
            )
        return None
