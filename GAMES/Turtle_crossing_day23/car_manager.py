COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        self.all_car=[]
        self.velocity=STARTING_MOVE_DISTANCE

    def create_car(self):
        rn = random.randint(1, 6)
        if rn==6:
            car=Turtle(shape="square")
            car.penup()
            car.shapesize(1,2)
            car.pos_y = (random.randint(-250,250))
            car.color(random.choice(COLORS))
            car.goto(300, car.pos_y)
            self.all_car.append(car)

    def move(self):
        for car in self.all_car:
            car.backward(self.velocity)
    def speed_up(self):
        #for car in self.all_car:   #because velocity is a n attribute
            self.velocity+=MOVE_INCREMENT
