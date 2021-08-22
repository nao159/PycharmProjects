from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.7)
        self.color("yellow")
        self.speed(0)
        self.new_location()

    def new_location(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.setpos(x=random_x, y=random_y)