from turtle import Turtle

START_POSITION = (0, -280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.moving_interval = 10
        self.setheading(90)
        self.goto(START_POSITION)

    def move(self):
        self.forward(self.moving_interval)

    def backwards(self):
        self.back(self.moving_interval)

    def at_finish(self):
        return self.ycor() > 270

    def at_start(self):
        self.goto(START_POSITION)