# The purpose of this project was to serve as an introduction to object oriented programming.
# The course provided code that was intended to serve as an "external library" that I had to import from.
# I have included that code as comments at the end of this file, so that you can run the code if desired.
# Lines 6 through 29 is the actual code I created for this project.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    choice = ""
    while choice not in ["espresso", "latte", "cappuccino", "off", "report"]:
        choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


