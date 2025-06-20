from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from typing import List, Tuple
from encryptor import Encryptor
from enums import Role

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
        
    def fetch_system_administrators(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE role_id = (?)", (Role.SYSTEM_ADMIN))
            return cursor.fetchall()
        
    def fetch_service_engineers(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE role_id = (?)", (Role.SERVICE_ENGINEER))
            return cursor.fetchall()
        
    def fetch_all_usernames_and_roles(self):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username, role_id FROM users")
            return cursor.fetchall()
        
    def get_usernames_and_roles(self):
        usernames_and_roles = {}
        usernames_and_roles_list = self.fetch_all_usernames_and_roles()

        for index, username_and_role in enumerate(usernames_and_roles_list):
            usernames_and_roles[str(index + 1)] = (
                f"username: {Encryptor.decrypt_data(username_and_role[0])} | role: {Role(username_and_role[1]).name}",
                lambda b=username_and_role: "back"
            )

        usernames_and_roles["0"] = ("Back", lambda: "back")
        return usernames_and_roles
    
    def get_service_engineers_options(self, function):
        service_engineers = {}
        service_engineers_list = self.fetch_service_engineers()

        for index, service_engineer in enumerate(service_engineers_list):
            service_engineers[str(index + 1)] = (
                f"username: {Encryptor.decrypt_data(service_engineer[0])} | role: {Role(service_engineer[1]).name}",
                lambda se=service_engineer: function(se)
            )

        service_engineers["0"] = ("Back", lambda: "back")
        return service_engineers
    
    def get_system_administrators_options(self, function):
        system_administrators = {}
        system_administrators_list = self.fetch_service_engineers()

        for index, system_administrator in enumerate(system_administrators_list):
            system_administrators[str(index + 1)] = (
                f"username: {Encryptor.decrypt_data(system_administrator[0])} | role: {Role(system_administrator[1]).name}",
                lambda sa=system_administrator: function(sa)
            )

        system_administrators["0"] = ("Back", lambda: "back")
        return system_administrators

        
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
            
    def update_password(self, id : int, new_password : str):
        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE users SET password = ? WHERE id = ?",
                (new_password, id)
            )
            conn.commit()