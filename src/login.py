from typing import List, Tuple
from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from database.repositories.user_repository import UserRepository
from encryptor import Encryptor
from input_handler import UserInput
from menus.service_engineer_menu import ServiceEngineerMenu
from menus.super_admin_menu import SuperAdministratorMenu
from menus.system_admin_menu import SystemAdministratorMenu

class Login:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.user_repository = UserRepository(db_connection)
        self.current_user = None

    #TODO: send password and username to database (encrypted?)

    def login(self):
        #username, password = self.get_username_and_password()
        self.authenticate(username_input="sup_adm01", password_input="SuperAdmin#2024!")

    def get_username_and_password(self): 
        username = UserInput.get_data_input("Username: ", "Username")
        password = UserInput.get_data_input("Password: ", "Password")
        return username, password
        
    def authenticate(self, username_input: str, password_input: str) -> bool:
        all_user_data: List[Tuple] = self.user_repository.fetch_all()

        for user in all_user_data:
            if (Encryptor.decrypt_data(user[1]) == username_input):
                user_match = user
                break

        if (user_match != None): #check_hashed_data geeft error
            if (Encryptor.check_hashed_data(password_input ,user_match[2])):
                user_dto = User(user[1], user[2], user[3])
                return True
            else:
                return False

        else:
            return False
        



        # hashed_username = Encryptor.hash_str(username_input)
        # user = self.user_repository.fetch_user_by_hash(hashed_username)
        
        # if(Encryptor.check_hashed_data(password_input, user[3])):
        #     role_menu = self.determine_menu(user[4])
        #     user_dto = User(user[0], user[1], user[2])

        # role_menu(user_dto)


        # This is where you'd use self.user_repository to check credentials
        # TODO: Hash password and verify against database
        pass

    def determine_menu(self, role_id: int):
        if role_id == 1:
            SuperAdministratorMenu().display
        elif role_id == 2:
            SystemAdministratorMenu().display
        elif role_id == 3:
            ServiceEngineerMenu().display
        else:
            None


