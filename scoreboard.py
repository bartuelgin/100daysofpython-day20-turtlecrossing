FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.player_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.player_score}", align="center", font=FONT)

    def increase_score(self):
        self.player_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game is Over.Max Level: {self.player_score}", align="center", font=FONT)
