import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "passwords.txt"

#SAVE PASSWORD
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{website} | {username} | {password}\n")

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    messagebox.showinfo("Saved", "Password saved successfully!")

#VIEW SAVED PASSWORDS
def view_passwords():
    if not os.path.exists(FILE_NAME):
        messagebox.showinfo("Info", "No passwords saved.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.read()

    # Show data in popup window
    view_window = tk.Toplevel(root)
    view_window.title("Saved Passwords")

    text_box = tk.Text(view_window, width=50, height=20)
    text_box.pack(padx=10, pady=10)
    text_box.insert(tk.END, data)

#UI/DESIGN
root = tk.Tk()
root.title("PasswordManager")
root.geometry("350x250")

# Labels & Inputs
tk.Label(root, text="Website:").grid(row=0, column=0, pady=5, padx=10)
website_entry = tk.Entry(root, width=30)
website_entry.grid(row=0, column=1)

tk.Label(root, text="Username:").grid(row=1, column=0, pady=5, padx=10)
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1)

tk.Label(root, text="Password:").grid(row=2, column=0, pady=5, padx=10)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=1)

# Buttons
save_button = tk.Button(root, text="Save Password", width=20, command=save_password)
save_button.grid(row=3, column=1, pady=10)

view_button = tk.Button(root, text="View Saved", width=20, command=view_passwords)
view_button.grid(row=4, column=1)

root.mainloop()
