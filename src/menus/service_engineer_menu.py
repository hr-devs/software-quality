from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from database.repositories.user_repository import UserRepository
from encryptor import Encryptor
from input_handler import UserInput
from menus.base_menu import BaseMenu

class ServiceEngineerMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user
    
    def display(self):
        menu = BaseMenu("Service Engineer Menu", self.get_options)
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
        
    def get_options(self):
        return {
            "1": ("Update your password", self.update_password),
            "2": ("Search Scooter", self.action),
            "3": ("Update Scooter attributes", self.action),
            "0": ("Back", lambda: "back")
        }
    
    def update_password(self):
        new_password = None

        # vraag oude password op (vind oude password)
        if(Encryptor.check_hashed_data(UserInput.get_data_input("current password: ", "Password"), self.user.password)):
            new_password = Encryptor.hash_str(UserInput.get_data_input("new password: ", "Password"))
            UserRepository(self.db_connection).update_password(self.user.id, new_password)
            self.user.password = new_password
            print("\nPassword updated!")
        
        else:
            print("\nIncorrect password")
            return        