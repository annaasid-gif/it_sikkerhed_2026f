from cryptography.fernet import Fernet
import bcrypt
import os

KEY_FILE = "key.key"

# Genererer eller loader krypteringsnøglen
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

# Kryptering af data
def encrypt_data(data: str) -> bytes:
    f = load_key()
    return f.encrypt(data.encode())

# Dekryptering af data
def decrypt_data(token: bytes) -> str:
    f = load_key()
    return f.decrypt(token).decode()

# Hashing af password
def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Validering af password
def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)
