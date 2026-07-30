from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")   #default 20#20
        self.penup()
        self.speed("fast")
        self.x_move=10
        self.y_move =10
        self.speed_num=1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *=(-1)
    def bounce_x(self):
        self.x_move *= (-1)
        self.speed_num *=1.2
        #this is one player game ,for 2pl u should seperate out of left or right
    #def ball_out(self):
     #   return self.xcor()>390 or self.xcor()< -390
