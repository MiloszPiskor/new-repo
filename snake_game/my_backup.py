from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

x_axis_values = [0, -20, -40]
snake_body_parts = []

for position in range(3):
    snake_body_part = Turtle("square")
    snake_body_part.color("white")
    snake_body_part.speed("fastest")
    snake_body_part.penup()
    snake_body_part.goto(x_axis_values[position], 0)
    snake_body_parts.append(snake_body_part)

def turn_left():
    snake_body_parts[0].left(90)

snake_body_parts[0].heading()
screen.listen()
snake_move = True
while snake_move:
    screen.update()
    time.sleep(0.1)
    for white_block in range(len(snake_body_parts) - 1, 0, -1):
        new_x = snake_body_parts[white_block -1].xcor()
        new_y = snake_body_parts[white_block -1].ycor()
        snake_body_parts[white_block].goto(new_x, new_y)

    snake_body_parts[0].forward(20)
    screen.onkey(turn_left, "a")

