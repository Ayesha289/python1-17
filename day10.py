# Calculator

import os
import day10art

clear = lambda: os.system('cls') 

def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2 

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(day10art.logo)
    num1 = float(input("What's the first number? "))
    for operator in operations:
        print(operator)

    choice = True

    while(choice):
        symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation = operations[symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if cont == 'y':
            num1 = answer
        else:
            choice = False
            clear()
            calculator()
calculator()