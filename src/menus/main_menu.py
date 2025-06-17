from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu
from menus.login_menu import LoginMenu
from login import Login

def main_menu(db_connection: DatabaseConnection, login: Login): 
    def get_options():
        option_username = (
            f"Username : {login.username}", login.set_username
        ) if login.username else ("Username", login.set_username)

        option_password = (
            f"Password : {login.password}", login.set_password
        ) if login.password else ("Password", login.set_password)

        return {
            "1": option_username,
            "2": option_password,
            "3": ("Login", login.login),
            "0": ("Exit", lambda: "exit")
        }

    menu = BaseMenu("Main Menu", get_options)
    menu.display()

