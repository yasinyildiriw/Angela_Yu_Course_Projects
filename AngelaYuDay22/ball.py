from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 3
        self.y_move = 2.25
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.99

    def collision(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.01
        self.collision()
