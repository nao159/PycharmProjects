from turtle import Turtle

FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.computer_score = 0
        self.color("white")
        self.up()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.write(f"{self.computer_score} : {self.player_score}", align="center", font=FONT)

    def player_won(self):
        self.player_score += 1
        self.clear()
        self.write(f"{self.computer_score} : {self.player_score}", align="center", font=FONT)

    def computer_won(self):
        self.clear()
        self.computer_score += 1
        self.write(f"{self.computer_score} : {self.player_score}", align="center", font=FONT)
