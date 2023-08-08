import random
import os
import graphics
from game_data import data

# function to get random persons data


def get_random_person():
    return random.choice(data)

# Function to clear the console


def clear():
    os.system("cls")
    
# Function to compare the followers of person A and B.


def compare_followers(A,B):
    # print(A,B)
    if A > B:
        return 'a'
    else:
        return 'b'
        
    
def play():
    # Some variables
    is_game_over = False
    score = 0
    person_A = get_random_person()
    while not is_game_over:
        clear()
        person_B = get_random_person()
        while person_A == person_B:
            person_B = get_random_person()
        print(graphics.logo)
        if score != 0:
            print(f"Current Score:{score}")
        print(f"Person A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}.")
        print(graphics.vs)
        print(f"Person B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}.")
        
        result = compare_followers(person_A['follower_count'], person_B['follower_count'])
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        # Comparing result and use choice
        if choice == result:
            score += 1
            person_A = person_B
        else:
            is_game_over = True
            print(f"Sorry, that's wrong, Final Score: {score}")

# initializing the function


play()

while input('Do you want to play again?(Y/N): ').lower() == 'y':
    clear()
    play()

