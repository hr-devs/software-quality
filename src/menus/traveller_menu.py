from menus.base_menu import BaseMenu

class TravellerMenu:
    def display(self):
        menu = BaseMenu("Traveller Menu", {
            "1": ("Search Traveller", self.action),
            "2": ("Add new Traveller", self.action),
            "3": ("Update Traveller", self.action),
            "4": ("Delete Traveller", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
