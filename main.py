import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

p1_paddle = Paddle(-350, 0)
p2_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(p1_paddle.up, "w")
screen.onkey(p1_paddle.down, "s")
screen.onkey(p2_paddle.up, "Up")
screen.onkey(p2_paddle.down, "Down")

in_game = True


def player_score(player):
    if player == "p1":
        scoreboard.update_p1_score()
    elif player == "p2":
        scoreboard.update_p2_score()
    ball.reset_position()
    scoreboard.show_score()


def pong():
    while in_game:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() < -280 or ball.ycor() > 280:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(p1_paddle) < 50 and ball.xcor() < -320 or ball.distance(p2_paddle) < 50 and ball.xcor() > 320:
            ball.bounce_x()

        # Detect collision with goal
        if ball.xcor() < -380:
            player_score("p2")
        elif ball.xcor() > 380:
            player_score("p1")

    screen.exitonclick()


pong()
