from data_transfer_objects import User
from database.database_connection import DatabaseConnection
from database.repositories.user_repository import UserRepository
from encryptor import Encryptor
from input_handler import UserInput


class UserService:
    def __init__(self, db_connection: DatabaseConnection, user: User):
        self.db_connection = db_connection
        self.user = user
        
    def update_password(self):
        new_password = None

        if(Encryptor.check_hashed_data(UserInput.get_data_input("current password: ", "Password"), self.user.password)):
            new_password = Encryptor.hash_str(UserInput.get_data_input("new password: ", "Password"))
            UserRepository(self.db_connection).update_password(self.user.id, new_password)
            self.user.password = new_password
            print("\nPassword updated!")
        
        else:
            print("\nIncorrect password")
            return        