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
    populate_dummy_data()
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
        

def populate_dummy_data():
    with sqlite3.connect('urban_mobility.db') as connection:
        cursor = connection.cursor()
        
        # Clear existing data
        cursor.execute("DELETE FROM activity_logs")
        cursor.execute("DELETE FROM scooters")
        cursor.execute("DELETE FROM travellers")
        cursor.execute("DELETE FROM users")
        cursor.execute("DELETE FROM roles")
        
        # Insert roles
        roles_data = [
            (1, 'super_admin'),
            (2, 'system_admin'),
            (3, 'service_engineer'),
        ]
        
        cursor.executemany("INSERT INTO roles (id, role_name) VALUES (?, ?)", roles_data)
        
        # Insert users
        users_data = [
            ('superadmin', 'hashed_password_123', 1),
            ('admin_rotterdam', 'hashed_password_456', 2),
            ('operator_jan', 'hashed_password_789', 3)
        ]
        
        cursor.executemany("INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)", users_data)
        
        # Insert travellers
        travellers_data = [
            ('Jan', 'de Vries', '1985-03-15', 'male', 'Coolsingel', 42, '3012 AA', 'Rotterdam', 'jan.devries@email.nl', '+31-6-12345678', 'NL123456789'),
            ('Sarah', 'van der Berg', '1992-07-22', 'female', 'Witte de Withstraat', 15, '3012 BK', 'Rotterdam', 'sarah.vandenberg@email.nl', '+31-6-23456789', 'NL234567890'),
            ('Mike', 'Thompson', '1988-11-08', 'male', 'Erasmusbrug', 3, '3011 BN', 'Rotterdam', 'mike.thompson@email.com', '+31-6-34567890', '123456789NL')
        ]
        
        cursor.executemany("""INSERT INTO travellers 
            (first_name, last_name, birthday, gender, street_name, house_number, zip_code, city, email_address, mobile_phone, driving_license_number) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", travellers_data)
        
        # Insert scooters
        scooters_data = [
            ('Segway', 'Ninebot MAX G30', 'SG2024001ABC', 25, 551, 85.5, 20.0, 90.0, 'Excellent condition', 51.92250, 4.47917, 0, 1245.8, '2024-01-15'),
            ('NIU', 'KQi3 Pro', 'NIU2024002DEF', 25, 486, 67.2, 15.0, 85.0, 'Recently serviced', 51.91845, 4.48234, 0, 892.3, '2024-02-10'),
            ('Xiaomi', 'Mi Electric Scooter 3', 'XM2024003GHI', 25, 275, 45.8, 10.0, 80.0, 'Good working order', 51.92456, 4.47652, 0, 654.1, '2024-01-28')
        ]
        
        cursor.executemany("""INSERT INTO scooters 
            (brand, model, serial_number, top_speed, battery_capacity, soc, soc_min_target, soc_max_target, description, latitude, longitude, out_of_service, mileage, last_maintenance_date) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", scooters_data)
        
        # Insert activity logs
        activity_logs_data = [
            ('2024-06-04', '08:15:32', 'superadmin', 'Logged in', 'System startup'),
            ('2024-06-04', '08:16:45', 'superadmin', 'Database backup created', 'Scheduled backup'),
            ('2024-06-04', '09:23:12', 'admin_rotterdam', 'Logged in', 'Morning shift start')
        ]
        
        cursor.executemany("""INSERT INTO activity_logs 
            (log_date, log_time, username, activity_description, additional_info) 
            VALUES (?, ?, ?, ?, ?)""", activity_logs_data)
        
        connection.commit()
        print("Database initialized and populated with dummy data successfully!")