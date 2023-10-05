import tkinter as tk
def validate_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    if entered_username == "dania" and entered_password == "Dbs!2345":
        result_label.config(text="Login successful", fg="green")
    else:
        result_label. config(text="Incorrect username or password", fg="red")

root = tk.Tk()
root.title("Login System")
root.configure (bg="efcfe3")

login_frame = tk.Frame(root, bg="#fbe7ef", padx=20, pady=20)
login_frame.pack()

username_label = tk.Label(login_frame, text="Usernane:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", bg="#be5683", fg="white")
login_button.grid(row=2, column=0, columnspan=2, pady=16)

result_label = tk.Label(login_frame, text="", fg="green", bg="#fbe7ef")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()