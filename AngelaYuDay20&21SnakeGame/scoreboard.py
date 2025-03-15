from turtle import Turtle
FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)
    def tekrar(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGNMENT,font= FONT)