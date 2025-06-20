from backup import Backup
from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from database.repositories.restore_codes_repository import RestoreCodesRepository
from database.repositories.user_repository import UserRepository
from enums import Role
from menus.base_menu import BaseMenu

class BackupMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.backup = Backup(db_connection)
        self.user = user
        self.user_repo = UserRepository(db_connection)
        self.restore_code_repo = RestoreCodesRepository(db_connection)

    def get_options(self):
        if(self.user.role_id == Role.SUPER_ADMIN.value):
            return {
                "1": ("Make Backup", self.backup.backup),
                "2": ("Restore Backup", self.display_restore_options),
                "3": ("Allow System Admin to Restore Backup", self.display_generate_restore_code),
                "0": ("Back", lambda: "back")
            }
        
        if(self.user.role_id == Role.SYSTEM_ADMIN.value):
            return {
                "1": ("Make Backup", self.backup.backup),
                "0": ("Back", lambda: "back")
            }

    def display(self):
        menu = BaseMenu("Backup Menu", self.get_options)
        menu.display()


    def display_restore_options(self):
        menu = BaseMenu("Restore Menu", self.backup.get_restore_options())
        print("\n!!! You will be logged out if you restore a backup !!!")
        menu.display()

    def display_generate_restore_code(self):
        selected = [None]

        def get_admin(sa):
            selected[0] = sa
            return "back"

        menu = BaseMenu("Choose a system admin that can restore a backup", lambda: self.user_repo.get_system_administrators_options(get_admin))
        menu.display()

        admin = selected[0]
        print(admin)
        #-------------

        selected = [None]

        def get_backup(b):
            selected[0] = b
            return "back"
        
        menu = BaseMenu("Choose a backup the system admin can restore", lambda: self.backup.get_restore_code_options(get_backup))
        menu.display()
        backup = selected[0]

        code = self.backup.generate_restore_code(admin[1], admin[3], backup)
        print(f"Restore code: {code} generated and usable")
    
