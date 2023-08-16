from turtle import Turtle

STARTING_SEGMENTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_SEGMENTS:
            self.add_segments(position)

    def add_segments(self, pos):
        snake_body = Turtle('square')
        snake_body.penup()
        snake_body.color('white')
        snake_body.goto(pos)
        self.segments.append(snake_body)

    def extend_snake(self):
        new_segment_pos = self.segments[-1].position()
        self.add_segments(new_segment_pos)

    # Moving the snake around the screen
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[i - 1].xcor()
            new_ycor = self.segments[i - 1].ycor()
            self.segments[i].goto(new_xcor, new_ycor)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
