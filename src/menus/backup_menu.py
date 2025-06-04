from menus.base_menu import BaseMenu

class BackupMenu:
    def display(self):
        menu = BaseMenu("Backup Menu", {
            "1": ("Make Backup", self.action),
            "2": ("Restore Backup", self.action),
            "3": ("Allow System Admin to Restore Backup", self.action),
            "4": ("Revoke System Admin to Restore Backup", self.action),
            "0": ("Back", lambda: "back")
        })
        menu.display()

    def action(self):
        print("You selected Submenu 2 action.")
