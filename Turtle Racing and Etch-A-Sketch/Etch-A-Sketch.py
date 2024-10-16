from turtle import Screen, Turtle

turtel = Turtle()
screen = Screen()
turtel.speed("fastest")
turtel.shape("turtle")
turtel.color("green")

def move_forwards():
    turtel.forward(10)
def move_backwards():
    turtel.backward(10)
def turn_left():
    heading = turtel.heading()
    turtel.setheading(heading + 10)
def turn_right():
    heading = turtel.heading()
    turtel.setheading(heading - 10)
def clear_screen():
    turtel.clear()
    turtel.penup()
    turtel.home()
    turtel.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()