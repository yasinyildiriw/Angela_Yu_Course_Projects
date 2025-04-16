from turtle import Screen
import time
from player import Player
from cars import Car
from scoreboard import ScoreBoard

tosba = Player()
SPEED = 0.1

screen = Screen()
screen.setup(width=800,height=600)
screen.tracer(0)
screen.listen()
screen.onkey(tosba.move,"Up")

score = ScoreBoard()
arabalar = []
for i in range(30):
    araba = Car()
    arabalar.append(araba)

is_game_on = True
while is_game_on:
    time.sleep(SPEED)
    screen.update()
    for car in arabalar:
        car.move()
        if car.distance(tosba) < 25:
            score.carpma()
            score.level = 1
            SPEED = 0.1
            tosba.restart()
            is_game_on = False
    if tosba.ycor()>290:
        tosba.restart()
        SPEED *= 0.9
        score.level += 1
        score.update_score_board()

screen.exitonclick()




