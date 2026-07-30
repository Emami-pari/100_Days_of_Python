FONT=("Arial",80,"normal")
ALIGNMENT="center"
from turtle import Turtle
class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r=0
        self.score_l=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.new_print()

    def new_print(self):
        self.clear()
        self.goto(100,200)
        self.write(self.score_r,False,ALIGNMENT,font=FONT)
        self.goto(-100,200)
        self.write(self.score_l,False,ALIGNMENT,font=FONT)
    def increase_score_r(self):
        self.score_r += 1
        self.new_print()

    def increase_score_l(self):
        self.score_l += 1
        self.new_print()

