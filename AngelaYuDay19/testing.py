from turtle import Turtle, Screen

tosba = Turtle()
ekran = Screen()
tosba.shape("turtle")
tosba.color("red")

def move_forward():
    tosba.forward(20)
def move_backward():
    tosba.backward(20)
def turn_right():
        tosba.right(30)
def turn_left():
    tosba.left(30)
def clear():
    tosba.clear()
ekran.listen()
# Fonksiyon içinde fonksiyon tanımlandığında içerideki fonksiyonun parantezleri konulmaz
ekran.onkey(key="Up", fun=move_forward)
ekran.onkey(key="Left", fun=turn_left)
ekran.onkey(key="Right",fun=turn_right)
ekran.onkey(key="Down",fun=move_backward)
ekran.onkey(key="space",fun=clear)
# Geçerli key'lerden bazıları Up, Down, Right, Left, space
ekran.exitonclick()
