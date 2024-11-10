#The purpose of this project was to work gain experience working with Turtle graphics,
#gaining experience with displaying basic GUI, using the colorgram and random modules.
#Not shown in this code are exercises drawing different shapes, using various
#methods in the turtle module.

from turtle import Turtle, Screen
import random

#The following code that is commented out was used to retrieve the colors in the subsequent
#"colors' list.
#import colorgram
#extracted_colors = colorgram.extract('hirst.jpg', 10)
#colors = []
#for color in extracted_colors:
#    rgb = color.rgb
#    colors.append((rgb.r, rgb.g, rgb.b))
#
#print(colors)

colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]
screen = Screen()
hirst = Turtle()

hirst.teleport(-200, -200)
screen.colormode(255)
hirst.hideturtle()

for y in range(10):
    for x in range(10):
        hirst.dot(20, random.choice(colors))
        hirst.teleport(x=hirst.xcor() + 50)
    hirst.teleport(y=hirst.ycor() + 50, x=-200)


screen.exitonclick()
