from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu

class TravellerMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user

    def display(self):
        menu = BaseMenu("Traveller Menu", self.get_options)
        menu.display()

    def get_options(self):
        return {
            "1": ("Search Traveller", self.action),
            "2": ("Add new Traveller", self.action),
            "3": ("Update Traveller", self.action),
            "4": ("Delete Traveller", self.action),
            "0": ("Back", lambda: "back")
        }
    
    def action(self):
        print("You selected Submenu 2 action.")
