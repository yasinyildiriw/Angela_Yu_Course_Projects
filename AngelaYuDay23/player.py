from turtle import Turtle
COORDINATE = (0,-280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(COORDINATE)
        self.showturtle()

    def move(self):
        self.forward(23)

    def restart(self):
        self.goto(COORDINATE)



