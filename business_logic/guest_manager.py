import model
import data_access

class GuestManager:
    def __init__(self):
        self.guest_dal = data_access.Guest_DAL()

    def find_guest_by_name(self, first_name: str, last_name: str) -> model.Guests | None:
        return self.guest_dal.find_guest(first_name, last_name)

    def create_guest(self, first_name: str, last_name: str, email: str, phone_number: str, address_id: int) -> model.Guests:
        return self.guest_dal.create_guest(first_name, last_name, email, phone_number, address_id)

    def get_guest_by_id(self, guest_id: int) -> model.Guests | None:
        return self._guest_dal.get_guest_by_id(guest_id)

    def change_guest_first_name(self, guest_id: int, new_first_name: str) -> bool:
        return self.guest_dal.update_first_name(guest_id, new_first_name)

    def change_guest_last_name(self, guest_id: int, new_last_name: str) -> bool:
        return self.guest_dal.update_last_name(guest_id, new_last_name)


    def change_guest_address_id(self, guest_id: int, new_address_id: int) -> bool:
        return self.guest_dal.update_address_id(guest_id, new_address_id)


    def change_guest_email(self, guest_id: int, new_email: str) -> bool:
        return self.guest_dal.update_email(guest_id, new_email)



    def change_guest_phone_number(self, guest_id: int, new_phone_number: str) -> bool:
        return self.guest_dal.update_phone_number(guest_id, new_phone_number)
        

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


# Menüfunktion außerhalb der Klasse
def admin_guest_update_menu():
    manager = GuestManager()

    print("\nAdmin-Menü zur Bearbeitung von Gastdaten")
    print("Geben Sie jederzeit 'exit' ein, um das Menü zu verlassen.")

    while True:
        # 1. Alle Gäste anzeigen
        print("\nAktuelle Gästeliste:")
        guest_ids = []
        for guest_id in range(1, 100):
            guest = manager.get_guest_by_id(guest_id)
            if guest:
                print(f"{guest.guest_id}: {guest.get_full_name()} | {guest.email} | {guest.phone_number}")
                guest_ids.append(guest.guest_id)

        # 2. Eingabe der Guest-ID
        eingabe = input("\nGuest-ID eingeben (oder 'exit'): ").strip()
        if eingabe.lower() == "exit":
            print("Admin-Menü wurde beendet.")
            break
        if not eingabe.isdigit():
            print("Ungültige Zahl.")
            continue
        guest_id = int(eingabe)
        if guest_id not in guest_ids:
            print("Keine gültige Guest-ID.")
            continue

        # 3. Auswahl des Feldes
        print("\nWas möchten Sie ändern?")
        print("1 = Vorname\n2 = Nachname\n3 = E-Mail\n4 = Telefonnummer\n5 = Adresse-ID")
        feld = input("Auswahl (1–5 oder 'exit'): ").strip()
        if feld.lower() == "exit":
            continue

        # 4. Neuen Wert eingeben
        neues_wert = input("Neuen Wert eingeben (oder 'exit'): ").strip()
        if neues_wert.lower() == "exit":
            continue

        # 5. Änderung ausführen
        success = False
        if feld == "1":
            success = manager.change_guest_first_name(guest_id, neues_wert)
        elif feld == "2":
            success = manager.change_guest_last_name(guest_id, neues_wert)
        elif feld == "3":
            success = manager.change_guest_email(guest_id, neues_wert)
        elif feld == "4":
            success = manager.change_guest_phone_number(guest_id, neues_wert)
        elif feld == "5":
            try:
                neues_wert = int(neues_wert)
                success = manager.change_guest_address_id(guest_id, neues_wert)
            except ValueError:
                print(" Adresse-ID muss eine Zahl sein.")
                continue
        else:
            print(" Ungültige Auswahl.")
            continue

        # 6. Feedback
        if success:
            print(" Änderung gespeichert.")
        else:
            print("Änderung fehlgeschlagen.")


# Startpunkt (wenn Datei direkt ausgeführt wird)
if __name__ == "__main__":
    admin_guest_update_menu()
