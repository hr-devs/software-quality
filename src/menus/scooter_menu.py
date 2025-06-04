from menus.base_menu import BaseMenu

class ScooterMenu:
    def display(self):
        menu = BaseMenu("Scooter Menu", {
            "1": ("Add new Scooter", self.action),
            "2": ("Update Scooter", self.action),
            "3": ("Delete Scooter", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
