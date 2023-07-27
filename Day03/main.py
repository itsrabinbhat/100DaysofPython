print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You're at a cross roads. Do you want to go 'left' or 'right':\n")
if choice.lower() == 'left':
    print("You fell into a pit.\nGame over!")
elif choice.lower() == 'right':
    choice = input("You came at a lake. Do you want to 'swim' over or take a 'boat':\n")
    if choice.lower() == 'swim':
        print("A shark ate you.\n Game over!")
    elif choice.lower() == 'boat':
        choice = input("You arrive at an Island. There is a house with 3 doors, 'red', 'blue' and 'green':\n")
        if choice.lower() == 'green':
            print("Congrats! You won!")
        elif choice.lower() == 'red':
            print("You entered a room on fire.\nGame over!")
        else:
            print("You entered a room full of toxic gas.\nGame over!")
    else:
        print("Wrong choice, Game over!")
else:
    print("Wrong choice, Game over!")