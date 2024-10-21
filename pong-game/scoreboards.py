from turtle import Turtle

POSITIONS = [(150,300), (-150,300)]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        for position in POSITIONS:
            self.penup()
            self.color("white")
            self.goto(position)

    def write_score(self, player_score, opponent_score):
        self.clear()
        self.goto(POSITIONS[0])
        self.write(f"{opponent_score}", font = ("Courier", 60, "bold"))
        self.goto(POSITIONS[1])
        self.write(f"{player_score}", font = ("Courier", 60, "bold"))
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"Game Over!", align= "center" , font=("Courier", 60, "bold"))








