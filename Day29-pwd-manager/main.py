import random
import string
import pyperclip
import json
from tkinter import *
from tkinter import messagebox

FONT = ('Ariel', 10, 'normal')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    pwd_input.delete(0, END)
    pwd_len = random.randint(10, 14)
    alphabets = string.ascii_letters
    nums = string.digits
    special_chars = string.punctuation
    chars = alphabets + nums + special_chars
    pwd = ""

    for _ in range(pwd_len):
        pwd += random.choice(chars)

    pwd_input.insert(0, pwd)
    pyperclip.copy(pwd)


# --------------------------- SEARCH -------------------------------------- #
def search():
    website = website_input.get().capitalize()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message='Website field can\'t be empty!')
        return

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        if website in data.keys():
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title='Oops', message=f"{website} doesn't exist.")

    except FileNotFoundError:
        messagebox.showinfo(title="Something went wrong!", message="You haven't saved any password yet!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get().capitalize()
    email = email_input.get()
    pwd = pwd_input.get()

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
        return
    elif len(pwd) < 8:
        messagebox.showinfo(title='Oops', message="Password is too short.")
        return

    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }}

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            data .update(new_data)

    except FileNotFoundError:
        with open('data.json', 'w') as f:
            json.dump(new_data, f, indent=4)

    else:
        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)

    finally:
        website_input.delete(0, END)
        pwd_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

img = PhotoImage(file='logo.png')
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.focus()
website_input.grid(column=1, row=1)

search_btn = Button(text='Search', width=14, command=search)
search_btn.grid(column=2, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.insert(0, "rabin@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

pwd_label = Label(text='Password:')
pwd_label.grid(column=0, row=3)

pwd_input = Entry(width=21)
pwd_input.grid(column=1, row=3)

pwd_gen_btn = Button(text="Generate", width=14, command=generate_pwd)
pwd_gen_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=35, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
