'''
The purpose of this project is to improve upon yestedays project. A focus was placed on learning and
gaining experience using try/except/else/finally statements, handling exceptions, and an introduction
to raising your own exceptions. I also was exposed to using the json format, and modified the code to
use json instead of csv.
'''
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "|", ":", ";", "\"", "'"]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    try:
        with open("./data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No password file found.")
    else:
        website_search = website_input.get()
        if website_search in data:
            email_search = data[website_search]['username/email']
            password_search = data[website_search]['password']
            messagebox.showinfo(title=f"{website_search} login information", message=f"Username/Email: {email_search}"
                                                                                     f"\nPassword: {password_search}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_search} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = [random.choice(LOWERCASE) for _ in range(0, 6)]
    password += [random.choice(UPPERCASE) for _ in range(0, 6)]
    password += [random.choice(SYMBOLS) for _ in range(0, 6)]
    password += [random.choice(NUMBERS) for _ in range(0, 6)]

    random.shuffle(password)
    random_password = ''.join(password)
    password_input.delete(0, END)
    password_input.insert(END, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    is_ok = False

    if website.__len__() == 0 or username.__len__() == 0 or password.__len__() == 0:
        messagebox.showinfo(title="Missing information", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail/Username: {username}"
                                               f"\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        new_data = {
            website: {
                "username/email": username,
                "password": password,
            }
        }

        try:
            with open("./data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            username_input.delete(0, END)
            username_input.insert(END, "default@email.com")

            messagebox.showinfo(title="Success", message="Your password was saved.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(width=False, height=False)

canvas = Canvas(width=200, height=200)
mypass_logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=mypass_logo)
canvas.grid(column=1, row=0)

website_label = Label(width=14, text="Website:", anchor="e")
website_label.grid(column=0, row=1)

username_label = Label(width=14, text="Email\\Username:", anchor="e")
username_label.grid(column=0, row=2)

password_label = Label(width=14, text="Password:", anchor="e")
password_label.grid(column=0, row=3)

website_input = Entry(width=30)
website_input.grid(column=1, row=1, columnspan=2,  sticky='W')
website_input.focus()

username_input = Entry(width=52)
username_input.grid(column=1, row=2, columnspan=2, sticky='W')
username_input.insert(END, "default@email.com")

password_input = Entry(width=30)
password_input.grid(column=1, row=3, sticky='W')

password_button = Button(text="Generate Password", highlightthickness=1, bd=1, command=generate_password)
password_button.grid(column=2, row=3, sticky='W')

add_button = Button(text="Add", width=44, highlightthickness=1, bd=1, command=save_password)
add_button.grid(column=1, row=4, columnspan=2,  sticky='W')

search_button = Button(text="Search", width=15, highlightthickness=1, bd=1, command=search)
search_button.grid(column=2, row=1, sticky='W')

window.mainloop()
