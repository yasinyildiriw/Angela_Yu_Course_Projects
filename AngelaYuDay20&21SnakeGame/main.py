from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# tracer() fonksiyonu,çizim hızını artırmak ve ekrana anında çizim yapmayı duraklatmak için kullanılır.
# turtle.tracer(n, delay)
# n: Kaç adımda bir güncelleme yapılacağını belirler.
# 0 yaparsan anında çizim tamamlanır (çizim animasyonu gözükmez).
# delay: Her çizim adımı arasındaki gecikme süresini (milisaniye cinsinden) belirler.
screen.tracer(0)
# turtle.update()
# Sadece tracer(0) kullanıldığında gereklidir.
# Ekrandaki tüm çizimleri bir anda günceller.
# Performansı artırmak için büyük çizimlerde kullanılır.
screen.update()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.right,"Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score += 1
        score.tekrar()
    # detect collusion with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.game_over()
        game_is_on = False
    # detect collusion with tail
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            score.game_over()
            game_is_on = False
screen.exitonclick()