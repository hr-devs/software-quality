from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu
from menus.login_menu import LoginMenu
from login import Login

def main_menu(db_connection: DatabaseConnection):
    menu = BaseMenu("Main Menu", {
        "1": ("Login", Login(db_connection).login),
        "0": ("Exit", lambda: "exit")
    })
    menu.display()
