from menus.base_menu import BaseMenu
from menus.login_menu import LoginMenu
from login import Login

def main_menu():
    menu = BaseMenu("Main Menu", {
        "1": ("Login", Login.login),
        "0": ("Exit", lambda: "exit")
    })
    menu.display()
