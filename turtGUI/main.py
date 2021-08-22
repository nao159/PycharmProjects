from turtle import Turtle, Screen
from random import randint

color_array = ["blue", "red", "yellow", "green", "violet"]

oleg = Turtle()
oleg.shape("turtle")
perimeter = 360


def draw_shapes():
    for angle in range(3, 11):
        rotation_amount = perimeter / angle
        draw_color = randint(0, len(color_array) - 1)
        oleg.color(color_array[draw_color])
        for _ in range(0, angle):
            oleg.forward(100)
            oleg.right(rotation_amount)


draw_shapes()


screen = Screen()
screen.exitonclick()
