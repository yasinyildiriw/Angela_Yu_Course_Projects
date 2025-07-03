from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#212121"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    calisma = WORK_MIN*60
    ara = SHORT_BREAK_MIN*60
    uzun_ara = LONG_BREAK_MIN*60
    reps += 1
    if reps % 4 == 0:
        timer_label.config(text="Long Break")
        countdown(uzun_ara)
        tik = "✓"
        carpi = int(reps/3)
        checkmark_label.config(text=tik*carpi)
    elif reps % 2 == 0:
        timer_label.config(text="Break")
        countdown(ara)
    else:
        timer_label.config(text="Work")
        countdown(calisma)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time):
    dakika = math.floor(time / 60)
    saniye = time % 60
    if 0 <= saniye < 10:
        saniye = f"0{saniye}"
    if 0 <= dakika < 10:
        dakika = f"0{dakika}"
    canvas.itemconfig(timer_text, text=f"{dakika}:{saniye}")
    if time > 0 :
        global timer
        timer = window.after(1000, countdown, time - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=GREEN)

timer_label = Label(text="Timer",font=(FONT_NAME,25,"italic"),fg=BLACK,bg=GREEN)
timer_label.grid(row=0,column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

checkmark_label = Label(fg=BLACK,bg=GREEN,font=(FONT_NAME,15,"italic"))
checkmark_label.grid(row=3,column=1)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,35,"italic"))
canvas.grid(row=1,column=1)



window.mainloop()
