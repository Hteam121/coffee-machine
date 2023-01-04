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

inputValue = input("What would you like? (expresso/latte/cappuccino):")


def report():
    output = f"Water: {resources['water']}ml" \
          f"Milk: {resources['milk']}ml" \
          f"Coffee: {resources['coffee']}g" \
          f"Money: ${resources['money']}"
    print(output)
