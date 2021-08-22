from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.home()
        self.x_move = 0.1
        self.y_move = 0.1
        self.move_speed = 0.01

    def moving(self):
        new_x = self.x_move + self.move_speed
        new_y = self.y_move + self.move_speed
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x + new_x, current_y + new_y)

    def touched_vertical_wall(self):
        self.y_move = -self.y_move

    def touched_paddle(self):
        self.move_speed += 0.01
        self.x_move = -self.x_move

    def reset(self):
        self.home()
        self.move_speed = 0.01
        self.touched_paddle()
