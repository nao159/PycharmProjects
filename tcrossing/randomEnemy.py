from turtle import Turtle
import random
from time import sleep

ENEMY_COLOR = ["red", "yellow", "blue", "green", "violet", "black"]


class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.up()
        self.color(random.choice(ENEMY_COLOR))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.new_y = random.randint(-230, 280)
        self.new_x = random.randint(300, 400)
        self.goto(x=self.new_x, y=self.new_y)

    def move(self):
        new_x = self.xcor() - 20
        self.goto(x=new_x, y=self.new_y)
        sleep(0.3)
        self.move()

    def create_enemy(self):
        self.__init__()