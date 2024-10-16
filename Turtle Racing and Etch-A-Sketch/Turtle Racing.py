from turtle import Screen, Turtle
import random

turtel = Turtle(shape = "turtle")
turtlik = Turtle("turtle")
turtla = Turtle("turtle")
turt = Turtle("turtle")
t = Turtle("turtle")

colors = ["green", "blue", "red", "orange", "purple"]
turtles = [turtel, turtlik, turtla, turt, t]
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle will win the race? Enter a color: ").lower()
index = 0
coordinates = -230, 150
for turtle in turtles:
    turtle.speed("slowest")
    turtle.color(colors[index])
    index += 1
    turtle.penup()
    turtle.goto(coordinates)
    coordinates = coordinates[0], coordinates[1] - 70

game_on = True
while game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"The winner is {winner_color}. Congratulations, You've won!")
            else:
                print(f"The winner is {winner_color}. Sorry, You've lost.")

        random_step = random.randint(1, 20)
        turtle.forward(random_step)











screen.exitonclick()