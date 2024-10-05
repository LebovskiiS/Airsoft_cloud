import os
import hashlib


class HashFunction:
    def __init__(self,iterations: int = 100000):
        self.iterations = iterations

    def get_hashed_password(self, password: str, salt: bytes = None) -> str:
        if not salt:
            salt = os.urandom(16)
        dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, self.iterations)
        return salt.hex() + dk.hex()

    def verify_password(self, stored_password: str, provided_password: str) -> bool:
        salt = bytes.fromhex(stored_password[:32])
        stored_password = stored_password[32:]
        dk = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, self.iterations)
        return stored_password == dk.hex()
