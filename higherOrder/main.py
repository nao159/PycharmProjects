from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
my_winner = screen.textinput("who will win?", "choose the winner")

colors = ["red", "yellow", "green", "blue"]
turtles = []

for i in range(4):
    t = Turtle(shape="turtle")
    t.up()
    t.color(colors[i - 1])
    t.setpos(x=-220, y=150 - i * 100)
    turtles.append(t)


def turtle_run():
    for each_turtle in turtles:
        each_turtle.forward(randint(0, 20))


is_race_begin = False
if my_winner:
    is_race_begin = True

while is_race_begin:
    turtle_run()
    for i in turtles:
        if i.xcor() > 290:
            winner = i.color()[1]
            is_race_begin = False
            if my_winner == winner:
                print(f"You have correct predicted the winner! The winner is {winner} colored turtle")
            else:
                print(f"You have lost, the winner is {winner} colored turtle")

screen.exitonclick()
