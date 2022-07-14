import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")
car_seq = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_seq +=1
    if car_seq % 6 == 0:
        car_manager.car_create()
    car_manager.car_move()


    #when player passes level
    if player.ycor() > 280:
        scoreboard.increase_score()
        scoreboard.update_score()
        car_manager.increase_car_speed()
        player.reset_turtle()

    #detect collision with car

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()