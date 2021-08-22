from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("PPArcade")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle(x_pos=360)
computer_paddle = Paddle(x_pos=-360)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=paddle.up)
screen.onkey(key="s", fun=paddle.down)
screen.onkey(key="e", fun=computer_paddle.up)
screen.onkey(key="d", fun=computer_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    ball.moving()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.touched_vertical_wall()
    if (350 <= ball.xcor() < 360) and ball.distance(paddle) < 50:
        ball.touched_paddle()
    elif (-350 >= ball.xcor() > -360) and ball.distance(computer_paddle) < 50:
        ball.touched_paddle()
    if ball.xcor() >= 400:
        ball.reset()
        scoreboard.computer_won()
    elif ball.xcor() <= -400:
        ball.reset()
        scoreboard.player_won()
screen.exitonclick()
