from menus.base_menu import BaseMenu

class ServiceEngineerManagerMenu:
    def display(self):
        #ALERT ALERT NOT SERVICE ENGINEER MENU ______ MANAGER MENUUUUU
        menu = BaseMenu("Service Engineer Manager Menu", {
            "1": ("Add new Service Engineer", self.action),
            "2": ("Update Service Engineer", self.action),
            "3": ("Reset password of Service Engineer", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
