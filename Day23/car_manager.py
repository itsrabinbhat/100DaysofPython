from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
MOVE_DISTANCE = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_DISTANCE

    def generate_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.setheading(180)
            Y_cor = random.randint(-250, 250)
            car.goto(300, Y_cor)
            self.cars.append(car)

    def move_cars(self):
        for each_car in self.cars:
            each_car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_DISTANCE/2
