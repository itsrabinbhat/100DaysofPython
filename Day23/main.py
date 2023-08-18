from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Capstone Project")
screen.tracer(0)

# Creating a turtle as player
player = Player()

car = CarManager()
score = Scoreboard()

# Moving player based on key press
screen.listen()
screen.onkeypress(player.move_player, 'Up')

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_cars()

    # Detect collision with cars
    for each_car in car.cars:
        if each_car.distance(player) < 20:
            is_game_on = False
            score.game_over()

    # Detect successful crossing
    if player.is_at_finish():
        player.goto_start()
        car.level_up()
        score.update_level()


screen.exitonclick()
