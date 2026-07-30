from turtle import Turtle
START_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DIS=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.snake_head=self.segment[0]   #new attribute
        self.flag=False
    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)
    def add_seg(self,pos):
        seg = Turtle(shape="square")
        seg.penup()
        seg.color("white")
        seg.goto(pos)
        self.segment.append(seg)
    def extend(self):
        self.add_seg(self.segment[-1].position())    #1more time add_seg will be run and add another turtle like before "on" the end of snake (the last segment)
    def head_tail_check(self):
        for j in range(2,len(self.segment)):
            self.segment[j].color('red')
            if self.snake_head.distance(self.segment[j])<10:
                print("yeeeeeeeeeeeeeeeeeeeeeeees")
                #self.segment[j].color("red")
                #self.flag=True

        #--------to reset as highest score
    def snake_reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()           
        self.create_snake()
        self.snake_head = self.segment[0]
    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            #print(self.segment[i-1].pos())    #the last seg
            self.segment[i].goto(self.segment[i-1].pos())
        self.snake_head.fd(MOVE_DIS)
        #self.segment[0].left(90)   #to test
    def up(self):
        if self.snake_head.heading() !=DOWN:
            self.snake_head.setheading(90)
    def down(self):
        if self.snake_head.heading() !=UP:
            self.snake_head.setheading(DOWN)
    def left(self):
        if self.snake_head.heading() !=RIGHT:
            self.snake_head.setheading(LEFT)
    def right(self):
        if self.snake_head.heading() !=LEFT:
            self.snake_head.setheading(RIGHT)
