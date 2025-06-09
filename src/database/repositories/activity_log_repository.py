from database.database_connection import DatabaseConnection
from typing import List, Tuple

class ActivityLogRepository():
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
    
    def create_table(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
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
            conn.commit()
    
    def fetch_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM activity_logs")
            return cursor.fetchall()
        
    def clear_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM activity_logs")
            conn.commit()

    def insert_activity_logs(self, logs_data: List[Tuple]):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany("""
                INSERT INTO activity_logs 
                (log_date, log_time, username, activity_description, additional_info) 
                VALUES (?, ?, ?, ?, ?)
            """, logs_data)
            conn.commit()