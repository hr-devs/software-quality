from database.database_connection import DatabaseConnection
from typing import List, Tuple

class ScooterRepository():
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
    
    def create_table(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scooters (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    brand TEXT NOT NULL,                            -- e.g., Segway, NIU
                    model TEXT NOT NULL,                            -- Model name/number
                    serial_number TEXT NOT NULL UNIQUE,             -- 10 to 17 alphanumeric characters

                    top_speed INTEGER NOT NULL,                     -- km/h
                    battery_capacity INTEGER NOT NULL,              -- in Wh
                    soc REAL NOT NULL,                              -- State of Charge, percentage (0.0 to 100.0)

                    soc_min_target REAL NOT NULL,                   -- Recommended minimum SoC, as percentage
                    soc_max_target REAL NOT NULL,                   -- Recommended maximum SoC, as percentage

                    description TEXT,                               -- Optional notes

                    latitude REAL NOT NULL,                         -- 5 decimal places, e.g. 51.92250 (Rotterdam region)
                    longitude REAL NOT NULL,                        -- 5 decimal places, e.g. 4.47917 (Rotterdam region)

                    out_of_service INTEGER NOT NULL DEFAULT 0,      -- 0 = available, 1 = out of service

                    mileage REAL NOT NULL DEFAULT 0,                -- Total distance in km
                    last_maintenance_date TEXT NOT NULL             -- ISO 8601 format: YYYY-MM-DD
                );
            """)
            conn.commit()
            
    def add_scooter(self, scooter_data: Tuple):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO scooters (
                    brand, model, serial_number,
                    top_speed, battery_capacity, soc,
                    soc_min_target, soc_max_target,
                    description,
                    latitude, longitude,
                    out_of_service, mileage, last_maintenance_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, scooter_data)
            conn.commit()
    
    def fetch_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM scooters")
            return cursor.fetchall()
        
    def clear_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM scooters")
            conn.commit()

    def insert_scooters(self, scooters_data: List[Tuple]):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany("""
                INSERT INTO scooters 
                (brand, model, serial_number, top_speed, battery_capacity, soc, 
                 soc_min_target, soc_max_target, description, latitude, longitude, 
                 out_of_service, mileage, last_maintenance_date) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, scooters_data)
            conn.commit()