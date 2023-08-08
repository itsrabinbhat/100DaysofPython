# required module for this project
import os
import time
import coffee_data


def greetings():
    print("Turning on", end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Welcome to the Coffee Machine')


def check_resources(resources, req_resources):
    if (resources['water'] < req_resources['water']
            or resources['milk'] < req_resources['milk']
            or resources['coffee'] < req_resources['coffee']):
        return False
    return True


def check_payment(inserted_amount, coffee):
    coffee_cost = coffee_data.menu[coffee]['cost']
    if inserted_amount >= coffee_cost:
        return True
    return False


def make_coffee(coffee_type):
    print(f"Making your {coffee_type}", end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    print(f"Here is your {coffee_type}☕. Enjoy!")


def off():
    os.system('cls')
    print("Turning off", end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    exit()


def report(resources):
    print(f"Water: {resources['water']}ml"
          f"\nMilk: {resources['milk']}ml"
          f"\nCoffee: {resources['coffee']}g"
          f"\nMoney: ${resources['profit']}")


available_resources = coffee_data.resources.copy()


def start_machine():
    greetings()
    user_input = ''
    profit = 0
    while user_input != 'off':
        user_input = input("\nWhat do you want?(latte/espresso/cappuccino): ").lower()
        if user_input == 'off':
            off()
        elif user_input == 'report':
            report(available_resources)
        elif user_input == 'latte' or user_input == 'espresso' or user_input == 'cappuccino':
            required_resources = coffee_data.menu[user_input]['ingredients']
            if check_resources(available_resources, required_resources):
                print("Please insert coins->")
                quarters = int(input("\tHow many quarters? "))
                dimes = int(input("\tHow many dimes? "))
                nickles = int(input("\tHow many nickles? "))
                pennies = int(input("\tHow many pennies? "))
                inserted_sum = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                if check_payment(inserted_sum, user_input):
                    profit += coffee_data.menu[user_input]['cost']
                    available_resources['profit'] = profit
                    # updating the available resources of the machine after making a coffee
                    available_resources['water'] -= required_resources['water']
                    available_resources['milk'] -= required_resources['milk']
                    available_resources['coffee'] -= required_resources['coffee']

                    print(f"Here is your ${round(inserted_sum - coffee_data.menu[user_input]['cost'], 2)} in change")
                    make_coffee(user_input)
                else:
                    print("Sorry that's not enough money, Money refunded.")
            else:
                print("Sorry not enough resources.")

        else:
            print(f"Sorry, We don't have {user_input}.")


start_machine()
