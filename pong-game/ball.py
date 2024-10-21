from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")

    def go_start(self):
        self.goto(0,0)
        self.setheading(random.randint(0, 360))

    def at_player(self, platform_player):
        return self.distance(platform_player) <= 50

    def at_computer(self, platform_computer):
        return self.distance(platform_computer) <= 50

    def at_upper_wall(self):
        return self.ycor() >= 360

    def bounce(self):
        self.setheading(self.heading() + random.randint(140, 220))

    def at_lower_wall(self):
        return self.ycor() <= -360

    def past_computer(self):
        return self.xcor() >= 490

    def past_player(self):
        return self.xcor() <= -490

    def heading_left(self):
        return 270 > self.heading() > 90

    def heading_right(self):
        return 270 <= self.heading() <= 360 or 0 <= self.heading() <= 90






