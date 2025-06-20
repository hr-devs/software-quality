from backup import Backup
from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from encryptor import Encryptor
from input_handler import UserInput
from menus.base_menu import BaseMenu
from database.repositories.user_repository import UserRepository

class ServiceEngineerManagerMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.backup = Backup(db_connection)
        self.user = user
        self.user_repo = UserRepository(db_connection)
    
    def display(self):
        #ALERT ALERT NOT SERVICE ENGINEER MENU ______ MANAGER MENUUUUU
        menu = BaseMenu("Service Engineer Manager Menu", self.get_options)
        menu.display()

    def reset_engineers_password(self):
        options = self.user_repo.get_service_engineers_options(self.reset_password)
        menu = BaseMenu("Select a Service Engineer", lambda: options)
        menu.display()
        
    def reset_password(self, service_engineer):
            new_password = Encryptor.hash_str(UserInput.get_data_input("new password: ", "Password"))
            print(type(service_engineer))
            print(service_engineer)
            self.user_repo.update_password(service_engineer[3], new_password)
            self.user.password = new_password
            print("\nPassword updated!")
    
    def get_options(self):
        return {
            "1": ("Add new Service Engineer", self.action),
            "2": ("Update Service Engineer", self.action),
            "3": ("Reset password of Service Engineer", self.reset_engineers_password),
            "0": ("Back", lambda: "back")
        }
        

    def action(self):
        print("You selected Submenu 2 action.")
