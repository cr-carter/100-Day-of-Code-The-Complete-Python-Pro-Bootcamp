#The purpose of this project was to gain further experience using the Turtle and Screen modules
#to create a GUI, manipulating objects within that GUI, and focusing more on utilizing objects.

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

game_is_on = True

while game_is_on is True:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
#    #Detect wall collision
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
#    #Detect paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.rebound()
#   #Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
#   #Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
