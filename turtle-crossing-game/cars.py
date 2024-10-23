from turtle import Turtle
import random

STARTING_POSITIONS = list(range(280, -210, -20))
SPEED = 10
all_cars = []

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    if color_tuple != ( 255, 255, 255):
        return color_tuple


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=0.8)
        self.penup()
        self.color(random_color())
        self.pace = 10
        self.setheading(180)
        self.set_position_x()
        self.set_position_y()
        all_cars.append(self)

    def set_position_y(self):
         return self.sety(random.choice(STARTING_POSITIONS))

    def set_position_x(self):
        return self.setx(random.randint(320, 400))

    def speed_up(self):
        self.pace += 10






