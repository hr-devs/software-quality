# submenu1.py

from menus.base_menu import BaseMenu
from menus.service_engineer_menu import ServiceEngineerMenu
from menus.system_admin_menu import SystemAdministratorMenu
from menus.super_admin_menu import SuperAdministratorMenu

class LoginMenu:
    def display(self):
        menu = BaseMenu("Login menu", {
            "1": ("Login", self.action),
            "2": ("Login as service engineer", ServiceEngineerMenu().display),
            "3": ("Login as system admin", SystemAdministratorMenu().display),
            "4": ("Login as super admin", SuperAdministratorMenu().display),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 1 action.")
