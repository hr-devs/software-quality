# main.py

from menus.main_menu import main_menu
import database

def main():
    print("Welcome to the Console Menu Application!")
    database.initialize_database()
    main_menu()

if __name__ == "__main__":
    main()
