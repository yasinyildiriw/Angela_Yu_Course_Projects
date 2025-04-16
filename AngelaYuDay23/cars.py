from turtle import Turtle
import random

COLORS = ["orange","red","green","blue","yellow","purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(x = random.randint(-380,380),y = random.randint(a=-240,b=270))
        self.showturtle()


    def move(self):
        self.forward(5)
        if self.xcor() < -400:
            self.goto(x = 400,y = random.randint(-240,270))


