#Coffee Machine

from day15menu import MENU
from day15art import logo

remainingWater = 300
remainingMilk = 200
remainingCoffee = 100
cash = 0
machineStart = True
print(logo)

def cashCounter(drink = ""):
    global remainingWater, remainingMilk, remainingCoffee, cash

    money = MENU[drink]['cost']
    cash = cash + money

    if(remainingWater <= 0):
        print("Sorry there is not enough water.")
    elif(remainingMilk <= 0):
        print("Sorry there is not enough milk.")
    elif(remainingCoffee <= 0):
        print("Sorry there is not enough coffee.")
    else:
        print("Please enter coins.")
        quarter = int(input("Quarters: "))
        dime = int(input("Dimes: "))
        nickel = int(input("Nickels: "))
        penny = int(input("Pennies: "))

        totalcash = (quarter*0.25) + (dime*0.10) + (nickel*0.05) + (penny*0.01)
        if (totalcash >= money):
            remain = round((totalcash - money), 2)
            print(f"Here is ${remain} in change.")
            print(f"Here is your {drink}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")

def checkList(drink = ""):
    global remainingWater, remainingMilk, remainingCoffee
    water = MENU[drink]['ingredients']['water']
    coffee = MENU[drink]['ingredients']['coffee']

    if drink != 'espresso':
        milk = MENU[drink]['ingredients']['milk']
        remainingMilk = remainingMilk - milk

    remainingWater = remainingWater - water
    remainingCoffee = remainingCoffee - coffee
    
while(machineStart):
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'espresso':
        checkList(drink = 'espresso')
        cashCounter(drink = 'espresso')
    elif choice == 'latte':
        checkList(drink = 'latte')
        cashCounter(drink = 'latte')
    elif choice == 'cappuccino':
        checkList(drink = 'cappuccino')
        cashCounter(drink = 'cappuccino')
    elif choice == 'off':
        machineStart = False
    elif choice == 'report':
        print(f"Water: {remainingWater}ml")
        print(f"Milk: {remainingMilk}ml")
        print(f"Coffee: {remainingCoffee}g")
        print(f"Money: ${cash}")
    else:
        print("Please input correctly.")