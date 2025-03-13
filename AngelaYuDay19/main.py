# Race of TURTLES
# I copied the turtle_coordinate_system for race and redesigned it
from turtle import Turtle, Screen
import random

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
ekran = Screen()
ekran.setup(width=800, height=450)
user_bet = ekran.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True
coordinate = [-150,-120,-90,-60,-30,0]
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-350,y=coordinate[i])
    turtles.append(new_turtle)
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 360:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print("Congratulations! Your bet is the winner ")
            else:
                print(f"Unfortunately {winning_color} won")
        distance = random.randint(0,10)
        turtle.forward(distance)

ekran.exitonclick()
