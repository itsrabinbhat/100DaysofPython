import turtle as t
import random as r

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.Screen().setup(height=400, width=500)
is_game_over = False
y = -100
my_turtles = []
for color in colors:
    my_turtle = t.Turtle(shape='turtle')
    my_turtle.penup()
    my_turtle.color(color)
    my_turtle.goto(x=-230, y=y)
    my_turtles.append(my_turtle)
    y += 40

choice = t.Screen().textinput(title='Make your bet!', prompt="Which turtle will win the race? Enter a color: ")


def random_step_forward(current_turtle):
    current_turtle.forward(r.randint(1, 10))


def check_winner(current_turtle):
    idx = my_turtles.index(current_turtle)
    winner = colors[idx]
    if choice.lower() == winner:
        t.write("Yay! You won.\n", font=("Arial", 12, 'bold'))
    else:
        t.write("Sry! You lost.\n", font=("Arial", 12, 'bold'))

    t.write(f'Winner is {winner} turtle!', font=("Arial", 12, 'normal'))


while not is_game_over:
    for each_turtle in my_turtles:
        random_step_forward(each_turtle)
        current_position = each_turtle.position()
        if current_position[0] >= 220:
            check_winner(each_turtle)
            is_game_over = True
            break


t.Screen().exitonclick()
