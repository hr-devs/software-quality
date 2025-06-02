# main_menu.py

from base_menu import BaseMenu
from submenu1 import SubMenu1
from submenu2 import SubMenu2

def main_menu():
    menu = BaseMenu("Main Menu", {
        "1": ("Go to Submenu 1", SubMenu1().display),
        "2": ("Go to Submenu 2", SubMenu2().display),
        "0": ("Exit", lambda: "exit")
    })
    menu.display()
