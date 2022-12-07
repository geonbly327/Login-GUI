import hashlib
import random
import string

def hash_password(password) -> tuple(hashlib.sha256, str):
    salt = _salt()
    password = password + salt

    hashed_password = hashlib.sha256(password.encode())

    return hashed_password, salt

def _salt() -> str:
    count = random.randint(16, 21)
    string_store = string.ascii_letters + string.digits + string.punctuation
    salt = "".join(random.choices(string_store, k=count))
    return salt

def verify_password(password, user_password, salt) -> bool:
    password = password + salt
    hashed_password = hashlib.sha256(password.encode())

    return True if hashed_password.hexdigest() == user_password.hexdigest() else False

if __name__ == "__main__":
    password = input("Enter password: ")
    hashed_password, salt = hash_password(password)
    print(f"salt : {salt}")
    print(f"hashed_password : {hashed_password}")
    print(f"sha256 : {hashed_password.hexdigest()}")