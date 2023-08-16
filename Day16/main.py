from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
make_coffee = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    choice = input(f"\nWhat do you want?{coffee_menu.get_items()}:").lower()
    if choice == 'report':
        make_coffee.report()
        money_machine.report()
        continue
    coffee = coffee_menu.find_drink(choice)

    if coffee is not None:
        if make_coffee.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            make_coffee.make_coffee(coffee)
