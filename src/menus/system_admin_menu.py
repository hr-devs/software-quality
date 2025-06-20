from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu
from menus.scooter_menu import ScooterMenu
from menus.service_engineer_manager_menu import ServiceEngineerManagerMenu
from menus.show_users_menu import ShowUsersMenu
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
            "2": ("Check list of users + roles", ShowUsersMenu(self.db_connection).display),
            "3": ("Service Engineer Menu", ServiceEngineerManagerMenu().display),
            "4": ("Scooter Menu", ScooterMenu().display),
            "5": ("Traveller Menu", TravellerMenu().display),
            "0": ("Back", lambda: "back")
        }
