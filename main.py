from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

items = Menu.get_items(Menu())

CoffeeMaker = CoffeeMaker()

MoneyMachine = MoneyMachine()

order = "on"

while not order == "off":
    order = input(f"What would you like? {items}: ")
    if order == "off":
        print("Turning the machine off.")
    elif order == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = menu.find_drink(order)
        if CoffeeMaker.is_resource_sufficient(drink):
            if MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)