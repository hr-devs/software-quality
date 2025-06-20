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
            "2": ("Update Scooter", self.update_scooter),
            "3": ("Delete Scooter", self.delete_scooter),
            "0": ("Back", lambda: "back")
        }

    def add_new_scooter(self):
        print("\nEnter scooter details:\n")

        brand = UserInput.get_data_input("Brand: ", "String")
        model = UserInput.get_data_input("Model: ", "String")
        serial_number = UserInput.get_data_input("Serial number (10-17 alphanumeric): ", "PostalCode")

        top_speed = int(UserInput.get_data_input("Top speed (km/h): ", "ZeroToHundred"))
        battery_capacity = int(UserInput.get_data_input("Battery capacity (Wh): ", "ZeroToHundred"))
        soc = UserInput.get_data_input("State of charge (0-100): ", "ZeroToHundred")
        soc_min_target = UserInput.get_data_input("Minimum SoC target (0-100): ", "ZeroToHundred")
        soc_max_target = UserInput.get_data_input("Maximum SoC target (0-100): ", "ZeroToHundred")

        description = input("Description (optional): ").strip()

        latitude = UserInput.get_data_input("Latitude (e.g. 51.92250): ", "FloatLatLong")
        longitude = UserInput.get_data_input("Longitude (e.g. 4.47917): ", "FloatLatLong")

        out_of_service = UserInput.get_data_input("Out of service? (0 = No, 1 = Yes): ", "YesNoInt")
        mileage = UserInput.get_data_input("Mileage (in km): ", "Float")
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

    def update_scooter(self):
        scooter_repo = ScooterRepository(self.db_connection)
        scooters = scooter_repo.fetch_all()

        if not scooters:
            print("No scooters found.")
            return

        scooter_options = {}
        print("\nSelect a scooter to update:\n")
        for idx, scooter in enumerate(scooters, start=1):
            scooter_id = scooter[0]
            brand = scooter[1]
            model = scooter[2]
            serial = scooter[3]
            scooter_options[str(idx)] = (f"{brand} {model} (Serial: {serial})", scooter_id)

        scooter_options["0"] = ("Back", None)

        for key, (label, _) in scooter_options.items():
            print(f"{key}. {label}")

        choice = UserInput.get_menu_choice(scooter_options.keys())
        if choice == "0":
            return

        selected_scooter_id = scooter_options[choice][1]

        fields = {
            "1": ("brand", "String"),
            "2": ("model", "String"),
            "3": ("serial_number", "PostalCode"),
            "4": ("top_speed", "ZeroToHundred"),    
            "5": ("battery_capacity", "ZeroToHundred"),  
            "6": ("soc", "ZeroToHundred"),               
            "7": ("soc_min_target", "ZeroToHundred"),    
            "8": ("soc_max_target", "ZeroToHundred"),    
            "9": ("description", None),
            "10": ("latitude", "FloatLatLong"),
            "11": ("longitude", "FloatLatLong"),
            "12": ("out_of_service", "YesNoInt"),
            "13": ("mileage", "Float"),
            "14": ("last_maintenance_date", "DateTime")
        }

        print("\nWhich field do you want to update?")
        for k, v in fields.items():
            print(f"{k}: {v[0]}")

        field_choice = UserInput.get_menu_choice(fields.keys())
        field_name, field_type = fields[field_choice]

        if field_type:
            new_value = UserInput.get_data_input(f"Enter new value for '{field_name}': ", field_type)
            if field_type in ("Int", "ZeroToHundred"):
                new_value = int(new_value)
        else:
            new_value = input(f"Enter new value for '{field_name}': ").strip()

        scooter_repo.update_scooter(selected_scooter_id, field_name, new_value)
        print(f"\nScooter {selected_scooter_id}'s '{field_name}' updated successfully.")

    def delete_scooter(self):
        scooter_repo = ScooterRepository(self.db_connection)
        scooters = scooter_repo.fetch_all()

        if not scooters:
            print("No scooters available to delete.")
            return

        scooter_options = {}
        print("\nSelect a scooter to DELETE:\n")
        for idx, scooter in enumerate(scooters, start=1):
            scooter_id = scooter[0]
            brand = scooter[1]
            model = scooter[2]
            serial = scooter[3]
            scooter_options[str(idx)] = (f"{brand} {model} (Serial: {serial})", scooter_id)

        scooter_options["0"] = ("Back", None)

        for key, (label, _) in scooter_options.items():
            print(f"{key}. {label}")

        choice = UserInput.get_menu_choice(scooter_options.keys())
        if choice == "0":
            return

        selected_scooter_id = scooter_options[choice][1]

        confirm = input(f"\nAre you sure you want to delete scooter ID {selected_scooter_id}? Type 'yes' to confirm: ").strip().lower()
        if confirm == "yes":
            scooter_repo.delete_scooter(selected_scooter_id)
            print("\nScooter deleted successfully.")
        else:
            print("\nDeletion cancelled.")
