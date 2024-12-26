#The purpose of this project is to gain more practice in creating classes, methods and attributes.
#The time module was also used, and I gained experience using the time module in conjunction with
#turtle graphics. I  also gained further experience accepting user input.

from turtle import Turtle, Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_on = True

while game_on:
    screen.update()
    screen.onkey(key="Up", fun=snake.direction_up)
    screen.onkey(key="Left", fun=snake.direction_left)
    screen.onkey(key="Down", fun=snake.direction_down)
    screen.onkey(key="Right", fun=snake.direction_right)

    time.sleep(.1)
    snake.move()

screen.exitonclick()

