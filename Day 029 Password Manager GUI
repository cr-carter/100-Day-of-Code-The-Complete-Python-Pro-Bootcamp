'''
The purpose of this project is to gain further experience writing programs that utilize a GUI.
This project explored more aspects of tkinter, focusing on using the grid to place widgets, using
messagebox to display and receive information from the user, and tie functionality to the buttons.
I also revisited the use of CSVs, was introduced to pyperclip, and reused code I had previously
written (generating passwords).
This code obviously does not produce a secure password list, as it is simply stored in a CSV file.
'''

import os.path
from tkinter import *
from tkinter import messagebox
import pandas
import random
import pyperclip

LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "|", ":", ";", "\"", "'"]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = [random.choice(LOWERCASE) for _ in range(0,6)]
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
        entry = {
            'Website': [website],
            'Username/Email': [username],
            'Password': [password],
        }

        data = pandas.DataFrame(entry)
        data.to_csv('./password.csv', mode='a', header=not os.path.exists('./password.csv'))

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

website_input = Entry(width=52)
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

window.mainloop()
