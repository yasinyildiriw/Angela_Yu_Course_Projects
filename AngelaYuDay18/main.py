from turtle import Turtle, Screen
from first_colorgram import renk_paleti
import random

daire = Turtle()
screen = Screen()
screen.colormode(255)
daire.penup()
daire.hideturtle()
daire.speed(0)
duple = renk_paleti()

def sira():
    for i in range(25):
        daire.fillcolor(random.choice(duple))
        daire.begin_fill()
        daire.circle(20)
        daire.end_fill()
        daire.forward(60)
daire.goto(-740, 350)
for j in range(4):
    sira()
    for k in range(2):
        daire.right(90)
        daire.forward(60)
    sira()
    daire.left(90)
    daire.forward(140)
    daire.left(90)
    daire.forward(60)
screen.exitonclick()