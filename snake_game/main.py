from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake_move = True
while snake_move:
    screen.update()
    time.sleep(0.1)
    snake.move()
    eating_spot = tuple(food.pos())

    # detect collision with food

    if snake.head.distance(eating_spot) < 15:
        food.relocate()
        scoreboard.add_score()
        snake.prolong()

    # detect collision with wall

    if snake.at_wall():
        snake_move = False
        scoreboard.game_over()

    # detect collision with tail

    if snake.hits_tail():
        snake_move = False
        scoreboard.game_over()


























screen.exitonclick()