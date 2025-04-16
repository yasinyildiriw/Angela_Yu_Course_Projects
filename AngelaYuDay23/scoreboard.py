from turtle import Turtle
FONT = ("Courier",15,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score_board()


    def update_score_board(self):
        self.clear()
        self.goto(-340,280)
        self.write(arg = f"Level {self.level}",align="left",font = FONT)
    def carpma(self):
        self.clear()
        self.goto(0,0)
        self.write(arg= "GAME OVER",align="center",font=FONT)
