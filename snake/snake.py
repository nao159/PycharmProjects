from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
STARTING_POSITION = [(20, 0), (0, 0), (-20, 0)]


class Snake():

    def __init__(self):
        self.snake_body = []
        self.snake_length()

    def snake_length(self):
        for number in STARTING_POSITION:
            self.increase_body(number)

    def increase_body(self, number):
        snake = Turtle(shape="square")
        snake.color("red")
        snake.up()
        snake.setpos(number)
        self.snake_body.append(snake)

    def extend(self):
        self.increase_body(self.snake_body[-1].position())

    def move(self):
        snake_body = self.snake_body
        for body_number in range(len(snake_body) - 1, 0, -1):
            new_x = snake_body[body_number - 1].xcor()
            nex_y = snake_body[body_number - 1].ycor()
            snake_body[body_number].setpos(new_x, nex_y)
        snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def reset(self):
        for body in self.snake_body:
            body.goto(1000, 0)
        self.snake_body.clear()
        self.snake_length()