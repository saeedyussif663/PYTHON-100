###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.penup()
tim.hideturtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)



screen = turtle_module.Screen()
screen.exitonclick()