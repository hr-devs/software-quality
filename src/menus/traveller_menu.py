from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from database.repositories.traveller_repository import TravellerRepository
from input_handler import UserInput
from menus.base_menu import BaseMenu

class TravellerMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user

    def display(self):
        menu = BaseMenu("Traveller Menu", self.get_options)
        menu.display()

    def get_options(self):
        return {
            "1": ("Add new Traveller", self.add_traveller),
            "2": ("Update Traveller", self.update_traveller),
            "0": ("Back", lambda: "back")
        }

    def add_traveller(self):
        print("\nEnter traveller details:\n")
        data = (
            UserInput.get_data_input("First name: ", "String"),
            UserInput.get_data_input("Last name: ", "String"),
            UserInput.get_data_input("Birthday (YYYY-MM-DD): ", "DateTime"),
            UserInput.get_data_input("Gender (male/female): ", "Gender"),
            UserInput.get_data_input("Street name: ", "String"),
            int(UserInput.get_data_input("House number: ", "Int")),
            UserInput.get_data_input("Zip code: ", "PostalCode"),
            UserInput.get_data_input("City: ", "String"),
            UserInput.get_data_input("Email address: ", "Email"),
            UserInput.get_data_input("Mobile phone: ", "PostalCode"),
            UserInput.get_data_input("Driving license number: ", "PostalCode")
        )

        traveller_repo = TravellerRepository(self.db_connection)
        traveller_repo.add_traveller(data)
        print("\nTraveller added successfully!\n")

    def update_traveller(self):
        traveller_repo = TravellerRepository(self.db_connection)
        travellers = traveller_repo.fetch_all()

        if not travellers:
            print("No travellers found.")
            return

        traveller_options = {}
        print("\nSelect a traveller to update:\n")
        for idx, traveller in enumerate(travellers, start=1):
            traveller_id = traveller[0]
            first_name = traveller[1]
            last_name = traveller[2]
            traveller_options[str(idx)] = (f"{first_name} {last_name} (ID: {traveller_id})", traveller_id)

        traveller_options["0"] = ("Back", None)

        for key, (label, _) in traveller_options.items():
            print(f"{key}. {label}")

        choice = UserInput.get_menu_choice(traveller_options.keys())
        if choice == "0":
            return

        selected_traveller_id = traveller_options[choice][1]

        fields = {
            "1": ("first_name", "String"),
            "2": ("last_name", "String"),
            "3": ("birthday", "DateTime"),
            "4": ("gender", "Gender"),
            "5": ("street_name", "String"),
            "6": ("house_number", "Int"),
            "7": ("zip_code", "PostalCode"),
            "8": ("city", "String"),
            "9": ("email_address", "Email"),
            "10": ("mobile_phone", "PostalCode"),
            "11": ("driving_license_number", "PostalCode")
        }

        print("\nWhich field do you want to update?")
        for k, v in fields.items():
            print(f"{k}: {v[0]}")

        field_choice = UserInput.get_menu_choice(fields.keys())
        field_name, field_type = fields[field_choice]

        new_value = UserInput.get_data_input(f"Enter new value for '{field_name.replace('_', ' ')}': ", field_type)

        traveller_repo.update_field(selected_traveller_id, field_name, new_value)
        print(f"\nTraveller ID {selected_traveller_id}'s '{field_name}' updated successfully.")

