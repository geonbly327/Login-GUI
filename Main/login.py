import customtkinter
import tkinter
import time

#appearance_mode 초기화
appearance_mode = "dark"

customtkinter.set_appearance_mode(appearance_mode)
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x400")

#theme 함수 : appearance_mode에 따라 테마 변경
def theme():
    global appearance_mode

    if appearance_mode == "dark":
        customtkinter.set_appearance_mode("light")
        appearance_mode = "light"
    else:
        customtkinter.set_appearance_mode("dark")
        appearance_mode = "dark"

#login 함수 : ID, PW가 입력되었는지 확인하고 ID, PW 출력
def login():
    print("Login")
    if (entry1.get() == ''):
        print("Please Write ID")
    elif (entry2.get() == ''):
        print("Please Wirte Password")
    else:
        print(f"ID : {entry1.get()}")
        print(f"PW : {entry2.get()}")

#signup 함수
def signup():
    print("Sign Up")

#enter_to_login 함수
def enter_to_login(value):
    login()

#frame 설정
frame = customtkinter.CTkFrame(master=root, width=500, height=350)
frame.pack(padx=60, pady=20, fill="both", expand=True)

#label
label = customtkinter.CTkLabel(master=frame, text="Login", font=("Arial", 20, "bold"))
label.pack(padx=10, pady=12)

#ID Entry : ID 입력, Tab 키로 PW로 전환 가능
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="ID", takefocus=False)
entry1.pack(padx=10, pady=5)

#PW Entry : PW 입력, Enter 키로 login 함수 호출 가능
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(padx=10, pady=5)
entry2.bind("<Return>", command=enter_to_login)

#Login Button : login 함수 호출
login_button = customtkinter.CTkButton(master=frame, text="Login", command=login, state="normal")
login_button.pack(padx=10, pady=5)

#Sign Up Button : signup 함수 호출
signup_button = customtkinter.CTkButton(master=frame, text="Sign Up", command=signup)
signup_button.pack(padx=10, pady=5)

#Remember Me CheckBox
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember ME")
checkbox.pack(padx=10, pady=20)

#Theme Button : 테마 변경
theme_button = customtkinter.CTkButton(master=frame, text="Theme", command=theme, width=100, height=25)
theme_button.pack(padx=10, pady=5)

#Exit Button : 종료
exit_button = customtkinter.CTkButton(master=frame, text="Exit", command=root.destroy, width=100, height=25)
exit_button.pack(padx=10, pady=5)

root.mainloop()