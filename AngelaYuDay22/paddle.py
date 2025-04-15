from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.hideturtle()
        self.penup()
    def paddle_cor(self, xcor, ycor):
        self.goto(xcor, ycor)
        self.showturtle()
        return self

    def paddle_up(self):
        self.setheading(90)
        self.forward(60)
        self.setheading(0)
    def paddle_down(self):
        self.setheading(270)
        self.forward(60)
        self.setheading(0)
