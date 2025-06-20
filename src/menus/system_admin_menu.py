from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu
from menus.scooter_menu import ScooterMenu
from menus.service_engineer_manager_menu import ServiceEngineerManagerMenu
from menus.traveller_menu import TravellerMenu
from services.user_service import UserService

class SystemAdministratorMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user

    def display(self):
        menu = BaseMenu("System Administrator Menu", self.get_options)
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
        
    def get_options(self):
        return {
            "1": ("Update your password", UserService(self.db_connection,self.user).update_password),
            "2": ("Search Scooter", self.action),
            "3": ("Update Scooter attributes", self.action),
            "4": ("Check list of users + roles", self.action),
            "5": ("See logs", self.action),
            "6": ("Service Engineer Menu", ServiceEngineerManagerMenu().display),
            "7": ("Scooter Menu", ScooterMenu().display),
            "8": ("Traveller Menu", TravellerMenu().display),
            "0": ("Back", lambda: "back")
        }

    # def display(self):
    #     menu = BaseMenu("System Administrator Menu", {
    #         "1": ("Update your password", self.action),
    #         "2": ("Search Scooter", self.action),
    #         "3": ("Update Scooter attributes", self.action),
    #         "4": ("Check list of users + roles", self.action),
    #         "5": ("Add new Service Engineer", self.action),
    #         "6": ("Update Service Engineer", self.action),
    #         "7": ("Reset password of Service Engineer", self.action),
    #         "8": ("See logs", self.action),
    #         "9": ("Add new Traveller", self.action),
    #         "10": ("Update Traveller", self.action),
    #         "11": ("Delete Traveller", self.action),
    #         "12": ("Add new Scooter", self.action),
    #         "13": ("Update Scooter", self.action),
    #         "14": ("Delete Scooter", self.action),
    #         "15": ("Search Traveller", self.action),
    #         "0": ("Back", lambda: "back")
    #     })
    #     menu.display()