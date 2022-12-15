import hashlib
import random
import string

#hash_password 함수 : password를 salt와 함께 해싱하여 반환
def hash_password(password, salt) -> str:
    password = password + salt
    hashed_password = hashlib.sha256(password.encode())

    return hashed_password.hexdigest()

#create_salt 함수 : salt를 생성하여 반환
def create_salt() -> str:
    count = random.randint(16, 21)
    string_store = string.ascii_letters + string.digits + string.punctuation
    salt = "".join(random.choices(string_store, k=count))
    return salt

#verify_password 함수 : password와 salt를 이용하여 user_password와 비교하여 True/False 반환
def verify_password(password, user_password, salt) -> bool:
    password = password + salt
    hashed_password = hashlib.sha256(password.encode())

    return True if hashed_password.hexdigest() == user_password else False

if __name__ == "__main__":
    password = input("Enter password: ")
    salt = create_salt()
    hashed_password = hash_password(password, salt)
    print(f"salt : {salt}")
    print(f"hashed_password : {hashed_password}")
    print(f"sha256 : {hashed_password.hexdigest()}")