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


    def get_facilities_by_room_id(self, room_id: int) -> list[model.Facility]:
        sql = """
            SELECT Facilities.facility_id, Facilities.facility_name

            FROM Facilities

            JOIN Room_Facilities 
            
            ON Facilities.facility_id = Room_Facilities.facility_id

            WHERE Room_Facilities.room_id = ?
        """
        results = self.fetchall(sql, (room_id,))
        return [model.Facility(facility_id, name) for facility_id, name in results]
