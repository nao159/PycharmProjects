from turtle import Screen
from ball import Ball
from time import sleep
from randomEnemy import Enemy

screen = Screen()
screen.title("TCrossing")
screen.setup(width=800, height=600)
screen.tracer(0)

ball = Ball()
enemy = Enemy()

screen.listen()
screen.onkey(key="w", fun=ball.move)

game_is_on = True
max_enemies_on_screen = 20
current_enemies_on_screen = 0
enemy_list = []
while game_is_on:
    screen.update()
    sleep(0.1)



screen.exitonclick()
