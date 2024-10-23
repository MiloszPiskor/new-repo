from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-240, 260)
        self.score = 1
        self.write(f"Level: {self.score}", align = "center", font = ("Courier", 15, "bold"))


    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align = "center", font = ("Courier", 15, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Courier", 30, "bold"))

