from backup import Backup
from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu
from menus.backup_menu import BackupMenu
from menus.service_engineer_manager_menu import ServiceEngineerManagerMenu
from menus.show_users_menu import ShowUsersMenu
from menus.system_admin_manager_menu import SystemAdminManagerMenu
from menus.traveller_menu import TravellerMenu
from menus.scooter_menu import ScooterMenu


class SuperAdministratorMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user

    def get_options(self):
        return {
            "1": ("Search Scooter", self.action),
            "2": ("Update Scooter attributes", self.action),
            "3": ("Check list of users + roles", ShowUsersMenu(self.db_connection).display),
            "4": ("See logs", self.action),
            "5": ("Service Engineer Menu", ServiceEngineerManagerMenu(self.db_connection, self.user).display),
            "6": ("System Administrator Menu", SystemAdminManagerMenu(self.db_connection, self.user).display),
            "7": ("Scooter Menu", ScooterMenu(self.db_connection, self.user).display),
            "8": ("Traveller Menu", TravellerMenu(self.db_connection, self.user).display),
            "9": ("Backup Menu", BackupMenu(self.db_connection, self.user).display),
            "0": ("Back", lambda: "back")
        }

    def display(self):
        menu = BaseMenu("Super Administrator Menu", self.get_options)
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")


        #     def display(self):
        # menu = BaseMenu("Super Administrator Menu", {
        #     "1": ("Update your password", self.action),
        #     "2": ("Search Scooter", self.action),
        #     "3": ("Update Scooter attributes", self.action),
        #     "4": ("Check list of users + roles", self.action),
        #     "5": ("Add new Service Engineer", self.action),
        #     "6": ("Update Service Engineer", self.action),
        #     "7": ("Reset password of Service Engineer", self.action),
        #     "8": ("See logs", self.action),
        #     "9": ("Add new Traveller", self.action),
        #     "10": ("Update Traveller", self.action),
        #     "11": ("Delete Traveller", self.action),
        #     "12": ("Add new Scooter", self.action),
        #     "13": ("Update Scooter", self.action),
        #     "14": ("Delete Scooter", self.action),
        #     "15": ("Search Traveller", self.action),
        #     "16": ("Add new System Administrator", self.action),
        #     "17": ("Update System Administrator", self.action),
        #     "18": ("Delete System Administrator", self.action),
        #     "19": ("Make Backup", self.action),
        #     "20": ("Restore Backup", self.action),
        #     "21": ("Allow System Admin to Restore Backup", self.action),
        #     "22": ("Revoke System Admin to Restore Backup", self.action),
        #     "0": ("Back", lambda: "back")
        # })
        # menu.display()
