from turtle import Turtle

WIDTH_MULTIPLIER = 1
HEIGHT_MULTIPLIER = 5
SHAPE = "square"
COLOR = "white"
UP = 90
DOWN = 270
MOVE_DISTANCE = 20
PADDLE_BOUNDARY = 225


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__(shape=SHAPE)
        self.turtlesize(stretch_wid=WIDTH_MULTIPLIER, stretch_len=HEIGHT_MULTIPLIER)
        self.color(COLOR)
        self.penup()
        self.setheading(UP)
        self.goto(x_pos, y_pos)

    def up(self):
        if self.ycor() < PADDLE_BOUNDARY:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if -PADDLE_BOUNDARY < self.ycor():
            self.backward(MOVE_DISTANCE)
