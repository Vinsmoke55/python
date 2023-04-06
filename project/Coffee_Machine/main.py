from art import logo
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


#interface for providing the money
def insert_coins():
    print("Please insert coins:")
    quarters=float(input("How many quarters?: "))
    dimes=float(input("How many dimes?: "))
    nickles=float(input("How many nickles?: "))
    pennies=float(input("How many pennies?: "))
    coin={"quarters":quarters,"dimes":dimes,"nickles":nickles,"pennies":pennies}
    return coin

#function to calculate money in $
def calculate_money(quarter,dime,nickle,penny):
    total=0.25*quarter+0.1*dime+0.05*nickle+0.01*penny
    return total

money=0
condition=True
while condition:
    print(logo)
    
    #prompt user by asking "what would you like"
    user_choice=input("What would you like? (espresso/latte/cappuccino): ")
    
    #turning off the coffee machine by entering "off" to the prompt
    if user_choice=="off":
        condition=False

    #when user enters "report" a report should be generated that shows the current resource values
    elif user_choice=="report":
        print(f'Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${money}')

    #if the user choice is espresso
    elif user_choice=="espresso":
        if resources["water"]<=MENU["espresso"]["ingredients"]["water"]:
            print("Sorry ther is no enough water.")
        elif resources["coffee"]<=MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry no enough coffee.")
        else:
            coins=insert_coins()
            money_by_customer=round(calculate_money(coins["quarters"],coins["dimes"],coins["nickles"],coins["pennies"]),2)
            if money_by_customer>=MENU["espresso"]["cost"]:
                return_money=money_by_customer-MENU["espresso"]["cost"]
                money_by_customer-=return_money
                money+=money_by_customer
                print(f"Here is ${round(return_money,2)} in change.")   #returning the extra money 
                resources["water"]-=MENU["espresso"]["ingredients"]["water"]
                resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
                print("Here is your espresso. Enjoy!!")

            else:
                print("Sorry that's not enough money. Money refunded")

    #if the user choic is latte
    elif user_choice=="latte":
        if resources["water"]<=MENU["latte"]["ingredients"]["water"]:
            print("Sorry ther is no enough water.")
        elif resources["coffee"]<=MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry no enough coffee.")
        elif resources["milk"]<=MENU["latte"]["ingredients"]["milk"]:
            print("Sorry no enought milk.")
        else:
            coins=insert_coins()
            money_by_customer=round(calculate_money(coins["quarters"],coins["dimes"],coins["nickles"],coins["pennies"]),2)
            if money_by_customer>=MENU["latte"]["cost"]:
                return_money=money_by_customer-MENU["latte"]["cost"]
                money_by_customer-=return_money
                money+=money_by_customer
                print(f"Here is ${round(return_money,2)} in change.")
                resources["water"]-=MENU["latte"]["ingredients"]["water"]
                resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"]
                resources["milk"]-=MENU["latte"]["ingredients"]["milk"]
                print("Here is your latte. Enjoy!!")
            else:
                print("Sorry that's not enough money. Money refunded")

    #if the user choice is cappuccino
    elif user_choice=="cappuccino":
        if resources["water"]<=MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry ther is no enough water.")
        elif resources["coffee"]<=MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry no enough coffee.")
        elif resources["milk"]<=MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry no enought milk.")
        else:
            coins=insert_coins()
            money_by_customer=round(calculate_money(coins["quarters"],coins["dimes"],coins["nickles"],coins["pennies"]),2)
            if money_by_customer>=MENU["cappuccino"]["cost"]:
                return_money=money_by_customer-MENU["cappuccino"]["cost"]
                money_by_customer-=return_money
                money+=money_by_customer
                print(f"Here is ${round(return_money,2)} in change.")
                resources["water"]-=MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"]-=MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"]-=MENU["cappuccino"]["ingredients"]["milk"]
                print("Here is your cappuccino. Enjoy!!")
            else:
                print("Sorry that's not enough money. Money refunded")
