# submenu2.py

from base_menu import BaseMenu

class SubMenu2:
    def display(self):
        menu = BaseMenu("Submenu 2", {
            "1": ("Do Submenu 2 Action", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
