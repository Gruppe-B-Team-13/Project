import os
import sqlite3

class DatabaseConnection:
    def __init__(self):
        # dynamisch relativer Pfad – funktioniert überall im Projekt
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.db_path = os.path.join(base_dir, "database", "hotel_reservation_sample(1).db")

    def connect(self):
        return sqlite3.connect(self.db_path)
