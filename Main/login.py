import customtkinter
import tkinter
import tkinter.messagebox
import time

from hash import *
from connect_db import *

# decorator
def deco(func):
    def wrapper(*args):
        print(f'---{func.__name__} start---')
        func(*args)
        print(f'---{func.__name__} end---')
    return wrapper

class App:
    def __init__(self, master) -> None:
        self.master = master

        # frame 설정
        self.frame = customtkinter.CTkFrame(master=self.master, width=500, height=350)
        self.frame.pack(padx=60, pady=20, fill="both", expand=True)

        # label
        self.label = customtkinter.CTkLabel(master=self.frame, text="Login", font=("Arial", 20, "bold"))
        self.label.pack(padx=60, pady=20, fill="both", expand=True)

        # Login Frame : Login entry 및 button
        self.login_frame = customtkinter.CTkFrame(master=self.frame)
        self.login_frame.pack(padx=0, pady=0)

        # ID Entry : ID 입력, Tab 키로 PW로 전환 가능
        self.entry1 = customtkinter.CTkEntry(master=self.login_frame, placeholder_text="ID", takefocus=False)
        self.entry1.pack(padx=10, pady=5)

        # PW Entry : PW 입력, Enter 키로 login 함수 호출 가능
        self.entry2 = customtkinter.CTkEntry(master=self.login_frame, placeholder_text="Password", show="*")
        self.entry2.pack(padx=10, pady=5)
        self.entry2.bind("<Return>", command=self.enter_to_login)

        # Remember Me CheckBox
        self.checkbox = customtkinter.CTkCheckBox(master=self.login_frame, text="Remember ME")
        self.checkbox.pack(padx=10, pady=10)

        # Login Button : login 함수 호출
        self.login_button = customtkinter.CTkButton(master=self.login_frame, text="Login", command=self.login, state="normal")
        self.login_button.pack(padx=10, pady=5)

        # Sign Up Button : signup 함수 호출
        self.signup_button = customtkinter.CTkButton(master=self.login_frame, text="Sign Up", command=self.signup)
        self.signup_button.pack(padx=10, pady=5)

        # Theme Button : 테마 변경
        self.theme_button = customtkinter.CTkButton(master=self.frame, text="Theme", command=self.theme, width=100, height=25)
        self.theme_button.pack(padx=10, pady=5)

        # Exit Button : 종료
        self.exit_button = customtkinter.CTkButton(master=self.frame, text="Exit", command=root.destroy, width=100, height=25)
        self.exit_button.pack(padx=10, pady=5)

    # theme 함수 : appearance_mode에 따라 테마 변경
    @deco
    def theme(self) -> None:
        global appearance_mode

        if appearance_mode == "dark":
            customtkinter.set_appearance_mode("light")
            appearance_mode = "light"
        else:
            customtkinter.set_appearance_mode("dark")
            appearance_mode = "dark"

    # login 함수 : ID, PW가 입력되었는지 확인하고 ID, PW 출력
    @deco
    def login(self) -> None:
        print("Login")

        if (self.entry1.get() == ''):
            self.warning_msgbox("Please Write ID")
        elif (self.entry2.get() == ''):
            self.warning_msgbox("Please Wirte Password")
        else:
            data = select(self.entry1.get())
            if data == ():
                self.warning_msgbox("ID not exists")
                pass
            else:
                salt = data[0]["salt"]
                if verify_password(self.entry2.get(), data[0]["pw"], salt):
                    self.info_msgbox("Login Success")
                else:
                    self.warning_msgbox("PW is not correct")

    # signup 함수
    @deco
    def signup(self) -> None:
        if len(self.entry1.get()) > 30:
            self.warning_msgbox("ID is too long")
            return

        data = select(self.entry1.get())
        if data != ():
            self.warning_msgbox("This ID already exists")
            pass
        else:
            salt = create_salt()
            hashed_pw = hash_password(self.entry2.get(), salt)

            insert(self.entry1.get(), hashed_pw, salt)
            self.info_msgbox("Sign Up Success")

    # enter_to_login 함수
    def enter_to_login(self, value) -> None:
        self.login()

    # Info Messagebox
    def info_msgbox(self, text):
        tkinter.messagebox.showinfo('Info', text)

    # Warning Messagebox
    def warning_msgbox(self, text):
        tkinter.messagebox.showwarning('Warning', text)

if __name__ == "__main__":
    # appearance_mode 초기화
    appearance_mode = "dark"

    customtkinter.set_appearance_mode(appearance_mode)
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("500x400")

    app = App(root)

    root.mainloop()