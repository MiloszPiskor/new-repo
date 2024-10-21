from turtle import Turtle


X_AXIS_COORDINATES = [470, -480]

class Platforms:
    def __init__(self):
        self.platforms = []
        self.create()
        self.opponent = self.platforms[0]
        self.player = self.platforms[1]
        self.opponent.speed("slow")
        self.moving_up = True
        self.player.score = 0
        self.opponent.score = 0

    def create(self):
        for platform in X_AXIS_COORDINATES:
            self.platformers = Turtle()
            self.platformers.penup()
            self.platformers.color("white")
            self.platformers.shape("square")
            self.platformers.shapesize(stretch_wid= 5, stretch_len= 1)
            self.platformers.goto(platform, 0)
            self.platforms.append(self.platformers)

    def player_move(self, x, y):
        self.player.sety(y)

    def at_upper_bound(self):
        return self.opponent.ycor() >= 350  # Upper boundary

    def at_lower_bound(self):
        return self.opponent.ycor() <= -350






