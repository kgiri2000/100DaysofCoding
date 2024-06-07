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


#record saving
money = 0.0


#Check if resources are sufficient or not
def is_suff(item):
    values = MENU[item]["ingredients"]
    if values["water"] <= resources["water"]:
        if values["coffee"] <= resources["coffee"]:

            if item == "espresso":
                return True
            elif values["milk"] <= resources["milk"]:
                return True
            else:
                return False


inp = input(" Please press ON to turn on the coffee machine: ")

while inp == "ON":
    print("What would you like for today: ")
    order = input()
    #Turning the machine OFF

    if order == "OFF":
        inp = "OFF"
        break
        #Priniting the report
    if order == "report":
        print("Water: " + str(resources["water"]))
        print("Milk: " + str(resources["milk"]))
        print("coffee: " + str(resources["coffee"]))
        print("Money: " + str(money))
    #Checking the resources
    if order == "espresso" or order == "latte" or order == "cappuccino":
        if is_suff(order) :
            print("Please insert the desired amounts of coins: ")
            pennies = int(input("Number of Pennies: "))
            dimes = int(input("Number of dimes: "))
            nickle = int(input("Number of nickle: "))
            quaters = int(input("Number of quaters: "))
            cash = 0.25 * quaters + 0.10 * nickle + 0.05 * dimes + 0.01 * pennies

            #Checking if there is sufficient amount of money
            if MENU[order]["cost"] <= cash:
                print("Here is your!!" + order)
                #Updating the resources
                resources["water"] -= MENU[order]["ingredients"]["water"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]

                if order == "latte" or order == "cappuccino":
                   resources["milk"] -= MENU[order]["ingredients"]["milk"]

                #Updating money
                money = money + MENU[order]["cost"]
                refund =  cash - MENU[order]["cost"]
                print("Your refund is: " + str(refund))


            else:
                print("Not enough money!! Please be back after getting RICH")
                print("Here is all your money back" + str(cash))
                break

        else:
            inp == "OFF"
            print("Not Sufficient Resources")
            break


#Thank you message
print("Thank you for shopping with us!!!")
