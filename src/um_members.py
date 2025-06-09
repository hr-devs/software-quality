# main.py

from menus.main_menu import main_menu
from database.database_connection import DatabaseConnection
from database.database_manager import DatabaseManager
from encryptor import Encryptor

def main():
    print("Welcome to the Console Menu Application!")

    Encryptor.generate_key()
    
    db_connection = DatabaseConnection()
    db_manager = DatabaseManager(db_connection)
    db_manager.initialize_database()
    db_manager.populate_dummy_data()

    main_menu()

if __name__ == "__main__":
    main()
