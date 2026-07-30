FONT = ("Courier", 24, "normal")
ALIGNMENT="left"
from turtle import Turtle
class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.new_print()

    def new_print(self):
        self.clear()
        self.goto(-250,220)
        self.write(f"level={self.level}",False,ALIGNMENT,font=FONT)

    def increase_level(self):
        self.level += 1
        self.new_print()
    def game_over(self):
        self.home()
        self.write("GAME OVER",False,"center",font=FONT)
