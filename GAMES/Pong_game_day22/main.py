from turtle import Screen
from paddle import Paddle
from ball import Ball
from board import Board
import time
screen=Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("my PONG game")
screen.listen()
paddle_r=Paddle((370,0))
paddle_l=Paddle((-370,0))
ball=Ball()
board_t=Board()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "u")
screen.onkey(paddle_l.down, "d")

game_on=True
while game_on:
    time.sleep(0.1/ball.speed_num)    # to slow down the motion of ball
    screen.update()
    ball.move()
    #collide to wall
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()                #need to bounce
    #collide to paddle_r
    if ball.distance(paddle_r)<50 and ball.xcor()> 345 or ball.distance(paddle_l)<50 and ball.xcor()< -345:
        ball.bounce_x()

    if ball.xcor()> 390:
        ball.home()
        ball.bounce_x()
        ball.speed_num=1
        board_t.increase_score_l()

    if ball.xcor() <-390:
        ball.home()
        ball.bounce_x()
        ball.speed_num=1
        board_t.increase_score_r()

screen.exitonclick()
