import model

class GuestManager:
    def __init__(self):
        self.__guests = []

    def add_guest(self, guest: model.Guests):
        self.__guests.append(guest)

    def remove_guest_byid(self, guest_id: int):
        self.__guests = [g for g in self._guests if g.guest_id != guest_id]

    def get_all_guests(self):
        return self.__guests

    def find_by_id(self, guest_id: int):
        for guest in self.__guests:
            if guest.guest_id == guest_id:
                return guest
        return None

    def add_loyalty_points_to_guest(self, guest_id: int, points: int):
        guest = self.find_by_id(guest_id)
        if guest:
            guest.add_points (points)
            return True
        return False

    def deduct_loyalty_points_from(self, guest_id: int, points: int):
        guest = self.find_by_id(guest_id)
        if guest:
            guest.deduct_points(points)
            return True
        return False


    def find_by_email(self, email: str):
        return [g for g in self._guests if g.email.lower() == email.lower()]

    def find_by_name(self, name: str):
        return [g for g in self._guests if g.name.lower() == name.lower()]

    def print_all_summaries(self):
        for g in self._guests:
            print(g.get_guest_summary())