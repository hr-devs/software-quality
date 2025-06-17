from os import path
import bcrypt
from cryptography.fernet import Fernet

class Encryptor:
    @staticmethod
    def generate_key(file_name="key.txt"):
        if not path.exists(file_name):
            key = Fernet.generate_key()
            with open(file_name, "wb") as f:
                f.write(key)
            return key
        else:
            return Encryptor.load_key(file_name)
        
    @staticmethod
    def load_key(filename="key.txt"):
        with open(filename, "rb") as f:
            return f.read()

    @staticmethod
    def encrypt_str(data: str, key_filename="key.txt") -> str:
        key = Encryptor.load_key(key_filename)
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data.decode()
    
    @staticmethod
    def encrypt_int(data: int, key_filename="key.txt") -> str:
        key = Encryptor.load_key(key_filename)
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(str(data).encode())
        return encrypted_data.decode()

    @staticmethod
    def decrypt_data(token: str, key_filename="key.txt") -> str:
        key = Encryptor.load_key(key_filename)
        fernet = Fernet(key)
        return fernet.decrypt(token).decode()
    
    @staticmethod
    def hash_str(password: str) -> str:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hashed_password.decode()
    
    @staticmethod
    def check_hashed_data(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())