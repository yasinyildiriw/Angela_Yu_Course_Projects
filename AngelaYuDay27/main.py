from tkinter import *

def convert():
    #mil_entry.get() string döner
    result = float(mil_entry.get())
    result *= 1.6
    result_label = Label(text=f"{round(result,2)}", font=("Arial", 20, "roman"))
    result_label.grid(row=1, column=1)

window = Tk()
window.title("Miles to Km")
window.minsize(width=400,height=300)

mil_entry = Entry(width=20)
mil_entry.grid(row=0, column=1)

is_equal_to_label = Label(text="is equal to",font=("Arial",20,"roman"))
is_equal_to_label.grid(row=1, column=0)

mil_label = Label(text="Miles",font=("Arial",20,"roman"))
mil_label.grid(row=0, column=2)

km_label = Label(text="Km",font=("Arial",20,"roman"))
km_label.grid(row=1, column=2)

button = Button(text="Calculate",command=convert)
button.grid(row=2, column=1)

window.mainloop()