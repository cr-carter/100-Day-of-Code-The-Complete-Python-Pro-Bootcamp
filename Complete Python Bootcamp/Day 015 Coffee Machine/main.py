# The purpose of this project is to work with a greater number of functions, global variables,
# dictionaries, lists, and modifying the dictionaries as global variables within functions.
# Careful attention was also paid to the logical flow of the program, as well as attemtping
# to make the program user friendly.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 600,
    "milk": 400,
    "coffee": 100,
    "money": 0.0,
}

# Function that will verify the user input and return their choice as a string
def user_prompt():
    """Prompt the user to input their choice, and return choice as a string"""
    choice = ""
    while choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return choice

# This function will simply display remaining resources from the resources dictionary
def display_resources():
    """Display resourcese available in the machine"""
    print(f"Water reservoir: {resources["water"]}")
    print(f"Milk reservoir: {resources["milk"]}")
    print(f"Coffee reservoir: {resources["coffee"]}")
    print(f"Money: ${resources["money"]}")

# This function takes the drink choice as a parameter, and will compare the ingredients 
# based on the MENU dictionary against the resources available in the resources dictionary
def ingredients_available(drink_choice):
    """Check if ingredients are available for specific drink"""
    available = True
    for key in MENU[drink_choice]['ingredients']:
        if MENU[drink_choice]["ingredients"][key] > resources[key]:
            available = False
    return available

# This function will request the user to input a number of coins, and return the amount paid
# as well as the price of the drink
def get_payment(drink):
    """Prompt user to enter coins for payment, return amount paid and the cost of the drink"""
    drink_cost = MENU[drink]["cost"]
    print(f"Your {drink} will cost ${drink_cost}")
    coins = {"quarters": 0,
             "dimes": 0,
             "nickles": 0,
             "pennies": 0,
            }
    for coin in coins:
        valid = False
        while not valid:
            amount = input(f"Please enter how many {coin} you have: ")
            try:
                amount = int(amount)
                if amount >= 0:
                    coins[coin] = amount
                    valid = True
            except:
                print("Invalid payment.")
    print(coins)
    total_paid = coins["quarters"] * 0.25 + coins["dimes"] * 0.10 + coins["nickles"] * 0.05 + coins["pennies"] * 0.01
    return total_paid, drink_cost

# This function will accept the payment and drink cost as parameters, and either return
# the change or return False
def get_change(payment, cost):
    global resources
    """Accept payment and cost of drink, return change or return False if payment is less than cost"""
    if payment >= cost:
        change = payment - cost
        resources["money"] += cost
        return change
    else:
        return False

# This function will subtract from the global resources dictionary based on the
# information found in the MENU dictionary
def make_drink(drink):
    """Reduce amount of resources left based on drink"""
    global resources
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

# Main program
def coffee_machine():
    # While continue to run until user enters "off"
    machine_on = True
    while machine_on:
        user_choice = user_prompt()
        if user_choice == "off":
            machine_on = False
        # Allow user to see remaining ingredients based off the resources dictionary
        elif user_choice == "report":
            display_resources()
        else:
            choice_available = ingredients_available(user_choice)
            # Check if ingredients are available to make drink
            if choice_available == False:
                print("Not enough product left for this selection.")
            else:
                # Get payment from user, get change
                payment, cost = get_payment(user_choice)
                change = get_change(payment, cost)
                # If the get_change function returns False due to the cost being higher than the payment,
                # inform the user that they did not pay enough
                if type(change) == bool:
                    print("Not enough money for this selection.")
                else:
                    # If the user paid enough, return their change and make the drink.
                    make_drink(user_choice)
                    if change > 0:
                        print(f"Here is your ${change} in change.")
                    print(f"Here is your {user_choice}. Enjoy!")


coffee_machine()
