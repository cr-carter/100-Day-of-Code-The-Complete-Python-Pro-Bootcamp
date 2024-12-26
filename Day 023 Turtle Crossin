#The purpose of this project is to gain more experience with the turtle graphics, with user input,
#the use of classes, and the random and time modules. One thing I would have liked to improve on with 
#this project (and I may come back to revisit it) is to create a seperate car class in order to have each 
#car move at slightly different speeds. Additionally, I noticed that each car uses about 0.1MB of RAM,
#but those cars do not seem to release to memory allocation after they are deleted. This is something I hope
#to learn more about as I continue on with the Udemy course.


import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")
screen.onkeypress(fun=player.move_down, key="Down")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()
    if random.randint(1, 6) == 1:
        for _ in range(scoreboard.level):
            car_manager.create_car()

    for car in car_manager.all_cars:
        if player.distance(car) < 22 and -15 < (player.ycor() - car.ycor()) < 15:
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
