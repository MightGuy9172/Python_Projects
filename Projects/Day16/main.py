
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine=MoneyMachine()
coffeeMaker=CoffeeMaker()
menu=Menu()

start=True

while start:
     option=menu.get_items()
     choice=input(f"What would u Like to have {option} or report or off: ").lower()
     if choice=="off":
         start=False
     elif choice=="report":
         coffeeMaker.report()
         moneyMachine.report()
     else :
         drink=menu.find_drink(choice)
         if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
                 coffeeMaker.make_coffee(drink)