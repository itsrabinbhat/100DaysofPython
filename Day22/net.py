from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, -290)
        self.color('gray')
        self.pensize(3)
        self.draw_net()

    def draw_net(self):
        self.setheading(90)
        for _ in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

