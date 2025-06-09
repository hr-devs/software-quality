import sqlite3

class DatabaseConnection():
    def __init__(self, db_name: str = 'urban_mobility.db'):
        self.db_name = db_name

    def get_connection(self):
        return sqlite3.connect(self.db_name)