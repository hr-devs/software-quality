from menus.base_menu import BaseMenu
from menus.login_menu import LoginMenu

def main_menu():
    menu = BaseMenu("Main Menu", {
        "1": ("Login", LoginMenu().display),
        "0": ("Exit", lambda: "exit")
    })
    menu.display()
