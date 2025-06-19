from database.database_connection import DatabaseConnection
from database.repositories.user_repository import UserRepository
from menus.base_menu import BaseMenu

class ShowUsersMenu:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.user_repo = UserRepository(db_connection)

    def get_options(self):
        return self.user_repo.get_usernames_and_roles()

    def display(self):
        menu = BaseMenu("All users", self.get_options)
        menu.display()

