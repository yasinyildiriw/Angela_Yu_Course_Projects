from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
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
    if len(website_info)>0 and len(email_info)>0 and len(password_info)>0 :
        is_ok = messagebox.askokcancel(title=website_info, message=f"These are the details entered:\n"
                                                           f"Email: {email_info}\n"
                                                        f"Password: {password_info}\nIs it OK to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_info} | {email_info} | {password_info}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty")

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

website_entry = Entry(width=69)
website_entry.grid(row=1,column=1,columnspan=2)
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


window.mainloop()
