import sqlite3
import os

def initialize_database():
    with sqlite3.connect('urban_mobility.db') as connection:
        cursor = connection.cursor()

        #users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                       
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                       
                role_id INTEGER NOT NULL  -- link with roles table
            );
        """)
        
        # roles
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                role_name TEXT NOT NULL
            );
        """)

        # travellers
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
        
        # specific details can only be eddited by specific role of user
        # scooters
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
        
        # activity_log
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS activity_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log_date TEXT NOT NULL,                       -- Format: YYYY-MM-DD
                log_time TEXT NOT NULL,                       -- Format: HH:MM:SS
                username TEXT NOT NULL,                       -- e.g., john_m_05, superadmin
                activity_description TEXT NOT NULL,           -- e.g., "Logged in", "User is deleted"
                additional_info TEXT                          -- e.g., "Suspicious", "username: mike12"
            );
        """)
        
        connection.commit()
    print(fetch_all_travellers())


def fetch_all_users():
    with sqlite3.connect('urban_mobility.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM users""")
        return cursor.fetchall()
    

def fetch_all_roles():
    with sqlite3.connect('urban_mobility.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM roles""")
        return cursor.fetchall()
    

def fetch_all_travellers():
    with sqlite3.connect('urban_mobility.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM travellers""")
        return cursor.fetchall()
    

def fetch_all_scooters():
    with sqlite3.connect('urban_mobility.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM scooters""")
        return cursor.fetchall()
        

def fetch_all_activity_logs():
    with sqlite3.connect('urban_mobility.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM activity_logs""")
        return cursor.fetchall()
    

def fetch_all_data():
    with sqlite3.connect('urban_mobility.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM users, roles, travellers, scooters, activity_logs""")
        return cursor.fetchall()
        
        