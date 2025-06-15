from database.database_connection import DatabaseConnection
from menus.base_menu import BaseMenu
from menus.login_menu import LoginMenu
from login import Login

def main_menu(db_connection: DatabaseConnection, login: Login): 
    option_username = ("Username : {}".format(login.username), login.set_username) if login.username != None else ("Username", login.set_username)
    option_password = ("Password : {}".format(login.password), login.set_password) if login.password != None else ("Password", login.set_password)
    print(option_password)
    
    options = {
        "1": option_username,
        "2": option_password,
        "3": ("Login", login.login),
        "0": ("Exit", lambda: "exit")
    }

    #TODO we callen display() maar die opties worden niet geupdate (ze staan vast vanaf de call). We moeten die display() functie herschrijven of een override maken.

    menu = BaseMenu("Main Menu", options)
    menu.display()
