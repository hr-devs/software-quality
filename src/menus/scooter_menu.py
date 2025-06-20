from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from input_handler import UserInput
from menus.base_menu import BaseMenu
from database.repositories.scooter_repository import ScooterRepository

class ScooterMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user
        
    def display(self):
        menu = BaseMenu("Scooter Menu", self.get_options)
        menu.display()

    def get_options(self):
        return {
            "1": ("Add new Scooter", self.add_new_scooter),
            "2": ("Update Scooter", self.action),
            "3": ("Delete Scooter", self.action),
            "0": ("Back", lambda: "back")
        }

    def action(self):
        print("You selected Submenu 2 action.")
        
    def add_new_scooter(self):
        print("\nEnter scooter details:\n")

        brand = UserInput.get_data_input("Brand: ", "String")
        model = UserInput.get_data_input("Model: ", "String")
        serial_number = UserInput.get_data_input("Serial number (10-17 alphanumeric): ", "PostalCode")

        top_speed = int(UserInput.get_data_input("Top speed (km/h): ", "Int"))
        battery_capacity = int(UserInput.get_data_input("Battery capacity (Wh): ", "Int"))
        soc = float(UserInput.get_data_input("State of charge (0.0-100.0): ", "Int")) 
        soc_min_target = float(UserInput.get_data_input("Minimum SoC target (0.0-100.0): ", "Int"))
        soc_max_target = float(UserInput.get_data_input("Maximum SoC target (0.0-100.0): ", "Int"))

        description = input("Description (optional): ").strip()

        latitude = float(UserInput.get_data_input("Latitude (e.g. 51.92250): ", "Int"))  # You could write a Float handler for more precision
        longitude = float(UserInput.get_data_input("Longitude (e.g. 4.47917): ", "Int"))

        out_of_service = int(UserInput.get_data_input("Out of service? (0 = No, 1 = Yes): ", "Int"))
        mileage = float(UserInput.get_data_input("Mileage (in km): ", "Int"))
        last_maintenance_date = UserInput.get_data_input("Last maintenance date (YYYY-MM-DD): ", "DateTime")

        scooter_data = (
            brand, model, serial_number,
            top_speed, battery_capacity, soc,
            soc_min_target, soc_max_target,
            description,
            latitude, longitude,
            out_of_service, mileage, last_maintenance_date
        )

        ScooterRepository.add_scooter(self, scooter_data)
        print("\nScooter added successfully!")
