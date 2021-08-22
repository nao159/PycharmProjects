from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard, gg

screen = Screen()
screen.setup(width=600, height=600)
screen.title("snake")
screen.bgcolor("blue")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_body[0].distance(food) < 18:
        food.new_location()
        snake.extend()
        scoreboard.increase_score()

    if snake.snake_body[0].xcor() > 290 or snake.snake_body[0].xcor() < -290 or snake.snake_body[0].ycor() > 290 or \
            snake.snake_body[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for snake_body in snake.snake_body[1:]:
        if snake.snake_body[0].distance(snake_body) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
