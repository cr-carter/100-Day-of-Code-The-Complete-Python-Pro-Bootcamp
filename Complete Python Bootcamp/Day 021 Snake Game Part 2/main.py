#The purpose of this project is to gain experience with inheritance, slicing lists and tuples.

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()

snake = Snake()

screen.onkey(key="Up", fun=snake.direction_up)
screen.onkey(key="Left", fun=snake.direction_left)
screen.onkey(key="Down", fun=snake.direction_down)
screen.onkey(key="Right", fun=snake.direction_right)

game_on = True
food = Food()


while game_on:
    screen.update()
    time.sleep(.15)
    snake.move()

#   #Detect if snake collides with food.
    if snake.head.distance(food) < 5:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

#   #Detect collision with wall
    if snake.head.xcor() > 281 or snake.head.xcor() < -281 or snake.head.ycor() > 281 or snake.head.ycor() < -281:
        game_on = False
        scoreboard.game_over()

#    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()

