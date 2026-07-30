FONT=("Arial",12,"normal")
ALIGNMENT="center"
from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score.txt", mode="r") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.new_print()
    def new_print(self):
        self.clear()
        self.write(f"Score={self.score} High score={self.high_score}",False,ALIGNMENT,font=FONT)
    def increase_score(self):
        self.score += 1
        self.new_print()
    def score_reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("score.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score=0
        self.new_print()
