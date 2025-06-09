from input_handler import UserInput
from encryptor import Encryptor
from database.repositories.user_repository import UserRepository
from database.database_connection import DatabaseConnection

class Login:
    #TODO: send password and username to database (encrypted?)
    #@staticmethod
    def get_username():
        return UserInput.get_data_input("Username: ", "Username")
        
    def get_password():
        return UserInput.get_data_input("Password: ", "Password")
        
    def validate_credentials(username, password):
        db_connection = DatabaseConnection()
        user_repository = UserRepository(db_connection)
        encrypted_username = Encryptor.encrypt_data(username)
        print(user_repository.search_username(encrypted_username))
        print(username)
        print(encrypted_username)
        # b'gAAAAABoR1I11_yHU96zv4ArzHhxiL5FXhga954kO4LSF-1XXQ4TQVg7TbpmtKg1RbqRizfn1qjHpaTMJBuQVrh6N-5eoIgi4w=='
        
        
    def login():
        username = Login.get_username()
        #password = Login.get_password()
        Login.validate_credentials(username, "password")