from input_handler import UserInput

class Login:
    @staticmethod
    def get_username_and_password():
        print(UserInput.get_data_input("Username: ", "Username"))
        print(UserInput.get_data_input("Password: ", "Password"))