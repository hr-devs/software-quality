# menus/traveller_menu.py

from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from input_handler import UserInput
from menus.base_menu import BaseMenu
from database.repositories.traveller_repository import TravellerRepository

class TravellerMenu:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user
        self.traveller_repo = TravellerRepository(db_connection)

    def display(self):
        menu = BaseMenu("Traveller Menu", self.get_options)
        menu.display()

    def get_options(self):
        return {
            "1": ("Search Travellers", self.show_travellers),
            "2": ("Add new Traveller", self.add_traveller),
            "3": ("Update Traveller", self.update_traveller),
            "4": ("Delete Traveller", self.delete_traveller),
            "0": ("Back", lambda: "back")
        }

    def show_travellers(self):
        travellers = self.traveller_repo.fetch_all()
        if not travellers:
            print("\nNo travellers found.\n")
            return
        print("\nAll Travellers:")
        for traveller in travellers:
            print(f"{traveller[0]} | {traveller[1]} {traveller[2]} | {traveller[8]}")
        print()

    def add_traveller(self):
        print("\nEnter traveller details:\n")
        data = (
            UserInput.get_data_input("First name: ", "String"),
            UserInput.get_data_input("Last name: ", "String"),
            UserInput.get_data_input("Birthday (YYYY-MM-DD): ", "DateTime"),
            UserInput.get_data_input("Gender (male/female): ", "String"),
            UserInput.get_data_input("Street name: ", "String"),
            int(UserInput.get_data_input("House number: ", "Int")),
            UserInput.get_data_input("Zip code: ", "PostalCode"),
            UserInput.get_data_input("City: ", "String"),
            UserInput.get_data_input("Email address: ", "Email"),
            UserInput.get_data_input("Mobile phone: ", "PostalCode"),
            UserInput.get_data_input("Driving license number: ", "PostalCode")
        )
        self.traveller_repo.insert_travellers([data])
        print("\nTraveller added successfully!\n")

    def update_traveller(self):
        travellers = self.traveller_repo.fetch_all()
        if not travellers:
            print("\nNo travellers found.\n")
            return

        traveller_options = {}
        print("\nSelect a traveller to update:\n")
        for idx, t in enumerate(travellers, start=1):
            traveller_options[str(idx)] = (f"{t[1]} {t[2]} | {t[8]}", t[0])

        traveller_options["0"] = ("Back", None)

        for key, (label, _) in traveller_options.items():
            print(f"{key}. {label}")

        choice = UserInput.get_menu_choice(traveller_options.keys())
        if choice == "0":
            return

        traveller_id = traveller_options[choice][1]

        fields = {
            "1": ("first_name", "String"),
            "2": ("last_name", "String"),
            "3": ("birthday", "DateTime"),
            "4": ("gender", "String"),
            "5": ("street_name", "String"),
            "6": ("house_number", "Int"),
            "7": ("zip_code", "PostalCode"),
            "8": ("city", "String"),
            "9": ("email_address", "Email"),
            "10": ("mobile_phone", "PostalCode"),
            "11": ("driving_license_number", "PostalCode"),
            "0": ("Back", None)
        }

        print("\nWhich field do you want to update?")
        for k, v in fields.items():
            print(f"{k}: {v[0]}")

        field_choice = UserInput.get_menu_choice(fields.keys())
        if field_choice == "0":
            return

        field_name, input_type = fields[field_choice]
        new_value = UserInput.get_data_input(f"Enter new value for '{field_name}': ", input_type)
        if input_type == "Int":
            new_value = int(new_value)

        self.traveller_repo.update_field(traveller_id, field_name, new_value)
        print(f"\nTraveller's '{field_name}' updated successfully.\n")

    def delete_traveller(self):
        travellers = self.traveller_repo.fetch_all()
        if not travellers:
            print("\nNo travellers available to delete.\n")
            return

        traveller_options = {}
        print("\nSelect a traveller to DELETE:\n")
        for idx, t in enumerate(travellers, start=1):
            traveller_options[str(idx)] = (f"{t[1]} {t[2]} | {t[8]}", t[0])

        traveller_options["0"] = ("Back", None)

        for key, (label, _) in traveller_options.items():
            print(f"{key}. {label}")

        choice = UserInput.get_menu_choice(traveller_options.keys())
        if choice == "0":
            return

        traveller_id = traveller_options[choice][1]

        confirm = input(f"\nAre you sure you want to delete traveller ID {traveller_id}? Type 'yes' to confirm: ").strip().lower()
        if confirm == "yes":
            self.traveller_repo.delete_traveller(traveller_id)
            print("\nTraveller deleted successfully.\n")
        else:
            print("\nDeletion cancelled.\n")
