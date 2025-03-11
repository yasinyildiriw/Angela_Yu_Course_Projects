# Random Walk

from turtle import Turtle, Screen
import random

tosba = Turtle()
colors = ["black", "green yellow", "medium blue", "indian red", "gold", "orchid", "bisque", "magenta"]
tosba.pensize(5)
tosba.speed(0)
ekran = Screen()

distance = 20

direction = [-90, 0, 90, 180]

for i in range(1000):
    tosba.color(random.choice(colors))
    tosba.forward(distance)
    tosba.setheading(random.choice(direction))




ekran.exitonclick()