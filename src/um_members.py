# main.py

from database.repositories.activity_log_repository import ActivityLogRepository
from login import Login
from menus.main_menu import main_menu
from database.database_connection import DatabaseConnection
from database.database_manager import DatabaseManager
from encryptor import Encryptor
from logger import Logger

def main():
    Encryptor.generate_key()
    
    db_connection = DatabaseConnection()
    db_manager = DatabaseManager(db_connection)
    db_manager.initialize_database()
    
    activity_repo = ActivityLogRepository(db_connection)
    logger = Logger(activity_repo)
    login = Login(db_connection)
    #logger.log_activity("test", "sus activity", "extra info", True)

    #print(db_manager.activity_log_repo.fetch_all())

    main_menu(db_connection, login)

if __name__ == "__main__":
    main()
