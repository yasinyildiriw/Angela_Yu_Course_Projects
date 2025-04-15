from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()

r_paddle = Paddle().paddle_cor(370,0)
l_paddle = Paddle().paddle_cor(-370,0)
screen.listen()
screen.onkey(r_paddle.paddle_up,"Up")
screen.onkey(r_paddle.paddle_down,"Down")
screen.onkey(l_paddle.paddle_up,"w")
screen.onkey(l_paddle.paddle_down,"s")

score = Scoreboard()

is_game_on = True
while is_game_on:
    screen.update()

    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350 :
        ball.collision()
    if ball.xcor() > 400:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -400:
        score.r_point()
        ball.reset_position()

