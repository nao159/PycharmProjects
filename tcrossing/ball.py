from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.up()
        self.setheading(90)
        self.goto(x=0, y=-250)

    def move(self):
        self.forward(20)
