from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net
import time

PADDLE_POS = [(350, 0), (-350, 0)]

# Screen setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Play Pong')
screen.tracer(0)

# paddles
r_paddle = Paddle(PADDLE_POS[0])
l_paddle = Paddle(PADDLE_POS[1])

# Ball and net
ball = Ball()
net = Net()

# Scoreboard
scoreboard = Scoreboard()


# Moving paddles
screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

is_game_on = True

while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    # Detect collision with top and bottom wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_off_paddle()

    # Check if r_paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()

    # Check if l_paddle misses the ball
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
