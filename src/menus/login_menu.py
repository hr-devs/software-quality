from menus.base_menu import BaseMenu
from menus.service_engineer_menu import ServiceEngineerMenu
from menus.system_admin_menu import SystemAdministratorMenu
from menus.super_admin_menu import SuperAdministratorMenu

class LoginMenu:
    def display(self):
        menu = BaseMenu("Login menu", {
            "1": ("Username", self.action),
            "2": ("Login", self.action),
            "3": ("Login", self.action),
            "4": ("Login as service engineer", ServiceEngineerMenu().display),
            "5": ("Login as system admin", SystemAdministratorMenu().display),
            "6": ("Login as super admin", SuperAdministratorMenu().display),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 1 action.")
