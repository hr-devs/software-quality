from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu

class SystemAdminManagerMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user
    
    def display(self):
        #ALERT ALERT NOT SYSTEM ADMIN MENU ______ MANAGER MENUUUUU
        menu = BaseMenu("System Admin Manager Menu", self.get_options)
        menu.display()

    def get_options(self):
        return {
            "1": ("Add new System Administrator", self.action),
            "2": ("Update System Administrator", self.action),
            "3": ("Delete System Administrator", self.action),
            "0": ("Back", lambda: "back")
        }

    def action(self):
        print("You selected Submenu 2 action.")
