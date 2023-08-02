import os
import art
import random


# Random number generator
def random_num_gen():
    return random.randint(1,100)

# Clear the console
def clear():
    os.system("clear")

def compare_nums(num,guess):
    if num == guess:
        return f"You got it, the ans was {num}."
    elif num > guess:
        return "Too low, Guess again."
    else:
        return "Too high, Guess again."
        
    

def play_game():
    guess_left = 0
    guess = 0
    is_game_over = False
    num = random_num_gen()
    
    # Displaying the Guess the Number art
    print(art.text2art("Guess The Number"))
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    level = input("Choose a difficulty. Type 'easy' of 'hard': ").lower()
    if level == 'easy':
        guess_left = 10
    elif level == 'hard':
        guess_left = 5
    else:
        print("Invalid choice, You lost!")
        return
    
        
    while not is_game_over:
        print(f"You have {guess_left} attempts remaining to guess.")
        guess = int(input("Make a guess: "))
        guess_left -= 1
        
        if guess_left == 0:
            is_game_over = True
            print("You've run out of guesses, You lost!")
            break
        if num == guess:
            is_game_over = True
            
        print(compare_nums(num,guess))
        
        
play_game()

while input("\nDo you want to play again?(Y/N)").lower() == 'y':
    clear()
    play_game()
