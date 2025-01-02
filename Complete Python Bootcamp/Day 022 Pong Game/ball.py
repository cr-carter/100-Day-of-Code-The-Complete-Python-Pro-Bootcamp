from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_change = 10
        self.y_change = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_change, self.ycor() + self.y_change)

    def bounce(self):
        self.y_change *= -1

    def rebound(self):
        self.x_change *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.rebound()
        self.move_speed = 0.1

