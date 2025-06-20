from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu

class ServiceEngineerMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user
    
    def display(self):
        menu = BaseMenu("Service Engineer Menu", {
            "1": ("Update your password", self.action),
            "2": ("Search Scooter", self.action),
            "3": ("Update Scooter attributes", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
