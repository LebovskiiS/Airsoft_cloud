import os
import hashlib
from confg import SECRET_KEY

class HashFunction:
    def __init__(self,iterations: int = 10):
        self.iterations = iterations

    def get_hashed_password(self, password: str) -> str:
        dk = hashlib.pbkdf2_hmac('sha256', password.encode(), SECRET_KEY.encode(), self.iterations)
        return dk.hex()

    def verify_password(self, stored_password: str, provided_password: str) -> bool:
        dk = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), SECRET_KEY.encode(), self.iterations)
        return stored_password == dk.hex()


hashed_function = HashFunction()
