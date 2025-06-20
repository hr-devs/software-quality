# input_handler.py

from datetime import datetime
import re

class UserInput:
    @staticmethod
    def get_menu_choice(valid_choices):
        while True:
            choice = input("\nSelect an option: ").strip()
            if choice in valid_choices:
                return choice
            print("Invalid choice. Try again.")

    @staticmethod
    def get_data_input(inputSentence, type):
        stringPattern = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]{1,80}$")
        intPattern = re.compile(r"^\d+$")
        datePattern = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")
        alphanumericPattern = re.compile(r"^[A-Za-z0-9\s-]{10,17}$")  # For serial number
        emailPattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        passwordPattern = re.compile(r"^[A-Za-z0-9~!@#$%&_\-+=`|\\(){}\[\]:;'<>,.?/]{12,30}$")
        usernamePattern = re.compile(r"^[A-Za-z_][A-Za-z0-9_'.]{7,9}$", re.IGNORECASE)
        genderPattern = re.compile(r"^(male|female)$", re.IGNORECASE)

        while True:
            userInput = input(inputSentence).strip()

            if type == "String":
                if stringPattern.fullmatch(userInput):
                    return userInput
                print("Invalid input. Only letters, spaces, hyphens, and apostrophes are allowed.")

            elif type == "Int":
                if intPattern.fullmatch(userInput):
                    return userInput
                print("Invalid input. Only whole numbers are allowed.")

            elif type == "FloatRange":
                try:
                    value = float(userInput)
                    if 0.0 <= value <= 100.0:
                        return value
                    print("Value must be between 0.0 and 100.0.")
                except ValueError:
                    print("Invalid input. Enter a decimal number (e.g., 75.0).")

            elif type == "FloatLatLong":
                try:
                    return float(userInput)
                except ValueError:
                    print("Invalid coordinate. Use decimal format (e.g., 51.92250).")

            elif type == "YesNoInt":
                if userInput in ["0", "1"]:
                    return int(userInput)
                print("Invalid input. Use 0 for No, 1 for Yes.")

            elif type == "Float":
                try:
                    return float(userInput)
                except ValueError:
                    print("Invalid number. Enter a decimal (e.g., 15.5).")

            elif type == "DateTime":
                if datePattern.fullmatch(userInput):
                    try:
                        valid_date = datetime.strptime(userInput, "%Y-%m-%d")
                        return userInput
                    except ValueError:
                        print("Date is not valid.")
                else:
                    print("Invalid input. Use YYYY-MM-DD format.")

            elif type == "PostalCode":
                if alphanumericPattern.fullmatch(userInput):
                    return userInput
                print("Invalid input. Must be 10-17 alphanumeric characters.")

            elif type == "Email":
                if emailPattern.fullmatch(userInput):
                    return userInput
                print("Invalid email format.")

            elif type == "Username":
                if usernamePattern.fullmatch(userInput):
                    return userInput
                print("Username must be 8-10 chars, start with letter/underscore, and only use _, ', or .")

            elif type == "Password":
                if passwordPattern.fullmatch(userInput):
                    return userInput
                print("Password must be 12-30 chars and include special characters.")

            elif type == "Gender":
                if genderPattern.fullmatch(userInput):
                    return userInput.lower()
                print("Invalid input. Please enter 'male' or 'female'.")

            else:
                print(f"Unknown input type: {type}")
