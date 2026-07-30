from turtle import Turtle
import random as r

class Food(Turtle):   # to inherit features from turtles class
    def __init__(self):
        super().__init__()     # to inherit all the attributes of turtle
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)   #is the circle will be 10*10??
        self.color("blue")
        self.speed("fastest")
        self.set_loc()

    def set_loc(self):
        self.goto(r.randint(-260,260),r.randint(-260,260))
