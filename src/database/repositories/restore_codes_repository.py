from data_transfer_objects import ActivityLog, RestoreCode
from database.database_connection import DatabaseConnection
from typing import List, Tuple

class RestoreCodesRepository():
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
    
    def create_table(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS restore_codes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    restore_code TEXT NOT NULL,
                    backup_file_name TEXT NOT NULL,
                    creation_date TEXT NOT NULL,
                    username TEXT NOT NULL,
                    role_id TEXT NOT NULL,
                    used INTEGER NOT NULL,
                    revoked INTEGER NOT NULL
                );
            """)
            conn.commit()
    
    def fetch_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM restore_codes")
            return cursor.fetchall()
        
    def clear_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM restore_codes")
            conn.commit()

    def insert_restore_codes(self, restore_codes: List[Tuple]):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany("""
                INSERT INTO restore_codes 
                (restore_code, backup_file_name, creation_date, username, role_id, used, revoked) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, restore_codes)
            conn.commit()

    def insert_restore_code(self, restore_code: RestoreCode):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO restore_codes 
                (restore_code, backup_file_name, creation_date, username, role_id, used, revoked) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (restore_code.restore_code, restore_code.backup_file_name, restore_code.creation_date, restore_code.username, restore_code.role_id, restore_code.used, restore_code.revoked))
            conn.commit()