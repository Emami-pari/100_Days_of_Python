STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_start_line()

    def check_finish_line(self):
        return self.ycor()>=FINISH_LINE_Y
    def up(self):
        self.fd(MOVE_DISTANCE)
    def go_start_line(self):
        self.goto(STARTING_POSITION)
