# Drawing random color geometric shapes

from turtle import Turtle, Screen

tim_krul = Turtle()

from random import randint
screen = Screen()

screen.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colors = (r, g, b)
    return colors
n = 3
tim_krul.pensize(4)
for j in range(8):
    tim_krul.pencolor(random_color())
    angle = 360 / n
    for i in range(n):
        tim_krul.forward(100)
        tim_krul.right(angle)
    n += 1


screen.exitonclick()
