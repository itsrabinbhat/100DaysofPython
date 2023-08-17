from turtle import Turtle

FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        self.clear()
        self.goto(0, 10)
        self.write("GAME OVER", align='center', font=FONT)
        self.goto(0, -20)
        self.write(f"Your Final Score: {self.score}", align='center', font=FONT)
