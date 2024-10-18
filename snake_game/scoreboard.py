from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=('Courier', 12, 'normal'))
        self.hideturtle()


    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Courier', 12, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"You lost! Final score: {self.score}", align="center", font=('Courier', 15, 'normal'))












