import time
import tracemalloc
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import bcrypt
import hashlib
import os

# Benchmark helper
def benchmark(func, *args):
    tracemalloc.start()
    start = time.perf_counter()
    result = func(*args)
    elapsed = (time.perf_counter() - start) * 1000
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, elapsed, peak / 1024

data = b"Anna A, Zealand Naestved" * 50  # ca. 1 KB

# ---------------- SYMMETRISK ----------------

def test_fernet():
    key = Fernet.generate_key()
    f = Fernet(key)
    _, enc_time, enc_mem = benchmark(f.encrypt, data)
    token = f.encrypt(data)
    _, dec_time, dec_mem = benchmark(f.decrypt, token)
    print("\n[Fernet AES-128]")
    print("Encrypt:", enc_time, "ms", "RAM:", enc_mem, "KB")
    print("Decrypt:", dec_time, "ms", "RAM:", dec_mem, "KB")

def test_aes128():
    key = os.urandom(16)
    cipher = AES.new(key, AES.MODE_EAX)
    _, enc_time, enc_mem = benchmark(cipher.encrypt, data)
    print("\n[AES-128]")
    print("Encrypt:", enc_time, "ms", "RAM:", enc_mem, "KB")

# ---------------- ASYMMETRISK ----------------

def test_rsa2048():
    key = RSA.generate(2048)
    cipher = PKCS1_OAEP.new(key)
    chunk = data[:190]
    _, enc_time, enc_mem = benchmark(cipher.encrypt, chunk)
    print("\n[RSA-2048]")
    print("Encrypt:", enc_time, "ms", "RAM:", enc_mem, "KB")

# ---------------- HASHING ----------------

def test_bcrypt():
    _, hash_time, hash_mem = benchmark(bcrypt.hashpw, b"Test123!", bcrypt.gensalt())
    print("\n[bcrypt]")
    print("Hash:", hash_time, "ms", "RAM:", hash_mem, "KB")

def test_sha256():
    _, hash_time, hash_mem = benchmark(hashlib.sha256, data)
    print("\n[SHA-256]")
    print("Hash:", hash_time, "ms", "RAM:", hash_mem, "KB")

# ---------------- RUN ----------------

if __name__ == "__main__":
    test_fernet()
    test_aes128()
    test_rsa2048()
    test_bcrypt()
    test_sha256()
