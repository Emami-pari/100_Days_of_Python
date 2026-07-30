from turtle import Screen
from snake import Snake
from food import Food
from score_board import Board
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
import time
screen.tracer(0)  #0 means animation is off and / 1 is on
screen.listen()
snake=Snake()
food=Food()
board_t=Board()                  # all the board, food snake are instance turtles
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)  #to slow down!sleep for 1second!ies out of for due to set a delay after moving all the pieces
    snake.move()
    #----------detect snake's collision with food
    if snake.snake_head.distance(food)<15:
        food.set_loc()
        #print("nom nom nom")
        board_t.increase_score()  #to count the number of collision
        snake.extend()
    #------------detect if a snake hits the wall
    if (snake.snake_head.xcor()>295 or snake.snake_head.xcor()< -295 or snake.snake_head.ycor()>295 or snake.snake_head.ycor()<-295):

        board_t.score_reset()
        snake.snake_reset()
    #------------detect if the head collide to each part of the tail
    if snake.flag:
        board_t.score_reset()
        snake.snake_reset()
screen.exitonclick()
