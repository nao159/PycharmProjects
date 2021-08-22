from turtle import Turtle

FONT = ("Arial", 26, "normal")


def gg():
    gg_score = Scoreboard()
    gg_score.home()
    gg_score.write("Game over", align="center", font=FONT)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as highest_score:
            best_score = highest_score.read()
            self.highest_score = int(best_score)
        self.penup()
        self.hideturtle()
        self.goto(0, y=250)
        self.color("white")
        self.write(f"Score = {self.score} | Highest score = {self.highest_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} | Highest score = {self.highest_score}", align="center", font=FONT)