from database.database_connection import DatabaseConnection
from typing import List, Tuple

class RoleRepository():
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
    
    def create_table(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS roles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                           
                    role_name TEXT NOT NULL
                );
            """)
            conn.commit()
    
    def fetch_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            return cursor.fetchall()
        
    def clear_all(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM roles")
            conn.commit()

    def insert_roles(self, roles_data: List[Tuple]):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(
                "INSERT INTO roles (id, role_name) VALUES (?, ?)", 
                roles_data
            )
            conn.commit()