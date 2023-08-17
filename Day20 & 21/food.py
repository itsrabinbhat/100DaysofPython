from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('skyblue')
        self.speed('fastest')
        self.penup()
        self.respawn_food()

    def respawn_food(self):
        x_cor = r.randint(-280, 280)
        y_cor = r.randint(-280, 280)
        self.goto(x_cor, y_cor)

