STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.shape("turtle")
        self.color("black")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)
