from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
money = MoneyMachine()
menu1 = Menu()
#latte = MenuItem(menu1.menu[0], )
items = menu1.menu
state = True
print("Which drink would you like:  ")
print(menu1.get_items())
item = input()

while state:
    if machine.is_resource_sufficient(item):
        order = menu1.find_drink(item)
        print("Insert your money:")
        received = input()
        money.money_received = received
        if item == "latte":
            price = items[0].cost
        elif item == "espresso":
            price = items[1].cost
        else:
            price = items[2].cost

        if money.make_payment(price):
           machine.make_coffee(order)

    state = False

machine.report()
money.report()










