from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce(self):
        self.y_move *= -1

    def bounce_off_paddle(self):
        self.ball_speed *= 0.9
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_off_paddle()
