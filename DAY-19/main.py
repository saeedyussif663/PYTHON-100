from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("make you bet", "which turtle will win the race? Enter color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

y_axis = -100

for i in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(-240, y_axis)
    y_axis += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"you have won. the winning turtle is {winning_turtle}")
            else:
                print(f"you have lost. the winning turtle is {winning_turtle}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()