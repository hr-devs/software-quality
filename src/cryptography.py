from os import path
from cryptography.fernet import Fernet

class Encryptor:
    def generate_key(file_name="key.txt"):
        if not path.exists(file_name):
            key = Fernet.generate_key()
            with open(file_name, "wb") as f:
                f.write(key)
            return key
        
    def load_key(filename="key.txt"):
        with open(filename, "rb") as f:
            return f.read()

    def encrypt_message(message: str) -> bytes:
        return Fernet.encrypt(message.encode())

    def decrypt_message(token: bytes) -> str:
        return Fernet.decrypt(token).decode()
    
    def hash_pwd(password: str) -> hash:
        bcrypt.hashpw(password, bcrypt.gensalt())
    
    def check_pwd(password: str, hashed_password):
        return bcrypt.checkpw(password, hashed_password)
