from turtle import Turtle

DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, paddle_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5, 1)
        self.goto(paddle_pos[0], paddle_pos[1])

    def up(self):
        ycor = self.ycor()
        if ycor < 300:
            ycor = ycor + 20
        self.goto(self.xcor(), ycor)

    def down(self):
        ycor = self.ycor()
        if ycor > -300:
            ycor = ycor - 20
        self.goto(self.xcor(), ycor)
