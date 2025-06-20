from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from database.repositories.user_repository import UserRepository
from encryptor import Encryptor
from input_handler import UserInput
from menus.base_menu import BaseMenu
from menus.scooter_menu import ScooterMenu
from services.user_service import UserService

class ServiceEngineerMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user
    
    def display(self):
        menu = BaseMenu("Service Engineer Menu", self.get_options)
        menu.display()
        
    def get_options(self):
        return {
            "1": ("Update your password", UserService(self.db_connection,self.user).update_password),
            "2": ("Scooter menu", ScooterMenu(self.db_connection, self.user).display),
            "0": ("Back", lambda: "back")
        }