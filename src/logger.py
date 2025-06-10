from typing import List
from database.repositories.activity_log_repository import ActivityLogRepository
from data_transfer_objects import ActivityLog
from encryptor import Encryptor
from datetime import datetime

class Logger:
    def __init__(self, activity_repo: ActivityLogRepository):
        self.activity_repo = activity_repo

    def log_activity(self, username: str, activity: str, additional_info: str, suspicious: bool):
        suspicious = 1 if suspicious else 0
        log = ActivityLog(
            log_date=Encryptor.encrypt_str(datetime.today().strftime('%Y-%m-%d')),
            log_time=Encryptor.encrypt_str(datetime.now().strftime('%H:%M:%S')),
            username=Encryptor.encrypt_str(username),
            activity_description=Encryptor.encrypt_str(activity),
            additional_info=Encryptor.encrypt_str(additional_info),
            suspicious=Encryptor.encrypt_int(suspicious),
            seen=Encryptor.encrypt_int(0) 
        )

        self.activity_repo.insert_activity_log(log)
