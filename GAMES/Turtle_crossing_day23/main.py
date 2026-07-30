import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Board

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
screen.onkey(player.up, "Up")
board=Board()
car_manager=CarManager()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    #check the F L
    if player.check_finish_line():
        board.increase_level()
        player.go_start_line()
        car_manager.speed_up()
    ##collide with car
    for car in car_manager.all_car:
        #if car.pos()==player.pos():
        if car.distance(player)<20:
            board.game_over()
            game_on=False
screen.exitonclick()
