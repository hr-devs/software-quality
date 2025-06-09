from database.database_connection import DatabaseConnection
from typing import List, Tuple

class UserRepository():
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
    
    def create_table(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                        
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                        
                    role_id INTEGER NOT NULL  -- link with roles table
                );
            """)
            conn.commit()
    
    def fetch_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
        
    def clear_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users")
            conn.commit()

    def insert_users(self, users_data: List[Tuple]):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(
                "INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)", 
                users_data
            )
            conn.commit()
    