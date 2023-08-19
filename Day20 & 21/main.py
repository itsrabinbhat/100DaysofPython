from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listening for the keystrokes
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True


# # Continue the game
# def continue_game():
#     global is_game_on
#     is_game_on = True
#     scoreboard.reset()
#     snake.reset()


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend_snake()
        food.respawn_food()

    # Detect collision with wall
    if (snake.snake_head.xcor() > 280
            or snake.snake_head.xcor() < -280
            or snake.snake_head.ycor() > 280
            or snake.snake_head.ycor() < -280):
        snake.reset()
        scoreboard.reset_score()

    # Detect collision with snake tail/body
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset_score()

screen.exitonclick()
