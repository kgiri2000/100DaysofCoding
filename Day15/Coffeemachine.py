"""
Kamal Girl
100 Days of Coding Python
"""
# Coffee Machine
# Print the report
# Check resources sufficient
# Process coins
# Check transaction successful?
# Make coffee

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    result = " "
    for key, value in resources.items():
        result += f"{key} : {value} \n"

    result += "Money: " + str(profit)
    return result


def checkresources(coffeetype):
    if (MENU[coffeetype]["ingredients"]["water"]) > (resources.get("water")):
        print("No water available")
        return False
    if coffeetype != "espresso":
        if (MENU[coffeetype]["ingredients"]["milk"]) > (resources.get("milk")):
            print("No milk available")
            return False
    if (MENU[coffeetype]["ingredients"]["coffee"]) > (resources.get("coffee")):
        print("No coffee available")
        return False

    return True


def getmoney():
    print("Please enter the money:\n ")
    print("Quarters: ")
    quarters = int(input())
    print("Dimes: ")
    dimes = int(input())
    print("Nickles: ")
    nickles = int(input())
    print("Pennies: ")
    pennies = int(input())

    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies


def makecoffee(coffeetype):
    #global rmilk
    rwater = MENU[coffeetype]["ingredients"]["water"]
    if coffeetype != "espresso":
        rmilk = MENU[coffeetype]["ingredients"]["milk"]
    rcoffee = MENU[coffeetype]["ingredients"]["coffee"]

    resources["water"] -= rwater
    if coffeetype != "espresso":
        resources["milk"] -= rmilk
    resources["coffee"] -= rcoffee
    return True


status = True
while status:
    print("What would you like? (espresso/latte/cappuccino):")
    x = input()

    if x == 'off':
        status = False
        break
    if x == 'report':
        print(report())
    if (x == "espresso") or (x == "latte") or (x == "cappuccino"):
        isavailable = checkresources(x)
        if isavailable:
            money = getmoney()
            cost = MENU[x]["cost"]
            if money > cost:
                profit += cost
                change = money - cost
                if makecoffee(x):
                    print(f"Your Money: {money} ")
                    print(f"Cost: {cost} ")
                    print(f"Here is your {x}. Enjoy!")
                    print(f"Your change: {change} ")

            else:
                print("Not Enough Money")


