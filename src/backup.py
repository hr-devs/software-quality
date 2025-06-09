import os
from shutil import copy
from datetime import datetime


class Backup:
    backup_files = ['key.txt', 'urban_mobility.db']
    backup_folder = 'backups'

    def backup(self):
        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        backup_subfolder = f'backups/backup_{timestamp}'
        os.makedirs(backup_subfolder)

        for file in self.backup_files:
            if os.path.isfile(file):
                copy(file, backup_subfolder)
                print(f"Copied '{file}' to '{self.backup_folder}'.")
            else:
                print(f"'{file}' is not a valid file.")

        return backup_subfolder

    def restore(self, backup_subfolder):
        path = f'backups/{backup_subfolder}'

        if not os.path.exists(path) or not os.path.isdir(path):
            print(f"Backup folder '{backup_subfolder}' not found!")
            return

        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)

            if os.path.isfile(file_path):
                original_location = file_name
                copy(file_path, original_location)
                print(f"Restored {file_path}")

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


