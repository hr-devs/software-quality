# main_menu.py

from menus.base_menu import BaseMenu
from menus.submenu_1 import SubMenu1
from menus.submenu_2 import SubMenu2

def main_menu():
    menu = BaseMenu("Main Menu", {
        "1": ("Go to Submenu 1", SubMenu1().display),
        "2": ("Go to Submenu 2", SubMenu2().display),
        "0": ("Exit", lambda: "exit")
    })
    menu.display()
