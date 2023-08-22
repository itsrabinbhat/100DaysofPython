import turtle
import pandas

# Screen setup
image = './blank_states_img.gif'
screen = turtle.Screen()
screen.setup(700, 490)
screen.bgpic(image)
screen.title('Name the states')

correct_guesses = []
state = turtle.Turtle()
state.hideturtle()
state.penup()
df = pandas.read_csv('50_states.csv')
score = 0

while len(correct_guesses) < 50:
    score = len(correct_guesses)
    # getting user input
    # screen.tracer(1)

    try:
        user_guess = screen.textinput(title=f'{len(correct_guesses)}/50 correct states',
                                      prompt="What's another state name?").title()

        # Comparing it to user input and plotting it into the map
        state_match = df[df.state.str.contains(user_guess)]

        if user_guess == 'Exit':
            break

        if user_guess not in correct_guesses:
            if not state_match.empty:
                state_data = state_match.values.flatten().tolist()
                correct_guesses.append(state_data[0])
                state.goto(state_data[1], state_data[2])
                state.write(state_data[0], align='center', font=('Courier', 10, 'normal'))

    except AttributeError:
        print(f"Your final score is {score}")
        break

