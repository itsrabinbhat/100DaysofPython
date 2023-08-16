import turtle as t
import random as r

draw = t.Turtle()
t.colormode(255)
draw.pensize(4)
color_list = [(246, 237, 224), (243, 216, 61), (242, 145, 72), (108, 175, 207), (26, 113, 168), (243, 218, 228),
              (246, 216, 1), (217, 237, 228), (228, 67, 109), (213, 132, 165), (194, 9, 37), (204, 225, 236),
              (112, 194, 163), (206, 174, 5), (12, 145, 106), (10, 176, 207), (161, 57, 103), (43, 181, 119),
              (240, 159, 189), (243, 74, 36), (230, 73, 9), (142, 217, 191), (251, 159, 144), (140, 212, 226),
              (106, 109, 172), (3, 106, 79), (188, 178, 218), (72, 31, 55), (196, 14, 10), (18, 59, 135)]


# Functions for drawing on screen
def forward():
    draw.color(r.choice(color_list))
    draw.setheading(90)
    draw.forward(10)


def backward():
    draw.color(r.choice(color_list))
    draw.setheading(-90)
    draw.forward(10)


def clockwise():
    draw.color(r.choice(color_list))
    draw.setheading(0)
    draw.forward(10)


def counter_clockwise():
    draw.color(r.choice(color_list))
    draw.setheading(180)
    draw.forward(10)


def clear_screen():
    draw.clear()


# Event listeners
t.listen()
t.onkey(forward, 'w')
t.onkey(backward, 's')
t.onkey(clockwise, 'd')
t.onkey(counter_clockwise, 'a')
t.onkey(clear_screen, 'c')

t.Screen().exitonclick()
