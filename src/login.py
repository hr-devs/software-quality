from typing import List, Tuple
from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from database.repositories.user_repository import UserRepository
from encryptor import Encryptor
from input_handler import UserInput
from menus.service_engineer_menu import ServiceEngineerMenu
from menus.super_admin_menu import SuperAdministratorMenu
from menus.system_admin_menu import SystemAdministratorMenu
from enums import Role

class Login:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.user_repository = UserRepository(db_connection)
        self.current_user = None
        self.username = None
        self.password = None

    def login(self):#, username, password): TODO should be added after debugging
        self.current_user = self.authenticate(username_input="sup_adm01", password_input="SuperAdmin#2024!")
        if (self.current_user != None):
            self.determine_menu(self.current_user)
        
    
    def set_username(self):
        username = UserInput.get_data_input("Username: ", "Username")
        self.username = username
    
    def set_password(self):
        password = UserInput.get_data_input("Password: ", "Password")
        self.password = password
        
    def authenticate(self, username_input: str, password_input: str):
        if (username_input == "super_admin" and password_input == "Admin_123?"):
            return User(
                username="super_admin",
                password="Admin_123?",
                role_id=1
            )

        all_user_data: List[Tuple] = self.user_repository.fetch_all()
        user_match = None

        for user in all_user_data:
            if (Encryptor.decrypt_data(user[1]) == username_input):
                user_match = user
                break

        if (user_match != None):
            if (Encryptor.check_hashed_data(password_input ,user_match[2])):
                return User(user[1], user[2], user[3])
            else:
                return None

        else:
            return None
        

    def determine_menu(self, user: User):
        if user.role_id == Role.SUPER_ADMIN.value:
            SuperAdministratorMenu(user).display()
        elif user.role_id == Role.SYSTEM_ADMIN.value:
            SystemAdministratorMenu(user).display()
        elif user.role_id == Role.SERVICE_ENGINEER.value:
            ServiceEngineerMenu(user).display()
        else:
            print("Unknown role ID. Access denied.")



