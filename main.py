# Imports & Libraries
import data
import art

# Global Scope
MENU = data.MENU
MENU_ITEMS = list(MENU.keys())

COFFEE_ASCII = art.COFFEE

RESOURCES = data.RESOURCES
MONEY = 0.0

# Features functions
# TODO 1: Prompt the user with the 3 coffee options, a "report" option that displays your current resources and an "off" option that kills the script
def coffee_choice():
    coffee_choice_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_choice_prompt == "off":
        for line in range(25):
            print("\n")
        return None
    elif coffee_choice_prompt == "report":
        print(f"You have :\n{RESOURCES}")
        return coffee_choice()
    elif coffee_choice_prompt in MENU_ITEMS:
        return coffee_choice_prompt
    else:
        input("You chose an inappropriate option, press anything to try again:\n")
        return coffee_choice()

# TODO 2: Check the available resources to see if it's enough considering the coffee choice made by the user
def check_resources(chosen_coffee):
    if chosen_coffee is None:
        return

    chosen_menu = MENU[chosen_coffee]

    # Check if resources are sufficient
    for ingredient, required_amount in chosen_menu['ingredients'].items():
        if RESOURCES.get(ingredient, 0) < required_amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True

# TODO 3: Prompt the user to mimic a coin insertion (quarter: , dimes: , nickels: , pennies: )
def coin_insertion(price):
    try:
        quarters_inserted = int(input("How many quarters are you putting in :\n"))
        dimes_inserted = int(input("How many dimes are you putting in :\n"))
        nickles_inserted = int(input("How many nickles are you putting in :\n"))
        pennies_inserted = int(input("How many pennies are you putting in :\n"))

        money_inserted = quarters_inserted + dimes_inserted + nickles_inserted + pennies_inserted
        if money_inserted < price:
            print(f"There is not enough money, you're being refunded.")
            return False
        elif money_inserted > price:
            print(f"The transaction has been successful, your change amounts to {money_inserted - price}$")
            return money_inserted

    except ValueError:
        print("You didn't provide the machine with appropriate currency !")


# TODO 4: Make coffee: Deduct resources and add money to the machine
def make_coffee():
    global MONEY

    chosen_coffee = coffee_choice()
    coffee_price = MENU[chosen_coffee]["cost"]
    if check_resources(chosen_coffee):
        print(f"Resources are sufficient. Please insert {coffee_price}$")
        coin_insert = coin_insertion(coffee_price)
        if not coin_insert:
            return
        else:
            MONEY += coffee_price
            for ingredient, required_amount in MENU[chosen_coffee]['ingredients'].items():
                RESOURCES[ingredient] -= required_amount
            print(f"Resources have been deducted, your coffee is being made.\n{COFFEE_ASCII}")
    else:
        print("Not enough resources to make the coffee.")

make_coffee()