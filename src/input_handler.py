import datetime
import re

class input:
    def get_menu_choice(valid_choices): # whitelisted with specified valid choices
        while True:
            choice = input("\nSelect an option: ").strip()
            if choice in valid_choices:
                return choice
            print("Invalid choice. Try again.")

    def get_data_input(inputSentence, type):
        stringPattern = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]{1,80}$")  # Adjust length as needed
        intPattern = re.compile(r"^\d+$")
        datePattern = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")
        alphanumericPattern = re.compile(r"^[A-Za-z0-9\s-]{1,20}$")
        emailPattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        passwordPattern = re.compile(r"^[A-Za-z0-9~!@#$%&_\-+=`|\\(){}\[\]:;'<>,.?/]{12,30}$")
        usernamePattern = re.compile(r"^[A-Za-z_][A-Za-z0-9_'.]{7,9}$", re.IGNORECASE)
        
        while True:
            if(type == "String"):
                userInput = input(inputSentence).strip()
                if stringPattern.fullmatch(userInput):
                    return userInput
                print("Invalid input. Only letters, spaces, hyphens, and apostrophes are allowed.")
                
            elif(type == "Int"):
                userInput = input(inputSentence).strip()
                if intPattern.fullmatch(userInput):
                    return userInput
                print("Invalid input. Only whole numbers are allowed.")
                
            elif(type == "DateTime"):
                userInput = input(inputSentence).strip()
                if datePattern.fullmatch(userInput):
                    try:
                        valid_date = datetime.strptime(userInput, "%Y-%m-%d")
                        return userInput
                    except ValueError:
                        print("Date is not valid.")
                else:
                    print("Invalid input. Only YYYY-MM-DD format is allowed.")
                    
            elif(type == "PostalCode"):
                userInput = input(inputSentence).strip()
                if alphanumericPattern.fullmatch(userInput):
                    return userInput
                print("Invalid input. Only postal codes are allowed")
                
            elif(type == "Email"):
                userInput = input(inputSentence).strip()
                if emailPattern.fullmatch(userInput):
                    return userInput
                print("Invalid input. Only Email addresses are allowed")
                
            elif(type == "Username"):
                userInput = input(inputSentence).strip()
                if usernamePattern.fullmatch(userInput):
                    return userInput
                print("Username must be 8-10 characters, start with a letter or underscore, and only contain letters, numbers, underscores (_), apostrophes ('), and periods (.)")  
                
            elif(type == "Password"):
                userInput = input(inputSentence).strip()
                if passwordPattern.fullmatch(userInput):
                    return userInput
                print("Password must be 12-30 characters and include lowercase, uppercase, number, and special character.")