import os
from datetime import datetime
import random
import string
from typing import List, Tuple
import zipfile
from data_transfer_objects import RestoreCode
from database.database_connection import DatabaseConnection
from database.repositories.activity_log_repository import ActivityLogRepository
from database.repositories.restore_codes_repository import RestoreCodesRepository
from database.repositories.user_repository import UserRepository
from encryptor import Encryptor


class Backup:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.restore_codes_repo = RestoreCodesRepository(db_connection)
        self.users_repo = UserRepository(db_connection)
        self.activity_logs_repo = ActivityLogRepository(db_connection)
        self.backup_files = ['key.txt', 'urban_mobility.db']
        self.backup_folder = 'backups'

    def backup(self):
        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        zip_path = os.path.join(self.backup_folder, f'backup_{timestamp}.zip')

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in self.backup_files:
                if os.path.isfile(file):
                    zipf.write(file)
                    print(f"Added '{file}' to '{zip_path}'.")
                else:
                    print(f"'{file}' is not a valid file.")

        return zip_path

    def restore(self, zip_filename):
        zip_path = os.path.join(self.backup_folder, zip_filename)

        if not os.path.exists(zip_path) or not zipfile.is_zipfile(zip_path):
            print(f"Backup file '{zip_filename}' not found or invalid!")
            return
        
        # Storing all data outside scope of backup + clearing those tables
        
        restore_codes = self.restore_codes_repo.fetch_all()
        self.restore_codes_repo.clear_all()

        users = self.users_repo.fetch_all()
        self.users_repo.clear_all()

        activity_logs = self.activity_logs_repo.fetch_all()
        self.activity_logs_repo.clear_all()

        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall()
            for name in zipf.namelist():
                print(f"Restored {name}")

        # Putting saved data back into database 

        self.restore_codes_repo.insert_restore_codes(restore_codes)
        self.users_repo.insert_users(users)
        self.activity_logs_repo.insert_activity_logs(activity_logs)

        # Logging user out, out of precausion

        print("You will now be logged out!")
        exit()
        
    def delete_existing_files(file_names, directory):
        for file_name in file_names:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"File not found: {file_path}")

    def get_backup_list(self):
        backup_list = []
        if not os.path.exists(self.backup_folder) or not os.path.isdir(self.backup_folder):
            print(f"Backup folder not found!")
            return backup_list

        for folder in os.listdir(self.backup_folder):
            backup_list.append(folder)

        return backup_list
    
    def get_restore_options(self):
        restore_options = {}
        backup_list = self.get_backup_list()

        for index, backup_name in enumerate(backup_list):
            restore_options[str(index + 1)] = (
                f"Restore {backup_name}",
                lambda b=backup_name: self.restore(b)
            )

        restore_options["0"] = ("Back", lambda: "back")
        return restore_options

    def get_restore_code_options(self, function):
        restore_options = {}
        backup_list = self.get_backup_list()

        for index, backup_name in enumerate(backup_list):
            restore_options[str(index + 1)] = (
                f"Backup {backup_name}",
                lambda b=backup_name: function(b)
            )

        restore_options["0"] = ("Back", lambda: "back")
        return restore_options

    def generate_restore_code(self, username, role_id, backup):
        chars = string.ascii_uppercase + string.digits
        all_restore_code_data: List[Tuple] = self.restore_codes_repo.fetch_all()
        all_codes = []
        for restore_code in all_restore_code_data:
            all_codes.append(Encryptor.decrypt_data(restore_code[1]))
        
        restore_code = RestoreCode("XXXX", backup, datetime.now().isoformat(), username, role_id, False, False)

        while True:
            code = ''.join(random.choices(chars, k=4))
            if code not in all_codes:
                restore_code.restore_code = code
                self.restore_codes_repo.insert_restore_code(restore_code)
                return code


