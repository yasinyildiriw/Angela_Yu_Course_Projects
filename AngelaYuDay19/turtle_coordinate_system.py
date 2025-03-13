from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-350,y=-150 + i*30)
    turtles.append(new_turtle)

ekran = Screen()
ekran.setup(width=800, height=450)
user_bet = ekran.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")





ekran.exitonclick()