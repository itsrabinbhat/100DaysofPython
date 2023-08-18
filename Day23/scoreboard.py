from turtle import Turtle

FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.show_level()

    def show_level(self):
        self.goto(-220, 250)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
