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
# Make a dictionary to filter through input key values


def report():
    output = f"Water: {resources['water']}ml" \
          f"Milk: {resources['milk']}ml" \
          f"Coffee: {resources['coffee']}g" \
          f"Money: ${resources['money']}"
    print(output)


def checkresources(drink):
    global flag
    if resources['water'] - MENU[drink]['ingredients']['water'] < 0:
        flag = False
        return "Sorry there is not enough water"
    if resources['milk'] - MENU[drink]['ingredients']['milk'] < 0:
        flag = False
        return "Sorry there is not enough milk"
    if resources['coffee'] - MENU[drink]['ingredients']['coffee'] < 0:
        flag = False
        return "Sorry there is not enough coffee"

    return 1


def coins():
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    pennies = input("How many pennies?: ")

    total = float(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01)
    return total


def drink(drink):
    global flag
    checkresources(drink)
    amount = coins()
    change = amount - MENU[drink]['cost']

    if change > 0:
        print(f"Here is ${change} in change")
    elif change < 0:
        print("insufficient funds")
        flag = False
    resources['money'] += amount


flag = True
while flag:
    inputValue = input("What would you like? (expresso/latte/cappuccino):")

    match inputValue:
        case "expresso":
            drink("expresso")
        case "report":
            report()
        case "off":
            flag = False
