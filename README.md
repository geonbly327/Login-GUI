# __Login-GUI__
Python의 tkinter와 MySQL을 이용한 간단한 로그인 GUI
>[⌨️ID, PW 입력창](#📌ID,-PW-입력창📌)  
>[🖱️Login 및 Sign Up 버튼](#📌Login-및-Sign-Up-버튼📌)  
>[🖱️Exit 버튼](#📌Exit-버튼📌)  
>[⚙️Theme 변경 함수](#📌Theme-변경-함수📌)  
>[⚙️Login 함수](#📌Login-함수📌)  
>[⚙️Hashing 함수](#📌Hashing-함수📌)  
>[⚙️Salting 함수](#📌Salting-함수📌)  
>[⚙️PW 확인 함수](#📌PW-확인-함수📌)  
***
### __📌ID, PW 입력창📌__
```python
# ID Entry
self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="ID", takefocus=False)
self.entry1.pack(padx=10, pady=5)

# PW Entry
self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
self.entry2.pack(padx=10, pady=5)
self.entry2.bind("<Return>", command=self.enter_to_login)
```
ID 입력창은 PW 입력창에서 Tab 키를 입력했을 때 넘어오지 않도록 설정
```python
takefocus=False 
```
PW 입력창에 비밀번호 입력할시에 *이 대신 보이도록 설정
```python
show="*"
```
PW 입력창에서 Enter 키 입력시 enter_to_login 함수 실행
```python
self.entry2.bind("<Return>", command=self.enter_to_login)
```
PW 입력창에서 Enter 키 입력으로 함수 실행시 인자를 넘겨주기 때문에 login 함수는 enter_to_login 함수를 통해서 실행
```python
def enter_to_login(self, value) -> None:
    self.login()
```
#
### __📌Login 및 Sign Up 버튼📌__
```python
# Login Button
self.login_button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.login, state="normal")
self.login_button.pack(padx=10, pady=5)

# Sign Up Button
self.signup_button = customtkinter.CTkButton(master=self.frame, text="Sign Up", command=self.signup)
self.signup_button.pack(padx=10, pady=5)
```
추후에 ID, PW를 입력하지 않았을 경우 Login 버튼 비활성화할 계획
```python
state="normal"
```
#
### __📌Exit 버튼📌__
```python
# Exit Button
self.exit_button = customtkinter.CTkButton(master=self.frame, text="Exit", command=root.destroy, width=100, height=25)
self.exit_button.pack(padx=10, pady=5)
```
프로그램 실행 종료
```python
command=root.destroy
```
#
### __📌Theme 변경 함수📌__
```python
# theme 함수
@deco
def theme(self) -> None:
    global appearance_mode

    if appearance_mode == "dark":
        customtkinter.set_appearance_mode("light")
        appearance_mode = "light"
    else:
        customtkinter.set_appearance_mode("dark")
        appearance_mode = "dark"
```
기본값은 dark 테마
```python
# appearance_mode 초기화
appearance_mode = "dark"
```
현제 appearance_mode에 따라 테마 및 appearance_mode 변경
```python
if appearance_mode == "dark":
    customtkinter.set_appearance_mode("light")
    appearance_mode = "light"
else:
    customtkinter.set_appearance_mode("dark")
    appearance_mode = "dark"
```
#
### __📌Login 함수📌__
```python
# login 함수
@deco
def login(self) -> None:
    print("Login")

    if (self.entry1.get() == ''):
        self.warning_msgbox("Please Write ID")
    elif (self.entry2.get() == ''):
        self.warning_msgbox("Please Wirte Password")
    else:
        print(f"ID : {self.entry1.get()}")
        print(f"PW : {self.entry2.get()}")
        self.info_msgbox("Login Success")
```
ID 또는 PW 입력창이 공백일 경우 경고창 실행
```python
# Warning Messagebox
def warning_msgbox(self, text):
    tkinter.messagebox.showwarning('Warning', text)
```
Login 성공시 Login 성공 알림창 실행
```python
# Info Messagebox
def info_msgbox(self, text):
    tkinter.messagebox.showinfo('Info', text)
```
#
### __📌Hashing 함수📌__
```python
#hash_password 함수
def hash_password(password) -> tuple(hashlib.sha256, str):
    salt = _salt()
    password = password + salt

    hashed_password = hashlib.sha256(password.encode())

    return hashed_password, salt
```
해싱하기 전에 PW에 솔팅
```python
password = password + salt
```
SHA-256 함수로 해싱
```python
hashed_password = hashlib.sha256(password.encode())
```
#
### __📌Salting 함수📌__
```python
#_salt 함수
def _salt() -> str:
    count = random.randint(16, 21)
    string_store = string.ascii_letters + string.digits + string.punctuation
    salt = "".join(random.choices(string_store, k=count))
    return salt
```
Salt의 길이는 16 이상 21 이하의 난수로 설정
```python
count = random.randint(16, 21)
```
Salt를 구성할 대문자 및 소문자 알파벳, 양의 정수, 문자를 하나의 문자열에 저장
```python
string_store = string.ascii_letters + string.digits + string.punctuation
```
count 길이의 문자열 만들기
```python
salt = "".join(random.choices(string_store, k=count))
```
#
### __📌PW 확인 함수📌__
```python
#verify_password 함수
def verify_password(password, user_password, salt) -> bool:
    password = password + salt
    hashed_password = hashlib.sha256(password.encode())

    return True if hashed_password.hexdigest() == user_password.hexdigest() else False
```
사용자가 입력한 PW를 해싱한 후 기존의 해싱된 PW와 비교
```python
True if hashed_password.hexdigest() == user_password.hexdigest() else False
```