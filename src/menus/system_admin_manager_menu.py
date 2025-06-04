from menus.base_menu import BaseMenu

class SystemAdminManagerMenu:
    def display(self):
        #ALERT ALERT NOT SYSTEM ADMIN MENU ______ MANAGER MENUUUUU
        menu = BaseMenu("System Admin Manager Menu", {
            "1": ("Add new System Administrator", self.action),
            "2": ("Update System Administrator", self.action),
            "3": ("Delete System Administrator", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
