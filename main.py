from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0) # To skip the moving animation

left_paddle = Paddle((-350, 0)) #immovable as of now
right_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Bounce off top and bottom walls only
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Paddle collision (flip x direction only)
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()  # ← left player gets a point

    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()  # ← right player gets a point