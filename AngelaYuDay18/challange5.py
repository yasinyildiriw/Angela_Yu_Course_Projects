# Drawing a spirograph

from turtle import Turtle, Screen
from random import randint

tosba = Turtle()
ekran = Screen()
ekran.colormode(255)

tosba.speed(0)

angle = 0
def rand_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color
for i in range(1000):
    tosba.right(angle)
    tosba.pencolor(rand_color())
    tosba.circle(100)
    angle += 1

ekran.exitonclick()