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
            "1": ("Check list of users + roles", ShowUsersMenu(self.db_connection).display),
            "2": ("Service Engineer Menu", ServiceEngineerManagerMenu(self.db_connection, self.user).display),
            "3": ("System Administrator Menu", SystemAdminManagerMenu(self.db_connection, self.user).display),
            "4": ("Scooter Menu", ScooterMenu(self.db_connection, self.user).display),
            "5": ("Traveller Menu", TravellerMenu(self.db_connection, self.user).display),
            "6": ("Backup Menu", BackupMenu(self.db_connection, self.user).display),
            "0": ("Back", lambda: "back")
        }

    def display(self):
        menu = BaseMenu("Super Administrator Menu", self.get_options)
        menu.display()

