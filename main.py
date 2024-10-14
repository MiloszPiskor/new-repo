import random
import turtle
from turtle import Screen, Turtle
turtlik = Turtle()
turtlik.hideturtle()
turtle.colormode(255)
turtlik.speed("fastest")
turtlik.penup()


# print(colorgram.extract("image.jpg",20 ))
# colors = colorgram.extract("image.jpg",20)
#
# colors_list = []
# for _ in range(len(colors)):
#     colors_list.append((tuple(colors[_].rgb)))

final_color_list = [(235, 231, 233), (227, 233, 228), (206, 159, 84), (56, 89, 129), (143, 92, 41), (221, 206, 109), (138, 27, 50), (133, 176, 201), (155, 48, 83), (45, 55, 103), (169, 159, 42), (130, 188, 143), (83, 21, 44), (38, 43, 66), (185, 94, 107), (186, 141, 170), (87, 118, 178), (58, 39, 32), (80, 152, 163), (89, 156, 93), (195, 82, 72), (45, 74, 77), (79, 73, 44), (162, 201, 218), (57, 121, 118), (219, 176, 187), (46, 75, 75), (170, 205, 168), (221, 181, 168), (178, 189, 212), (153, 35, 34), (43, 66, 66)]

# TODO 10 dots in height and width, dot_size = 20, space_between = 50

set_height = turtlik.teleport

set_height(-250,-200)

def draw_a_line():
    for _ in range(10):
        turtlik.dot(20, random.choice(final_color_list))
        turtlik.forward(50)

def move_left():
    turtlik.setheading(90)
    turtlik.forward(50)
    turtlik.setheading(180)
    turtlik.forward(500)
    turtlik.setheading(0)

for _ in range(10):
    draw_a_line()
    move_left()

# draw_a_line()
# set_height(-250,50)
# draw_a_line()
# set_height(-250, 100)
# draw_a_line()






screen = Screen()
screen.exitonclick()