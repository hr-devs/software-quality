# submenu1.py

from menus.base_menu import BaseMenu

class SubMenu1:
    def display(self):
        menu = BaseMenu("Submenu 1", {
            "1": ("Do Submenu 1 Action", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 1 action.")
