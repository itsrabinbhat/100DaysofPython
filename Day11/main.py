import os
import graphics
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare_score(user_score,dealer_score):
    if user_score == dealer_score and user_score <= 21:
        return "It's a Draw!"
    elif user_score == 0:
        return "Congrats,You hit the BlackJack & You won!"
    elif dealer_score == 0:
        return "Dealer hit the BlackJack & You lost!"
    elif user_score > 21 and dealer_score > 21:
        return "You lost!"
    elif user_score > 21:
        return "You lost!"
    elif dealer_score > 21:
        return "Congrats, You won!"
    elif user_score > dealer_score:
        return "Cograts, You won!"
    else:
        return "You lost!"
    
    

def get_score(cards):
    score = sum(cards)
    
    # check for black jack
    if score == 21 and len(cards) == 2:
        score = 0
    
    # change 11 to 1 if the sum of cards is > 21
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def start_game():
    print(graphics.logo)
    user_cards = []
    dealer_cards = []
    is_game_over = False
    
    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
        
    while not is_game_over:
        user_score = get_score(user_cards)
        dealer_score = get_score(dealer_cards)
        
        print(f"Your Cards:{user_cards}, Current Score:{user_score}")
        print(f"Dealer's first card:{dealer_cards[0]}")
        # print(f"Dealer score:{dealer_score}")
        
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            print(compare_score(user_score,dealer_score))
            is_game_over = True
            
        else:
            choice = input("Do you want to get another cards?(Y/N): ").lower()
            
            if choice == 'y':
                user_cards.append(deal_card())
                
                if dealer_score != 0 and dealer_score < 17:
                    dealer_cards.append(deal_card())
                
                print(f"Your fincal Cards:{user_cards}, Final Score:{user_score}")
                print(f"Dealer's first card:{dealer_cards[0]}")
            elif choice == 'n':
                print(compare_score(user_score,dealer_score))
                is_game_over = True
            else:
                print("Invalid Choice! Game over.")
                is_game_over = True
                
                
start_game()

while not input("\nDo you want to play the game again?(Y/N): ").lower() == 'n':
    os.system("clear")
    start_game()
