from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.x_position = x_pos
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=self.x_position, y=0)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(x=self.x_position, y=new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(x=self.x_position, y=new_y)
