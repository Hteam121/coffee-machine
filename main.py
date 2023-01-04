# Starter Values

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# Main body

def report():
    output = f"Water: {resources['water']}ml\n" \
          f"Milk: {resources['milk']}ml\n" \
          f"Coffee: {resources['coffee']}g\n" \
          f"Money: ${round(resources['money'], 2)}\n"
    print(output)


def checkresources(drink):
    if resources['water'] - MENU[drink]['ingredients']['water'] < 0:
        return "Sorry there is not enough water"
    if resources['milk'] - MENU[drink]['ingredients']['milk'] < 0:
        return "Sorry there is not enough milk"
    if resources['coffee'] - MENU[drink]['ingredients']['coffee'] < 0:
        return "Sorry there is not enough coffee"

    return 0


def coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = float(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01)
    return total


def drink(drink):
    amount = coins()
    change = amount - MENU[drink]['cost']

    if change > 0:
        print(f"Here is ${round(change, 2)} in change")
        resources['money'] += amount - change
    elif change < 0:
        print("insufficient funds")
    else:
        resources['money'] += amount - change

    if checkresources(drink) != 0:
        print(checkresources(drink))
    else:
        resources['water'] -= MENU[drink]['ingredients']['water']
        resources['milk'] -= MENU[drink]['ingredients']['milk']
        resources['coffee'] -= MENU[drink]['ingredients']['coffee']

        print("Here is your Latte, Enjoy!")


flag = True
while flag:
    inputValue = input("What would you like? (expresso/latte/cappuccino):")

    match inputValue:
        case "expresso":
            drink("expresso")
        case "latte":
            drink("latte")
        case "cappuccino":
            drink("cappuccino")
        case "report":
            report()
        case "off":
            flag = False

# End program
