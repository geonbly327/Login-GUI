import customtkinter
import tkinter

appearance_mode = "dark"

customtkinter.set_appearance_mode(appearance_mode)
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x400")

def theme():
    global appearance_mode

    if appearance_mode == "dark":
        customtkinter.set_appearance_mode("light")
        appearance_mode = "light"
    else:
        customtkinter.set_appearance_mode("dark")
        appearance_mode = "dark"

def login():
    print("Login")
    if (entry1.get() == ''):
        print("Please Write ID")
    elif (entry2.get() == ''):
        print("Please Wirte Password")
    else:
        print(f"ID : {entry1.get()}")
        print(f"PW : {entry2.get()}")

def signup():
    print("Sign Up")

def enter_to_login(value):
    login()

frame = customtkinter.CTkFrame(master=root, width=500, height=350)
frame.pack(padx=60, pady=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login", font=("Arial", 20, "bold"))
label.pack(padx=10, pady=12)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="ID", takefocus=False)
entry1.pack(padx=10, pady=5)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(padx=10, pady=5)
entry2.bind("<Return>", command=enter_to_login)

login_button = customtkinter.CTkButton(master=frame, text="Login", command=login)
login_button.pack(padx=10, pady=5)

signup_button = customtkinter.CTkButton(master=frame, text="Sign Up", command=signup)
signup_button.pack(padx=10, pady=5)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember ME")
checkbox.pack(padx=10, pady=20)

theme_button = customtkinter.CTkButton(master=frame, text="Theme", command=theme)
theme_button.pack(padx=10, pady=5)

out_button = customtkinter.CTkButton(master=frame, text="Out", command=root.destroy)
out_button.pack(padx=10, pady=5)

root.mainloop()