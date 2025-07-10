from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_func():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_lists = password_letters + password_symbols + password_numbers

    shuffle(password_lists)

    password = "".join(password_lists)
    password_entry.delete(0,END)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info_to_data():
    website_info = website_entry.get()
    email_info = email_user_entry.get()
    password_info = password_entry.get()

    new_data = {
        website_info:{
            "email": email_info,
            "password": password_info,
        }
    }
    if len(website_info)>0 and len(email_info)>0 and len(password_info)>0 :
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty")
# --------------------------- SEARCH BUTTON ----------------------------#
def search():
    website_info = website_entry.get()
    try:
        with open("data.json", "r") as file:
            bilgi = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website_info in bilgi:
            sifre = bilgi[f"{website_info}"]["password"]
            email = bilgi[f"{website_info}"]["email"]
            messagebox.showinfo(title=f"{website_info}", message=f"Email: {email}\n Password: {sifre}")
        else:
            messagebox.showinfo(message=f"No such a website like {website_info} in saved websites")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas =Canvas(width=200,height=200,highlightthickness=0)
lock_image =PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:",font=("Courier",10,"roman"))
website_label.grid(row=1,column=0)

email_user_label = Label(text="Email/Username:",font=("Courier",10,"roman"))
email_user_label.grid(row=2,column=0)

password_label = Label(text="Password:",font=("Courier",10,"roman"))
password_label.grid(row=3,column=0)

website_entry = Entry(width=44)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_user_entry = Entry(width=69)
email_user_entry.grid(row=2,column=1,columnspan=2)
email_user_entry.insert(0,"@gmail.com")

password_entry = Entry(width=44)
password_entry.grid(row=3, column=1)

password_generator_button = Button(text="Generate Password",width=20, command=password_func)
password_generator_button.grid(row=3,column=2)

add_button = Button(text="Add", width=59,bg="green", command=save_info_to_data)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=20, command=search)
search_button.grid(row=1, column=2, columnspan=2)

window.mainloop()
