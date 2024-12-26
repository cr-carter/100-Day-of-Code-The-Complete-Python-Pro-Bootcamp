#The purpose of this project is to work with multiple object instances,
#using those instances in lists, accepting user input using the turtle
#graphics module, and gaining more familiarity with the turtle GUI

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_index = []

for i in range(0,7):
    turtle_index.append(Turtle(shape="turtle"))
    turtle_index[i].color(colors[i])
    turtle_index[i].teleport(x=-230, y=150 - (i * 50))
    turtle_index[i].penup()

user_bet = ""
while user_bet not in colors:
    user_bet = screen.textinput(title="Who will win?", prompt="Which turtle will win the race? "
                                "Red, Orange, Yellow, Green, Blue, Indigo, Violet?")
    if type(user_bet) is str:
        user_bet = user_bet.lower()

race_on = True
while race_on:
    for turtle in turtle_index:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            print(turtle.pencolor())
            race_on = False
            winner = turtle.pencolor()
print(f"{winner.title()} is the winner!")
if user_bet == winner:
    print("You won!")
else:
    print("You lost!")

screen.exitonclick()
