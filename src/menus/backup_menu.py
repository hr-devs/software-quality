from backup import Backup
from menus.base_menu import BaseMenu

class BackupMenu:
    def __init__(self, backup: Backup):
        self.backup = backup

    def get_options(self):
        return {
            "1": ("Make Backup", self.backup.backup),
            "2": ("Restore Backup", self.display_restore_options),
            "3": ("Allow System Admin to Restore Backup", self.action),
            "4": ("Revoke System Admin to Restore Backup", self.action),
            "0": ("Back", lambda: "back")
        }

    def display(self):
        menu = BaseMenu("Backup Menu", self.get_options)
        menu.display()

    def get_restore_options(self):
        # for key, (label, _) in self.backup.get_restore_options().items():
        #     print(f"{key}: {label}")

        return self.backup.get_restore_options()

    def display_restore_options(self):
        menu2 = BaseMenu("Restore Menu", self.get_restore_options)
        print("\n!!! You will be logged out if you restore a backup !!!")
        menu2.display()

    def action(self):
        print("You selected Submenu 2 action.")
