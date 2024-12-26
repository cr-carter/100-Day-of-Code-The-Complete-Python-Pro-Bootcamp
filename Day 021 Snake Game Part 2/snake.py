from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.second_segment = self.segments[1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.teleport(position[0], position[1])
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(0, len(self.segments))[::-1]:
            if i > 0:
                x_cor = self.segments[i - 1].xcor()
                y_cor = self.segments[i - 1].ycor()
                self.segments[i].teleport(x_cor, y_cor)
            else:
                self.segments[0].forward(20)
    
    def direction_up(self):
        if int(self.head.xcor()) != int(self.second_segment.xcor()):
            self.head.setheading(UP)

    def direction_right(self):
        if int(self.head.ycor()) != int(self.second_segment.ycor()):
            self.head.setheading(RIGHT)

    def direction_down(self):
        if int(self.head.xcor()) != int(self.second_segment.xcor()):
            self.head.setheading(DOWN)

    def direction_left(self):
        if int(self.head.ycor()) != int(self.second_segment.ycor()):
            self.head.setheading(LEFT)
