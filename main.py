from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_is = "".join(password_list)

    pass_e.insert(0, string=f"{password_is}")
    pyperclip.copy(f"{password_is}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_e.get()
    passe = pass_e.get()
    use = user_e.get()
    new_data = {
        web: {
            "email": use,
            "password": passe,
        }
    }
    if len(web) == 0 or len(passe) == 0:
        messagebox.showerror(message="Don't leave anything empty")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                web_e.delete(0, END)
                web_e.focus()
                pass_e.delete(0, END)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                web_e.delete(0, END)
                web_e.focus()
                pass_e.delete(0, END)


# ---------------------------- Find PASSWORD ------------------------------- #
def searchf():
    web = web_e.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
            email = data[web]["email"]
            passw = data[web]["password"]
            print(data)
            if web in data:
                messagebox.showinfo(title=web, message=f"Email:{email}\nPassword: {passw}")
                pyperclip.copy(f"{passw}")
    except:
        messagebox.showerror(title=web, message=f"Website not found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="img.png")
canvas.create_image(120, 100, image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
username = Label(text="Username:")
username.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

web_e = Entry(width=32)
web_e.focus()
web_e.grid(column=1, row=1)
user_e = Entry(width=50)
user_e.insert(END, string="manik@email.com")
user_e.grid(column=1, row=2, columnspan=2)
pass_e = Entry(width=32)
pass_e.grid(column=1, row=3)

button = Button(text="Generate Password", command=generate)
button.config(width=14)
button.grid(column=2, row=3)

add = Button(text="Add", command=save)
add.config(width=43)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", command=searchf)
search.config(width=14)
search.grid(column=2, row=1)

window.mainloop()
