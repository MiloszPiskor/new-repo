from turtle import Turtle
import scoreboard

X_AXIS_VALUES = [0, -20, -40]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def positions_equal(pos1, pos2, tolerance=0.1):
    return abs(pos1[0] - pos2[0]) < tolerance and abs(pos1[1] - pos2[1]) < tolerance

class Snake:

    def __init__(self):
        self.body_parts = []
        self.speed = 20
        self.create()
        self.head = self.body_parts[0]

    def create(self):
        for position in range(3):
            snake_body_part = Turtle("square")
            snake_body_part.color("white")
            snake_body_part.speed("fastest")
            snake_body_part.penup()
            snake_body_part.goto(X_AXIS_VALUES[position], 0)
            self.body_parts.append(snake_body_part)

    def prolong(self):
        snake_body_part = Turtle("square")
        snake_body_part.color("white")
        snake_body_part.speed("fastest")
        snake_body_part.penup()
        snake_body_part.goto(self.body_parts[len(self.body_parts) -1].pos())
        self.body_parts.append(snake_body_part)



    def move(self):
        for white_block in range(len(self.body_parts) -1, 0, -1):
            new_x = self.body_parts[white_block - 1].xcor()
            new_y = self.body_parts[white_block - 1].ycor()
            self.body_parts[white_block].goto(new_x, new_y)

        self.body_parts[0].forward(self.speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def at_wall(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() <-290:
            return True


    def hits_tail(self):
        for body_part in self.body_parts[1:]:
            if positions_equal(self.head.position(), body_part.position()):
                return True
        return False


    # def hits_tail(self):
    #         for _ in range(1, len(self.body_parts) -1, 1):
    #             if self.head.position() == self.body_parts[_].position():
    #                 return True

