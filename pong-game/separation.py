from turtle import Turtle

class Separation(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        for y_axis_value in range(360, -361, -80):
            self.goto(0, y_axis_value)
            self.stamp()
            self.hideturtle()
