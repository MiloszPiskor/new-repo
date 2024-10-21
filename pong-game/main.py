from turtle import Screen
from separation import Separation
from platforms import Platforms
import time
from ball import Ball
import random
from scoreboards import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 800)
screen.title("Pong game")
screen.tracer(0)

ball = Ball()

separation = Separation()

platform = Platforms()

screen.listen()

score = Scoreboard()

screen.onclick(platform.player_move, 1)

game_on = True

ball.setheading(333)
while game_on:
    screen.update()
    score.write_score(player_score= platform.player.score, opponent_score= platform.opponent.score)
    time.sleep(0.1)
    position = platform.opponent.ycor()
    ball.forward(20)
    if platform.opponent.score >= 10 or platform.player.score >= 10:
        game_on = False
        score.game_over()


    # Move up or down depending on the direction
    if platform.moving_up:
        platform.opponent.sety(position + 40)
        if platform.at_upper_bound():
            platform.moving_up = False
    else:
        platform.opponent.sety(position - 40)
        if platform.at_lower_bound():
            platform.moving_up = True

    if ball.at_player(platform.player) or ball.at_computer(platform.opponent):
        ball.bounce()

    # if ball.heading_left():
    #     if ball.at_upper_wall():
    #         ball.left(random.randint(40, 70))
    #     if ball.at_lower_wall():
    #         ball.right(random.randint(40, 70))
    # elif ball.heading_right():
    #     if ball.at_upper_wall():
    #         ball.right(random.randint(40, 70))
    #     if ball.at_lower_wall():
    #         ball.left(random.randint(70, 70))
    if ball.at_lower_wall() and ball.heading_left():
            ball.right(random.randint(20, 40))
    elif ball.at_lower_wall() and ball.heading_right():
            ball.left(random.randint(20,  40))

    if ball.at_upper_wall() and ball.heading_left():
            ball.left(random.randint(20, 40))
    elif ball.at_upper_wall() and ball.heading_right():
            ball.right(random.randint(20, 40))



    if ball.past_player():
        platform.opponent.score += 1
        ball.go_start()

    if ball.past_computer():
        platform.player.score += 1
        ball.go_start()







screen.mainloop()
