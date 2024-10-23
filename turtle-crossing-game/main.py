from turtle import Screen, colormode
import time
from player import Player
from scoreboard import Scoreboard
from cars import Car, all_cars, SPEED

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
score = Scoreboard()
car = Car()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.backwards, "Down")

game_on = True

while game_on:

    for car in all_cars[::4]:
        car.forward(SPEED)
        if car.distance(player) < 25:
            game_on = False
            score.game_over()


    time.sleep(0.1)
    screen.update()


    if player.at_finish():
        score.update_score()
        player.at_start()
        SPEED += 5

    car = Car()




screen.exitonclick()