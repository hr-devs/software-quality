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

    def show_travellers(self): # NOT PROPERLY IMPLEMENTED
        travellers = self.traveller_repo.fetch_all()
        for traveller in travellers:
            print(f"{traveller[0]} | {traveller[1]} {traveller[2]} | {traveller[8]}")

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
        print("Traveller added successfully!")

    def update_traveller(self):
        travellers = self.traveller_repo.fetch_all()
        traveller_dict = {}
        for i, t in enumerate(travellers):
            traveller_dict[str(i + 1)] = (f"{t[1]} {t[2]} | {t[8]}", t[0])  # ID is t[0]

        traveller_dict["0"] = ("Back", lambda: "back")
        menu = BaseMenu("Select a traveller to update", lambda: traveller_dict)
        selected_id = menu.display()

        if selected == "back" or selected not in traveller_dict:
            return

        traveller_id = traveller_dict[selected_id][1]

        field_options = {
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
            "0": ("Back", lambda: "back")
        }

        def get_field_menu():
            return {k: (v[0], lambda f=v[0], t=v[1]: (f, t)) for k, v in field_options.items()}

        field_menu = BaseMenu("Select field to update", get_field_menu)
        selected = field_menu.display()
        if selected == "back":
            return

        field, input_type = field_options[selected]
        new_value = UserInput.get_data_input(f"Enter new value for {field}: ", input_type)
        if input_type == "Int":
            new_value = int(new_value)

        self.traveller_repo.update_field(traveller_id, field, new_value)
        print(f"{field} updated successfully!")

    def delete_traveller(self):
        travellers = self.traveller_repo.fetch_all()
        traveller_dict = {}
        for i, t in enumerate(travellers):
            traveller_dict[str(i + 1)] = (f"{t[1]} {t[2]} | {t[8]}", t[0])

        traveller_dict["0"] = ("Back", lambda: "back")
        menu = BaseMenu("Select a traveller to delete", lambda: traveller_dict)
        selected_id = menu.display()

        if selected_id == "back" or selected_id not in traveller_dict:
            return

        traveller_id = traveller_dict[selected_id][1]
        self.traveller_repo.delete_traveller(traveller_id)
        print("Traveller deleted successfully.")
