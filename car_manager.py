COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_create()
        self.speed = STARTING_MOVE_DISTANCE

    def car_create(self):
        car = Turtle()
        car.penup()
        car.left(180)
        car.goto(300, random.randint(-250,280))
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(1, 2)
        self.car_list.append(car)

    def car_move(self):
        #  for car_num in range(len(self.car_list)):
        #  self.car_list[car_num]

        for car in self.car_list:
           car.forward(self.speed)

    def increase_car_speed(self):
        self.speed += MOVE_INCREMENT




