#Draw dashed line

from turtle import Turtle,Screen

tosba = Turtle()

tosba.shape("arrow")

tosba.color("black")

for i in range(10):
    tosba.pendown()
    tosba.forward(5)
    tosba.penup()
    tosba.forward(5)

screen = Screen()

screen.exitonclick()