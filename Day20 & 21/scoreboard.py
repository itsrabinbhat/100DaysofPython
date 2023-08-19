from turtle import Turtle

FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.read_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def save_high_score(self):
        with open('score.txt', 'w') as f:
            f.write(f"{self.high_score}")

    def read_high_score(self):
        with open('score.txt', 'r') as f:
            s = f.read()
            self.high_score = int(s)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 10)
        self.write("GAME OVER", align='center', font=FONT)
        self.goto(0, -20)
        self.write(f"Your Final Score: {self.score}", align='center', font=FONT)
