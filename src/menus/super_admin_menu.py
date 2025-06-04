# submenu2.py

from menus.base_menu import BaseMenu

class SuperAdministratorMenu:
    def display(self):
        menu = BaseMenu("Super Administrator Menu", {
            "1": ("Update your password", self.action),
            "2": ("Search Scooter", self.action),
            "3": ("Update Scooter attributes", self.action),
            "4": ("Check list of users + roles", self.action),
            "5": ("Add new Service Engineer", self.action),
            "6": ("Update Service Engineer", self.action),
            "7": ("Reset password of Service Engineer", self.action),
            "8": ("See logs", self.action),
            "9": ("Add new Traveller", self.action),
            "10": ("Update Traveller", self.action),
            "11": ("Delete Traveller", self.action),
            "12": ("Add new Scooter", self.action),
            "13": ("Update Scooter", self.action),
            "14": ("Delete Scooter", self.action),
            "15": ("Search Traveller", self.action),
            "16": ("Add new System Administrator", self.action),
            "17": ("Update System Administrator", self.action),
            "18": ("Delete System Administrator", self.action),
            "19": ("Make Backup", self.action),
            "20": ("Restore Backup", self.action),
            "21": ("Allow System Admin to Restore Backup", self.action),
            "22": ("Revoke System Admin to Restore Backup", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
