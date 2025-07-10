from tkinter import *
import pandas
import random

BGCOLOR = "#B1DDC6"
SURE = 5000
choosen_word = {}
veri = {}
# CSV
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("common_1ok.csv")
    veri = original_data.to_dict(orient="records")
else:
    veri = data.to_dict(orient="records")
word_dict = data.to_dict(orient="records")

def is_known():
    word_dict.remove(choosen_word)
    veri = pandas.DataFrame(word_dict)
    veri.to_csv("words_to_learn.csv", index=False)
    change_word()


def change_word():
    global choosen_word,flip_timer
    window.after_cancel(flip_timer)
    choosen_word = random.choice(word_dict)
    ingilizcesi = choosen_word["English"]
    canvas.itemconfig(card_img, image=card_front)
    canvas.itemconfig(language, text="English",fill="black")
    canvas.itemconfig(word, text=f"{ingilizcesi}",fill="black")
    flip_timer = window.after(SURE, flip_card)

def flip_card():
    global choosen_word
    turkcesi = choosen_word["Turkish"]
    canvas.itemconfig(word, text=f"{turkcesi}", font=("Ariel", 60, "bold"), fill="white")
    canvas.itemconfig(language, text="Turkish", font=("Ariel", 40, "italic"), fill="white")
    canvas.itemconfig(card_img, image=card_back)


# UI SETUP
window = Tk()
window.title("Flash Cards")
window.minsize(width=790,height=550)
window.config(padx=50, pady=50, bg=BGCOLOR)
flip_timer = window.after(SURE, flip_card)

canvas = Canvas(width=800, height=526, bg=BGCOLOR, highlightthickness=0)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
card_img = canvas.create_image(400,263,image= card_front)
language = canvas.create_text(400,150, text="English", font=("Ariel",40,"italic"))
word = canvas.create_text(400, 263, text=f"{random.choice(data["English"])}", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0,columnspan=2)

right = PhotoImage(file="right.png")
right_button = Button(image=right, highlightthickness=0, bg=BGCOLOR,command=is_known)
right_button.grid(row=1,column=1)

wrong = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, bg=BGCOLOR, command=change_word)
wrong_button.grid(row=1,column=0)
change_word()


window.mainloop()
