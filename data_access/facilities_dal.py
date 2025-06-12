from data_access.base_dal import BaseDataAccess
import model

class Facilities_DAL(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def get_all_facilities(self) -> list[model.Facility]:
        sql = """
            SELECT facility_id, facility_name
            FROM Facilities
        """
        results = self.fetchall(sql)
        return [model.Facility(facility_id, name) for facility_id, name in results]

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

    def create_facility(self, facility: model.Facility) -> None:
        sql = """
            INSERT INTO Facilities
            VALUES (?, ?)
        """
        self.execute(sql, (facility.facility_id, facility.name))
    
    def update_facility(self, facility: model.Facility) -> None:
        sql = """
            UPDATE Facilities
            SET facility_name = ?
            WHERE facility_id = ?
        """
        self.execute(sql, (facility.facility_name, facility.facility_id))

    def delete_facility(self, facility_id: int) -> None:
        sql = """
            DELETE FROM Facilities
            WHERE facility_id = ?
        """
        self.execute(sql, (facility_id,))


    def get_facility_by_id(self, facility_id: int) -> model.Facility | None:
        sql = """
            SELECT facility_id, facility_name
            FROM Facilities
            WHERE facility_id = ?
        """
        result = self.fetchone(sql, (facility_id,))
        if result:
            facility_id, facility_name = result
            return model.Facility(facility_id, facility_name)
        return None
