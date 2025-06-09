from database.database_connection import DatabaseConnection
from typing import List, Tuple

class TravellerRepository():
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
    
    def create_table(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS travellers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    birthday TEXT NOT NULL,  -- should be -> YYYY-MM-DD
                    gender TEXT NOT NULL, -- should be -> 'male' or 'female'

                    street_name TEXT NOT NULL,
                    house_number INTEGER NOT NULL,
                    zip_code TEXT NOT NULL, -- format correctly

                    city TEXT NOT NULL,

                    email_address TEXT NOT NULL UNIQUE,
                    mobile_phone TEXT NOT NULL, -- format correctly

                    driving_license_number TEXT NOT NULL -- format correctly (2 formats possible)
                );
            """)
            conn.commit()
    
    def fetch_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM travellers")
            return cursor.fetchall()
        
    def clear_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM travellers")
            conn.commit()

    def insert_travellers(self, travellers_data: List[Tuple]):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany("""
                INSERT INTO travellers 
                (first_name, last_name, birthday, gender, street_name, house_number, 
                 zip_code, city, email_address, mobile_phone, driving_license_number) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, travellers_data)
            conn.commit()
