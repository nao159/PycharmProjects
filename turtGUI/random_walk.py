from turtle import Turtle, Screen
import random
import colorgram

screen = Screen()
screen.colormode(255)
oleg = Turtle()
oleg.up()
oleg.ht()
oleg.setx(-200)
oleg.sety(-200)
colors = colorgram.extract('drunk_elaina.jpg.jpg', 5)
formatted_colors = []

for i in range(0, len(colors)):
    color = colors[i]
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    formatted_color = (r, g, b)
    formatted_colors.append(formatted_color)

print(formatted_colors)


def draw_painting():
    while oleg.ycor() <= 200:
        for meter in range(5):
            oleg.forward(80)
            oleg.st()
            oleg.dot(50, random.choice(formatted_colors))
            oleg.ht()
        oleg.setx(-200)
        y = oleg.ycor() + 100
        oleg.setpos(-200, y)


draw_painting()
