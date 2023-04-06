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
}


def insert_coins():
    print("Please insert coins:")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))


money=0
condition=True
while condition:
    
    #prompt user by asking "what would you like"
    user_choice=input("What would you like? (espresso/latte/cappuccino): ")
    
    #turning off the coffee machine by entering "off" to the prompt
    if user_choice=="off":
        condition=False

    #when user enters "report" a report should be generated that shows the current resource values
    elif user_choice=="report":
        print(f'Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${money}')

    elif user_choice=="espresso":
        if resources["water"]>=MENU["espresso"]["ingredients"]["water"] and resources["coffee"]>=MENU["espresso"]["ingredients"]["coffee"]:
            insert_coins()

